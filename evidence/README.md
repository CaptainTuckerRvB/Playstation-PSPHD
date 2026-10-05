# Evidence Records

Store one JSON evidence record per file under `records/`. The required fields and their basic types are defined in [schema.json](schema.json). Use the literal string `UNKNOWN` when a required text value is not established; do not fill gaps with guesses.

Run the validator and tests from the repository root:

```sh
python3 tools/validate_evidence.py evidence/records
python3 -m unittest discover -s tests -v
```

The validator checks required-field presence only. The schema is the documentation contract; full JSON Schema validation is not currently configured.