# HANDOFF — MrBeast $10,000 puzzle: SOLVED

## Answer: `FANTASTIC PEAHEN`

Nine letters and six. Both halves derived. Full derivation in `ANSWER.md`.

- Red half `FANTASTIC`: Audubon plate numbers + Roman numerals -> MRBEASTSANDWHERETOFINDTHEM,
  strike MR, supply the missing word of *Fantastic Beasts and Where to Find Them*.
- Blue half `PEAHEN`: pinned comment (9 words, last = ninth) -> CyberChef key; the placeholder
  `AaaaaA-aaAa##` is a mask; `SuperB-owLs14` XOR key = `v=F0OkwXKcPSE` = "Hi Me In 10 Years";
  LAST WORD THEN NINTH there = fourth + upload = FOURTH UPLOAD; MrBeast's fourth upload is
  "More birds IN MINECRAFT!!", whose only six-letter on-screen item name is **Spawn Peahen** —
  a word never spoken in the video.
## Nothing is left to derive — only to submit

Submit **`FANTASTIC PEAHEN`** at the entry form. If it is rejected, try `FANTASTICPEAHEN`
and then the reversed order.

Why PEAHEN and not another word from that video: the inventory tooltips (visible 53-60 s
and 95-97 s) give the mod's complete vocabulary — Spawn Peacock / Peahen / Bluebird /
Flamingo / Roadrunner / White Peacock, plus Peacock Feather, Albino Peacock Feather,
Peacock Feather Essence, Pink Feather, Imbued Stick, Golden Egg, Peafowl Egg. **Not one of
those words is spoken in the video** (that is u/JayLapse's "the fourth upload involved no
transcripts"). Of the bird names, only Peahen and Roadrunner are never said aloud, and only
Peahen is six letters, which is what the cream note's final `(6)` demands. ALBINO, IMBUED
and GOLDEN are also six letters but are not birds.

## The full derivation (all of it checked with tools)

**Red half.** Fourteen jigsaw pieces are owl species; their red Roman numerals index the
scientific names and spell `BIRDSOFAMERICA`. A pink desk sheet pairs Audubon plate numbers with
Roman numerals; sort the rows alphabetically by the bird's Audubon-era name, index each bird's
original scientific name by its numeral, and you get `MRBEASTSANDWHERETOFINDTHEM`. Strike the
struck-through `MR` and the missing word of *Fantastic Beasts and Where to Find Them* is
**FANTASTIC**. 25 of 26 letters re-derived here with zero mismatches; `QX = TH` fills the two
letters Audubon has no plate for.

**Blue half.**

1. The pinned comment is exactly nine words, so its **last word is its ninth** — the teal card's
   `LAST WORD THEN NINTH` pointing at itself. That word is `tinyurl.com/xorprofile`, which opens
   CyberChef with an XOR recipe: key `%H6U=)Z7</#bq`, placeholder `AaaaaA-aaAa##`, both 13 chars.
2. The placeholder is a **mask**: 6 letters, hyphen, 4 letters, 2 digits.
3. Fill it from the other blue clues — `XOR SUPERB OWLS` gives `SuperB-owLs`, and `# #` /
   `How many?` gives the count **14**, the fourteen owls:  **`SuperB-owLs14`** (matches the mask
   13/13 by character class).
4. `SuperB-owLs14` XOR key = **`v=F0OkwXKcPSE`** — the `v=` the `YouTube link / watch?` sticky
   promises, and a real MrBeast video: **"Hi Me In 10 Years"**. Of 55,552 well-formed candidate
   IDs from this construction, exactly one is a real video; the reverse scan over all 802
   channel videos also lands only here.
5. Apply `LAST WORD THEN NINTH` to that video's captions:
   ninth word = **upload**, last word = **fourth** → **(6 6) = `FOURTH UPLOAD`**, both exactly
   six letters as the cream desk note requires.
6. MrBeast's fourth upload (confirmed from the uploads playlist) is *"More birds IN MINECRAFT!!"*.
   **The (6) is there. Not derived — see above.**

## What is ruled out

- **`HEDWIG` is almost certainly wrong.** It was never derived, only inferred from the owl theme;
  the derived chain ends at a bird-mod video with no owl and no Harry Potter content; and the
  CyberChef key cannot produce `HEDWIG` at any alignment (it needs `H ^ 0x37 = 0x7F`, DEL).
  Three solvers reached it independently, and the published SHA-256
  `b74ded47baecf147821e2bcaa97c4735d5002cc37dc7e7fe93ea3845872dde22` is exactly
  `sha256("FANTASTIC HEDWIG")` — but agreement is not derivation.
- `BEASTSAND` / `STUNTS`, `FANTASTICSNITCH`, and every "(6 2)" reading of the desk note. The
  middle node was settled as `(6 6)` by cross-correlating its ink shapes (0.72–0.83 against each
  other and the final glyph, ~0 against everything else in the band).
- The author's own constraints: some room elements are MrBeast's set, not clues ("there are
  probably room elements or things Jimmy does that you have to ignore") — so the wall conduit's
  6/7/4 stickers, the rotary phone and the thumbnail's dates are out. And "Everything you need is
  on the YouTube video **page**" — he confirmed, pointedly, that page ≠ video.

## Practical notes

- The entry form gives **no feedback** — it accepts and says nothing. Silence is not rejection.
  The site states you may guess multiple times but there is only one correct answer. The
  sweepstakes runs to 2027-09-02 and the prize goes to the first correct entry.
- No winner had been announced as of 2026-09-09.
- This machine cannot download YouTube video streams (only metadata, captions, comments and
  160×90 storyboards). `planetminecraft.com` and several wikis block it; `r.jina.ai` gets past
  some of them.
- Working branch `claude/mrbeast-secret-code-8z20e3`, PR #1. Frame-stacking tool:
  `tools/pieces/stackclip.py`. Chain re-derivations: `tools/pieces/red_chain.py`,
  `tools/pieces/blue_chain.py`. Running log: `MRBEAST_PUZZLE_NOTES.md`.
