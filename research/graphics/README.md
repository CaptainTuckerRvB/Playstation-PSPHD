# Graphics

Documentation-only map of what the permitted local source packets and existing findings establish. Names in documentation are not proof of implementation, effect, or support in every PSPHD title/build.

## Documented names

- The local graphics/textures packet lists `--antialias`, `--present`, `--gputhread`, `--gpu-renderthread`, `--force-triangle-clip-off`, `--force-native-aspect-ratio`, `--use-higher-precision-depth`, `--optimize-fb-self-resolves`, `--force-dsf-present`, and `--bend-30hz-lock`. Only names are established; see `CMD-PSPHD-002` / `PSPHD-00007` (packet: `research/sources/psphd_ps4devwiki_graphics_textures.md`).
- The packet has headings for official rendering patches under Syphon Filter Dark Mirror and Resistance Retribution and lists `ApplyDepthReadback()` under “Official Depth Readback Usage.” It does not associate the function with either title or establish effects; see `GFX-PSPHD-001` / `PSPHD-00009` (packet: `research/sources/psphd_ps4devwiki_graphics_textures.md`).

## Not established by the allowed materials

- Renderer architecture, GLES/API use, PSPHD↔Piglet relationship, rendering backend, shader system, and shader behavior.
- Framebuffer implementation or behavior, VRAM layout/management, depth representation/precision behavior, readback semantics, or GPU-hook semantics.
- Whether the names `--present`, `--gputhread`, `--gpu-renderthread`, `--use-higher-precision-depth`, and `--optimize-fb-self-resolves` do what their names might suggest.
- Antialiasing behavior, general filtering, mesh smoothing, or any graphics-hack effect beyond the presence of the source-attributed patch function names.

Do not infer an internal pipeline or apply behavior across emulator variants. No tested graphics result or emulator version is recorded here.

## Sources and status

`index.json` and `research/commands/index.json` retain evidence IDs, source URL/revision mappings, and local packet filenames. The observations are names and headings in a manual extraction, not independently reproduced PSPHD behavior.
