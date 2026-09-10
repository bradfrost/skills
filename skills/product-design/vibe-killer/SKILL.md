---
name: vibe-killer
description: Convert a vibe-coded webpage into a page built entirely from YOUR design system. Takes an AI-generated artifact, a landing page, a prototype, or any page carrying bespoke CSS, works out what each region is trying to do, and rebuilds it from real components and real tokens. Use when the user says "rebuild this with our design system", "convert this page", "make this use our components", "de-vibe this", "kill the vibes", "turn this artifact into something real", pastes an HTML file or a URL and names their design system, or wants a before/after demo of a page moving onto the system. Builds a one-time profile of the design system's runtime and component vocabulary, then converts against it. Companion to ds-adoption-plan, which plans a whole product's migration; this one converts a single page and hands back working code.
---

# Vibe Killer

Somebody typed a prompt and got back a webpage. It has a purple gradient
hero, three cards with emoji in little rounded squares, and 400 lines of CSS
that exist nowhere else in the world. It looks fine. It is also a dead end:
nothing in your organization can maintain it, theme it, audit it, or reuse
one pixel of it.

This skill takes that page and rebuilds it out of your design system, so it
stops being an orphan and starts being infrastructure. Same content, same
job, running on the components your team already maintains.

The point is not tidiness. A page built from your system inherits every
investment behind it: your themes, your accessibility work, your tokens,
your browser support, your one place to fix a bug. A vibe-coded page
inherits nothing and asks you to maintain it forever.

## What this is not

- **Not `ds-adoption-plan`.** That one prices and schedules a whole
  product's migration. This one converts one page, right now, and hands you
  code you can run.
- **Not `product-inspection`.** That one grades a shipped product across ten
  stations. This one is a single procedure with a single deliverable.
- **Not a linter.** Nothing here reports on the original page and stops.
  Every run ends with a converted page or an honest explanation of why it
  couldn't produce one.

## Ground rules

1. **Never invent a component, a prop, a slot, or a token.** Every name in
   the output was read from the system's own catalog. If you're reaching for
   something you remember, stop and go read it. Content projected into a slot
   name that doesn't exist is silently dropped by most component libraries,
   which means the page renders empty with no error anywhere, and you won't
   notice until someone else does.
2. **Evidence tags travel with everything.** `[verified]` means you read it
   out of the system's catalog, MCP, manifest, repo, or docs and could point
   at the line. `[reported]` means a human told you. A conversion built
   mostly on `[reported]` names is still worth doing; it just says so at the
   top of the receipt.
3. **Zero bespoke CSS is the target, and the gap is a finding.** No custom
   classes, no hardcoded colors or spacing, no font declarations, no
   `<link>` to Google Fonts. When the system genuinely doesn't cover
   something, that's a **system gap**: name it in the receipt, propose it
   upstream, and mark the placeholder loudly in the code. Quietly
   hand-rolling a component is the one failure mode that makes this whole
   exercise pointless.
4. **Convert what the page is doing, not what it looks like.** A tell is a
   clue about intent. A gradient band at the top of the page means "this is
   the entry point," and the entry point maps to your hero or page header.
   The gradient itself is not a requirement, it's an artifact of a model's
   default taste. `reference/THE-TELLS.md` is the decoder.
5. **Content is sacred, chrome is not.** Never rewrite the page's words to
   make the conversion easier, and never drop a section because it's awkward
   to map. If some copy has AI tells of its own, flag it in the receipt and
   let the human decide. That's their call, not yours.
6. **Accessibility gets fixed on the way through.** Vibe-coded pages are
   reliably bad here: divs acting as buttons, skipped heading levels,
   `outline: none`, images with no alt text, contrast that was never
   checked. You're rebuilding the markup anyway, so rebuild it right. Every
   fix goes in the receipt, because it's some of the most persuasive
   evidence the conversion was worth doing.
7. **A page you never rendered is a claim, not a result.** Run the checks in
   phase 4. If you have no way to render or validate, say that plainly in
   the receipt rather than implying it works.
8. **No shame, ever.** Somebody made a thing, and making things is good. The
   original page is not stupid and neither is the person who prompted it.
   The receipt reports counts and facts, never snark.

## The design system: the evidence chain

This skill is design-system-agnostic. Reach your system's catalog down this
chain, using whatever exists. Never require a vendor.

1. **The system's own MCP server or CLI.** If it exposes component lookup,
   search, compose, or validate tools, use them on every run. This is the
   only source that makes a mapping `[verified]` and the only one that stays
   current on its own.
2. **A machine-readable export.** `custom-elements.json`, a component
   manifest, a token JSON, a Storybook `index.json`. Ask the user to point
   at it.
3. **The repo.** If the system's source is on disk or reachable, read the
   component files. Slower, completely authoritative.
4. **The docs site.** Component pages carry the API and the usage guidance.
   Watch for staleness; published docs commonly trail the shipped version.
5. **The design library.** Authoritative for what the system *contains* and
   for design-side naming, not for code APIs. A variant labeled `Primary` in
   Figma tells you nothing about whether the prop is `variant` or
   `appearance`. `reference/FIGMA-ACCESS.md` covers how to reach it.
6. **Interview.** Ask. Tag everything that comes back `[reported]`.

**Check the don'ts, not just the names.** The intuitively-named component is
often the wrong one, and a good catalog says so in its own guidance. Read
the target's don't-use notes and accessibility notes before you commit to a
mapping. When the catalog corrects your first instinct, that correction is
worth recording; it's usually the most interesting line in the autopsy.

## Modes

### Mode 1 — Convert a page (the common case)

Run the four phases in order. Give a one-line status between each.

1. **Get the profile.** Read `vibe-killer/SYSTEM.md` if it exists and confirm
   it's still current. If there isn't one, run `intake/SYSTEM-INTAKE.md`
   first. It takes a few minutes and everything afterward is faster and more
   accurate.
2. **Ask the posture question** below. Don't skip it and don't guess.
3. **Phase 1 — Forensics** (`phases/phase-1-forensics.md`). Read the source,
   catalog the tells, and write down what each region is *for*.
4. **Phase 2 — Mapping** (`phases/phase-2-mapping.md`). Every region gets a
   real component, a real composition, or an honest gap.
5. **Phase 3 — Conversion** (`phases/phase-3-conversion.md`). Write the page.
6. **Phase 4 — Proof** (`phases/phase-4-proof.md`). Validate it, count what
   changed, write the receipt.

### Mode 2 — Build or refresh the system profile

Run `intake/SYSTEM-INTAKE.md` on its own. Also the right move when the system
ships a major version, when a conversion produced a component name nobody
could find, or when the runtime URLs stopped working.

### Mode 3 — Convert against a different system

Same page, second profile. This is the head-to-head: what does each system
make easy, and where does each one leave you writing your own markup? Keep
both receipts and diff the gap lists.

## The posture question (ask this every run)

Two ways a conversion can go, and they produce genuinely different pages.
Ask before phase 2, in roughly these words:

> **Which way do you want this to go?**
>
> **A. Your system's rules win** (this is what I'd recommend). I take what
> the page is *for*, its content, its hierarchy, what each region is doing,
> and I rebuild it the way your system would have built it in the first
> place. Where the original made a call your system disagrees with, your
> system wins. The result will look like your product. It will not look like
> a screenshot of the original.
>
> **B. Follow the original's lead.** I hold the original's layout and visual
> decisions as closely as your components allow, and swap out what's
> underneath. Worth it when the shapes have to match for a before/after,
> when someone genuinely likes the design, or when the page is a faithful
> mockup of something real.
>
> **Default is A.** Most vibe-coded pages are carrying design decisions
> nobody actually made. Porting those faithfully means importing somebody
> else's accident into your codebase, and then maintaining it.

If the user picks B, say plainly what B costs before you start: the honest
version is that "hold the original's look" often means the gap list gets
longer, because a bespoke visual choice with no equivalent in the system
becomes either a gap or an override, and overrides are the thing this whole
skill exists to delete. Record the posture at the top of the autopsy so a
later reader knows why the page looks how it looks.

## Where the converted page goes

**Default: one standalone, runnable page.** A single file that loads your
system's real runtime and renders in a browser with no build step. That's
the demo, and it's the thing you can hand to anyone.

**Ask where they want it.** Some people want it written into a repo instead,
as real templates in their framework's syntax, sitting next to their other
pages. Ask once, then do that instead. When you're writing into a repo,
follow that project's conventions over anything here, and never invent a new
folder or pattern the project doesn't already use.

Either way, `vibe-killer/` keeps the paper trail.

## Files in this kit

- `intake/SYSTEM-INTAKE.md` — the interview that builds `SYSTEM.md`
- `reference/THE-TELLS.md` — the field guide to vibe-coded pages, and what
  each tell means about intent
- `reference/CAPABILITIES.md` — what this skill can and cannot do
- `reference/FIGMA-ACCESS.md` — reaching a design library, and what each
  bridge actually sees
- `phases/phase-1-forensics.md` — read the page, catalog the tells
- `phases/phase-2-mapping.md` — region to component, with evidence
- `phases/phase-3-conversion.md` — write the page
- `phases/phase-4-proof.md` — validate, count, and write the receipt
- `templates/system.md`, `templates/autopsy.md`, `templates/receipt.md` —
  output shells

## State (in the user's project)

```
vibe-killer/
├── SYSTEM.md                        ← the design system profile, built once
└── kills/
    └── YYYY-MM-DD-<slug>/
        ├── autopsy.md               ← tells found, regions mapped
        ├── receipt.md               ← the before/after scorecard
        └── (the converted page, unless it went into the repo)
```

A sibling of any `ds-inspection/`, `product-inspection/`, or
`ds-adoption-plan/` folder. They coexist happily in one project. If you can
write files, keep this folder. If you can't (plain chat), produce each
artifact as its own message the user can save, and don't fold them together.

## Voice

Plain, energetic, specific. Findings are counts and file references, never
vibes: "31 bespoke class names, 47 hardcoded hex values, 0 focus styles"
beats "lots of custom CSS." The person reading the receipt should finish it
knowing exactly what moved onto the system, what didn't, and what to do
about the part that didn't.
