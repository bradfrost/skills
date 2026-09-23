---
name: product-to-storybook
description: Backfill an existing product's screens into your design system's Storybook as representative page templates, rebuilt from the LOCAL design system wherever the product already uses it, with every region that isn't from the system flagged in plain sight. Use when the user says "get this product into Storybook", "backfill our screens", "represent this product in the design system", "I want to see how a component change ripples across products", "relocate these pages into Storybook", or names a product (a site, an app, a repo, a URL) and a Storybook. Relocation, not translation: it moves screens in and flags what isn't from the system; it never converts bespoke UI onto the system (that's vibe-killer) and never plans a migration (that's ds-adoption-plan). Also runs a refresh that reports how far the product has drifted from its Storybook copy since the last capture.
---

# Product to Storybook

Your design system's Storybook shows every component in isolation. It shows
almost nothing about the products those components live in. So when you
change a card or a table, you're guessing at what happens downstream, and
the only way to stop guessing is to open every product, one at a time, and
look.

This skill fixes that. It takes an existing product, works out its core page
templates, and rebuilds representative versions of them inside your
Storybook, using your *local* design system wherever the product already
uses it. Once every product is in there, a change to one component shows its
ripple across all of them at once, and you can design the next version of a
product right there in Storybook, without tripping over a backend.

It's a backfill. The screens it produces are page templates with a real
cross-section of content frozen into them, not live mirrors of every URL.
That's the point: representative enough to design against, and detached
enough that nothing behind them can break.

## What this is not

- **Not `vibe-killer`.** That one *translates* a bespoke page onto your
  system. This one *relocates* a product's screens into Storybook and flags
  what isn't from the system. It never converts a region, ever. If you want
  the flagged regions converted, that's a vibe-killer run afterward.
- **Not `ds-adoption-plan`.** That one prices and schedules a migration.
  This one produces screens you can look at today, plus a list of gaps the
  system might want to close.
- **Not a prototyping tool.** Every screen it builds already exists. "This
  product doesn't exist yet" is prototyping, and prototyping is a different
  job with different placeholders.
- **Not production work.** It writes stories and fixtures. It does not
  author recipes, patterns, or components in your library on its own. When
  the product carries UI that isn't from the system, it *asks* what you want
  done with it, and the answer is recorded before it does anything.

## Ground rules

1. **The local design system wins.** Stories render with the version of the
   system that's checked out next to them, not the version the product pins.
   That's what makes the ripple visible. The product's pinned version gets
   recorded, and every prop or slot that no longer exists locally gets
   flagged as **version drift** in the gap ledger, not silently fixed.
2. **Templates, not URLs.** A site with 3,000 pages has maybe five
   templates. Find the templates and their permutations (within reason), and
   build those. The inventory gets shown to the user and confirmed *before*
   a single story is written, because a wrong grouping here is the one
   mistake that wastes the whole run.
3. **Real content, frozen once.** Every story carries a cross-section of the
   product's actual content, chosen to show the shapes the system has to
   support: the post with the YouTube embed, the card with the 60-character
   title, the list with 40 tags. Captured into fixtures with a date and a
   source URL. Never lorem, and never fetched live.
4. **Never a real person's data.** Screens behind a login get fixtures
   written from the *shape* of the data, not from anyone's account. If you
   find real user data in a capture, stop, delete it, and say so. This is a
   stop condition, not a warning.
5. **Everything is marked.** Every region in a story says where it came
   from: `data-origin="system"`, `data-origin="product"`, or
   `data-placeholder="missing-component"`. `reference/MARKERS.md` is the
   convention. The gap ledger is scraped from these marks, so a region you
   forgot to mark is a gap you'll never see.
6. **Product CSS stays in its lane.** Anything the product's own stylesheet
   contributes is wrapped in `@scope` and loaded only on that product's
   stories. Then you prove it: render a design system story before and after,
   and confirm it didn't change. The ripple runs from the system outward.
   It never runs from a product back into the system.
7. **Some shift is expected, and you say so.** A story built on the local
   system should look a little different from the live page, because the
   local system is newer than what the product pins. The side-by-side report
   shows both and tells the reader plainly which differences are version
   drift and which are the skill getting it wrong.
8. **Nothing gets overwritten on a refresh.** A later run reports what
   drifted and asks. The person may have redesigned that screen on purpose.

## How a run goes

### Mode 1 — Backfill a product

1. **Storybook intake** (`intake/STORYBOOK-INTAKE.md`), once per design
   system. Learns how this Storybook writes a story, where product screens
   should live, and how the system loads. Skip it when
   `product-to-storybook/STORYBOOK.md` already exists and is current.
2. **Product intake** (`intake/PRODUCT-INTAKE.md`), once per product. Five
   questions, each with a default. Records the answers in the product's
   `GARAGE.md` so a refresh doesn't ask again.
3. **Phase 1 — Inventory** (`phases/phase-1-inventory.md`). Find the
   templates and their permutations. **Stop and show the user.** Wait.
4. **Phase 2 — Capture** (`phases/phase-2-capture.md`). Choose the content
   cross-section and freeze it into fixtures.
5. **Phase 3 — Relocation** (`phases/phase-3-relocation.md`). Write the
   stories. System components where the product uses them, marked regions
   everywhere else, product CSS scoped.
6. **Phase 4 — Proof** (`phases/phase-4-proof.md`). Render, compare side by
   side, prove the system's own stories didn't change, write the gap ledger
   and the report.

### Mode 2 — Refresh (drift check)

`phases/refresh.md`. Re-reads the product, compares it to what's in
Storybook, and reports what moved: templates added or removed, permutations
changed, the pinned version bumped, new UI that isn't from the system. It
writes a drift report and changes nothing else.

### Mode 3 — Build or refresh the Storybook profile

Run `intake/STORYBOOK-INTAKE.md` on its own. The right move when the
Storybook moves to a new major version, when stories start landing in the
wrong section, or when the system's load order changed.

## Reading the product

A source repo, a live URL, or both. Question 1 of `intake/PRODUCT-INTAKE.md`
says what each one buys, in the words the user sees. Record which one you
had; every downstream artifact says so.

## Where things go

**Stories** go into the design system repo, in the Storybook section the
user chose (default: `Products/<product>/`). One story file per template,
permutations as named stories inside it, each template leading with a
representative `Default`. Fixtures sit next to the story file.

**The paper trail** lives at the design system repo's root:

```
product-to-storybook/
├── STORYBOOK.md                     ← how this Storybook works, built once
├── markers.css                      ← the origin/placeholder stylesheet
└── <product>/
    ├── GARAGE.md                    ← intake answers, source, pinned version
    ├── INVENTORY.md                 ← templates and permutations, confirmed
    ├── GAPS.md                      ← the gap ledger
    ├── REPORT.md                    ← side-by-side proof, what was verified
    └── drift/
        └── YYYY-MM-DD.md            ← one per refresh
```

A sibling of any `ds-inspection/`, `vibe-killer/`, or `ds-adoption-plan/`
folder. If the product repo carries `adoption-plan/MAPPING.md` or
`product-inspection/GARAGE.md` from the sibling skills, read them first.
They already say which regions are system and which are custom, and you
confirm that against the rendered page instead of starting over.

## Files in this kit

- `intake/STORYBOOK-INTAKE.md` — learn the host Storybook, once
- `intake/PRODUCT-INTAKE.md` — the five questions, once per product
- `phases/phase-1-inventory.md` — templates and permutations, then the
  checkpoint
- `phases/phase-2-capture.md` — the content cross-section, frozen
- `phases/phase-3-relocation.md` — write the stories
- `phases/phase-4-proof.md` — render, compare, prove, report
- `phases/refresh.md` — the drift check
- `reference/MARKERS.md` — the origin and placeholder convention
- `reference/CAPABILITIES.md` — what this skill can and cannot do
- `templates/` — output shells for every file in the paper trail

## Voice

Plain, energetic, specific. The inventory is a list of templates with
counts. The gap ledger is a table with screenshots. The report says what was
rendered, what matched, what shifted, and why. The person reading it should
finish knowing exactly which screens are now in Storybook, which regions
aren't from the system, and what to do about them.
