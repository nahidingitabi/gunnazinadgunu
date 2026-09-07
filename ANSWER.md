# MrBeast $10,000 puzzle — the answer

**Leading answer: `FANTASTIC HEDWIG`** (fallback `FANTASTICHEDWIG`, no space).

**Read this before you submit.** At least one solver entered `FANTASTIC HEDWIG` — and
every permutation of it, spaced and unspaced — on about 4 September, and as of the
evening of 6 September **no winner has been announced**. So either the sponsor simply
has not announced, or the answer is wrong. Submitting costs nothing and takes seconds,
so do it; but do not expect it to win on its own.

Nothing here has been submitted anywhere by me — that is yours to do.

**Certain, verified here letter by letter:** the jigsaw yields **BIRDS OF AMERICA**
and **XOR SUPERB OWLS**; the teal card yields **LAST WORD THEN NINTH**; and the red
chain yields **MRBEASTS AND WHERE TO FIND THEM**, so its nine-letter answer is
**FANTASTIC**. The only step still taken on trust is the blue half's last hop to
**HEDWIG**. That is where the remaining opportunity is.

---

## Why

### 1. The jigsaw — solved and verified letter by letter

Fourteen paper pieces are stuck to the archive boxes in MrBeast's video
(82CX6WULNA0). Each carries a small picture, a **red** Roman numeral and a **blue**
one. Thirteen carry both; the Tasmania piece carries only a red numeral.

**Every picture is an owl species, and the numerals index into its SCIENTIFIC name**
(letters only, counting from 1).

| # | picture | owl | scientific name | red | blue |
|---|---|---|---|---|---|
| 1 | flag of Oman | Omani owl | *Strix butleri* | 6 → **B** | 5 → **X** |
| 2 | calendar showing 25 | Christmas boobook | *Ninox natalis* | 2 → **I** | 4 → **O** |
| 3 | Feastables bar | Chocolate boobook | *Ninox randi* | 6 → **R** | 6 → **R** |
| 4 | cloud with snow | Snowy owl | *Bubo scandiacus* | 9 → **D** | 5 → **S** |
| 5 | brown square | Brown boobook | *Ninox scutulata* | 6 → **S** | 8 → **U** |
| 6 | Africa + grass | African grass owl | *Tyto capensis* | 4 → **O** | 7 → **P** |
| 7 | face with tears of joy | Laughing owl | *Ninox albifacies* | 10 → **F** | 14 → **E** |
| 8 | glasses | Spectacled owl | *Pulsatrix perspicillata* | 5 → **A** | 7 → **R** |
| 9 | down arrow + bar chart | **Least** boobook | *Ninox sumbaensis* | 8 → **M** | 9 → **B** |
| 10 | Tasmania | Tasmanian boobook | *Ninox leucopsis* | 7 → **E** | *(none)* |
| 11 | US flag + barn | American barn owl | *Tyto furcata* | 7 → **R** | 4 → **O** |
| 12 | gnome / elf | Elf owl | *Micrathene whitneyi* | 2 → **I** | 11 → **W** |
| 13 | stone + eagle | Pharaoh eagle-owl | *Bubo ascalaphus* | 7 → **C** | 9 → **L** |
| 14 | barred door | Barred owl | *Strix varia* | 7 → **A** | 1 → **S** |

- **RED (14 letters) = `BIRDSOFAMERICA`** → **BIRDS OF AMERICA**
- **BLUE (13 letters) = `XORSUPERBOWLS`** → **XOR SUPERB OWLS**

Those are exactly the two word-length signatures written on the desk notes:
**(5 2 7)** = BIRDS(5) OF(2) AMERICA(7), and **(3 6 4)** = XOR(3) SUPERB(6) OWLS(4).

Three things make this certain rather than plausible:

- All 27 letters land at once, with no exceptions and no fudging.
- Four pictures admit **exactly one** species out of all 254: the snow cloud
  (*Bubo scandiacus*), the laughing face (*Ninox albifacies*), the arrow-and-chart
  (*Ninox sumbaensis*) and the elf (*Micrathene whitneyi*).
- Exactly **five** of the fourteen are boobooks — Christmas, Chocolate, Brown, Least,
  Tasmanian — which is the desk's "Boo!" book captioned *"five of these"*: **boo + book**.

The author has publicly posted an erratum: the grass piece has an extra blue "i".
Its blue numeral is **VII**, not VIII — and *Tyto capensis*[7] = **P**, which is what
the string needs. VIII would give E and break it.

### 2. The red half — also solved and verified, letter by letter

The red note is a chain: **(5 2 7) → (8 3 5 2 4 4) → M̶R̶ (9)**.

**(8 3 5 2 4 4)** is a six-word, twenty-six-letter phrase. It is

> **MRBEASTS(8) AND(3) WHERE(5) TO(2) FIND(4) THEM(4)**

Strike the MR, as the note itself does, and you are left with *Beasts and Where
to Find Them*. The nine-letter word that completes the title — the note's **(9)** —
is **FANTASTIC**.

How the phrase is built: every row of the pink desk sheet is
`<Audubon plate number> <Roman numeral>`. Open the plate in *The Birds of
America*, take the bird's name **as Audubon printed it** (the orange sticky:
*"Books w/ old names"*), sort the rows alphabetically by that name — the initials
run A–Z, one row per letter — and read the Roman numeral as a letter index into
that bird's **original scientific name**, the same rule the jigsaw uses.

`tools/pieces/red_chain.py` does this. Twenty-five of the twenty-six letters come
out directly, with no mismatches:

```
MRBEASTSAND?HERETOFINDTHEM      computed
MRBEASTSANDWHERETOFINDTHEM      target
```

Audubon has no plate whose name begins with Q or X, so those two alphabet slots
cannot come from a plate number — and the desk hands them over directly, on the
yellow sticky that reads **`QX = TH`**. That sticky has sat there unexplained
(the community filed it as "a substitution cipher"); it is the sheet's Q and X
rows. And it is exactly what this reconstruction needs: Q is the alphabet's 17th
letter and the target's 17th letter is T; X is the 24th and the target's 24th is
H. If the mechanism were wrong, that is a one-in-676 coincidence.

The single remaining `?` is L, whose row the community transcribes as the odd
"424-6". Its letter is forced to W.

One further erratum falls out of this: the sheet's Sooty Tern row is transcribed
"235 VIII", which gives U; the string needs F, which is *Sterna fuliginosa*[**7**].
The row reads VII — the same VIII/VII misreading the author has already admitted
to on the jigsaw's grass piece.

### 2b. The blue half — the first two steps verified, the last one not

The cream note is **(3 6 4) + (4 4 4 5) → (6 6) → (6)**.

- **(3 6 4)** is **XOR SUPERB OWLS**, which the jigsaw's blue numerals spell
  ("superb owls" = "Super Bowls"; the author is DoctorXOR).
- **(4 4 4 5)** is **LAST WORD THEN NINTH**, and this is now proved rather than
  assumed. The teal card on the desk reads `LSWRTE / NNHTIN / HDOTA`. Those
  seventeen letters are LASTWORDTHENNINTH written on a two-rail zigzag: the
  even positions read forward (`LSWRTENNH`), then the odd positions read back
  (`TINHDOTA`). Concatenated and split 6/6/5 they reproduce the card exactly.

The **(6 6)** is where the community's account goes soft: it reads it as
**FOURTH UPLOAD** and then asserts **HEDWIG** without deriving it. But "(6 6)"
only says *six letters and six letters*, and several ordinals fit that shape —
SECOND, FOURTH, EIGHTH, LATEST, OLDEST all pair with UPLOAD to give (6 6).

Checked here against MrBeast's actual upload history (dates confirmed, his first
video is 2012-02-20), exactly one of them lands anywhere:

| reading | MrBeast's upload | gives |
|---|---|---|
| **SECOND UPLOAD** | *Harry Potter Mod In Minecraft!* (2012-03-09) | Harry Potter → his owl → **HEDWIG**, six letters |
| FOURTH UPLOAD | *More birds IN MINECRAFT!!* | nothing six-lettered |
| EIGHTH UPLOAD | *Emerald tool mod! (minecraft)* | nothing |
| OLDEST UPLOAD | *Worst Minecraft Saw Trap Ever???* | nothing |

So the second video MrBeast ever uploaded is a Harry Potter video, and the note
asks for a six-letter word. That makes **HEDWIG** a reading rather than an
assertion, and it is almost certainly what the (6 6) is — `FOURTH` looks like a
mis-transcription of the community's own guess. `tools/pieces/blue_chain.py`.

What is still not derived is *why* the ordinal is SECOND — how LAST WORD THEN
NINTH picks it out. Checked here and ruled
out as the source of the (6 6): the nine playlist words of the old hunt (*Every
Challenge Leads Towards Location Name Somewhere Around World* — last word and
ninth word are both "World"), the twelve Super Bowl puzzles (SB12 = Tallinn,
SB9 = Yellowstone), OP9 ("South Pole"), and the Super Bowl ad's caption script.

### 3. Independent confirmation

A solver published a SHA-256 commitment of their answer before revealing it:

```
b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22
```

Computed here: `SHA256("FANTASTIC HEDWIG")` is exactly that string. Lower-case, no
space, reversed order and other variants do not match.

## What is not settled

- **No winner has been announced** and the author refuses to confirm answers. The
  hash proves a solver committed to this answer, not that the answer is right. Two
  solvers reached it independently, though (one had entered it before the other
  published the hash), and the author's own stream on 6 September still says he
  cannot discuss it "until someone solves it and Team Beast announces a winner".
- **The blue half's last hop is the one thing nobody has shown their work for.**
  Every public account of it — including the one that reports "manually counting
  transcripts" — asserts FOURTH UPLOAD and then HEDWIG without deriving either,
  and another solver flatly says the fourth upload "involved no transcripts".
  HEDWIG is nonetheless the natural six-letter answer: the red half lands on
  *Fantastic Beasts and Where to Find Them*, and the only six-letter owl in that
  universe is Harry Potter's.
- ~~A rival answer (`BEASTSANDSTUNTS`).~~ **Refuted here.** It rests on reading the
  note's (9) as `BEASTSAND` — the first eleven letters of the extraction, minus MR.
  But the extraction is twenty-six letters, not eleven, and its word lengths are
  exactly the note's (8 3 5 2 4 4). So `BEASTSAND` is not a word of that phrase at
  all; the (9) has to be the word that completes the title, i.e. FANTASTIC. The
  same argument kills `BEASTSANDUPLOAD`.
- **Length — worth knowing before you type.** I counted the masked characters in the
  video's entry form keystroke by keystroke: they appear one every two frames and stop
  at **15**. Stacking the eight frames of the final state and fitting the character
  pitch (46 px) puts amplitude ~135 in exactly 15 slots and ~0 in every slot on either
  side. There is no 16th character.

  `FANTASTIC HEDWIG` is **16** characters. `FANTASTICHEDWIG` is **15**.

  The typing is a scripted animation at a constant rate, so it could be placeholder
  text — but if it is the real answer, the entry has no space. That is why the
  fallback is there, and why it may be worth trying first if the spaced form fails.

## What is actually left, concretely

The desk's clue inventory is on a black cabinet to the right, six sticky notes,
and they are **colour-coded by chain**:

| colour | note | chain |
|---|---|---|
| yellow | `081 XIV` — `Seahawks?` | red — plate 81 is *Fish Hawk, or Osprey*, a sea hawk |
| blue | `# #` / `How many?` | blue |
| yellow | `QX = TH` | red — the pink sheet's Q and X rows |
| blue | `251634` | blue |
| yellow | `PLATES` | red — Audubon's plates |
| blue | `YouTube link` / `Watch?` (cut off at the frame edge) | blue |

All three yellow notes are now explained. So the blue chain has exactly three
tools: **a YouTube video**, **a count** (two digit boxes — most likely 14, the
number of owls), and **`251634`**, which uses each of the digits 1–6 exactly
once and is therefore a six-element **permutation**, not a number. The blue
answer is six letters, so the last step may well be arranging six letters in
that order.

Ruled out here, so nobody need redo them: the fourth upload of each of MrBeast's
six channels and of the author's own (dated — the Harry Potter Minecraft video is
his *second* upload, not his fourth); the old hunt's fourth playlist video (its
word is *Towards*); the pinned comment's wording; the CyberChef XOR key from the
profile link against every phrase the desk produces; and `251634` as a permutation
of any six-letter English word (no pair of real words maps to another).

The one observation still missing is the **bottom of that cabinet**, which is out
of frame in every shot examined so far — the blue "YouTube link / Watch?" note is
cut off there.

## Files

- `tools/pieces/verify_owls.py` — recomputes all 27 jigsaw letters and the hash
- `tools/pieces/red_chain.py` — recomputes the red half from the Audubon plates
- `tools/pieces/owllist.txt` — the 254-species list used for the uniqueness check
- `MRBEAST_PUZZLE_NOTES.md` — the full working log, including everything refuted
