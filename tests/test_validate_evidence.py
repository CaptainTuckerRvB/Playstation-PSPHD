import unittest

from tools.validate_evidence import load_required_fields, validate_record


class ValidateRecordTests(unittest.TestCase):
    def test_record_with_all_required_fields_passes(self):
        required_fields = load_required_fields()
        record = {field: "UNKNOWN" for field in required_fields}

        self.assertEqual(validate_record(record, required_fields), [])

    def test_missing_fields_are_reported(self):
        required_fields = ["id", "status", "evidence"]

        self.assertEqual(
            validate_record({"id": "TEST-00001"}, required_fields),
            ["missing required field: status", "missing required field: evidence"],
        )

    def test_non_object_record_is_rejected(self):
        self.assertEqual(
            validate_record([], ["id"]),
            ["record must be a JSON object"],
        )


if __name__ == "__main__":
    unittest.main()