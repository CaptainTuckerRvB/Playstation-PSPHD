# PSPHD Research

Research notes on the Sony PSP emulator used by some PlayStation 4 and PlayStation 5 releases, commonly referred to in this project as PSPHD. The exact scope, versions, and behavior are **UNKNOWN** until supported by cited evidence.

This repository is a documentation and research foundation. It does not contain emulator code, and it does not implement a game conversion, texture, or package workflow.

## Research Status

No PSPHD behavior has been established by this repository yet. Treat undocumented details as **UNKNOWN**. Findings must distinguish:

- `OBSERVED`: recorded directly from identified evidence.
- `VERIFIED`: independently reproduced and documented.
- `INFERRED`: supported by evidence but not directly demonstrated.
- `UNKNOWN`: evidence is insufficient or absent.

Do not promote an inference to an observation or verification. See [AGENTS.md](AGENTS.md) for research and contribution rules.

## Research Indexes

- [Emulator versions](research/versions/README.md)
- [Games](research/games/README.md)
- [Configuration](research/configuration/README.md)
- [Commands](research/commands/README.md)
- [Lua](research/lua/README.md)
- [Graphics](research/graphics/README.md)
- [Textures](research/textures/README.md)
- [Compatibility](research/compatibility/README.md)

Each index starts empty. Its current state is `UNKNOWN`; entries should be added only with traceable sources and a confidence/status label.

## Evidence

Evidence records are JSON documents described by [the evidence schema](evidence/schema.json). Use `UNKNOWN` for fields that cannot yet be established. Validate records with the included standard-library tool:

```sh
python3 -m unittest discover -s tests -v
python3 tools/validate_evidence.py evidence/records
```

The validator checks for schema-required fields; it is not a full JSON Schema implementation.

## Long-Term Research Context

The intended research direction may eventually connect PSP game analysis, emulator/configuration analysis, verified compatibility research, texture extraction, PPSSPP texture-pack compatibility, optional external texture upscaling/remastering, texture reintegration, and PS4 package generation. This is context only: **none of that pipeline is implemented here**.

## Sources

These sources are starting points, not proof that any particular PSPHD behavior exists. Record the specific page, revision, or artifact used for each finding.

- [andshrew/PlayStation-PS1HD](https://github.com/andshrew/PlayStation-PS1HD) — documentation organization inspiration only. PS1-specific code and behavior are not reused or assumed to apply.
- [PS4 Developer Wiki: PSP Emulation](https://www.psdevwiki.com/ps4/PSP_Emulation) — community-maintained research reference.
- [PS4 Developer Wiki: PSP Classics Emulator Compatibility List](https://www.psdevwiki.com/ps4/PSP_Emulation_Compatibility_List) — community-maintained compatibility reference.
- [PPSSPP](https://www.ppsspp.org/) and [its source repository](https://github.com/hrydgard/ppsspp) — reference emulator and project documentation; PSPHD equivalence is not assumed.
- REA — source named for future research. The exact project identity and canonical URL are **UNKNOWN** and must be resolved before citing specific REA material.

## Scope and Materials

Keep the repository lightweight and prefer free/open-source tools. Do not add proprietary Sony binaries, decrypted commercial game files, copyrighted assets, or other restricted material. This repository documents research; it is not an emulator.
 
