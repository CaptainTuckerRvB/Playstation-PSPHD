# Evidence

This directory holds machine-readable or source-linked material supporting research findings. Keep provenance, context, and restrictions clear; do not commit proprietary binaries, decrypted commercial game files, copyrighted assets, or other restricted material.

- `findings/`: durable finding records using the schema in `schema/`; the example record is fictional.
- `schema/`: JSON schema for findings; validate records with `python3 tools/validation/validate_findings.py`.
- `logs/`: permitted logs or references and notes describing their capture context.
- `traces/`: permitted traces or references and notes describing how they were produced.
- `hashes/`: hashes and non-sensitive identification metadata; a hash does not establish provenance or behavior by itself.
- `index/`: cross-references between findings, sources, and evidence items.

The existing `records/` directory holds the earlier evidence-record format validated against [schema.json](schema.json) by `tools/validate_evidence.py`. Use `UNKNOWN` when a required value is not established. Run the standard-library validators and tests from the repository root:

```sh
python3 tools/validate_evidence.py evidence/records
python3 tools/validation/validate_findings.py
python3 -m unittest discover -s tests -v
```

The validators check required fields (and finding status values and duplicate IDs); they are not full JSON Schema implementations.