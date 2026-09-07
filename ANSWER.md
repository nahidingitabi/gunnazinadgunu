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

`tools/pieces/red_chain.py` does this. All twenty-three transcribed rows land on
target, with no mismatches:

```
MRBEASTSAND?HERE?OFINDT?EM      computed
MRBEASTSANDWHERETOFINDTHEM      target
```

The three `?` are the L, Q and X rows, which the community transcription of the
sheet does not carry (its L and X rows are written oddly — "424-6", "X VI" — and
no Q row was copied at all). So the sheet has twenty-six rows, not twenty-three.

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

What that instruction is applied to, and therefore the **(6 6)** and the final
**(6)**, is the one thing on the desk still unverified here. The community's
answer is **FOURTH UPLOAD** and then **HEDWIG** — Harry Potter's snowy owl, which
keeps the whole puzzle in one universe with FANTASTIC. Checked here and ruled
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
  hash proves a solver committed to this answer, not that the answer is right.
- Some solvers dissent; a rival answer (`BEASTSANDSTUNTS`) was argued and rebutted.
- **Length — worth knowing before you type.** I counted the masked characters in the
  video's entry form keystroke by keystroke: they appear one every two frames and stop
  at **15**. Stacking the eight frames of the final state and fitting the character
  pitch (46 px) puts amplitude ~135 in exactly 15 slots and ~0 in every slot on either
  side. There is no 16th character.

  `FANTASTIC HEDWIG` is **16** characters. `FANTASTICHEDWIG` is **15**.

  The typing is a scripted animation at a constant rate, so it could be placeholder
  text — but if it is the real answer, the entry has no space. That is why the
  fallback is there, and why it may be worth trying first if the spaced form fails.

## Files

- `tools/pieces/verify_owls.py` — recomputes all 27 letters and the hash
- `tools/pieces/owllist.txt` — the 254-species list used for the uniqueness check
- `MRBEAST_PUZZLE_NOTES.md` — the full working log, including everything refuted
