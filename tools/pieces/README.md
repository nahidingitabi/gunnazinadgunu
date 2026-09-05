# Piece-reading toolchain

Everything used to read the jigsaw pieces off the box stack. Written for the
1080p footage; all of it works unchanged on higher-resolution clips, which is
what it is really waiting for.

Run these from a directory containing `clipmap.json`, with the clips in
`/root/.claude/uploads/*/`.

| script | use |
|---|---|
| **`pipe4k.py CLIPID T0 T1 [OUT]`** | **start here for a new clip.** Picks the sharpest reference frame in the range, builds the homography cache, auto-detects every piece outline, super-resolves each one and writes `OUT/ATLAS.png` — every piece, raw and contrast-stretched, side by side. |
| **`piecesr.py SPEC.json OUT.png`** | fuses ONE piece across *several camera angles*. Each piece is its own plane, so a per-piece quad plus pyramid ECC (¼→½→1) can register shots that a single global homography cannot. `SPEC` = `{"canon":{"w":..,"h":..},"shots":[{"cache":"h803.npz","quad":[[x,y]×4]},…]}`; quads are in each cache's reference-frame coordinates, and the tool tries all four cyclic rotations and keeps the best-correlating one. |
| `homo.py CID REFT OUT.npz --range T0:T1 CX0 CY0 CX1 CY1` | ORB(15000)+RANSAC homography of every frame onto the reference |
| `warpreg.py CACHE REGIONS.json OUTDIR` | masked-median SR of listed regions from a cache |
| `sharp.py CID T0 T1 x0,y0,x1,y1 OUT [N] [SCALE]` | ranks frames by Laplacian variance over a crop |
| `allquads.py FRAME x0,y0,x1,y1 [minarea]` / `findquad.py` | piece outlines via `b* < 16 & L > 135`, returned as min-area-rect corners |
| `inkq.py IMG x0,y0,x1,y1:label …` | red-vs-blue verdict from Δa\* against the card's *own* paper (cancels the tungsten cast). Δa\* > +1.5 red, < +0.5 blue |
| `gwidth.py`, `strokes.py` | glyph width / stroke-run profiles — **both too noisy at 1080p**; numerals were read by eye off the fused images instead |
| `emomatch2.py CROP.png [N]` | ranks Noto Color Emoji glyphs against a picture crop (histogram + shape). **Fails its controls: 1 of 3.** Flags match well (Oman scored 0.95 vs 0.73 next); faces and pale prints do not. Do not trust it beyond flags. |

## Calibration notes

* Best 1080p frame of the box stack: **t = 803.527** (clip `67592638`), the
  first frame of the 803.49–806.96 shot. Laplacian variance 117 against 15 and
  51 in the neighbouring shots. Nothing in the video is closer to the boxes.
* A piece is ~45 px wide at 1080p; its numerals ~10 px. Super-resolution buys
  about 3× and then stops. **At 2160p the same pieces are ~90 px** — that is
  what the numerals and pictures actually need.
* Region coordinates passed to `warpreg.py` must lie inside the cache's `ctx`
  window, or the region comes back EMPTY.
