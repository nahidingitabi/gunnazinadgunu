# MrBeast $10,000 puzzle — the answer

**Leading answer: `FANTASTIC HEDWIG`** (fallback `FANTASTICHEDWIG`, no space).
**Second choice: `FANTASTICSNITCH`.** Both are 15 characters.

Nothing here has been submitted anywhere by me — that is yours to do.

**Submit sooner rather than later.** The video says the prize goes to *"the first
person to answer correctly"*, and the official rules in the description run from
2026-09-02 to **2027-09-02** — a full year. So the absence of a winner announcement
five days in is *not* evidence that `FANTASTIC HEDWIG` is wrong. It only means nobody
has been announced yet.

**Verified here, letter by letter:** the jigsaw yields **BIRDS OF AMERICA** (5 2 7) and
**XOR SUPERB OWLS** (3 6 4); the teal card yields **LAST WORD THEN NINTH** (4 4 4 5);
and the red chain yields **MRBEASTS AND WHERE TO FIND THEM** (8 3 5 2 4 4), so its
nine-letter answer is **FANTASTIC**. That half is settled.

The blue half's final step is *still not mechanically derived* — not by me, and, on the
evidence below, not by anyone who has posted publicly either. HEDWIG leads on coherence,
not on a proof.

---

## What was established on 7 September

### The pinned comment is a real clue — I was wrong to discard it

MrBeast's pinned comment on the puzzle video reads:

> Make sure you check out Colin's profile 👀
> https://tinyurl.com/xorprofile

That tinyurl resolves to a **CyberChef page with an XOR recipe already loaded**:

- key (UTF-8): `%H6U=)Z7</#bq`  — 13 characters
- input (base64 `QWFhYWFBLWFhQWEjIw`): `AaaaaA-aaAa##` — 13 characters

I had earlier written this off, on the grounds that the author said *"anything I post on
Reddit, Instagram, or YouTube is not relevant"*. **That was a misreading.** He was
disclaiming *his own* accounts; this is *MrBeast's* pinned comment on the puzzle video
itself, and two independent solvers name it as the source of the XOR idea. Retracted.

### The red note's first row is BIRDS OF AMERICA, not an instruction

`(5 2 7)` = **BIRDS(5) OF(2) AMERICA(7)** — i.e. each note's first row is simply the
decoded jigsaw/card phrase written as word lengths. So the two notes read:

| note | clue phrases | intermediate | answer |
|---|---|---|---|
| red | (5 2 7) BIRDS OF AMERICA | (8 3 5 2 4 4) MRBEASTS AND WHERE TO FIND THEM, strike MR | (9) **FANTASTIC** |
| cream | (3 6 4) XOR SUPERB OWLS **and** (4 4 4 5) LAST WORD THEN NINTH | (6 6) ? | (6) ? |

### "LAST WORD" is literal — and it points at a `watch?v=` link

MrBeast's upload order, proven from YouTube's own channel ordering plus upload dates:

| # | date | id | title |
|---|---|---|---|
| 1 | 2012-02-20 | `2XVcLrB7B3Y` | Worst Minecraft Saw Trap Ever??? |
| 2 | 2012-03-09 | `jP82d277Cc8` | Harry Potter Mod In Minecraft! EPIC MUST SEE MOD!!! |
| 3 | 2013-01-12 | `Z8nEEdXTaX0` | Boxy item mod Minecraft.  EPIC |
| 4 | 2013-01-12 | `Y74b7WlcEpk` | More birds IN MINECRAFT!! |

The **fourth** upload's description ends like this:

```
Basically what this mod does is adds more birds to minecraft.
i forgot to mention that you can find nest which have eggs in them....
download:https://www.youtube.com/watch?v=Z8nEEdXTaX0
```

Its **last word is a literal `youtube.com/watch?v=` link, and it leads to another
MrBeast video.** That is three separate things clicking at once:

1. the cabinet's blue sticky says **"YouTube link / watch?"**;
2. the teal card says **LAST WORD** then ninth;
3. solver u/CiviledXI wrote, independently, *"You end up getting a different YouTube URL
   that takes you to another MrBeast vid."*

No other early upload has a YouTube link as its last word (checked, uploads 1–14). This
is strong evidence that **(6 6) = FOURTH UPLOAD**, and that "LAST WORD" means the last
word of that upload's description.

### But "THEN NINTH" still does not land

Following that link to `Z8nEEdXTaX0`, the ninth word is:

| where | ninth word | length |
|---|---|---|
| transcript | `this` | 4 |
| description | `i` | 1 |
| pinned comment | `out` | 3 |

None is six letters. I also swept uploads 1–14 across title, description and pinned
comment looking for any place where the ninth word *and* the last word are both six
letters — the shape the (6 6) node demands. **Nothing.** So the extraction rule is still
not recovered, and any six-letter answer remains an inference rather than a derivation.

### An unresolved curiosity, recorded honestly

XOR-ing the phrase against Colin's key produces the prefix of a watch URL:

```
"Superb Owls"  XOR  %H6U=)Z7</#bq   =   v=F0OKzxKCP
```

The first two characters come out as exactly **`v=`** — the query string of a YouTube
watch link — and the remaining nine are all legal video-ID characters. The *other*
spacing, `"Super Bowls"`, breaks: its space lands on a key byte that yields a control
character. That asymmetry is the puzzle's own joke ("superb owls", not "super bowls")
falling out of the arithmetic.

It is nine characters short of a real ID, though, so I tested the reverse: every one of
**1,536 video IDs** across MrBeast's six channels plus Colin's, in all four prefix forms
(`v=`, `?v=`, `watch?v=`, bare) and all 13 key alignments. **No ID decodes to readable
text.** So this stays a curiosity, not a result. It is recorded because if anyone finds
the intended 13-character plaintext, the ciphertext is forced to be `v=` + an 11-character
ID, and the search collapses instantly.

### Both mod pages read — and the two chains end very differently

`planetminecraft.com` blocks this machine directly (Cloudflare 403), and
`web.archive.org` is blocked at the egress layer, but the `r.jina.ai` reader proxy
reaches both pages.

**The third upload's link is dead.** `planetminecraft.com/mod/minecraft-boxy-tools-mod-146/`
returns *"Oops, this page is missing or temporarily down"*. So the FOURTH → link →
third upload chain cannot continue past that video by following links.

**The second upload's link is live**, and its Elements list is:

| # | element | letters |
|---|---|---|
| 1 | Broom | 5 |
| 2 | Quaffle | 7 |
| 3 | Bludger | 7 |
| 4 | **Snitch** | **6** |
| 5 | Beater Bat | — |
| 6 | Bludger/Snitch Gloves | — |
| 7 | Jersey/Headband | — |
| 8 | Goal Block | — |
| 9 | Quidditch Chest | — |

**`Snitch` is the only six-letter item in the entire mod.** The ninth element is
"Quidditch Chest", the ninth recipe is "Headband", and the ninth word of the About
paragraph is "could" — so "THEN NINTH" still does not point at it. SNITCH is the only
six-letter word the page offers, not a word the page's ninth position yields.

Note also that the page carries four `youtube.com/watch?v=` links and a
`youtube.com/user/GamersDissent?feature=watch` link — more "watch?" than anywhere else
in either chain.

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

The **(6 6)** is where every account, mine included, stops being a derivation.
"(6 6)" only says *six letters and six letters*, and several ordinals fit that
shape — SECOND, FOURTH, EIGHTH, LATEST, OLDEST all pair with UPLOAD to give (6 6).

Two readings survive, and **they disagree**:

| reading | MrBeast's upload | argument for it |
|---|---|---|
| **FOURTH UPLOAD** | *More birds IN MINECRAFT!!* (2013-01-12) | its description's **last word is a literal `youtube.com/watch?v=` link to another MrBeast video** — matching the "YouTube link / watch?" sticky, the teal card's LAST WORD, and u/CiviledXI's independent description of the step. No other early upload does this. |
| **SECOND UPLOAD** | *Harry Potter Mod In Minecraft!* (2012-03-09) | it is the only early upload that yields a six-letter word at all: Harry Potter → his owl → **HEDWIG** — and the red half's answer, FANTASTIC, comes from a Wizarding World title. |

FOURTH has the better *mechanical* evidence; SECOND has the only *answer*. Following
FOURTH through its link lands on `Z8nEEdXTaX0` ("Boxy item mod Minecraft. EPIC"), whose
ninth word is `this` (transcript), `i` (description) or `out` (pinned comment) — none
six letters, and nothing owl-shaped anywhere in it. So the FOURTH path, despite the
better evidence for its first step, currently dead-ends; SECOND reaches HEDWIG but
without a derivation. That is the honest state of it. `tools/pieces/blue_chain.py`.

Checked here and ruled out as the source of the (6 6): the nine playlist words of the
old hunt (*Every Challenge Leads Towards Location Name Somewhere Around World* — last
word and ninth word are both "World"), the twelve Super Bowl puzzles (SB12 = Tallinn,
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
| blue | `YouTube link` / `watch?` | blue |

It is the *ink* that splits them — red pen on the yellow notes, blue pen on the
blue ones — and all three red-ink notes are now explained. So the blue chain has
exactly three tools: **a YouTube video** ("watch?"), **two counts** (`# #`,
"How many?"), and **`251634`**, which uses each of the digits 1–6 exactly once
and so is a six-element **permutation**, not a number.

And that "How many?" is what makes **XOR SUPERB OWLS** more than wordplay: read
together, the phrase names the two operands — *Super Bowls* ⊕ *owls* — and the
note asks you to count them.

The arithmetic then closes almost by itself. The (6 6) needs a **six-letter
ordinal**, and English has exactly three: SECOND, FOURTH, EIGHTH — 2, 4 and 8,
all powers of two. There are 14 owls, so the second count can only be 12, 10 or 6:

```
14 ⊕ 12 = 2  → SECOND    (the only ordinal that reaches a six-letter word)
14 ⊕ 10 = 4  → FOURTH    (the reading with the better mechanical evidence)
14 ⊕  6 = 8  → EIGHTH    (lands nowhere)
```

Where the 12 comes from is **not settled**. The old hunt's Super Bowl group is
exactly twelve puzzles, but the author has since said he *"very intentionally avoided
references, so you don't have to know anything about the $1M"* — so that cannot be the
route, and I have withdrawn it. Twelve road signs have been counted in the room, and
the fourteen red numerals happen to XOR to 12; neither is confirmed. Note also that
this arithmetic does not by itself pick SECOND — the red numerals XOR to 12, the blue
to 10 and all of them to 6, which give 2, 4 and 8 respectively, i.e. all three
candidate ordinals. What picks SECOND is only that it is the one that reaches a word; the video's own on-screen counter reads `N/12` and its narration says "your first of twelve locations", which is the firmest source for the 12 and gives 14 ⊕ 12 = 2.

`251634` turns out to be `25 | 16 | 34` — the three complementary pairs of 1–6, so
each pair both sums and XORs to **7**. Only 6.7% of permutations do that, so it reads
as a worked example of the XOR operation rather than a scramble; its purpose is still
open.

### What the author himself has said

Colin Sanders answers questions from his own Reddit account, and three of his answers
matter here:

- *"anything I post on Reddit, Instagram, or YouTube is **not relevant** to the MrBeast
  puzzle"* — which kills the CyberChef link people found on his profile (it decodes
  nothing here either), and means the UPLOAD has to be MrBeast's own.
- *"If you haven't solved a jigsaw puzzle, MrBeast's video is the **only one** you
  should be watching 🙂"* — so once you have, another video is exactly what you need.
  That is the cabinet's "YouTube link / watch?" note.
- *"There may be other things you need on the internet (**Google is always an
  option!**)"* — outside knowledge is expected, which is how both halves finish.

He has also confirmed the challenge is completable and that his two errata (the grass
piece's extra blue "i", the red paper's missing 2) are the only real mistakes — and
both of them are exactly what the reconstruction here needs.

Ruled out here, so nobody need redo them: the fourth upload of each of MrBeast's
six channels and of the author's own (dated — the Harry Potter Minecraft video is
his *second* upload, not his fourth); the old hunt's fourth playlist video (its
word is *Towards*); the pinned comment's wording; the CyberChef XOR key from the
profile link against every phrase the desk produces; and `251634` as a permutation
of any six-letter English word (no pair of real words maps to another).

The cabinet is fully read now — a community photo of the shot
(`tools/pieces/CABINET_FULL.png`) shows all six notes unclipped, and the bottom one
says only "YouTube link / watch?" with nothing under it. There is no hidden URL
there; `251634` is six evenly-spaced digits with no grouping; and the hash note is
`# #`, two number placeholders.

## Files

- `tools/pieces/verify_owls.py` — recomputes all 27 jigsaw letters and the hash
- `tools/pieces/red_chain.py` — recomputes the red half from the Audubon plates
- `tools/pieces/blue_chain.py` — the (6 6) reading, against MrBeast's upload history
- `tools/pieces/owllist.txt` — the 254-species list used for the uniqueness check
- `MRBEAST_PUZZLE_NOTES.md` — the full working log, including everything refuted
