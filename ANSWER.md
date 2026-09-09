# MrBeast $10,000 puzzle — the answer

**Red half: `FANTASTIC` — derived and verified.**
**Blue half: the chain is now derived end-to-end except its last hop.**

## ★ The blue chain, solved

Every blue clue is consumed. Each step was checked with tools, not assumed.

### 1. The pinned comment hands you the key

MrBeast's pinned comment is **exactly nine words**, so its **last word IS its ninth**:

> Make(1) sure(2) you(3) check(4) out(5) Colin's(6) profile(7) 👀(8) **https://tinyurl.com/xorprofile(9)**

That is "LAST WORD THEN NINTH" pointing at itself. The tinyurl resolves to CyberChef with
an XOR recipe preloaded — key `%H6U=)Z7</#bq` (13 chars), input `AaaaaA-aaAa##` (13 chars).

### 2. The placeholder is a fill-in mask

`AaaaaA-aaAa##` = **6 letters · hyphen · 4 letters · 2 digits**, with a specific case pattern.

### 3. What to type: the blue jigsaw string plus the count

- `XOR SUPERB OWLS` — the blue jigsaw's own phrase supplies the operand: **SUPERB / OWLS**,
  and the hyphen in the mask falls exactly where the space between them goes.
- `# #` / `How many?` — supplies the two digits: **14**, the fourteen owl pieces.

```
input :  SuperB-owLs14
mask  :  AaaaaA-aaAa##      ← character class matches 13/13
```

### 4. Run the XOR

```
SuperB-owLs14  XOR  %H6U=)Z7</#bq  =  v=F0OkwXKcPSE
```

`v=` — exactly what the `YouTube link / watch?` sticky promises. And `F0OkwXKcPSE` is a real
MrBeast video: **"Hi Me In 10 Years"** — a 2015 message to his future self, schedule-uploaded
to 2025-10-04. Confirmed live via YouTube oEmbed.

**This is not a coincidence.** Sweeping every well-formed candidate ID from this construction —
the hyphen family, the space family, and arbitrary two-character suffixes, **55,552 IDs** — and
querying each against YouTube, **exactly one is a real video**: the mask-perfect one. The reverse
scan also lands once: XOR-ing the key against `v=`+ID for all 802 videos on MrBeast's channel
yields exactly one English string, `SuperB-owLs14`.

### 5. "LAST WORD THEN NINTH", second use — this yields the (6 6)

Fetched the captions of `F0OkwXKcPSE` and counted:

| | word | letters |
|---|---|---|
| **NINTH word** | *"I'm gonna schedule **upload** this video…"* | **UPLOAD** — 6 |
| **LAST word** | *"…this is October **fourth**."* | **FOURTH** — 6 |

## **(6 6) = FOURTH UPLOAD** ✓ — both words exactly six letters, as the note demands.

### 6. The last hop — not finished

MrBeast's **fourth upload**, confirmed from the channel's own uploads playlist (all 1,000
entries, oldest last):

1. `2XVcLrB7B3Y` Worst Minecraft Saw Trap Ever???
2. `jP82d277Cc8` Harry Potter Mod In Minecraft!
3. `Z8nEEdXTaX0` Boxy item mod Minecraft. EPIC
4. **`Y74b7WlcEpk` "More birds IN MINECRAFT!!"** ← here

A showcase of a mod that "adds **five new Birds**" — peacock, bluebird, flamingo, one he only
calls "a runner", and a white peacock. The mod is **Exotic Birds** (whose forum thread is titled
"Herons, Owls, Pelicans and MORE!").

**The six-letter word must be read off this video, and not from its transcript** — solver
u/JayLapse, who appears to have solved it, corrected another solver with exactly that:
*"the fourth upload involved no transcripts."* The transcript's ninth and last words are `Mod`
and `watching`, which fits: they are not it.

**This machine cannot play the video.** YouTube serves no downloadable format to this IP — only
160×90 storyboard thumbnails, too small to read the on-screen item names. The last step needs
someone who can simply watch it.

### What to do

Open **https://www.youtube.com/watch?v=Y74b7WlcEpk** and read the **six-letter word** — most
likely a bird or item name shown on screen, or the mod's name. Then submit
`FANTASTIC <that word>`.

Candidates visible from what could be recovered here, none confirmed: **EXOTIC** (the mod's
name), **RUNNER** (the bird he does not name), **TOUCAN / MAGPIE / PARROT / PIGEON / BUDGIE**
(the six-letter birds in the Exotic Birds roster).

### What this overturns

- **HEDWIG is almost certainly wrong.** It rested entirely on theme, and the derived chain ends
  at a bird-mod video with no owl and no Harry Potter content. The CyberChef key also cannot
  produce `HEDWIG` at any alignment.
- **`BEASTSAND` + `STUNTS` is wrong** — u/JayLapse says so directly, and the red chain gives far
  more than "mrbeastsand".
- **The community reading "(6 6) = FOURTH UPLOAD" was right all along**, and my doubt of it was
  wrong. It is now derived rather than guessed.


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

## The hash matches — and "no reply" is not "wrong"

u/CiviledXI published a SHA-256 of their answer on 5 September, before anyone posted
words publicly, precisely so answers could be compared without revealing them:

```
b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22
```

Computed here:

```
sha256("FANTASTIC HEDWIG") = b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22
```

**Exact match.** So three solvers who worked independently — CiviledXI, u/Huge-Stable-7397
and u/CivilActive6029 — all arrived at `FANTASTIC HEDWIG`, and CiviledXI is the one who
derived the red half correctly and unaided.

That matters for how a non-response should be read. **Nobody has received any reply at
all.** Huge-Stable-7397 entered on 4 September, CiviledXI on 5 September; as of
7 September neither has heard anything, and no winner has been announced. The entry is a
sweepstakes form, not a checker — it does not tell you that you are wrong. So unless the
form explicitly rejected the answer, submitting and hearing nothing is **not** evidence
against `FANTASTIC HEDWIG`.

## The middle node is (6 6), settled

Another solver reads the cream note's middle node as `(6 2)`, and my own first pass on a
360p frame read it that way too. Settled here by comparing ink shapes rather than by
squinting.

Threshold the upright note across the band holding the middle node, the arrow and the final
node, label the connected ink blobs, and cross-correlate them pairwise. The strokes merge at
this resolution so the blobs are not cleanly one-digit-each, but the pattern is unambiguous:

```
middle-node upper glyph  vs  middle-node lower glyph   +0.81
middle-node lower glyph  vs  final-node glyph          +0.83
middle-node upper glyph  vs  final-node glyph          +0.72
the arrow / other marks in the same band vs any of them  ≈ 0.0
```

Three marks that mutually correlate at 0.72–0.83 while everything else in the same band sits
at zero are **the same character written three times**. Rendered side by side, the middle
node plainly carries two identical glyphs and the final node one of the same shape.

The final node is `(6)` — the answer's second half is a six-letter word, which is not in
dispute. So the middle node is **`(6 6)`**, and the `(6 2)` reading is wrong. Every
"six-letter word plus a two-letter word" line of attack can be dropped.

## What the CyberChef box will and will not accept

The placeholder is not filler. **`AaaaaA-aaAa##` is a legality template.** For the XOR
output to be fully printable ASCII, the key forces:

- **no uppercase at positions 2, 4 and 7** (`A` there XORs to a control character),
- **no lowercase at positions 12 and 13**.

The placeholder satisfies exactly those five constraints and nothing else about it is
arbitrary — lowercase at 2 and 4, a hyphen at 7, digits at 12 and 13. So it is telling you
the *shape* of the string you are meant to paste: **eleven characters of mixed case,
letters/digits/hyphen, then two digits.** Eleven characters plus two digits is also, exactly,
a YouTube video ID plus the two numbers the `# #` / `How many?` sticky asks for.

**A correction.** Two turns ago I made much of `"Superb Owls"` XOR-ing to `v=F0OKzxKCP` —
the `v=` of a watch URL. That is worth much less than I said: `'S' ^ '%' = 'v'` and
`'u' ^ 'H' = '='`, so **any** input beginning `Su` produces `v=`. The phrase begins `Su`,
and that is the whole of it. No coincidence, no signal.

**Tested exhaustively against that template, all negative:**

| test | result |
|---|---|
| every 13-char substring of ~2.6 MB of puzzle material (frame OCR, transcripts, descriptions, the official $1M PDF, the mod page, the Reddit corpus) | no output contains an English word of 4+ letters; none has the form `WORD WORD` |
| all 1,024 case variants of `xorsuperbowls` (13 chars = the key's length) | nothing readable — XOR only flips bit 5, so case cannot rescue a garbage output |
| `Superb Owls` / `Superb owls` + all 100 two-digit endings → 162 syntactically valid video IDs | **every one checked against YouTube; not one is a real video** |
| the pinned comment's own id `UgzlKjB7zrL4QAj0AiZ4AaABAg` (26 chars = 2×13) at all 13 alignments | never printable — it has an uppercase at position 7 |
| every candidate video ID + two digits | never printable, for the same reason |
| `251634`, `82CX6WULNA0`, `BIRDSOFAMERICA`, `LASTWORDTHENNINTH`, `MRBEASTSANDWHERETOFINDTHEM`, `FANTASTIC`, at all 13 alignments, forwards and reversed | nothing |

So if something is meant to be pasted there, **it is a string I have never read** — which is
plausible: the room's 1080p coverage is partial, and one yellow note (`CODE … ON … →`) is
physically hidden under another sheet. The template above is the filter to apply to any
candidate: eleven mixed characters then two digits, with no capital in slots 2, 4 or 7.

## The XOR box cannot output HEDWIG — but it can output SNITCH

Prompted by the suggestion to actually *type the random-looking thing into the box*, and
by a screenshot of the live page (which confirms the decode exactly: input
`AaaaaA-aaAa##`, 13 chars, output `d)W4\hwV]nBAR`).

The key is 13 bytes, and the placeholder is 13 characters — so the intended input is 13
characters. XOR is its own inverse, so for any desired **output** the required **input** is
forced. And for some outputs that required input is **not typeable**: it lands on a
control character.

**Work it through for a `(6 6)` output** — six letters, a space, six letters, which is
exactly 13 characters:

- The space at position 7 needs input `z`. Typeable ✓
- Positions 2, 4 and 7 of the output can only be **lowercase** (their key bytes push
  uppercase into control characters), so the **first word cannot be all-caps**.
- Positions 12 and 13 can only be **uppercase**, so the **second word must end in two
  capitals** — i.e. the second word is the all-caps one.

Now test the two candidates as that second word:

```
HEDWIG   offsets 0..7:  -  -  -  -  -  -  -  -     never typeable
SNITCH   offsets 0..7:  -  -  -  -  -  -  -  OK    typeable at offset 7
```

`HEDWIG` fails at **every** alignment. At offset 7 — the second-word slot — it needs
`H ^ 0x37 = 0x7F`, which is DEL. There is no key press that produces it. `SNITCH` at that
same offset needs the input suffix `drfw!9`, all typeable.

**What this does and does not show.** It is not proof: `drfw!9` is not a natural-looking
string, so the box may well not be the final step at all — it may only be MrBeast's way of
telling solvers that XOR is involved. But it is the **first hard, non-aesthetic asymmetry
between the two candidates**, and it runs against HEDWIG. If the CyberChef box is the last
step of the blue chain, then the answer cannot be HEDWIG, and SNITCH fits the one slot the
key leaves open.

## What the author said on 7 September

Three statements from u/DoctorXOR, none of which I had:

**Some of the room is not his.** (14:33)
> "I will never want to intentionally have true red herrings… And sometimes it [is]
> impossible to use everything in the environment. **In this case, MrBeast already had
> his whole video planned, and I had to add clues without modifying anything else in the
> room. So there are probably room elements or things Jimmy does that you have to
> ignore.**"

This **retracts** my argument that the conduit stickers must be clues because `674` and
Nauru appear nowhere in the official $1,000,000 document. Their absence from the old hunt
never made them Colin's; a conduit with numbered junction boxes is exactly the kind of
fixture that was already on the wall. The same now applies to the rotary phone and the
thumbnail's dates. With it goes the `blue 6 ⊕ white 4 = 2` argument — `14 owls ⊕ 12`
stands on its own.

What Colin *added* is the real clue set: the jigsaw pieces, the two desk notes, the pink
sheet, the six stickies, the teal card, the orange sticky. Everything else in that room is
MrBeast's set.

**It is the video *page*, not the video.** (14:59, then 16:13)
> "Everything you need is on the YouTube video page."

A solver asked whether he meant the *page* or the *video*, saying it makes a huge
difference. He replied: **"It does make a difference, doesn't it? 😉"**

So the title, description and pinned comment are deliberately in play — which is the
author's own confirmation that the pinned comment, and through it the CyberChef XOR key,
belongs to the puzzle.

Worth noting alongside it: **the pinned comment is exactly nine words** —
`Make(1) sure(2) you(3) check(4) out(5) Colin's(6) profile(7) 👀(8) <tinyurl>(9)` — so its
**last word is its ninth word**. "LAST WORD THEN NINTH" closes on itself there and points
at the CyberChef link.

## Only one chain still reaches a living page

Four of MrBeast's early uploads end their description with an external link. Fetched
through the `r.jina.ai` reader (which gets past the Cloudflare block that stops curl,
the Wayback Machine and Chromium here):

| upload | last word of description | state today |
|---|---|---|
| **2nd** — Harry Potter Mod In Minecraft! | `planetminecraft.com/mod/123-quidcraft-quidditch-mod/` | **live** |
| 3rd — Boxy item mod | `planetminecraft.com/mod/minecraft-boxy-tools-mod-146/` | **404** |
| 4th — More birds IN MINECRAFT!! | `youtube.com/watch?v=Z8nEEdXTaX0` (→ the 3rd upload) | live video, but its own last word is the 404 above |
| 8th — Emerald tool mod! | `planetminecraft.com/mod/emeralds-mod-146147/` | **404** |

If following "LAST WORD" to a destination is the intended step, a setter building this in
2026 would have checked that the destination still exists. **Only the second upload's
does.** The fourth upload's link — the one with the best surface evidence, being a literal
`watch?v=` — leads to a video whose own trail dead-ends at a missing page.

That, plus two independent routes to the number 2 (`14 owls ⊕ 12 = 2` from the video's own
`N/12` counter, and `blue 6 ⊕ white 4 = 2` from the conduit, the only pairing of those
three stickers giving a six-letter ordinal), is the case for **SECOND UPLOAD**.

What still does not follow is the last step. On the QuidCraft page the Elements list has
**exactly nine** entries — Broom, Quaffle, Bludger, Snitch, Beater Bat, Bludger/Snitch
Gloves, Jersey/Headband, Goal Block, Quidditch Chest — so "THEN NINTH" has a clean
referent there, but the ninth is *Quidditch Chest*, not a six-letter word. `Snitch` is the
only six-letter item on the page, and it sits fourth.

## The "watch?" sticky resolves — and the nine

`YouTube link / watch?` has a literal referent. MrBeast's Super Bowl teaser is
`OBQELGS13XA`, and its title *begins with the word* **Watch**: "Watch My Super Bowl Ad To
Win $1,000,000!" The main video names it explicitly — *"you first had to watch my Super
Bowl teaser titled Watch My Super Bowl Ad to Win a Million Dollars"*. It is also the one
video the whole Super Bowl half of the hunt hangs off, which is what `XOR SUPERB OWLS`
points at.

Its description carries a playlist — `PLj-VLkYRjRxm5HVGFVpPP5W7jkvvzd1q7` — holding
**exactly nine videos**, which is what the main video means by *"looked at the pinned
comments of all of these videos, you would get nine puzzles"*. All nine pinned comments,
recovered here for the first time:

| # | video | pinned comment ends with |
|---|---|---|
| 1 | I Built 100 Wells In Africa | `pin.it/3DIjEcxdY` |
| 2 | Changing the Lives of 600 Strangers | `reddit.com/user/BeastForce67/…` |
| 3 | I Cleaned The World's Dirtiest Beach | `imgur.com/gallery/puzzle-mD2eHYD` |
| 4 | $1 vs $500,000 Experiences! | `imageshack.com/user/BeastForce67` |
| 5 | POKEMON GO STEREOTYPES | `photobucket.com/share/753ba093…` |
| 6 | $10,000 Every Day You Survive In The Wilderness | `medium.com/@beastforce67/puzzle-…` |
| 7 | I Adopted 100 Dogs! | `pixelfed.social/BeastForce67` |
| 8 | I Spent 100 Hours Inside The Pyramids! | `imgpile.com/u/beastforce67` |
| 9 | Anything You Can Fit In The Circle I'll Pay For | `500px.com/p/beastforce67` |

A **nine**-video playlist is the most literal referent "THEN NINTH" has anywhere in the
material. But the extraction still does not land: tested and failed on the teaser's own
captions (9th word `Well,`, last `this.`), the nine titles, the nine pinned comments, the
nine-word sentence they spell (*Every Challenge Leads Towards Location Name Somewhere
Around World* — its ninth word **is** its last word, "World"), the twelve Super Bowl
locations (verified verbatim from the transcript), and the main video's description.

## More closed doors

- **`251634` is not atomic numbers.** Worth testing because the video *teaches* this
  trick — the tenth Super Bowl puzzle is La+Ho+Re = **LAHORE**. Every split of `251634`
  into atomic numbers gives either the wrong length or nonsense; the only six-letter
  readings are `He B S Se` → HEBSSE and `Mn H C Se` → MNHCSE.
- **No pair of YouTube IDs XORs to a real video.** The main video against the teaser, the
  Colin video, the wilderness video and all nine playlist entries, in base64url index
  space: not one result is an ID MrBeast has ever published.

## Every clue, used and unused

The right question, once an answer stalls, is which props the solve never consumed. A
puzzle this tight does not leave spare parts.

### Used, and load-bearing

| clue | what it does |
|---|---|
| 14 jigsaw pictures | each is an owl species |
| red Roman numerals | index the scientific names → `BIRDSOFAMERICA` |
| blue Roman numerals | index the scientific names → `XORSUPERBOWLS` |
| pink sheet (plate № + numeral) | → `MRBEASTSANDWHERETOFINDTHEM` |
| orange sticky "Books w/ old names… Alphabetize?" | the red chain's sort rule |
| green sticky "LSWRTE…" + "Should I call it bird fence?" | rail fence → `LASTWORDTHENNINTH` |
| red note `(5 2 7) → (8 3 5 2 4 4) → M̶R̶ (9)` | the red chain's skeleton |
| yellow `081 XIV / Seahawks?` | worked example of the red mechanism |
| yellow `QX = TH` | the two alphabet slots Audubon has no plate for |
| yellow `PLATES` | says the numbers are plate numbers |
| "Boo! book — five of these" | confirms five boobooks among the fourteen |
| cream note `(3 6 4) + (4 4 4 5) → (6 6) → (6)` | the blue chain's skeleton |

### Never used — this is where the missing step must live

| # | clue | status |
|---|---|---|
| 1 | **`LAST WORD THEN NINTH`** | decoded, never successfully applied. **This is the hole itself.** |
| 2 | **pipe stickers: blue `6`, red `7`, white `4`** | see below — the largest unexplained object |
| 3 | **`251634`** (blue sticky) | I called it a worked XOR example. That is an inference, not a use. |
| 4 | **`# #` / `How many?`** (blue sticky) | never resolved; "14 owls ⊕ 12 Super Bowls" is a guess |
| 5 | **`YouTube link / watch?`** (blue sticky) | points somewhere; the destination was never pinned down |
| 6 | **the rotary phone** on the desk | flagged by two other solvers as unused; still unused |
| 7 | yellow note `CODE … ON … →` | physically hidden under another sheet; never read |
| 8 | the LOGIN ATTEMPTS dates on the thumbnail | never used |
| 9 | the pink sheet's odd `424-6` row | never read |

### The pipe — retracted on 8 September

**The author has since said the room contains elements to ignore**, which undercuts the
argument below. Kept for the record; see "What the author said on 7 September".

### The pipe is not set dressing (superseded)

On the brick wall to MrBeast's right, a vertical conduit carries three junction boxes,
each with a round numbered sticker: **6 (light blue)** on top, **7 (red)** in the middle,
**4 (white)** at the bottom. Two things make it worth attention:

- **The colours are the puzzle's own two chains** — blue and red — plus one neither.
- **Neither `674` nor Nauru (whose dialling code it is, and which the community chased)
  appears anywhere in the official $1,000,000 answer document.** So this is not left-over
  scenery from the old hunt. It was placed, and nothing explains it.

The one arithmetic that fits: **6 ⊕ 4 = 2**, the only pairing of the three that yields a
*six-letter* ordinal — SECOND — which is exactly what the `(6 6)` slot needs, and it is
the blue sticker that carries the 6. `6 ⊕ 7 = 1`, `7 ⊕ 4 = 3` and `6 ⊕ 7 ⊕ 4 = 5` all give
five-letter ordinals that cannot fill `(6 6)`. That is suggestive, not conclusive — but it
points at SECOND UPLOAD rather than FOURTH.

### And the entry page says guessing is free

`puzzle-video-sweepstakes.mrbeast.app` states: *"You can guess multiple times, but there
is only 1 correct answer."* So extra guesses are explicitly allowed — they simply return
no information, because the form never says which one was right.

## Ruled out after the three submissions failed

- **(6 6) is not two words from an early upload's description.** All sixty oldest
  uploads fetched and parsed: not one has a six-letter ninth word *and* a six-letter
  last word. (Four of them do end their description in a `youtube.com/watch?v=` link —
  #4, #17, #18, #20 — so the "LAST WORD is a watch link" observation holds, but the
  words themselves never fit (6 6).)
- **(6 6) is not `v=<ID>` XOR-ed with Colin's key.** This one closes by arithmetic
  rather than by search. For a 13-character plaintext `WORD1 WORD2` (6 + space + 6) to
  encrypt to `v=` + an 11-character video ID, the key forces:
  - plaintext[0..1] = `Su` (that is what produces `v=`),
  - plaintext[6] = space → ciphertext `z` ✓,
  - **plaintext[11] ∈ {O…W, Z} and plaintext[12] ∈ {A…I}** — both *uppercase only*.

  So the second word's last two letters would have to be capitals inside an otherwise
  lower-case word. No English word does that, so this route is closed, and the `Su` →
  `v=` coincidence is just that.

## Ruled out today

- **(6 6) → (6) is not a letter-XOR.** All 17,468 six-letter words were XOR-paired
  (packed 5 bits per letter, every field ≤ 25): 5,949 valid triples exist, and not one
  involves HEDWIG, SNITCH, GOLDEN, SUPERB, SECOND, FOURTH or UPLOAD.
- **(6 6) is not a MrBeast video title.** None of the 1,536 titles across his six
  channels is two six-letter words.
- **(6 6) is not two owl names.** Ordered by the red string `BIRDSOFAMERICA`, the
  fourteen pieces run 1–14; the **last** is the Barred owl and the **ninth** is the
  Least boobook. `BARRED` is six letters — and it is the *only* six-letter owl name
  among the fourteen — but `LEAST` is five, so the pair does not fit (6 6).
- **`251634` is a worked example, not data.** The six stickies split three red / three
  blue, and each colour has the same three roles: a worked example, a gap-filler, and a
  statement of what the numbers are. Red: `081 XIV → Seahawks?` (worked example),
  `QX = TH` (gap-filler), `PLATES` (what the numbers are). Blue: `251634` (worked
  example — 25|16|34 are the three complementary pairs of 1–6, each summing *and*
  XOR-ing to 7), `YouTube link watch?` (gap-filler), `# #` / `How many?` (what the
  numbers are). So `251634` encodes no answer.

## Only if you ever learn the answer was actually rejected

These are **not** worth submitting on spec — the form cannot tell you anything, so
spraying variants buys no information. Keep them only in case a rejection ever becomes
known:

| # | submit | why |
|---|---|---|
| 1 | `HEDWIG FANTASTIC` / `HEDWIGFANTASTIC` | the teal card says **LAST WORD THEN NINTH** — read as an assembly rule that is *six then nine*, i.e. blue before red. Huge-Stable-7397 flagged this exact ambiguity and never resolved it. |
| 2 | `FANTASTICBARRED` | the **last** of the fourteen pieces is the Barred owl, and `BARRED` is the only six-letter owl name in the set |
| 3 | `FANTASTICUPLOAD` | the literal last word of the (6 6) |
| 4 | `FANTASTICBEASTS` | completes the title the red half is punning on |
| 5 | `FANTASTICSTUNTS` | the answer the AI-assisted writeups converged on |

---

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
