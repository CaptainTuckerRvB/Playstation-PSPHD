import json
import tempfile
import unittest
from pathlib import Path

from tools.validation.validate_findings import (
    load_schema,
    main,
    validate_record,
)


class ValidateFindingsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = load_schema()
        cls.required_fields = schema["required"]
        cls.allowed_statuses = schema["properties"]["status"]["enum"]

    def make_record(self, record_id="TEST-00001", status="UNKNOWN"):
        return {
            "id": record_id,
            "status": status,
            "target": "FICTIONAL TEST DATA",
            "subsystem": "test",
            "title_or_game": "UNKNOWN",
            "emulator_version": "UNKNOWN",
            "finding": "Synthetic test record; no claim about PSPHD behavior.",
            "evidence_references": [],
            "confidence": "UNKNOWN",
            "related_findings": [],
            "tests": [],
            "notes": [],
        }

    def test_record_with_required_fields_and_allowed_status_passes(self):
        self.assertEqual(
            validate_record(
                self.make_record(), self.required_fields, self.allowed_statuses
            ),
            [],
        )

    def test_missing_required_fields_are_reported(self):
        errors = validate_record(
            {}, self.required_fields, self.allowed_statuses
        )

        self.assertIn("missing required field: id", errors)
        self.assertIn("missing required field: status", errors)

    def test_invalid_status_is_rejected(self):
        errors = validate_record(
            self.make_record(status="MAYBE"),
            self.required_fields,
            self.allowed_statuses,
        )

        self.assertIn("invalid status: 'MAYBE'", errors)

    def test_non_object_record_is_rejected(self):
        self.assertEqual(
            validate_record([], self.required_fields, self.allowed_statuses),
            ["record must be a JSON object"],
        )

    def test_duplicate_ids_make_validator_return_nonzero(self):
        with tempfile.TemporaryDirectory() as directory:
            findings_dir = Path(directory)
            record = self.make_record()
            (findings_dir / "one.json").write_text(
                json.dumps(record), encoding="utf-8"
            )
            (findings_dir / "two.json").write_text(
                json.dumps(record), encoding="utf-8"
            )

            self.assertEqual(main([str(findings_dir)]), 1)

    def test_invalid_status_makes_validator_return_nonzero(self):
        with tempfile.TemporaryDirectory() as directory:
            record_path = Path(directory) / "invalid.json"
            record_path.write_text(
                json.dumps(self.make_record(status="INVALID")),
                encoding="utf-8",
            )

            self.assertEqual(main([str(record_path)]), 1)


if __name__ == "__main__":
    unittest.main()
