# PSPHD

Research, documentation, analysis tooling, and compatibility research for the official Sony PlayStation Portable (PSP) emulator used on PlayStation 4 and PlayStation 5 systems, commonly referred to by the community as PSPHD.

This project uses the structure and research approach of [andshrew/PlayStation-PS1HD](https://github.com/andshrew/PlayStation-PS1HD) as a reference model while independently investigating PSPHD. PS1HD is a documentation reference only: no PS1HD code is copied, and PS1 behavior is not assumed to apply to PSPHD.

## Background

Sony introduced official PSP emulation on PlayStation 4 as part of its PlayStation Classics and PSP-related releases. PSPHD is the name used by this project for the emulator under investigation; its exact versions, implementation details, and behavior must be established by evidence.

The research scope includes reports and artifacts concerning possible title-specific configuration, scripting, graphics behavior, compatibility modifications, and other PS4-specific functionality. These are topics to investigate, not claims that any particular behavior is universal or verified. Much of PSPHD remains undocumented, so unsupported details are **UNKNOWN**.

This repository exists to systematically investigate and document behavior using reproducible evidence. It is a research foundation, not an emulator, and it does not yet implement the longer-term analysis, texture, or package workflow described below.

## Goals

The project aims to document and understand:

- PSPHD emulator versions
- PSPHD-based PS4 releases
- PSPHD configuration and title-specific configuration
- Emulator commands
- Lua scripting
- Allegrex CPU modifications
- Graphics, GLES, and Piglet behavior
- Texture handling, extraction, and replacement
- Framebuffer and shader behavior
- Memory, audio, and video behavior
- Title-specific compatibility modifications
- PS4 package structure and runtime behavior
- Differences between PSPHD implementations
- Compatibility with existing PPSSPP texture packs

These bullets define research scope. Listing a feature does not establish that it exists in PSPHD or describe how it behaves. See the [research indexes](#research-indexes) for the current state of each topic.

## Research Philosophy

Observed behavior in one title, release, or emulator version is not automatically universal. Every important conclusion must be classified:

- `OBSERVED`: directly recorded from a binary, configuration file, running emulator, trace, log, package, or other primary evidence.
- `VERIFIED`: observed behavior independently reproduced through a controlled test or supported by multiple independent sources of evidence.
- `INFERRED`: strongly supported by available evidence but not yet directly reproduced.
- `UNKNOWN`: insufficient evidence exists to make a reliable conclusion.

Do not present an inference as verified. AI-generated reasoning is not evidence by itself. See [AGENTS.md](AGENTS.md) for research and contribution rules.

## Evidence First

Store research findings independently from explanatory documentation. Each durable finding should identify its target, emulator/version where known, game/title where applicable, subsystem, conclusion, status, evidence references, confidence, related findings, and reproduction or verification status.

Records use [the evidence schema](evidence/schema.json). Its required fields are `id`, `status`, `target`, `emulator_version`, `game`, `subsystem`, `finding`, `evidence`, `confidence`, `related_findings`, and `reproduction_status`. Use `UNKNOWN` rather than guessing when a value is not established. Evidence references should identify a source and a useful locator; reproduction details belong in the record's status and supporting evidence.

Validate records and run the basic tests from the repository root:

```sh
python3 tools/validate_evidence.py evidence/records
python3 -m unittest discover -s tests -v
```

The validator checks required-field presence only; it is not a full JSON Schema implementation.

## Emulator Versions

The project will maintain a version matrix for evidence-backed PSPHD implementations and PSP-derived PS4 releases. Where known and supported by sources, entries should record:

- Release/title and PS4 title ID
- Firmware information and PSP source title
- PSPHD configuration and emulator files
- Graphics configuration and scripts
- Known patches and observed differences
- Evidence references

No PSPHD version mapping is established by this repository yet. See [research/versions/](research/versions/README.md).

## PSPHD-Based Releases

Research will cover PSP-related PS4 releases documented by the PS4 Developer Wiki and other legitimate research sources. Categories include PSP Remaster releases, PSP Classics, PSP-derived PS4 releases, title-specific emulator configurations, relevant demos, and unknown or unclassified emulator variants. A release's inclusion in a research source is not by itself a locally verified compatibility result.

See [research/games/](research/games/README.md).

## Configuration

Configuration research may investigate file names and concepts mentioned in research sources, including `config-title.txt`, `config-emu-ps4.txt`, `package-ps4.conf`, `revision.conf`, emulator arguments, title-specific configuration, runtime configuration, and temporary configuration. Their presence or effect in a PSPHD release is **UNKNOWN** until evidenced.

Each documented option should identify its syntax, known or suspected purpose, observed behavior, affected subsystem, title, emulator/version, evidence, and confidence. Keep suspicion distinct from observation.

See [research/configuration/](research/configuration/README.md).

## Emulator Commands

Document command-line options and runtime commands only when supported by evidence. Each entry should record syntax, purpose, observed behavior, subsystem, version/title, evidence, and confidence. Unknown commands or effects must remain explicitly marked `UNKNOWN`.

See [research/commands/](research/commands/README.md).

## Lua

The Lua research index is for investigating whether and how PSPHD releases use Lua. Questions may include script loading and execution, available functions, emulator interaction, compatibility patches, title-specific scripts, tooling scripts, and configuration behavior. Do not infer support or behavior from another emulator or from a file name alone.

See [research/lua/](research/lua/README.md).

## Graphics

Graphics research concerns the PSPHD rendering path and related PS4 behavior. Topics to investigate include GLES, Piglet, texture formats and caches, CLUT handling, framebuffer behavior, filtering, scaling, anti-aliasing, shaders, VRAM behavior, rendering compatibility, and title-specific graphics modifications. These topics are not findings until documented with evidence.

See [research/graphics/](research/graphics/README.md).

## Texture Research

Investigate whether and how PSPHD handles runtime texture identification, extraction, and replacement. Relevant metadata may include hashes, dimensions, formats, mipmaps, CLUT information, cache behavior, and title-specific behavior. Original extracted assets must never be overwritten; restricted assets must not be committed.

The intended future workflow is:

```text
PSP Game
	-> PSPHD
	-> Texture Extraction
	-> Validation
	-> Pause
	-> Original / PPSSPP Pack / External Upscale / External Remaster
	-> Validation
	-> PSPHD Texture Representation
	-> PS4 Package
```

The external transformation stage is intentionally separate from extraction and packaging. This workflow is a target, not implemented functionality.

See [research/textures/](research/textures/README.md).

## PPSSPP Texture Compatibility

An eventual goal is to investigate whether existing PPSSPP texture packs can be used with PSPHD with minimal modification where technically possible. PPSSPP packs are considered a potential input format, not evidence of PSPHD's internal format or behavior.

The intended architecture is:

```text
PPSSPP Texture Pack
	-> PSPHD Importer
	-> PSPHD Internal Texture Representation
	-> PS4 Texture Mapping
```

Original PPSSPP identifiers should be retained if an importer is developed, so imported assets remain traceable and reversible. No importer or texture pipeline is implemented in Phase 0.

## Reverse Engineering

Static and dynamic reverse engineering may be used where appropriate and lawful. REA is a named research reference intended for possible use in binary analysis, function discovery, call relationships, data-flow investigation, evidence collection, and runtime/reconstruction research. The exact REA project identity and canonical URL remain **UNKNOWN**; resolve them before citing specific REA material. Other open-source tools may be used when appropriate. No AI-generated conclusion is verified without supporting evidence.

## Analysis Architecture

The intended long-term architecture is:

```text
PSP Game
	-> PSPHD analysis
	-> Emulator/version comparison
	-> Evidence collection
	-> Compatibility determination
	-> Texture extraction
	-> Optional texture transformation
	-> Texture validation
	-> PS4 package generation
	-> Runtime validation
```

This is a target architecture, not a statement that every stage currently exists. The project has not implemented this pipeline.

## Research Indexes

- [Emulator versions](research/versions/README.md)
- [Games and releases](research/games/README.md)
- [Configuration](research/configuration/README.md)
- [Commands](research/commands/README.md)
- [Lua](research/lua/README.md)
- [Graphics](research/graphics/README.md)
- [Textures](research/textures/README.md)
- [Compatibility](research/compatibility/README.md)

These indexes are initial scaffolding. No PSPHD behavior or compatibility result has been established by this repository; undocumented details remain `UNKNOWN`.

## Development Environment

The project prioritizes free and open-source tooling. The primary environment includes GitHub, GitHub Codespaces, Git, and Python. Node.js, Ghidra where practical, REA, PPSSPP, and legally available PS4 development/research tools may be used when relevant. Heavy or platform-specific tools should not be added to the Codespace unless they provide a clear benefit.

## Legal and Research Boundaries

Do not commit proprietary Sony binaries, decrypted commercial game files, copyrighted game assets, proprietary keys, or other restricted material. Research tooling should operate on material the researcher is legally permitted to possess and analyze. Prefer source links and descriptive metadata over redistribution.

## Project Status

**Phase 0 — Repository and research foundation.** The repository structure, evidence model, minimal development environment, and research methodology are established. It is not currently an emulator, and the future analysis and content-processing pipeline is not implemented.

## References

These references are starting points, not proof that any particular PSPHD behavior exists. Cite the specific page, revision, or artifact used for each finding.

- [andshrew/PlayStation-PS1HD](https://github.com/andshrew/PlayStation-PS1HD) — documentation and research-approach reference model only; no code or PS1 behavior is transferred.
- [PS4 Developer Wiki: PSP Emulation](https://www.psdevwiki.com/ps4/PSP_Emulation)
- [PS4 Developer Wiki: PSP Classics Emulator Compatibility List](https://www.psdevwiki.com/ps4/PSP_Emulation_Compatibility_List)
- [PPSSPP](https://www.ppsspp.org/) and [its source repository](https://github.com/hrydgard/ppsspp) — separate emulator and project; equivalence with PSPHD is not assumed.
- REA — project identity and canonical source URL are **UNKNOWN**; resolve them before citing specific material.

## Disclaimer

This repository contains research, documentation, and tooling concerning software behavior. Users are responsible for complying with applicable laws, licenses, and terms governing software and content they analyze.
 
