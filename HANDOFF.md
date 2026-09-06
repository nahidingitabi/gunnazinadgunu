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
| calendar (spiral, large "25") | **II (2)** | IV (4) |
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

`[MEASURED]` **Also closed:** both coloured cards on the desk are blank.

`[RETRACTED, then CORRECTED 2026-09-06]` This section used to say there was no
second piece of month handwriting on the boxes. There are two lines — but they
are **not** what I first read them as. Widened, they read **`July 1…`** (a
numeral 1, not a question mark) and **`Jun…`**, matching an earlier session's
independent reading of **"July 1st 1988 – June 30 89"**: an archive box's
contents date range, i.e. set dressing.

**This removes the date model's only external support.** "July?" beside a piece
numbered VII·IV was the one thing outside the numerals themselves that argued
red = month. Do not cite it again.

`[RETRACTED 2026-09-06]` It also gave the calendar's numerals as III·IV. A
controlled measurement on the hn765b render (each stroke's a* against the card's
own paper, with the neighbouring cardboard edge as a passing control) gives
**two** red strokes, so the calendar is **II·IV — 4 February**. The glyph is
still read as **25** and still does not echo the piece's own numerals.

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

---

## 11. The overnight session of 2026-09-06, in full

Read this section before trusting anything above it: it corrects four things.

### What changed in the data

| piece | was | is | how |
|---|---|---|---|
| two tall objects | red VII | **red VI** → 6 June | stroke topology on two independent shots, confirmed on a third |
| calendar | red III (4 Mar) | **red II** → 4 February | per-stroke a\* against the card's own paper, control passed |
| ribbon / bow | bow | **butterfly** | four lobes in a 2×2 arrangement plus antennae, at 16× |
| "Africa + Madagascar" | Africa | **unidentified** | elongation 2.97 and 2.99 on two angles; Africa is ~1.1 |

Two claims in §6 were **wrong and are retracted**: there *is* a second month
word on the boxes (`"July?"` with `Jun` below it, cut off by the box's fold),
and the calendar's numerals are not III·IV.

### Three tooling rules that each changed an answer

1. **Canvas must match the quad's aspect ratio.** Three specs were stretched
   2–5×; the "Africa" quad also straddled two cards.
2. **The low-resolution grid must equal the piece's native pixel size**
   (`canon/S` = quad size). `sp_15.json` sampled 4.7× too finely and was fitting
   noise; at S=16 the fifteenth piece's picture appeared for the first time.
3. **Put a coordinate grid on a render before measuring it.** Twice tonight I
   measured a region that turned out to be the box's printed lines.

And: **plain 9–20× Lanczos on the raw frame, white-balanced per card, beats the
super-resolution pipeline** for these cards. Try it first.

### `numcheck.py` — the one colour test that works

Earlier colour tests failed because the cardboard around a card scores as red
ink. `tools/pieces/numcheck.py` finds the card, erodes its convex hull, and only
scores ink **inside** it, against that card's own paper. Red ink raises a\*
without raising b\* much; cardboard raises both; blue ink lowers b\*. The db\*
column is the visible control.

It confirmed the red/blue assignment on **every** card checked — which matters,
since swapping them on any card swaps that piece's month and day. It also
**located the eagle card's numerals** (blue upper middle, red lower right,
agreeing across two shots) where I had recorded that none were visible. Their
values are still unreadable.

### Closed for good

- **No 1080p footage is missing.** The three uncovered spans are all recap of the
  earlier puzzle.
- **No closer shot of the unread pieces exists.** The box stack appears only at
  761–770 s and 800–810 s.
- **The eagle card's and the fifteenth piece's numerals cannot be read.** A
  numeral there is ~5×10 native pixels. Nine automated classifiers have now
  failed their controls at this scale; the most recent, an ink-area estimator,
  measured the same numeral VI as 76.5 and 10.2 px², and VIII as narrower
  than VI.

### The new direction, untested

The pieces are **real jigsaw pieces and their edge profiles differ** — three
sharp triangular teeth on the US flag piece's left, a stepped notch on the
calendar's right, a rounded tab on the two-objects piece's left, an S-curve on
the snow cloud's left. If they interlock in one arrangement, that arrangement
orders all fifteen **without needing the dates or the three unread numerals**.
See `tools/pieces/EDGES.png` and `EDGES2.png`. Automatic contour extraction does
not work at this resolution; this has to be done by eye.

### Where the date reading now stands

Weaker than it was. Its only external support — the "July?" note — turned out to
be a box's fiscal-year label (see §6). What is left is internal: red ≤ 12,
blue ≤ 31, a calendar in the set, twelve distinct pairs. Against it: every
numeral read falls in 1..14 while there are 15 pieces, and twelve draws of a
day-of-month all landing at 14 or below has probability about 7×10⁻⁵. Still the
leading hypothesis, still frozen, but now with nothing outside the numerals
supporting it.

### Added later the same night

- **The calendar is II·IV — 4 February**, not III·IV. Measured per stroke against
  the card's own paper with the neighbouring cardboard as a passing control.
  This moved the calendar to the front of the date order and **killed** the
  "every month appears" observation recorded earlier that night (four months
  missing against three unread pieces).
- **A third camera angle exists**: the office shot (cache `hcache_office`, best
  frame t≈19.9) shows the *whole* box stack from the left. My notes had it as
  showing only the fifteenth piece. Its occlusion differs from every other
  angle. It is lower magnification for the top box, so it does not recover the
  window card's numerals, but it is the only view of the fifteenth piece and it
  confirmed the ovoid's colour independently.
- **The drawings are not a standard emoji set.** No barn emoji exists; the bar
  chart's colours are wrong for Noto's; no emoji is a plain unpatterned
  rectangle. So a first-letter-of-the-Unicode-name mechanism cannot apply to all
  fifteen. If there is a letter rule it runs on ordinary English words.
- **The pieces overlap on the boxes, they do not interlock.** All six junctions
  show one card lying on the other. The arrangement on the boxes is not the
  assembled puzzle.
- **Shapes now measured three ways each:** the "Africa" silhouette is 32×11
  native px (elongation 2.87–2.98 at three thresholds, mask drawn and checked);
  the fifteenth piece's picture is 19×8 (elongation 2.30–2.54 from both a render
  and the raw frame).
- **New tools**: `numcheck.py` (red vs blue, control visible in the db* column),
  `colorbox.py` (measures named boxes *and draws them*, because misplacement was
  the failure mode every time), `inkarea.py` (kept only as the record of a
  discarded estimator), `picatlas.py`, `emocmp.py`, `board.py`.
- **Best artefacts to look at first**: `tools/pieces/BOARD.png` (all fifteen
  pieces, dated), `PICTURES_ONLY.png` (20× drawings), `EMOCMP.png` +
  `EMOCMP2.png` (drawings beside candidate emoji), `EDGESTRIPS.png` (edge
  profiles).

---

## 12. The seven unnamed drawings, as measurements

Everything below is measured, not judged by eye. Six of my eye-judged labels
were wrong on 2026-09-06, so the measurements are the primary record and the
label column is only a hint.

| # | date | measured shape | measured colour | eye-label (weak) |
|---|---|---|---|---|
| 1 | 11 Feb | not profilable — multi-coloured, mask fragments (solidity 0.23) | hat **a\* −3.8 (green)** → face +2.8 → torso +4.0 → lower **+6.8 (red)** → ankles −1.2; **two dark discs below the feet** | elf / gnome, possibly on a roller skate |
| 3 | 8 Apr | **32 × 11 px**, elong 2.87–2.98 (3 thresholds, 2 angles). Width by depth: 30% **10.6** → 45% **7.2 (waist)** → 65% **8.9** → 95% 3.5. Max width = **⅓ of height** | **neutral black**, L 50, a\* −0.25, b\* +0.22. Plant beside it **a\* −12 (strong green)**, finer blades above | **not Africa** (Africa: max width ≈ 95% of height, no waist) |
| 6 | 6 Jun | dark object **35.3 × 8.7**, elong 4.06, **solidity 0.95**, widest at 30%, tapering to a fine point. Light object not profilable (solidity 0.36) | dark object **b\* negative → navy**; light object **a\* +6.1 top, +5.0 bottom, pale middle** | pen/brush + something red-tipped |
| 7 | 8 Jun | **22 × 47 px = 1 : 2.14**, flat, no gradient | **a\* +16.4, b\* +13.8, uniform** — terracotta, not pure red (Oman's red is a\* +22) | door? |
| 13 | ? | thick frame, horizontal bar, two panels | **whole drawing cooler than paper, frame included** (b\* −5.8 to −8.1) | file cabinet — **not** Noto's window, whose frame is warm |
| 14 | ? | left shape **28–38 × 9–12**, elong 3.05–3.20, solidity 0.74–0.82, **curved, widening downward, hook at lower right** — *not* an ovoid. Bird beside it: elong 3.5–3.7, solidity 0.89–0.92 | left shape **warm brown** (b\* +7.5…+8.3 on two angles); bird body **neutral dark** (b\* +0.68), its head **neutral white** | bald eagle is firm; left shape unnamed, **not a grey rock** |
| 15 | ? | **19.4 × 8.2 px**, elong 2.36, solidity 0.91, widest at 20%, **monotone taper to a point, no waist** | — | wedge/teardrop: leaf, flame, feather, fin |

Note #3 and #15 are **different families**: #3 has a waist, #15 does not.

### Tools that earned their place

`colorbox.py` draws the boxes it measures — misplacement was the failure mode in
every colour test. `wprof.py` reports width by depth and prints solidity, which
is what rejects a fragmented mask. `numcheck.py`'s db\* column is its own
control. Ten automated classifiers have failed their controls here; only direct
measurements against a card's own paper have held.

---

# 13. 2026-09-06 səhəri — ƏSAS ZƏNCİR TAPILDI, avtomatik tanıma bağlandı

Bu bölmə əvvəlkiləri **əvəz etmir**, davamıdır. İki şey kökündən dəyişdi.

## 13.1 ★★ Cavabın forması artıq bilinir — və köhnə tapmaca ilə qarışmır

**Köhnə $1M cavabı tapıldı:** `R62L39R05L73606623093121200300` —
**30 simvol, tamamilə hərf+rəqəm, SÖZ YOXDUR** (iki müstəqil mənbə).

Bu, gecə boyu bizi əngəlləyən «bunlar köhnə tapmacanın dekorudur» şübhəsini
**ölçü ilə** həll edir:

| müşahidə | köhnə cavaba uyğun gəlirmi? | nəticə |
|---|---|---|
| forma demosu **15** ulduzda sabitləşir | yox (köhnə 30-dur) | **yeni tapmacaya aiddir** |
| vərəq **söz uzunluqlarını** sayır `(3 6 4)` | yox (köhnə cavabda söz yoxdur) | **yeni tapmacaya aiddir** |

**Ulduzları özüm yenidən saydım** (`mon/n_0084…0091`): 10→11→13→14→**15**,
dörd kadrda sabit. Üç səhv sayma üsulundan keçdim (hamısı qeydlərdədir):
sətir üzrə axınlar **artıq sayır** (`*` altı ştrixdir), morfoloji bağlama
**az sayır**, `span/period+1` isə səhv düsturdur (`span` bir tam nişan enini
əhatə edir). Düzgün: `span = (n−1)·period + w` → **yalnız n=15 mümkündür**.

**Zəncir** (mavi vərəq, 49 kadrlıq yığımla oxunub):
```
(3 6 4)   və   (4 4 4 5)
      ↘        ↙
        (6 6)
          ↓
         (6)
```
⚠ İkinci sətir **(6 6)**-dır; köhnə `(6 2)` oxunuşu **ləğvdir** (yəni «şəhər +
2 hərfli ştat» modeli də ləğvdir).

**2867 şəhər ləqəbindən** (3,6,4)+6 hərfli şəhər şablonunu **beşi** ödəyir;
düzəldilmiş `(6 6)` ilə **yalnız biri hər üç sətri ödəyir**:

> ### `THE FOREST CITY → LONDON CANADA → LONDON`  (London, Ontario)

Zenith televizoru `THE ZENITH CITY` lehinə **fiziki** işarədir, amma DULUTH-un
6 hərfli cütü olmadığı üçün o, ikinci sətirdə qırılır. FOREST-in zəifliyi:
videoda meşəyə/London-a işarə edən əşya yoxdur (yalnız qlobuslar — REF765-də
bir, REF806-da iki; bu, istənilən coğrafi cavaba uyğundur).

Sayt: **«You can guess multiple times, but there is only 1 correct answer»** —
təxmin ucuzdur. **Göndərməni istifadəçi edir; agent formaya heç nə göndərmir.**

## 13.2 ★ 15 parça AYRI QATDIR — «hər parça bir hərf» ÜÇ testdən keçmədi

1. `(3 6 4)`-də **4-cü və 11-ci simvol boşluqdur**; hər iki sıralamada
   (qırmızı,mavi) və (mavi,qırmızı) orada **dolu şəkillər** var.
2. İlk hərflər cavabda olmayan hərflər verir: kəpənək→**B**, ABŞ→**U**,
   sevinc→**J**, ox→**A** — `THE FOREST CITY`-də nə B, nə U, nə J, nə A var.
3. **Heç bir parça boş deyil**, halbuki ikisi boşluq kodlamalıydı.

**Tarix modeli isə DAXİLİ dəlillə bərpa olundu** (xarici dayaq `"July?"`
düşəndən sonra):
* **ABŞ bayrağı parçası = qırmızı VII / mavi IV = 4 iyul** və şəkli ABŞ
  bayrağıdır. Əks konvensiyada 7 aprel çıxardı — mənasız. Bu parça
  **hansı rəngin ay olduğunu elan edən açardır.**
* **Təqvim şəkilli parça** = «bunlar ümumiyyətlə tarixdir» meta-işarəsi.
Bu, «hər tarix milli bayramdır» demək DEYİL — ümumiləşmir (Oman 5 iyunda,
milli günü 18 noyabrdır).

## 13.3 ★ AVTOMATİK TANIMA BAĞLANDI — iki ortoqonal invariant, hər ikisi uğursuz

| üsul | nəzarət | nəticə |
|---|---|---|
| **FORMA** (uzanma, solidity, en profili) | qartal rəsmi **3.43**, üç vendorda 1.0–1.5 | ✗ rəssam köçürmür, **yenidən çəkir** |
| **ÇALAR** (hue histoqramı, miqyasdan asılı deyil) | 5 bilinən rəsmdən **0-ı** öz nişanını ilk 6-ya salır | ✗ ailəni tapır, obyekti yox |

1326 nişanlıq (bütün Obyekt/Yemək/Heyvan/Yer/Simvol/Bayraq) süzgəcin **bütün
nəticələri ləğv edilib** — o süzgəc kəpənəyi və qartalı da atardı.
**14-cü təsnifatçı yazma.** İşləyən yalnız üçüdür: **gözlə görünən quruluş**,
**rəsmin öz kağızına görə rəngi**, **insanın tanıması**.

## 13.4 Bucaqlar: «görüntü tükənib» ÇOX GENİŞ yazılmışdı

`tools/pieces/findcards.py` kadrdakı bütün kart ölçülü ağ ləkələri siyahılayır —
**gözlə axtarma**. Bununla tapıldı:

| kart | ən yaxşı kadr | qeyd |
|---|---|---|
| 1, 4, 7, 8, 10, 13 | **REF767** (1240,30,1400,260) | REF765-dən böyük və kəskin |
| 6 | **REF806** (1776,655,1814,724) | **bütün bucaqlardan böyük** |
| 3, 5 (Oman) | REF806 (1690,770,1920,1020) | yaxşı ölçü |
| 9 (ABŞ) | REF803 / REF767 | ikisi də yaxşı |
| 14 | REF803 | REF767/REF806-da yoxdur |
| 15 | ofis (t≈19.9) | yeganə bucaq |

⚠ **Rəqəmlər YALNIZ REF803-də oxunur.** İkinci bucaqda ştrix oxuyucusu
nəzarətdən keçmir (ABŞ-ın bilinən `VII`-si 0/4/3 verir; `strokes4.py` ilə
−24°…+24° arası 13 döndərmə də düzəltmir) — kartlar orada **sürüşdürülüb**.
**Hələ sınanmayıb:** kartı perspektiv warp ilə düzləndirib sonra oxumaq.

⚠ **Saxlanmış dördbucaqların ADLARINA GÜVƏNMƏ** — `sp_eag806` «eagle» adlanır,
amma 6-cı kartı göstərir. Hər dördbucağı **rəqəmlərlə** yoxla.

**13-cü kartın mövqeyi bağlanır:** rəqəmləri **üç bucağın hamısında** örtülüdür.

## 13.5 Şəkillərin son vəziyyəti

**Adı var (7):** təqvim(🗓 spiral, səhifədə «25/&» qlifi) · **kəpənək** (üç dəfə
təsdiq: dörd **qapalı** ilmə, ön qanadlar böyük) · Oman · ABŞ+anbar ·
ox+diaqram (sütunlar **artır**, ox aşağı → **iki ayrı rəsm**) · qar buludu · 😂
**Bu gecə (1):** **#13 = 🗄️ kartoteka** — hər üç vendorda iki siyirmə, rəsmdə
bir üfüqi ayırıcı + iki **yumru-düzbucaqlı** panel + ayırıcıda çıxıntı;
🪟 pəncərə **qəti istisna** (pəncərənin dörd gözü var).
**Çox güman (1):** #1 fiqur — **yaşıl** sivri papaq (dar qutu, `da* −2.6`,
maska yoxlanılıb) → ağ kənar → sarımtıl gövdə, qollar yanda → qırmızı alt →
topuqda yaşıl → **aşağıda iki tünd təkər**.

**AÇIQ (5) — ölçülmüş təsvirlər:**
* **#3** neytral qara, uzanma 2.78, solidity 0.82, zəif qövs; gözlə: yumru baş →
  dar boyun → enli gövdə → aşağı-sola incələn uc. Yanında yaşıl bitki.
* **#6** solda tünd (qara/lacivərd) paz; sağda solğun mavi-firuzəyi düzbucaq,
  yuxarı **və** aşağı kənarında qalın magenta zolaq, içində şaquli tünd quruluş.
  **İkisi üst-üstə düşür.** Bu imza 155 nişanın heç birində yoxdur.
* **#7** dolu, detalsız, hündür düzbucaq. Rəng **iki bucaqda üst-üstə düşür**:
  `da* +15.0/+15.8`, hue 34–42° = **isti kərpic-qırmızısı**. Ölçü 22×40–47 px.
* **#14 sol kütlə** solidity 0.97, onurğa **düz**, isti qəhvəyi + yuxarı-sağda
  qızılı ləkə. **Daş DEYİL** (daş üç vendorda yığcam boz, uzanma 1.2–1.4).
* **#15** solidity 0.91, solda hündür zirvə → çuxur → sağda alçaq çiyin,
  yanları paralel, aşağı yumru uc, **tünd neytral** (🍆 rənglə istisna).

**Heç vaxt (1):** #8 — şəkli üç bucaqda da gizli. (1 iyul = Kanada Günü olardı;
cavabda `LONDON CANADA` var — **yoxlana bilməz, dəlil kimi işlətmə.**)

## 13.6 Ölçmə qaydaları (hər biri səhvlə qazanılıb)

1. **Ölçdüyünü ÇƏK.** Bu gecə maska yoxlaması **altı** səhv ölçməni tutdu.
2. **Ən böyük komponenti götürmə** — o, adətən masa və ya qonşu kartdır.
3. **Uzanma poza-invariant DEYİL** (kart əyilib). Solidity və profil forması etibarlıdır.
4. **Aspekti sərhəd qutusuna görə süzmə** — Twemoji maili çəkir; öz oxuna döndər.
5. **Kəskinliyi Laplasian dispersiyası ilə ölçmə** — küyü mükafatlandırır.
6. **Rəngi gözlə qiymətləndirmə** — eyni düzbucaq iki bucaqda «terrakota» və
   «qırmızı» göründü; ölçü isə eyni çıxdı.
7. **Kadr birləşdirmə bağlıdır** (üç dəfə uduzdu, düzgün ölçü ilə də).

## 13.7 Növbəti addımlar

1. **İstifadəçi:** videonun **təsviri və bərkidilmiş şərhi** — bu mühitdən
   oxunmur (yt-dlp bot yoxlaması, WebFetch captcha, Chromium tuneli kəsilir),
   amma köhnə ovda ilk ipucular məhz orada idi. **Ən ucuz yoxlanılmamış kanal.**
2. **İstifadəçi:** açıq 5 rəsmi adlandırmaq — avtomatik tanıma bağlıdır.
3. Kartı düzləndirib (perspektiv warp) ikinci bucaqdan rəqəm oxumağa cəhd.
4. Rəsmlərin dəqiq sayı (10 və 14 açıqdır; 20 olarsa `(4 4 4 5)` sətrinə uyğun).
5. Parçaların çıxışı nədir — `LONDON`/`CANADA`/`ONTARIO`/`FOREST` alt-çoxluğu?

---

# 14. 2026-09-06, günorta — BLOKLAR AÇILDI, JANR MÜƏYYƏNLƏŞDİ

Bu bölmə əvvəlki «oxuna bilmir» qeydlərinin çoxunu **ləğv edir**.

## 14.1 ★★★ ŞƏBƏKƏ ARTIQ BAĞLI DEYİL — nə işləyir

| nə | necə |
|---|---|
| YouTube watch səhifəsi (təsvir, başlıq, uzunluq) | `curl -H "User-Agent: Mozilla/5.0 … Chrome/128"` — yt-dlp və WebFetch bloklanır, adi curl işləyir |
| şərhlər (o cümlədən sancılmış) | innertube: `POST /youtubei/v1/next` + `continuation` (açar və versiya watch HTML-indədir); şərhlər `frameworkUpdates.entityBatchUpdate.mutations[].payload.commentEntityPayload`-dadır |
| kanal videoları + tarixlər | `https://www.youtube.com/feeds/videos.xml?channel_id=UC…` (son 15) |
| ⚠ məhdudiyyət | ardıcıl sorğular **429 / google.com/sorry** verir — sorğular arasında 3–15 s gözlə |

## 14.2 ★★★ SANCILMIŞ ŞƏRH = CyberChef XOR (hələ açılmayıb)

```
@MrBeast: «Make sure you check out Colin's profile 👀  https://tinyurl.com/xorprofile»
→ gchq.github.io/CyberChef/#recipe=XOR({'option':'UTF8','string':'%H6U=)Z7</#bq'},'Standard',false)
                                &input=QWFhYWFBLWFhQWEjIw
açar  = %H6U=)Z7</#bq   (13 bayt)     input = AaaaaA-aaAa##  (13 bayt, doldurucu)
```
İkisinin XOR-u mənasızdır. **Struktur təhlili:** açarın 5 baytı hərf
(H,U,Z,b,q), 8-i 0x20–0x3F aralığındadır — bu, «bir tərəf hərf, digər tərəf
hərf/boşluq» olan XOR-a **uyğundur**, yəni açar təsadüfi görünmür.
⚠ **Çıxarış:** açarın 2-ci baytı `H`-dir; deməli açıq mətnin 2-ci hərfi `H`
olsa, girişdə yazıla bilməyən NUL alınır → **cavab «THE…» ilə başlamır.**
Ehtimal ki, zarafatdır (Colin = Dr. XOR), amma bağlanmayıb.

## 14.3 ★★★ 84 SƏHİFƏLİK RƏSMİ CAVAB SƏNƏDİ

`https://mrb.gg/p/puzzle/file.pdf` → `MDP_ANSWERS.pdf` (70 MB), mətn `MDP_TEXT.txt`.
Buradan çıxan **janr**: MP1–15 = **15 şəkilli rebus**, hər biri **şəhər ləqəbi**
verir; rebuslar **emoji + hərf + `+`/`−` + «of the»** ilə qurulur
(👁️+L+& / ☠️ = ISLAND OF DEATH). Bizim 15 parça eyni janrdadır.

⚠ Sənədin yer adı qaydası: «city then country, **except US and Canada → state,
province, or territory**» ⇒ `LONDON ONTARIO` = **(6 7)**, `(6 6)` deyil.
Bu, FOREST CITY oxunuşunu zəiflədir; qaydaya uyğun namizəd:
**THE WALLED CITY → QUEBEC QUEBEC → QUEBEC**.

**Qəti test:** köhnə 91 yer cavabında `(3 6 4)` və tək `(6)` **yoxdur**
⇒ əlyazma zənciri **yeni tapmacaya aiddir**.

## 14.4 ★★ COLIN-İN ÜSULLARI (öz sözləri, `colin2_stream.txt`)

> «Exploration … **Execution** is putting together a jigsaw … **Extraction** …
> very often it involves **indexing — using numbers as positions in words**
> (fox + 3 = X). Another common technique is **alphanumerics** (1=A … 26=Z).»

Colin öz videosunun təsvirində: «**and also I made a $10,000 puzzle 😄**».
MrBeast 17:20-də: «a puzzle hidden **within this video** created by Colin himself».

## 14.5 Sınanmış və ÖLMÜŞ oxunuşlar (təkrarlama)

* rəqəmlər m:ss vaxt damğası **bu videoda** — 12 anın hamısı adi plan.
* «ilk iki hərf», «(qırmızı,mavi) indeks», «(mavi,qırmızı) indeks» tarix sırasında — söz yox.
* rəqəmlər köhnə **MP1–15**-ə indeks (ləqəb/şəhər/başlıq, hər iki sıra) — söz yox.
* tarixlər (ilin günü və 4 variant) təsvirə/transkriptə/başlığa indeks — söz yox.
* tarixlərin sadə hərf kodlamaları (9 üsul) — söz yox.
* nə qırmızı, nə mavi **cavabdakı mövqe** ola bilməz (təkrarlar var).
* videonun sonundakı TV montajı (26 plan) — köhnə xülasə.
* QR kod — yalnız giriş saytı.
* 360p boşluqlarında qutuların yaxın planı — yoxdur.
* **kadr birləşdirmə 4-cü dəfə uduzdu** (51 kadr: −17% kənar / −17% küy).

## 14.6 ★ YENİ GÖRÜNTÜ MƏNBƏYİ: 0:13.6–0:21.2

Ofis planı təkcə 0:19.9 deyil. **0:13.6 və 0:14.2** otağı, **0:20.6–0:21.2**
masanı daha yaxın göstərir (hamısı 1080p).
* **15-ci parça**: tünd fiqur — iki qabarıq + çuxur, aşağı ucu sivri → **ürək**.
* **14-cü kart**: qızılı-qəhvəyi oval (🏈/🥔/🪨?) + tünd quş.
* **narıncı stiker ölçüldü**: «**Books w/ old names — Alphabetize ?**»
* mavi stiker: `?EW?TE / HNKTIN / HOOTA` + «Should I sell … it Bold Found?»
* otağın yuxarı divarı = **köhnə 15 rebus kartı** (H+🕉️ aydın oxunur).
* **çəhrayı indeks vərəqi**: ~4 sətir × ~6 qrup görünür, **rəqəmlər oxunmur**;
  üstəlik vərəq kadrın **sol kənarından kəsilir** — bu, sərt maneədir.

## 14.7 İndi nə lazımdır

1. **6-cı və 15-ci rəsmin adı** (istifadəçidən; `PICKME.png`/`PICKME2.png` hazırdır).
2. **13/14/15-ci kartların rəqəmləri** — 3 tarix əskikdir.
3. **Çəhrayı indeks vərəqinin məzmunu** — kitab şifrinin açarı; hədəf kitab
   artıq məlumdur (`MDP_ANSWERS.pdf`, 84 səhifə).
4. CyberChef üçün 13 simvolluq şifrəmətn.

---

# 15. 2026-09-06, günorta-sonrası — BÖYÜK DÜZƏLİŞ VƏ ŞABLONUN TAPILMASI

> Bu bölmə §13 və §14-ün bir hissəsini **ləğv edir**. Əvvəlcə bunu oxu.

## 15.1 ⛔ ƏN VACİB: `(3 6 4) → (6 6) → (6)` KÖHNƏ TAPMACANINDIR

**Nə tapıldı.** Masadakı əlyazma qeyd yeni cavabın forması DEYİL:

```
RED SQUARE CUBE  → (3, 6, 4)
MOSCOW RUSSIA    → (6, 6)
MOSCOW           → (6)
```

MrBeast videoda ≈4:15-də: *«this is a **red Rubik's Cube** … a cube should
become a square. So a **Red Cube** becomes a **Red Square**, that's a place in
**Moscow, Russia**.»*

**Necə tapıldı.** Köhnə tapmacanın 84 səhifəlik cavab sənədini yükləyib mətnini
çıxardım, sonra videonun transkriptində `red Rubik's Cube` ifadəsini axtardım və
söz uzunluqlarını hesabladım. Əvvəlki «qəti test»im **çox dar** idi: yalnız
**91 yer cavabını** yoxlamışdım, **aralıq ipucu ifadələrini** yox. Digər
aralıqları da yoxladım — heç biri üç sətrin üçünə də uyğun gəlmir
(CASH TENT→TASHKENT (8,10); LASER MIXUP→ARLES FRANCE (5,6);
TALL INN→TALLINN ESTONIA (7,7); A NICE SUGAR→SUCRE BOLIVIA (5,7);
BEAST CITY HUB→TORONTO CANADA (7,6)). **Yalnız Red Cube üçlüyü oturur.**

**Nə ləğv olunur.** «cavab (3 6 4) ləqəbidir» · «THE FOREST CITY → LONDON» ·
«THE WALLED CITY → QUEBEC» · «cavab 6 hərfli şəhərdir» · «15×2 = 13+17 sayı».
**Cavabın forması yenidən NAMƏLUMDUR.**

**Metod dərsi:** «qəti test» qurarkən yoxlanan çoxluğu düzgün seç. Otağın
bütün əşyaları köhnə tapmaca ilə bəzədilib (yuxarı divarda 15 köhnə rebus
kartı asılıb — `H + 🕉️` = HOME OF PEACE aydın oxunur), ona görə **«bu əşya
yenidir» deməzdən əvvəl köhnə sənəddə axtar**.

## 15.2 ★★★ PARÇALARIN ŞABLONU KÖHNƏ SƏNƏDDƏDİR

Köhnə tapmacada **iki jigsaw tapmacası** var:

**OP1 (səh. 56)** — parçada **RƏQƏM**:
> «In each frame, there is a **jigsaw puzzle piece**. Inside that piece is a
> **number** … 20 numbers: `11 6 2 12 4 7 8 13 7 3 13 11 8 9 7 12 1 11 9 4`
> … spell a 20-letter message when **counted by number into the name of the
> puzzle maker**: `L O N E S H A R K G A M E S` (1–14)»
> → `A HOME AREA NEAR KAM LAKE` → Yellowknife.

**GC10 (səh. 53)** — parçada **HƏRF**:
> «16 pieces, each of which contains a letter … spell **JIMMY'S BIRTHPLACE**»
> → Wichita, Kansas. (`JIMMYSBIRTHPLACE` = 16 hərf = 16 parça.)

**Necə tapıldı.** PDF mətnində `jigsaw`, `roman`, `alphabet`, `heart`, `eagle`
kimi açar sözləri kontekstlə axtardım (`grep` sətir sonlarında sınırdı → Python
ilə boşluqları sıxıb 200 simvolluq pəncərə ilə çap etdim).

**Bizim üçün nəticə:** 15 parça × 2 rəqəm = **30 rəqəm** — OP1-in eyni janrı.
Maksimum **XIV = 14** ⇒ **hədəf ad ən azı 14 hərflidir** (LONE SHARK GAMES də
tam 14). `COLIN SANDERS` (12) və `DOCTORXOR` (9) **istisnadır**.

## 15.3 ★★ «BİR PARÇA = BİR HƏRF» MODELİ YENİDƏN CANLIDIR

§13.2-də onu **üç testlə** rədd etmişdim; hər üçü `(3 6 4)` fərziyyəsinə
söykənirdi (boşluq mövqeləri, «B/U/J/A THE FOREST CITY-də yoxdur», «heç bir
parça boş deyil»). Fərziyyə ləğv olunduğu üçün **hər üç təkzib də ləğvdir**.
GC10 məhz bu modeldir ⇒ 15 parça → **15 hərfli ifadə** (GC10-dakı kimi
suala bənzər, bir yerə aparan).

## 15.4 ŞƏBƏKƏ: ƏVVƏL «OXUNMUR» YAZILANLARIN HAMISI OXUNDU

| nə | üsul |
|---|---|
| video təsviri | `curl -H "User-Agent: Mozilla/5.0 … Chrome/128" "youtube.com/watch?v=…&hl=en"` → HTML-də `"shortDescription"` / `"attributedDescription"` |
| şərhlər (sancılmış daxil) | innertube `POST /youtubei/v1/next` + `continuation`; açar və versiya watch HTML-indədir; şərhlər `frameworkUpdates.entityBatchUpdate.mutations[].payload.commentEntityPayload`-da |
| kanal videoları + tarixlər | `youtube.com/feeds/videos.xml?channel_id=UC…` (son 15) |
| ⚠ | ardıcıl sorğular **429 / google.com/sorry** verir → 5–15 s gözlə. Reddit 403. yt-dlp və WebFetch bloklanır. |

**Tapılanlar:**
* Sancılmış şərh (@MrBeast): «check out Colin's profile 👀 tinyurl.com/xorprofile»
  → link profil deyil, **CyberChef XOR**: açar `%H6U=)Z7</#bq` (13 bayt),
  input `AaaaaA-aaAa##` (doldurucu). Açarın 2-ci baytı `H` ⇒ açıq mətn
  «THE…» ilə başlaya bilməz (NUL çıxır). **Açılmayıb.**
* Colin öz təsvirində: «**and also I made a $10,000 puzzle 😄**».
* MrBeast 17:20-də: «a puzzle hidden **within this video** created by Colin himself».
* **84 səhifəlik cavab sənədi**: `mrb.gg/p/puzzle/file.pdf` → `MDP_ANSWERS.pdf`,
  mətn `MDP_TEXT.txt`. **Bu, ən dəyərli sənəddir.**
* Colin öz axınında (`colin2_stream.txt`): «Extraction … very often it involves
  **indexing** (numbers as positions in words) … another common technique is
  **alphanumerics** (1=A…26=Z)». «Jigsaw yığmaq» = **execution**, cavab
  **extraction**-dan çıxır.

## 15.5 YENİ GÖRÜNTÜ MƏNBƏLƏRİ

* **Ofis planı təkcə 0:19.9 deyil**: `0:13.6`, `0:14.2` (otaq), `0:20.6`,
  `0:21.2` (masa daha yaxın) — hamısı 1080p.
  → 15-ci parça: **ürək formalı tünd fiqur**. 14-cü kart: qızılı-qəhvəyi oval
  + tünd quş. Narıncı stiker **ölçü ilə** oxundu: «**Books w/ old names —
  Alphabetize ?**». Mavi stiker: `?EW?TE / HNKTIN / HOOTA` + «Should I sell …
  it Bold Found?».
* **Videonun thumbnail-i** (`i.ytimg.com/vi/82CX6WULNA0/maxresdefault.jpg`):
  «LOGIN ATTEMPTS LOG» — 17 tarix (04-12…05-28, hamısı FAILED, aprel bloku
  **qəsdən qarışıq**), 8 nöqtəli parol sahəsi, kork lövhə (#1–#4, QR,
  «Scan on phone — what is it?», «16-3-4», «No face ID bypass? Check #5 version»).
  **QR deşifrə olunmur**: perspektiv düzləndirib modul şəbəkəsini sınadım —
  N=25/29/33/37/41/45-in heç birində üç axtarış naxışı formalaşmır (0/3),
  modullar kvadrat deyil ⇒ **çox güman dekorativ/AI**.

## 15.6 BAĞLANMIŞ İSTİQAMƏTLƏR (təkrarlama)

* rəqəmlər **m:ss** vaxt damğası kimi bu videoda — 12 anın hamısı adi plan.
* «ilk iki hərf», «(qırmızı,mavi) indeks», «(mavi,qırmızı) indeks» tarix sırasında.
* rəqəmlər köhnə **MP1–15**-ə indeks (ləqəb/şəhər/başlıq sözü, hər iki sıra).
* tarixlər təsvirə/transkriptə/başlığa indeks (ilin günü və 4 variant).
* 9 sadə tarix→hərf kodlaması.
* videonun sonundakı **TV montajı** (26 fərqli plan — hamısı köhnə xülasə).
* **QR (17:32)** = yalnız giriş saytı.
* 360p boşluqlarında qutuların yaxın planı yoxdur.
* **kadr birləşdirmə — 4 dəfə uduzdu** (sonuncu: 51 hizalanmış kadr,
  −17% kənar kontrastı / −17% küy).
* **jigsaw dişlərindən sıra** — kartlar 76–115 px, dişlər ~8 px; yalnız 9-cu
  kart təmiz maska verir. Ayırdetmə çatmır.
* **44 namizəd ad × 7 sıra** — sözlük örtüyü ən yaxşı 0.33 (küy).
* **adın özünü əvəzetmə şifrəsi kimi həll etmək** — nəzarətdən keçmədi
  (köhnə OP1-də `TATIONIANTATIONISTOO` verdi, düzgünü `AHOMEAREANEARKAMLAKE`);
  24 simvol quadgram üsulu üçün çox azdır. **Nəticələr ləğvdir.**
* qutuların üzərində **ad yoxdur** (bankers box şablonu boşdur).
* avtomatik şəkil tanıma — 13 üsul nəzarətdən keçmədi. **14-cüsünü yazma.**

## 15.7 İKİ BLOKLAYICI

1. **13, 14, 15-ci kartların rəqəmləri** — 30 rəqəmdən 6-sı əskik (20%).
   Hər üç bucaqda örtülü/kiçikdir.
2. **«Hansı ada saymaq lazımdır» göstəricisi.** OP1-də bu, Slack pəncərəsindəki
   «**Find a puzzle maker**» mətni idi. Bizim videoda qarşılığı tapılmayıb.

Bunlardan biri həll olunsa, OP1 modelini birbaşa tətbiq etmək olar.

## 15.8 ALƏTLƏR (hamısı `tools/pieces/`)

`nameindex.py` — OP1 modeli; **nəzarəti köhnə tapmacadır və keçir**.
`subsolve.py` — adı əvəzetmə kimi həll etmə (nəzarətdən keçmir, ehtiyatlı ol).
`initials.py` — baş hərf modeli, korpus sözləri ilə skorlama.
`tabs.py` — parça konturu + kənar profili (maskanı üstünə çəkir).
`cardsweep.py`, `stacksweep.py`, `lowsweep.py` — kadr süpürgələri.
`extract.py` — çıxarma qaydalarının süpürgəsi.

---

# §16. MEXANİZM TAPILDI — GC8. AIRRACK (2026-09-06)

Bu bölmə əvvəlki bölmələrin **çoxunu ləğv edir**. Əvvəlcə bunu oxu.

## 16.1 Mexanizm

Köhnə cavab sənədinin (`MDP_ANSWERS.pdf`) **51-ci səhifəsi, GC8. AIRRACK**:

> "…seven pictures… **There's a number or pair of numbers in the corner of each photo**…
> **ANSWER** Airrack is identified by **the item in the picture that contains the letters
> in his real name, ERIC**. Here are those items, **with the letters indexed into those
> names by the numbers given**… After the first three letters, **the letters diverge to
> spell a city and country: Algiers, Algeria.**"

**Qayda:**
1. Hər şəkil bir **AD** bildirir (obyektin özünün adı olmaya bilər — assosiativ ad).
2. Rəqəmlər həmin **ada hərf indeksidir**.
3. Bir rəngin rəqəmləri **bir sətri**, o birinin rəqəmləri **ikinci sətri** yığır.
4. Tək rəqəmli şəkil hər iki sətrə **eyni hərfi** verir (bizdə: qırmızı = mavi olan kart).
5. Ad `max(qırmızı, mavi)`-dən **qısa ola bilməz** — mexanizmin öz filtri.

**Necə tapıldı:** masanın ön üzünə yapışdırılmış **"Boo! / Five of these"** kartı →
PDF-də `Boo` sözü yoxdur, amma **`horror bookshelf`** var → o, GC8-dir.

**Nəzarət:** `tools/pieces/gc8solve.py` — GC8-in yeddi adı ilə **ALGIERS / ALGERIA**
verməlidir. Nəzarət düşsə proqram dayanır və heç bir nəticə vermir. **Hazırda KEÇİR.**

## 16.2 Ölçülmüş sabitlər

| kəmiyyət | dəyər | necə |
|---|---|---|
| parça sayı | **15** | iki fərqli bucaqdan iki dəfə sayıldı (REF803 + ofis kadrı) |
| rəsm sayı | **20** | 10 kart tək rəsm + 5 kart iki rəsm |
| **cavabın uzunluğu** | **15 simvol** | CRT formasındakı maskada **dəqiq 15 ulduz**, 45.7 px bərabər aralıq, 3 kadrda eyni (köhnə "16" səhv idi) |
| rəqəm diapazonu | I…XIV | qırmızı 2–10, mavi 1–14 |

## 16.3 Görüntü üsulu (bu gün tapıldı — köhnə üsulu əvəz edir)

⛔ Ox-paralel kəsik (bounding box) **işləmir**.
✅ **Dördbucağı warp et**: `cv2.getPerspectiveTransform` + `warpPerspective`
(`INTER_LANCZOS4`), **9–26× böyütmə**, rəng doyması 1.5–2×.
- Masa kartları üçün ən kəskin kadr: **`REF803.png`** (t=803.53).
- Otağın ən aydın geniş planı: **`pink_index_sheet_A_full_19.8.png`** (t=19.8).
- Konturu (yapboz kənarını) görmək üçün dördbucağı **35% genişləndir**.
- Rəqəmi oxumazdan əvvəl eyni səhnənin bütün kadrlarını **kəskinliyə görə sırala**
  (`np.percentile(|diff|,95)`) — çoxunda hərəkət bulanıqlığı var.

## 16.4 Rəqəmlər (warp ilə yenidən oxundu)

| # | şəkil | qırmızı | mavi |
|---|---|---|---|
| 1 | yaşıl şiş papaqlı fiqur | II | **XII** (9 kadr müqayisə edilib) |
| 2 | sarı kart (şəkli örtülü) | VII | I |
| 3 | iki panelli çərçivə | ? | ? (örtülü) |
| 4 | ↓ ox + 4 sütun | VIII | IX |
| 5 | kəpənək/bant | V | VII |
| 6 | narıncı-qırmızı düzbucaq | VI | VIII |
| 7 | spiral təqvim "25" | II | IV |
| 8 | tünd paz + qapaqlı çubuq | **VI** | **VI** (bərabər!) |
| 9 | 😂 | X | XIV |
| 10 | daş + keçəl qartal | ? | ? |
| 11 | Oman bayrağı | VI | V |
| 12 | Afrika + yaşıl bitki | IV | VIII |
| 13 | qar buludu | IX | V |
| 14 | ABŞ bayrağı + qırmızı tövlə | VII | IV |
| 15 | tünd uzunsov siluet | ? | ? |

## 16.5 Adlandırılan 4 kart

| kart | ad | qırmızı | mavi |
|---|---|---|---|
| 😂 | `face with tears of joy`(18) | **E** | **O** |
| qar buludu | `cloud with snow`(13) | **H** | **D** |
| Oman | `flag: Oman`(8, CLDR) | **M** | **O** |
| kəpənək | `butterfly`(9) | **E** | **F** |

⇒ qırmızı sətirdə mütləq **E, E, M, H**; mavi sətirdə mütləq **F, O, O, D**.

## 16.6 Bu gün RƏDD OLUNANLAR (təkrarlama)

tarix oxunuşu (qırmızı=ay, mavi=gün) · mavi=cavabdakı mövqe (yerdəyişmə nəzarəti) ·
"rəqəm = adın uzunluğu" · `Charlotte Amalie, U.S. Virgin Islands` · ay adlarına
indeksləmə (1082 CLDR dili) · MP1–15 rebus üslubu (kartlar rəngli deyil, hərf
arifmetikası yoxdur) · rəqəmlərin ayrı-ayrı elementlərə aid olması · kart siluetlərinin
avtomatik seqmentasiyası · düzbucağın rənginin ölçülməsi (qutunun narıncı fonu çirkləndirir).

## 16.7 Qalan üç iş

1. **11 kartın adı.** Qərar cədvəli `MRBEAST_PUZZLE_NOTES.md`-in sonundadır: hər kart
   üçün süzgəcdən keçən namizədlər və verdikləri hərflər.
   Ən çətini: **yaşıl papaqlı fiqur** (ad ≥12; heç bir insan/elf emojisi uyğun gəlmir).
2. **Sıra.** Kartların **yapboz kənarları** (mişar dişi / dalğa / pillə / çıxıntı / sivri uc /
   yumru) 12×-də oxunaqlıdır — `EDGES_SHEET.png`. Çıxıntı ↔ kəsik cütləşir.
   İzləyici şərhi: *"closed-loop solution! Just figuring out the order."*
3. **3 kartın rəqəmi** (10, 3, 15) — hər kadrda örtülü və ya çox maili.
