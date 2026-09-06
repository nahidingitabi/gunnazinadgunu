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
| top dark box, lower row | 2 — **butterfly** · red-brown rectangle |
| right of the top box | 1 — cloud with snow |
| middle box | 2 — calendar · two tall objects |
| right box | 1 — US flag + barn |
| tilted "CONTENTS FROM … DEPT" box | 2 — 😂 · rock + eagle |
| lower box | 2 — Oman flag · **unidentified silhouette** + green plant |
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
| **butterfly** 🦋 | V (5) | VII (7) |
| red-brown rectangle | VI (6) | VIII (8) |
| calendar (spiral, large "25") | III (3) | IV (4) |
| two tall objects | **VI (6)** | VI (6) |
| 🇺🇸 US flag + red barn | VII (7) | IV (4) |
| 🇴🇲 Oman flag | VI (6) | V (5) |
| **unidentified silhouette** (elongation 3.0) + green plant | IV (4) | VIII (8) |
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


## 6. What is settled, and what is closed for good

`[MEASURED]` **Numeral reading is finished: 12 of 15.** The other three cannot
be read from this footage, each for a different reason, and none of them is an
algorithm problem:

| piece | why it cannot be read |
|---|---|
| window | its numerals sit **physically underneath** a neighbouring piece |
| rock + eagle | below 1080p — best view is 124×50 px; three separate attempts all failed |
| the fifteenth (lowest box) | below 1080p — 31×42 px, and it appears in no other shot |

`[MEASURED]` **The top-row ambiguity is resolved.** Magnifying the seam shows
the "I VII" piece and the window piece are **separate** — the first's lower-right
edge steps away with a yellow card beneath it, the second has its own left
margin and shadow line. So the count stays **fifteen**, the yellow card is not a
piece, and the I-VII numerals belong to the hidden-picture piece.

`[MEASURED]` **Also closed:** both coloured cards on the desk are blank; there is
no second piece of month handwriting anywhere on the boxes; the calendar's glyph
is **25**, which does *not* echo that piece's own numerals (III·IV), so it is
stock art rather than a confirmation of anything.

## 7. The date reading — leading, and frozen

`[MEASURED]` Handwriting on the box beside the US-flag piece reads **"July?"**,
and that piece's numerals are **VII · IV**, with a US flag on it. Read as
**red = month, blue = day**, that is the Fourth of July, and it explains at
once: red never exceeds 12, blue never exceeds 31, both colours repeat freely
(several dates share a month), and a calendar is among the pictures. All twelve
month-day pairs are distinct, as an ordering key requires.

`[INFERRED]` Its weakness is that the box is an archive box and "July?" may
simply label its contents. Its one testable prediction — that the unread pieces
would bring new months — **died with the numerals above**. It can now be neither
confirmed nor refuted from this material, so it is **frozen**: leading
hypothesis, nothing further built on it. Six models in this hunt died from
building on an untested one.

Dates, in order: 11 Feb (skater) · 4 Mar (calendar) · 8 Apr (Africa + plant) ·
7 May (bow) · 5 Jun (Oman) · 8 Jun (rectangle) · 1 Jul (hidden picture) ·
**4 Jul (US flag + barn)** · 6 Jul (two objects) · 9 Aug (arrow + bar chart) ·
5 Sep (snow cloud) · 14 Oct (laughing face).

## 8. Method — what actually moved the needle

`[MEASURED]` **Iterative back-projection beats the masked median**, because a
median discards the sub-pixel information that makes many frames worth more than
one. Same frames, same registration, different estimator:

| piece | median | IBP | |
|---|---|---|---|
| US flag + barn | 8.7 | **49.9** | 5.7× |
| two objects | 5.4 | **13.7** | 2.5× |
| fifteenth piece (283 frames) | 0.74 | **10.85** | 14.7× |
| rock + eagle, multi-shot | 1.4 | 1.2 | no gain |
| rock + eagle, **single shot + hand-placed quad** | — | **86.3** | 72× vs multi-shot |

**The binding constraint is registration, not the estimator.** The last row is
the proof: same solver, same frames, only the quad placed by hand instead of
automatically. Two corollaries, both measured:

* **Multi-shot is not always better than single-shot.** The calendar fused badly
  across shots and cleanly from one; the two-objects piece did the opposite
  (1.1 single against 13.7 multi). It depends on the angle between the shots and
  must be measured per piece.
* Set the low-resolution grid to the piece's **true pixel size** (canonical
  width / S ≈ native width). Wrong S either blurs or amplifies noise.

## 9. Where to pick up

1. **The pictures still need names** — that is the critical path. Several of my
   labels have already been wrong (the user corrected rock, eagle and the
   laughing face; back-projection then retired "red square", which is a
   *vertical* rectangle). Two more fell on 2026-09-06: the "bow" is a
   **butterfly**, and the "Africa" silhouette is **not Africa** (its elongation
   measures 3.0 against Africa's 1.1). `tools/pieces/PICS_MAX.png` (15x) and
   `PIECES_RAW803.png` (9x) are the current atlas — and note that **plain
   Lanczos zoom on the raw frame beat the whole back-projection pipeline**,
   because back-projection is only as good as its quad.
2. Two-picture pieces must yield **one** thing between them: seven pieces carry
   one picture, four carry two, which totals ~20 pictures against 15 pieces, so
   first-letter-per-picture cannot be the mechanism as it stands.
3. Only then re-test the date reading and the letter models against the names.

**Standing constraints:** never submit anything to the contest form — every
submission is the user's. Never probe the entry endpoint. Keep the old $1M
puzzle's material out of this work. **There is no 4K of this video; do not ask
again.** Answer the user in Azerbaijani.

---

## 10. Added 2026-09-06 (overnight)

Four things changed since §9 was written:

1. **The last open numeral is closed.** The two-objects piece reads **VI in both
   colours** → 6 June, not 6 July. Measured on two shots from different camera
   angles, and confirmed a third time on the h806 shot at 12x raw zoom. It is the
   only piece whose red and blue numerals are equal.

2. **A systematic bug in the piece specs.** Each spec's canonical canvas was
   compared against its own quad's aspect ratio. Three were badly stretched — the
   "Africa" renders 3.0–3.9x too wide, the first calendar spec up to 5.1x — and
   the "Africa" quad was also in the wrong place, straddling two cards. Nine
   other specs are sound. **Check this ratio before trusting any render.**

3. **Raw Lanczos zoom beats the pipeline.** 9–16x Lanczos on the raw frame,
   white-balanced against each card's own paper and chroma-amplified, is more
   legible than any super-resolved render for these cards. Use it first.

4. **Two questions are now closed for good:**
   - *Is 1080p footage missing?* No. The three spans with no 1080p (72–300,
     420–551, 640–722 s) are all recap of the earlier puzzle; no piece appears in
     them.
   - *Is there a closer shot of the unread pieces?* No. Contact sheets over the
     whole room segment (722–1066 s) show the box stack only around 761–770 and
     800–810 s, which is what the existing caches already cover.
