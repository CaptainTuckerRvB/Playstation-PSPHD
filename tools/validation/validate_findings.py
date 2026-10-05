"""Validate finding JSON records against the repository schema."""

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_FINDINGS = ROOT / "evidence" / "findings"
SCHEMA_PATH = ROOT / "evidence" / "schema" / "finding.schema.json"


def load_schema(schema_path=SCHEMA_PATH):
    with schema_path.open(encoding="utf-8") as schema_file:
        return json.load(schema_file)


def find_records(paths):
    records = []
    for path in paths:
        if path.is_file() and path.suffix == ".json":
            records.append(path)
        elif path.is_dir():
            records.extend(sorted(path.rglob("*.json")))
    return records


def validate_record(record, required_fields, allowed_statuses):
    if not isinstance(record, dict):
        return ["record must be a JSON object"]

    errors = [
        f"missing required field: {field}"
        for field in required_fields
        if field not in record
    ]
    if "status" in record and record["status"] not in allowed_statuses:
        errors.append(f"invalid status: {record['status']!r}")
    if "id" in record and (
        not isinstance(record["id"], str) or not record["id"]
    ):
        errors.append("id must be a non-empty string")
    return errors


def validate_files(paths, required_fields, allowed_statuses):
    errors = []
    seen_ids = {}

    for record_path in find_records(paths):
        try:
            with record_path.open(encoding="utf-8") as record_file:
                record = json.load(record_file)
        except (OSError, json.JSONDecodeError) as error:
            errors.append((record_path, f"could not read JSON: {error}"))
            continue

        record_errors = validate_record(
            record, required_fields, allowed_statuses
        )
        for error in record_errors:
            errors.append((record_path, error))

        if isinstance(record, dict):
            record_id = record.get("id")
            if isinstance(record_id, str) and record_id:
                if record_id in seen_ids:
                    errors.append(
                        (
                            record_path,
                            f"duplicate id {record_id!r}; "
                            f"first used in {seen_ids[record_id]}",
                        )
                    )
                else:
                    seen_ids[record_id] = record_path

    return errors


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[DEFAULT_FINDINGS],
        help="Finding JSON files or directories (default: evidence/findings)",
    )
    args = parser.parse_args(argv)

    try:
        schema = load_schema()
        required_fields = schema["required"]
        allowed_statuses = schema["properties"]["status"]["enum"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        parser.error(f"could not load finding schema: {error}")

    errors = validate_files(args.paths, required_fields, allowed_statuses)
    if errors:
        for record_path, error in errors:
            print(f"{record_path}: {error}")
        return 1

    print("Finding records valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
