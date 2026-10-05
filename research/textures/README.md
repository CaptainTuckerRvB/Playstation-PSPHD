# Textures

Documentation-only map of texture-related names in the permitted local source packets. This is an organization of labels, **not** a claim about PSPHD's internal texture pipeline or the order in which operations occur.

## Documented option names

The local graphics/textures packet lists:

- Names listed under Texture Dumping / Missing Texture Dumping: `--texsave`, `--texmissingsave`
- Names listed under Texture Loading / Texture Cache: `--texloadmode`, `--texcachemode`
- Names listed under Texture Replacement: `--texreplace`, `--texswitch`, `--replacementfilter`, `--replacementalpha`
- Names listed under CLUT Handling / Auto Resampler: `--texclutmode`, `--autoresampler`

These are names and source headings only; they do not establish runtime effects. See `TEX-PSPHD-001` / `PSPHD-00002` (packet: `research/sources/psphd_ps4devwiki_graphics_textures.md`; source URL is recorded in the index). `--texloadcores` does not occur in the local source packets; its existence, syntax, and meaning are **UNKNOWN**, not disproven.

## Other texture-related names

- Hash-mode labels: `drawbounds`, `drawboundsloco`, `patchworkheroes`, `locoroco2`, `rondo`, and `full`; see `TEX-PSPHD-002` / `PSPHD-00003`. The packet does not establish their algorithm, purpose, or title association.
- The local graphics/textures packet also labels texture-scale directories `4x/` and `8x/`. Their source context, supported formats, meaning, and behavior are not established by an existing finding.

## Unknowns

Option values, defaults, syntax beyond the recorded tokens, effects, precedence, activation conditions, file formats/paths, dump contents, replacement matching and selection, cache/hash algorithms, CLUT behavior, resampling behavior, and title/version scope are **UNKNOWN**. The names do not establish that dumping or replacement works, or how it works.

No PSPHD↔PPSSPP texture compatibility conclusion is supported by these records. Do not transfer PPSSPP behavior or assume the labels describe an internal stage sequence.

## Sources and status

See `index.json` for evidence IDs, source URLs/revisions, packet filenames, and caveats. These are source-attributed option/mode names, not independently tested PSPHD behavior. Do not store game textures or other copyrighted assets here.
