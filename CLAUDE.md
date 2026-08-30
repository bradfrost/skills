# Working in this repo

Every word in this repo is published under Brad Frost's name: the README, the
skills, the interview questions, the refusal messages a stranger reads at
2am. There is no "internal" prose here.

## Before you write or edit ANY prose, load the voice canon

This is not optional and it is not a judgment call. A README, a SKILL.md, an
error message, and a blog post are all Brad's public voice.

1. **Global voice rules** (Notion, applies everywhere):
   `https://www.notion.so/bradfrost/Global-applies-everywhere-75f4777e77aa4c9bb1781681223a2ab6`
2. **Blog/newsletter voice** (the closest long-form lane), canonical in
   bf-brain at `docs/voice/blogging-newsletters.md`; the Notion page is its
   mirror.

If you can't reach them, STOP and say so. Do not draft from memory. Silent
drift is exactly the failure this rule exists to prevent, and it has already
happened once (2026-08-30: a full README section written without loading the
canon, which Brad caught immediately).

## The tells that gave it away last time

- **Em dashes.** Global canon: they "pile up fast and are a tell-tale signal
  of AI writing." Brad's own copy uses commas, semicolons, ampersands
  ("sleep & balance", "friction & intention"), and parentheses. One offending
  draft had 14 em dashes; Brad's interview copy has 0.
- **Flat register.** Brad's default is enthusiastic and energetic:
  exclamation points ("Let's go!", "Thanks so much!"), CAPS for real emphasis
  ("REFUSE"), the occasional emoji doing actual work (🥵).
- **Telegraphic fragments.** "Six questions, about five minutes, and every
  one has a default." Brad writes complete sentences that flow.
- **Explaining without handing back agency.** Brad constantly returns
  control to the reader: "that you set for yourself," "your own terms," "you
  can adjust your settings if needed."

## Brad's patterns, observed in this repo's own copy

- Mechanism explained inline with "which means": *"your quiet hour limits are
  in effect, which means tool calls are paused"*
- "It's important to know/say that…" for an honest caveat, with no
  candor-announcing preamble
- Italic contrast pairs: *"meant to inform you, not shame you"*
- Parenthetical softeners after a hard message: *"(You can adjust your
  settings if needed)"*
- "Default:" as a label, then the recommendation
- Second person throughout, with the reader's own words quoted back to them

## The verbatim rule

The README quotes the interview questions and refusal messages. Those strings
are Brad's, edited line by line with him. **Quote them exactly from the
shipped SKILL.md files. Never paraphrase, tighten, or "improve" them in the
docs** — if the README and the skill disagree, the skill wins and the README
is wrong.

## Honesty rules that outrank good marketing copy

- Never claim enforcement that doesn't exist. Every limit is labeled
  **enforced**, **advisory**, or **nothing** per surface
  (`skills/mental-health/limits-setup/ENFORCEMENT.md`).
- Energy figures are floor estimates from published vendor numbers. Never
  invent a conversion; never present an estimate as a measurement.
- If a claim can't be verified, say so plainly instead of softening it.
