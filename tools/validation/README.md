# Validation Tools

Keep validation checks deterministic and explain what they do and do not establish. `validate_findings.py` validates finding JSON files against the required fields and allowed statuses in `evidence/schema/finding.schema.json`, and rejects duplicate IDs. The earlier evidence-record validator remains at `../validate_evidence.py`.