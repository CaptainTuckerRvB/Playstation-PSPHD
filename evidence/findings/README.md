# Findings

Store durable, evidence-backed research conclusions here as JSON records using [the finding schema](../schema/finding.schema.json). The [example record](EXAMPLE-00001.json) is fictional and demonstrates structure only; it is not a PSPHD finding.

Use `UNKNOWN` instead of filling evidence gaps with guesses. Validate findings from the repository root with `python3 tools/validation/validate_findings.py`. The existing `evidence/records/` format and validator remain separate.