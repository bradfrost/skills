---
name: ds-token-architecture
description: Check a design token set against the Subatomic three-tier architecture (definitions → usage → components) and hand back evidence-tagged findings plus a prioritized work order, or establish a tier ladder from a production codebase that has no tokens yet. Use when the user pastes their token JSON and asks "is this right?", asks to audit, assess, review, or grade their tokens, asks whether their tokens are properly tiered or semantic, wants to know if dark mode or a second brand will be a remap or a rewrite, or has a codebase full of hardcoded values and wants to build token foundations from it code-first. Companion to ds-inspection (which grades the whole system across ten stations); this one goes deep on the token layer alone.
---

# Design Token Architecture Check

Nine checks against the three-tier architecture Ian and I teach in
[Subatomic](https://designtokenscourse.com/), run on a real token set with
real evidence. The output is a sheet of nine lights and a work order that
says what to fix Monday morning. There's no score, because a number out of a
hundred hides the one finding that matters: whether a second theme would be
a remap or a rewrite.

It also runs the other direction. A team with a product and no tokens can
use **establish mode** to get from "every color in production" to a tier
ladder, without letting a scanner make the design decisions.

## Ground rules (read first, apply at every check)

1. **Evidence before judgment.** Every finding cites its evidence and carries
   a tag: `[verified]` (you read the file, the variable, or the tool output
   yourself) or `[reported]` (a human told you and you couldn't confirm).
   Counts, file names, and token names, never vibes. "6 of 41 tier 2 color
   tokens hold raw hex" beats "some tokens aren't aliased."
2. **Check the structure, not the vocabulary.** The architecture's words
   (`definitions`, `usage`, `theme`, `knockout`) are one set of words. A
   system that says `primitives`, `semantic`, `sys`, and `on-brand` is
   following the architecture. The intake's vocabulary translation exists so
   findings speak the team's language. A structural gap is a finding; a
   different word for the same structure is not.
3. **Read the source, not the build.** Built CSS often resolves references to
   literals, which makes a tiered system look flat. Judge tiers and
   references from the JSON, the Figma alias structure, or the config.
4. **Do the arithmetic.** A token named `on-brand` is a contrast *claim*.
   Resolve the values and compute the ratio, per theme, before you call the
   pair green. Names are not evidence of what they promise.
5. **Probe the design side every run.** Tokens usually exist in Figma too,
   and a bridge is often connected that you won't notice unless you look.
   Ask, check your tools, make one real call, record the result.
   `reference/FIGMA-ACCESS.md` says what each bridge can see; the native
   bridge needs a layer selected to read variable definitions, and
   whole-collection reads need the Console bridge.
6. **Scope claims to what you read.** "The 12 components I sampled," never
   "your components." Say what you did not inspect.
7. **Where the architecture has no opinion, say so.** Opacity scales,
   layout tokens, sizing tokens, structured data-viz palettes: the course
   doesn't cover them. Describe what the system does in the report's "no
   guidance" section instead of grading it against a rule that doesn't
   exist.
8. **The human makes the calls.** You surface, sort, and propose. The team
   decides what to rename, what to merge, and in what order. In establish
   mode this is non-negotiable: every merge changes pixels, and a script
   doesn't get to make that call.
9. **No shame.** A flat pile of tokens was the right call when someone made
   it under a deadline. The report says what it costs to carry now.

## Files in this kit

- `intake/TOKEN-INTAKE.md` — the check-in; produces `ds-token-architecture/PROFILE.md`
- `checks/check-01…09-*.md` — one file per check, each self-contained
- `establish/ESTABLISH.md` — the code-first procedure for a system with no tokens yet
- `reference/SUBATOMIC-ARCHITECTURE.md` — the architecture the checks test against, with lesson pointers
- `reference/FIGMA-ACCESS.md` — what each Figma bridge can actually see
- `templates/report.md`, `templates/work-order.md`, `templates/ladder.md` — output shells

## State (in the user's project)

```
ds-token-architecture/
├── PROFILE.md                       ← the token set, its sources, the access map
├── reports/YYYY-MM-DD-report.md     ← the nine-light sheet and check records
├── work-orders/YYYY-MM-DD-work-order.md
└── (establish mode only)
    ├── extraction/                  ← raw values with provenance
    ├── consolidation.md             ← proposed merges, team decisions
    └── ladder.md                    ← the proposed tiers
```

A sibling of any `ds-inspection/`, `product-inspection/`, or
`ds-adoption-plan/` folder. If you can write files, keep this folder. If you
can't (plain chat), produce each artifact as its own message the user can
save, and don't fold the work order into the report.

## Modes

Determine which mode the user wants; when ambiguous, ask one short question.

### Mode 1 — Assess (the common case)

1. **Check in.** On the first run, open with this, word for word:

   > This design token inspection will help you improve (or establish!)
   > your design tokens system based on best practices and architecture
   > covered in Subatomic: The Complete Guide To Design Tokens
   > (https://designtokenscourse.com). Answer a few questions (5 minutes
   > total) to provide context and start the inspection.

   Then run `intake/TOKEN-INTAKE.md`. If `PROFILE.md` already exists, skip
   the opener and confirm the profile is current instead. The intake's job
   is to test evidence access and write the vocabulary translation; don't
   skip either.
2. **Announce the plan.** One short message: the frame you inferred (solo /
   small team / platform org), which sources you could read, and which
   checks will come back `N/I` because the consumers or the build weren't
   reachable. Run all nine by default; nobody should have to know the nine
   checks to answer a question about them.
3. **Run checks 1 → 9 in order.** Check 1 establishes whether tiers exist;
   the rest read its record. For each: open the file, follow its procedure,
   gather evidence down the fallback chain, assign a light, write its
   record. One-line status between checks ("Check 4: red. 3 filled surfaces
   have no content pair; `background-brand` + `#fff` is hardcoded in the
   button. Moving to 5.").
4. **Write the report** from `templates/report.md` into `reports/`. The
   short version at the top is for a teammate who reads nothing else.
5. **Write the work order** from `templates/work-order.md`. Every red is a
   fix-now item with a first move; every yellow is scheduled. Every item
   cites its check and evidence.
6. **Confirm the outputs exist** before you report back: `PROFILE.md`, the
   report, and the work order, as three files (or three messages). A
   work-order-shaped table inside the report is not the work order.

### Mode 2 — Single check

Run intake-lite if there's no `PROFILE.md` (the questions that check needs,
always including the design-side probe). Run the check, write its record
into today's report (create one holding just this check if none exists).
Offer the natural next check without pushing.

### Mode 3 — Establish

For a codebase with no token set. Run intake (mode `establish`), then
`establish/ESTABLISH.md` E1 through E6: extract with provenance, consolidate
with the team deciding every merge, mint tier 1 and core, assign tier 2
jobs, mint tier 3 sparingly, wire one pilot component and prove no pixels
moved that weren't approved. Establish mode ends by running mode 1 against
what was built. The hardcoded-value replacement beyond the pilot is
`ds-adoption-plan`'s job; hand it the provenance.

### Mode 4 — Re-check

Read the most recent report. Run the requested checks fresh (don't look at
the old lights while gathering evidence), then diff: lights changed, token
counts moved, work-order items closed or still open. The delta is the
result.

## The course learner in plain chat

A common caller is someone who took the course, pasted their `tokens.json`,
and asked whether they did it right. They have one file and no repo. That's
enough for checks 1 through 7. Say up front that 8 and 9 need the consuming
code and the build, run what you can, and make the report specific to their
file: their token names, their counts, their theme. Tag everything you
couldn't reach. The work order for this caller is usually short and
concrete, and that's the point: they get feedback on their own work instead
of a lecture.

## Voice

Plain, specific, warm. Findings name tokens, files, and counts. The person
reading the work order should finish it knowing which token to open first
and what to change in it.
