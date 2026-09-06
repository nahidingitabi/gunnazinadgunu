# HANDOFF — the jigsaw pieces (continues `BRIEFING.md`)

> **This is not a cold start.** Read `BRIEFING.md` first for the contest, the
> author, the entry form and everything ruled out before the pieces were found.
> This file carries only what changed since, and it changes the picture a lot.
> Full running log: `MRBEAST_PUZZLE_NOTES.md` (Azerbaijani).
>
> Labels: `[MEASURED]` I measured it from the footage · `[USER]` the user read it
> off the images with their own eyes · `[INFERRED]` reasoning · `[DEAD]` tested
> and abandoned, do not redo.

---

## 1. What the jigsaw actually is

Colin's own live-stream instruction was *"the first thing you should do is look
for a jigsaw puzzle."* The jigsaw is **not a graphic in the edit** — it is
**physical paper pieces taped onto the cardboard box stack** in the back-right
corner of the office set.

`[MEASURED]` **There are 15 pieces**, all on that one stack. Counted exhaustively
in the office wide shot (t = 20.30), where the whole stack is visible at once:

| where on the stack | pieces |
|---|---|
| top dark box, upper row | 4 — skater · "I VII" · window · arrow+bar-chart |
| top dark box, lower row | 2 — ribbon/bow · red-brown rectangle |
| right of the top box | 1 — cloud with snow |
| middle box | 2 — calendar · two tall objects |
| right box | 1 — US flag + barn |
| tilted "CONTENTS FROM … DEPT" box | 2 — 😂 · rock + eagle |
| lower box | 2 — Oman flag · Africa + green plant |
| lowest small box | 1 — not yet read |

The big foreground "PUZZLE CLUES" box carries **no** pieces, and nothing
elsewhere in the room does either.

## 2. Anatomy of one piece `[MEASURED]`

```
 ┌─sawtooth─┐                         ╭──rounded tab
 │  BLUE    │   picture 1   picture 2  │
 │  RED     │                          │
 └──────────┘──────────────────────────╯
```

* **Two Roman numerals stacked at the left end** — one **red**, one **blue**.
  Which one sits on top varies from piece to piece, so **colour is the only
  reliable discriminator**, never position. Colour was measured, not eyeballed:
  Δa\* of the ink against a ring of the card's *own* paper (`inkq.py`), which
  cancels the warm tungsten cast. Δa\* > +1.5 = red, < +0.5 = blue.
* **One or two pictures** to the right of the numerals. Two-picture pieces are
  confirmed, not an artefact of overlap — the second picture sits inside the
  same continuous white outline.
* **Edge shape**: left edge sawtooth (3 teeth), right edge a rounded bulge.
  So the pieces chain **left-to-right in one dimension**, not into a 2-D image.

## 3. The reads

`[MEASURED]` Twelve pieces, each confirmed from **two independent camera
angles**, so these are not single-frame artefacts:

| piece | red | blue |
|---|---|---|
| figure on roller skates | II (2) | XI (11) |
| "I VII" — picture hidden behind another piece | VII (7) | I (1) |
| down arrow + bar chart | VIII (8) | IX (9) |
| ribbon / tied bow | V (5) | VII (7) |
| red-brown rectangle | VI (6) | VIII (8) |
| calendar (spiral, large "25") | III (3) | IV (4) |
| two tall objects | VII (7) | VI (6) |
| 🇺🇸 US flag + red barn | VII (7) | IV (4) |
| 🇴🇲 Oman flag | VI (6) | V (5) |
| Africa silhouette + green plant | IV (4) | VIII (8) |
| cloud with snow | IX (9) | V (5) |
| 😂 face with tears of joy | X (10) | XIV (14) |

Still unread: **window**, **rock + eagle**, **the 15th piece** on the lowest box.

**V versus X is genuinely distinguishable** in the fused images (V converges at
the bottom, X crosses), so "VIII really means XIII" etc. is *not* an available
escape hatch. The reads stand.

## 4. Pictures — corrected `[USER]`

The user identified three from the fused images directly, correcting my
guesses: the golden lumpy object is a **rock/stone**, the bird is an **eagle**,
and the yellow face is the **laughing (tears of joy)** emoji. **Treat my other
picture identifications as provisional** — several are probably still wrong.
Current list, in the order above:

figure with a green cone hat on roller skates · unknown (hidden) · long down
arrow + 3-bar chart (pink/yellow/green) · tied bow drawn in thin dark outline ·
solid terracotta rectangle · spiral calendar showing a large "25" · one dark
brown tall object + one blue/white tall object with a red top · US flag + red
barn with a gambrel roof and cupola · Oman flag · black Africa silhouette +
green bushy plant · cloud with snow · face with tears of joy · window (frame
with a divider) · **rock + eagle** · unknown.

## 5. What is ruled out — by arithmetic, not by taste `[DEAD]`

The numerals are **not a permutation** in either colour: red repeats 6 and 7,
blue repeats 4, 5 and 8. Twelve red reads cover only eight distinct values, and
three unread pieces cannot supply the six missing ones. That single fact kills:

* **chain / closed loop** — "red = this piece's id, blue = the next piece's id".
  Tempting, because five pieces do form a perfect closed 5-cycle
  (US flag → bow → snow → bar chart → Africa → US flag, 7→5→9→8→4→7), but the
  successor is ambiguous everywhere else.
* **ordinary dominoes** — equal ends touching. Eight values occur an odd number
  of times; a chain allows at most two.
* **"red = letter index, blue = position in the answer"** and its mirror. Blue V
  is on both the Oman and the snow-cloud piece, so two letters would claim the
  same position.
* **"the two numerals are the letter-counts of the two pictures"**. About half
  fit strikingly (BARCHART = 8, DOWNARROW = 9, ROLLERSKATE = 11, BARN = 4) and
  the other half do not fit at all.

Do not re-derive these. If you revive one, say which specific read you are
overturning and show the measurement.

### 5a. The one reading still alive — and its open test

`[MEASURED]` The two colours behave differently: **red never exceeds 10, blue
reaches 14**. Two numerals meaning the same kind of thing would not do that.
That asymmetry reads as **red = a letter index inside a short word, blue = a
position in a long string**.

A counting argument briefly made blue look like a permutation of 1..15 (nine
distinct values, three duplicate pairs, six missing values, three unread
pieces — it balanced exactly). It predicted that one numeral in each duplicate
pair was misread. **I tested that and it failed:** both blue V numerals (Oman
flag, cloud with snow) read as a clean isolated V across three independent
renders. The collision is real, so blue is not a permutation. `[DEAD]`

What survives is weaker but testable: if blue is a position, **pieces sharing a
blue must yield the same letter**. Under emoji CLDR names, one of the three
pairs agrees (`FLAGUNITEDSTATES`[7] = `SPIRALCALENDAR`[3] = I — and the
calendar picture does have spiral rings) and two do not. One hit in three is
what chance gives, so this is not yet evidence. **The test cannot run until the
picture names are right, and the user has said mine are not.** Settle the
pictures first, then re-run this check — not the other way round.


## 6. The blocker, and the one thing that would break it open

`[MEASURED]` In 1080p a piece is **~45 px wide**; its numerals are ~10 px. Every
shot in the video was scanned — **there is no closer frame**. Multi-frame
super-resolution buys about 3× and then stops.

**There is no 4K.** The user has confirmed this video maxes out at 1080p, so
higher-resolution source is not coming and must not be asked for again. Every
remaining gain has to come from processing: more frames per piece, better
registration, and a real super-resolution estimator instead of a median.

## 7. Tools built for this (in the session scratchpad)

| tool | what it does |
|---|---|
| `piecesr.py SPEC.json OUT.png` | **the important one** — per-piece multi-shot SR. Each piece (or box face) is its own plane, so frames from *different camera angles* can be fused: warp each shot's reference quad to a canonical rectangle, then lock every frame to the template with **pyramid ECC** (¼ → ½ → 1, homography). A single global homography cannot do this — the box stack is 3-D — which is why the earlier multi-angle attempt failed. |
| `homo.py` / `warpreg.py` | single-shot ORB+RANSAC homography cache, then masked-median SR of listed regions |
| `sharp.py` | ranks frames in a time range by Laplacian variance over a crop |
| `allquads.py` / `findquad.py` | auto-detect piece outlines (b\* < 16 & L > 135) and return min-area-rect corners |
| `inkq.py` | red-vs-blue ink verdict from Δa\* against the card's own paper |
| `gwidth.py` / `strokes.py` | glyph width and stroke-run profiles (both **too noisy at this resolution** — read numerals by eye from the fused images instead) |

Homography caches: `h803.npz` (ref **t=803.527**, ctx 1450,300–1920,1050, 101
frames — the best shot in the video), `h806.npz`, `h807.npz`, `hn765b.npz`,
`hcache_office.npz`. Fused outputs: `PSR_topbox.png`, `PSR_usflag.png`,
`PSR_eagle.png`, `GLYPHS_top.png`.

## 8. Where to pick up

1. Read the last three pieces (window, rock+eagle, the 15th) with `piecesr.py`.
2. Pin down the ambiguous pictures — the two tall objects, the calendar's
   number, the hidden picture on the "I VII" piece.
3. Extract the **edge profiles** of the pieces (tooth count, tab shape). That is
   an assembly route that does not depend on the numerals at all, and the
   numerals have so far refused every ordering.
4. Build a model only from measurements. Four models have already been built and
   retracted in this hunt; each time the cause was modelling ahead of the data.

**Standing constraints:** never submit anything to the contest form — every
submission is the user's. Never probe the entry endpoint. Keep the old $1M
puzzle's material out of this work. Answer the user in Azerbaijani.
