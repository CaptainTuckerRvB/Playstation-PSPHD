## Source Metadata

- Source ID: S1; S4
- Original title: “PSP Emulation - PS4 Developer wiki.pdf” (S1); “PSP Classics Configuration Files (Official) - PS4 Developer wiki” (S4)
- Original URL: https://www.psdevwiki.com/ps4/index.php?title=PSP_Emulation&oldid=297238 (S1); https://www.psdevwiki.com/ps4/index.php?title=PSP_Classics_Configuration_Files_(Official)&oldid=295120 (S4)
- Source type: Community wiki pages, represented by supplied extractions
- Extraction status: Manual topical extraction; source pages were not independently fetched or verified here
- Notes: The packet has no source metadata internally. S1/S4 attribution is retained from existing evidence references PSPHD-00002, PSPHD-00007, and PSPHD-00009; the packet documents names and headings, not option or API behavior.

# PSPHD Graphics, Rendering and Texture Systems

## Graphics Architecture

### Known Rendering Features

### Framebuffer Handling

### Depth Buffer Handling

### VRAM Behavior

### GPU Threading

## Graphics CLI Options

--antialias
--present
--gputhread
--gpu-renderthread
--force-triangle-clip-off
--force-native-aspect-ratio
--use-higher-precision-depth
--optimize-fb-self-resolves
--force-dsf-present
--bend-30hz-lock

## Texture System

### Texture Dumping

--texsave

### Missing Texture Dumping

--texmissingsave

### Texture Loading

--texloadmode

### Texture Cache

--texcachemode

### Texture Hash Modes

- drawbounds
- drawboundsloco
- patchworkheroes
- locoroco2
- rondo
- full

### Texture Replacement

--texreplace
--texswitch
--replacementfilter
--replacementalpha

### CLUT Handling

--texclutmode

### Auto Resampler

--autoresampler

### Texture Scale Directories

4x/
8x/

## Official Rendering Patches

### Syphon Filter Dark Mirror

### Resistance Retribution

## Official Depth Readback Usage

ApplyDepthReadback()

## Explicitly Unknown