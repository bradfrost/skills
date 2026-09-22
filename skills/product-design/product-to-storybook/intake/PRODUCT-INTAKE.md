# Product intake

<!-- DRAFT STATUS: every quoted question in this file is draft wording. Brad
wordsmiths each one after the hub dry run, before the PR merges. Search for
WORDSMITH to find them. Delete this banner and the markers when done. -->

Five questions, each with a default, asked in one batch. The answers go into
`product-to-storybook/<product>/GARAGE.md` so a refresh never asks twice.

Budget five minutes. If the user already answered any of these in
conversation, don't ask again; write the answer down and say you did.

---

## Before you ask

Look for what the product repo already knows about itself:

- `adoption-plan/MAPPING.md` (from `ds-adoption-plan`) — which regions are
  system and which are custom, already worked out. Carry it across with its
  evidence tags and confirm it against the render in phase 3.
- `product-inspection/GARAGE.md` — the product's profile, including how it
  loads the system and which version it pins.
- `package.json` — the pinned design system version. Record it now; phase 3
  compares it to the local version.
- The product's `CLAUDE.md` or `AGENTS.md` — how the team wants the repo
  read.

Say what you found first.

---

## The five questions

Ask all five together. Lead with the defaults so a person in a hurry can
say "defaults are fine" and move on.

### 1. Where's the product?

<!-- WORDSMITH -->
> **Where's the product?** A path to the repo, a live URL, or both. A repo
> gives me the richest results, because the templates are right there in the
> source and I can see exactly which parts come from your design system. A
> live URL works too, but the template list becomes my best guess from the
> rendered pages, and I'll ask you to check it.
>
> **Default:** both, if you have both.

Record: repo path, URL, and which one you actually had. If it's URL-only,
every template in the inventory gets tagged `[inferred]`.

### 2. Where's your design system's Storybook?

<!-- WORDSMITH -->
> **Where's your design system's Storybook?** I'll look for it myself and
> tell you what I found; I just need you to confirm I've got the right one.
>
> **Default:** the one in `product-to-storybook/STORYBOOK.md`, if the intake
> already ran.

If the Storybook intake hasn't run, run it now and come back.

### 3. Where should product screens live?

<!-- WORDSMITH -->
> **Where should this product's screens live in Storybook?** They need a
> home of their own so nobody mistakes a product screen for a system
> component.
>
> **Default:** `Products/<product name>/`. (If your Storybook already has a
> section for product pages, I'll suggest that one instead.)

Record the section title and the file path it maps to, from the Storybook
profile.

### 4. What do we do with UI that doesn't come from your design system?

<!-- WORDSMITH -->
> **Some of this product's UI won't come from your design system.** A site
> header the product built itself, a widget, a layout nobody made a
> component for. I'll flag every one of those so you can see them at a
> glance. What do you want done with them in the stories?
>
> - **A. Bring them in as-is.** The product's own markup and CSS, scoped so
>   it can't leak into anything else, and outlined so it's obvious what's
>   not from the system. *(Default. You lose nothing and you see the gaps.)*
> - **B. Split each one into its own recipe or pattern.** Same markup, but
>   filed as a named piece next to the stories, which makes it easy to turn
>   into a real component later. I'll set up the files; I won't turn them
>   into production components.
> - **C. Leave them out.** A marked placeholder where each one was. The
>   page reads as a wireframe wherever the system has no answer.
> - **D. Something else.** Tell me.
>
> **Default:** A.

Record the letter. Option C is the only one that hides UI, so if they pick
it, say plainly that the side-by-side report will show holes and that's
expected.

### 5. Where should gaps go?

<!-- WORDSMITH -->
> **Every region that isn't from your system is a possible gap in it.** I'll
> keep a ledger of those no matter what. Do you also want them filed?
>
> - **A. The ledger only** (`GAPS.md` next to the stories).
> - **B. The ledger, plus a GitHub issue per distinct gap** on your design
>   system's repo. One issue per gap, not per product: the same site header
>   seen in six products is one issue that says "seen in 6 products." I'll
>   check for an open issue before filing and update it instead of
>   duplicating.
> - **C. Both, but show me the list before you file anything.**
>
> **Default:** A.

Record the letter and, for B or C, the repo the issues go to and the label
to use.

---

## When the product needs a login

Don't ask this up front. It comes up in phase 1 or 2 the moment a page
refuses to render without a session. When it does, say this:

<!-- WORDSMITH -->
> This screen needs a login. Here's how I handle that: I never touch
> credentials, and I never put a real person's data into a fixture. If you
> have the repo, I'll build the fixtures from the shape of the data in the
> templates. If I need to see the rendered page, sign in yourself in your
> own browser and I'll read what's on screen, then write fixtures with made
> up values in the real shapes.

Record the choice in `GARAGE.md`. If a capture turns out to contain real
user data anyway, stop, delete it, and say so before continuing. That's rule
4 in `SKILL.md` and it has no exceptions.

---

## Write the garage

Fill `templates/garage.md` and save it to
`product-to-storybook/<product>/GARAGE.md`. Read the five answers back in
five lines. Then start phase 1.
