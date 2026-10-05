# PSPHD Research Rules

These rules apply to research notes, evidence, and tooling in this repository.

## Retrieval-First Research

Optimize for low token use and high information recall. For ordinary tasks, do not load the whole research repository. First identify the relevant research area, then consult `evidence/index/` for relevant evidence IDs, related findings, and whether the question is already answered. Retrieve only relevant records and source details. Prefer existing verified findings; repeat analysis only when evidence is insufficient. Mark gaps `UNKNOWN`.

Evidence priority: `VERIFIED` findings, `OBSERVED` primary evidence, existing tests, direct source artifacts, `INFERRED` conclusions, then model reasoning. Model reasoning alone is never evidence.

Keep durable knowledge in repository files. Summarize findings in compact structured records, but never replace detailed findings with summaries that omit evidence references. In responses, use IDs and references instead of reproducing research documents or large evidence excerpts.

For normal responses, use:

```text
STATUS:
CONCLUSION:
EVIDENCE:
CONFIDENCE:
NEXT ACTION:
```

- Do not invent PSPHD behavior, versions, commands, configuration options, compatibility results, or supported features. Mark undocumented or unresolved details `UNKNOWN`.
- Cite the specific source for each factual claim. Prefer primary artifacts and reproducible observations; record source revisions, locations, and capture context where available.
- Separate direct observations, independently reproduced results, inferences, and unknowns. Explain what an observation does and does not establish.
- Do not treat the PS1HD project as evidence about PSPHD. It is a documentation-structure reference only; do not copy its code or transfer PS1 findings to PSPHD.
- PPSSPP is a separate project. Do not assume its behavior, formats, or compatibility apply to PSPHD without evidence.
- Keep evidence records separate from explanatory index pages and validate records against `evidence/schema.json`.
- Do not commit proprietary Sony binaries, decrypted commercial game files, copyrighted assets, or other restricted material. Link to lawful references instead of redistributing them.
- Do not implement emulator code or the future game/texture/package pipeline as part of this research foundation.
- Prefer free/open-source dependencies. Avoid adding dependencies when Python's standard library is sufficient.
- Keep changes focused, lightweight, and reproducible. Tests must not require proprietary software or game content.