---
name: storybook-to-product
description: Carry UI designed and built in your design system's Storybook into the production product, all the way to a pull request. Assesses the work region by region, sorts real copy from placeholder content, translates the story's markup and styles into the product's own templates, wires it to the product's data, scripts, forms, and links, and proves in a browser that the product matches the story. Use when the user says "ship this story", "take this Storybook page to production", "port the redesign into the site", "carry this over from Storybook", "storybook to product", or points at a story and a product repo. The reverse of product-to-storybook, which brings product screens into Storybook. Also runs a catch-up that carries later Storybook changes over, one pull request at a time.
---

# Storybook to Product

You designed the next version of a product right there in Storybook, out of
the design system's real components, with real content, without tripping
over a backend. It looks finished. It's front-of-the-front-end code that's
largely ready for production.

Largely. Between that story and the live product sits everything Storybook
never had to deal with: the product's own templating language, its data
files, the modal that opens when you click the thumbnail, the form that
posts to a serverless function, the copy somebody invented to fill out the
design, and the design system release the new components haven't shipped
in yet.

This skill closes that distance. It assesses the work, carries the markup
and styles into the product in the product's own language, wires them up
to everything behind them, and proves the product now matches what you
designed. It ends with a pull request, and it records exactly which version
of each story shipped, so the next round of Storybook tweaks can follow
with a catch-up instead of a do-over.

## What this is not

- **Not `product-to-storybook`.** That one brings a product's existing
  screens *into* Storybook. This one takes screens *out* of Storybook and
  into production. They're built to work as a pair: when a story came from
  `product-to-storybook`, this skill reads its paper trail and gets most of
  its answers for free.
- **Not `ds-adoption-plan`.** That one plans a migration of a product's
  bespoke UI onto the system, from the product outward. This one starts
  from a finished design and asks what it takes to ship it. It borrows
  the adoption plan's effort grades so the two estimates read the same.
- **Not `vibe-killer`.** That one rebuilds a single page out of the system.
  Here the page is already built from the system; the job is getting it
  into production.
- **Not a release tool.** It never publishes the design system, never
  merges, and never deploys.

## Ground rules

1. **The story is the spec, and the product is the destination.** The
   story decides *what* renders. The product decides *how* it's written:
   its templating language, its file names, its CSS architecture, its
   class names. A handoff that makes the product look like Storybook code
   is a handoff the product's maintainers will undo.
2. **Assess before you touch.** Every region gets a disposition, every
   behavior gets named, and every system dependency gets checked, all
   before a single product file changes. The assessment gets shown to the
   user and confirmed, because a wrong retirement deletes something the
   business still needs.
3. **Invented content never ships.** A fixture mixes real copy with
   placeholder content that exists only to fill a shape. Every field gets a
   provenance and a decision, and the build gets searched for every
   invented value before anyone calls it done. Fake people on a live page
   is the one outcome this skill exists to prevent.
4. **Content and media are the person's call.** Defaults for copy, based on
   evidence. Every image and every video, asked.
5. **Unreleased means ask.** When a story leans on design system work the
   product can't install yet, the skill stops and asks what to do. It never
   ships a product pointed at a local copy of the design system.
6. **Nothing from Storybook leaks into production.** Origin markers,
   `@scope` wrappers, decorators, fixture leftovers: all stripped, then
   proven stripped by searching the built output.
7. **Every trigger gets a target.** Storybook shows the look of an
   interaction and none of the behavior. Every modal, form, toggle, and
   link gets wired, and every trigger is walked in a real browser.
8. **The product's own rules win.** A `CLAUDE.md`, `AGENTS.md`, or process
   config in the product repo outranks anything here.
9. **It ends at a pull request.** Merging and deploying belong to a person,
   every time, even when every check is green.
10. **Nothing gets overwritten on a catch-up.** A field changed in both
    Storybook and production is a conflict, and a person decides. The live
    edit might be the right one.

## How a run goes

### Mode 1: Handoff

1. **Intake** (`intake/HANDOFF-INTAKE.md`). Four questions, each with a
   default. Records the answers in the product repo's
   `storybook-to-product/HANDOFF.md`.
2. **Phase 1: Assessment** (`phases/phase-1-assessment.md`). Map every
   region, check every system dependency, inventory every behavior,
   estimate. Ask the release gate question if it comes up. **Stop and show
   the user.** Wait.
3. **Phase 2: Content** (`phases/phase-2-content.md`). Tag every field's
   provenance, propose defaults, ask once in a batch. Every asset, asked.
4. **Phase 3: Integration** (`phases/phase-3-integration.md`). Bump the
   design system, translate the markup, bring the styles home, retire what
   was confirmed.
5. **Phase 4: Wiring** (`phases/phase-4-wiring.md`). Data, behaviors,
   forms, links, the document around the page, and the link record.
6. **Phase 5: Proof** (`phases/phase-5-proof.md`). Build, search for
   leaks, side by side with the story, exercise every behavior, axe, the
   report, and the pull request.

### Mode 2: Catch-up

`phases/catch-up.md`. Reads the link record, finds every story change since
the version that shipped, checks production for edits made since the
handoff, and carries the difference over in its own pull request.

## Where things go

**The product's code** changes on a branch in the product repo, in the
product's own conventions.

**The paper trail** lives at the product repo's root:

```
storybook-to-product/
├── HANDOFF.md                ← intake answers, both versions, runs
├── ASSESSMENT.md             ← regions, dependencies, behaviors, estimate
├── CONTENT.md                ← every field and asset, with its decision
├── REPORT.md                 ← what was proven, side by sides
├── links.json                ← which story version is in production
└── catch-up/
    └── YYYY-MM-DD.md         ← one per catch-up
```

A sibling of any `ds-adoption-plan/` or `product-inspection/` folder. When
the story came from `product-to-storybook`, its paper trail in the design
system repo (`product-to-storybook/<product>/`) is read first and gets a
**Handoffs** note once the work merges. `reference/LINKS.md` explains how
the two sides stay connected.

## Files in this kit

- `intake/HANDOFF-INTAKE.md`: the four questions, and the ones that wait
  for their moment
- `phases/phase-1-assessment.md`: regions, dependencies, behaviors,
  estimate, then the checkpoint
- `phases/phase-2-content.md`: whose content ships, field by field
- `phases/phase-3-integration.md`: markup and styles, in the product's
  language
- `phases/phase-4-wiring.md`: data, behaviors, forms, links
- `phases/phase-5-proof.md`: build, render, exercise, report, pull request
- `phases/catch-up.md`: carry later Storybook changes over
- `reference/TRANSLATION.md`: story constructs to product templates
- `reference/LINKS.md`: the connective tissue between Storybook and the
  product
- `reference/CAPABILITIES.md`: what this skill can and cannot do
- `templates/`: output shells for every file in the paper trail

## Voice

Plain, energetic, specific. The assessment is a table of regions with
dispositions and a number at the bottom. The content ledger shows both
values side by side. The report says what was built, what was proven, and
what's still waiting on somebody. The person reading it should finish
knowing exactly what's in the pull request, what they need to decide, and
whether it's ready to ship.
