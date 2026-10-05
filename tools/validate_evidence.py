"""Check evidence JSON files for fields required by the repository schema."""

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RECORDS = ROOT / "evidence" / "records"
SCHEMA_PATH = ROOT / "evidence" / "schema.json"


def load_required_fields(schema_path=SCHEMA_PATH):
    with schema_path.open(encoding="utf-8") as schema_file:
        schema = json.load(schema_file)
    return schema["required"]


def validate_record(record, required_fields):
    if not isinstance(record, dict):
        return ["record must be a JSON object"]
    return [
        f"missing required field: {field}"
        for field in required_fields
        if field not in record
    ]


def find_records(paths):
    records = []
    for path in paths:
        if path.is_file() and path.suffix == ".json":
            records.append(path)
        elif path.is_dir():
            records.extend(sorted(path.rglob("*.json")))
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[DEFAULT_RECORDS],
        help="JSON record files or directories (default: evidence/records)",
    )
    args = parser.parse_args()

    try:
        required_fields = load_required_fields()
    except (OSError, json.JSONDecodeError, KeyError) as error:
        parser.error(f"could not load evidence schema: {error}")

    record_paths = find_records(args.paths)
    if not record_paths:
        print("No JSON evidence records found.")
        return 0

    failures = 0
    for record_path in record_paths:
        try:
            with record_path.open(encoding="utf-8") as record_file:
                record = json.load(record_file)
            errors = validate_record(record, required_fields)
        except (OSError, json.JSONDecodeError) as error:
            errors = [f"could not read JSON: {error}"]

        if errors:
            failures += 1
            for error in errors:
                print(f"{record_path}: {error}")
        else:
            print(f"{record_path}: required fields present")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())