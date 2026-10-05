# Playstation-PSPHD
Notes from investigating the official Sony PlayStation Portable emulator for PlayStation 4 and Playstation 5

Background
 
Sony introduced official PSP emulation on PlayStation 4 as part of its modern PlayStation Classics ecosystem. The emulator, commonly referred to by the scene as PSPHD, provides a native PSP emulation environment with additional PS4-specific functionality, including graphical enhancements, configuration options, scripting, and title-specific compatibility modifications.
 
This repository documents the investigation of PSPHD and its surrounding ecosystem.
 
The goal is to build an evidence-based understanding of:
 
- PSPHD emulator versions
- Emulator configuration
- CLI commands
- Lua scripting
- Allegrex CPU patches
- Graphics and GLES behavior
- Texture handling and replacement
- Audio and video handling
- Memory mapping
- Title-specific compatibility modifications
- PS4 package structure
- PSPHD-based commercial releases
- Runtime behavior
- Differences between PSPHD implementations
- Compatibility with existing PPSSPP texture packs
 
The long-term goal is to use this research to develop an independently reproducible PSP-to-PS4 compatibility and preservation workflow.
 
Research Philosophy
 
PSPHD is poorly documented and many behaviors are not yet understood.
 
This project therefore distinguishes between:
 
- OBSERVED — directly observed from a running system, binary, configuration, trace, or other primary evidence.
- VERIFIED — independently reproduced through testing.
- INFERRED — strongly supported but not directly demonstrated.
- UNKNOWN — insufficient evidence.
 
Conclusions should never be presented as verified when they are only inferred.
 
PSPHD Research
 
Emulator Versions
 
Version| Date| Release| Notes
?| ?| Initial PSPHD releases| Research pending
?| ?| LocoRoco 2 Remastered| Research pending
?| ?| Resistance: Retribution| Research pending
?| ?| Patapon 2| Research pending
 
Official PSPHD-Based Releases
 
Research targets include known PSP-derived PS4 releases and titles documented by the PS4 Developer Wiki.
 
Current research categories include:
 
- PSP Remaster releases
- PSP Classics
- PSP demos
- Title-specific PSPHD implementations
- Unknown/unclassified PSP emulator variants
 
See:
 
- "research/games/"
- "research/versions/"
- "research/compatibility/"
 
Configuration
 
PSPHD configuration research includes:
 
- "config-title.txt"
- "config-emu-ps4.txt"
- "package-ps4.conf"
- "revision.conf"
- emulator command-line arguments
- title-specific configuration
- runtime configuration changes
- temporary configuration files
 
Configuration behavior should be documented with the emulator version and title from which it was observed.
 
Emulator Commands
 
Known PSPHD commands and options are documented in:
 
"research/commands/"
 
Each command should include:
 
- syntax
- known purpose
- observed behavior
- affected subsystem
- emulator version
- title
- evidence
- confidence
 
Unknown commands should remain explicitly marked as unknown.
 
Lua
 
PSPHD supports Lua-based functionality used by some titles and emulator configurations.
 
Lua research includes:
 
- script loading
- script order
- available functions
- emulator configuration functions
- compatibility patches
- game-specific scripts
- tooling scripts
- trophy-related scripts
 
See:
 
"research/lua/"
 
Graphics
 
Graphics research focuses on the PSPHD rendering pipeline, including:
 
- GLES
- Piglet
- texture handling
- texture formats
- texture caches
- CLUT handling
- framebuffer behavior
- filtering
- scaling
- anti-aliasing
- rendering compatibility
- shader behavior
- VRAM behavior
 
See:
 
"research/graphics/"
 
Texture Research
 
PSPHD provides functionality for saving textures while games are running.
 
Research will document:
 
- texture extraction
- texture identification
- texture hashes
- dimensions
- formats
- mipmaps
- CLUT information
- texture replacement
- title-specific texture behavior
 
Original extracted assets must always be preserved.
 
The intended processing pipeline is:
 
PSP Game
   ↓
PSPHD
   ↓
Texture Extraction
   ↓
Validation
   ↓
[Pause]
   ↓
Original / PPSSPP Pack / External Upscale / Remaster
   ↓
Validation
   ↓
PSPHD Texture Package
   ↓
PS4 Package
 
PPSSPP Texture Compatibility
 
PSPHD research will include compatibility with existing PPSSPP texture packs.
 
PPSSPP texture packs will be treated as an input format rather than the internal PSPHD format.
 
The intended pipeline is:
 
PPSSPP Texture Pack
        ↓
PSPHD Importer
        ↓
PSPHD Texture Representation
        ↓
PS4 Texture Mapping
 
Original PPSSPP identifiers should be retained so imported assets remain traceable to their source.
 
Reverse Engineering
 
Static reverse engineering is supported by open-source analysis tools and, where appropriate, REA.
 
REA is intended to assist with:
 
- binary analysis
- function discovery
- call relationships
- data-flow investigation
- evidence collection
- runtime/reconstruction research
 
AI-generated conclusions must not be treated as evidence without verification.
 
Evidence
 
Research findings are stored separately from explanatory documentation.
 
Each finding should contain:
 
- unique ID
- target
- emulator version
- game/title
- observation
- evidence
- confidence
- related findings
- reproduction status
 
Example:
 
id: GLES-00001
status: VERIFIED
target: PSPHD
subsystem: graphics
finding: ...
evidence:
  - ...
tests:
  - ...
confidence: high
 
Compatibility Research
 
The project maintains a compatibility database covering known PSPHD-related releases and research targets.
 
Current reference material includes the PS4 Developer Wiki PSP emulation and compatibility documentation.
 
Tools
 
The project intends to remain usable with free and open-source tooling wherever practical.
 
Primary development environment:
 
- GitHub
- GitHub Codespaces
- Git
- Python
- Node.js
- Ghidra
- REA
- PPSSPP
- PS4 development/research tooling where legally available
 
Project Status
 
Early research / documentation
 
The project is not an emulator.
 
It is a research and tooling project intended to understand PSPHD behavior and develop reproducible methods for PSP-to-PS4 compatibility and preservation.
 
Disclaimer
 
This repository contains research and documentation concerning software behavior.
 
Do not distribute copyrighted game content, proprietary Sony binaries, decrypted commercial software, or other material that you do not have the right to distribute.
 
Users are responsible for complying with applicable laws and the licenses and terms applicable to any software or content they analyze.
 
References
 
- PS4 Developer Wiki
- PPSSPP
- REA
- PlayStation-PS1HD
 
