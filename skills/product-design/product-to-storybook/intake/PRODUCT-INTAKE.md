# Product intake

<!-- WORDSMITH: the opening and the five questions are Brad's final wording.
The login script below is still draft (bradfrost/skills#33). -->

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

## The opening

Say this first, before any question, in exactly these words:

> This skill takes your existing product UI and backfills a representation
> into your Storybook workshop environment. Representing product screens in
> Storybook directly connects product to system, applies atomic design
> principles, and unlocks the ability to prototype product screens using
> the design system's UI components. Answer a few questions to begin the
> backfill process.

## The five questions

Ask all five together, right after the opening. Lead with the defaults so a
person in a hurry can say "defaults are fine" and move on.

### 1. Where does the product live?

> **Where does the product live?** Please provide a path to the product
> source code repository and/or a URL to the live product. Product source
> code will produce richer results as it surfaces imports, templates, design
> system usage, and more. A live product URL works too, but rendered pages
> don't provide as much context.
>
> Provide access to the product repo and/or product URL.

Record: repo path, URL, and which one you actually had. If it's URL-only,
every template in the inventory gets tagged `[inferred]`.

### 2. Where does your design system's Storybook live?

The Storybook intake runs before this question, so the path is already
known. Surface it and ask for confirmation:

> **Where does your design system's Storybook live?** The intake identified
> the path as `/path/to/storybook/`.
>
> - This is correct (Y)
> - Provide another path

Fill in the real path from `STORYBOOK.md`. If the intake somehow hasn't
run, run it now and come back; never ask this question with a blank path.

### 3. What Storybook category should the product screens belong to?

> **What Storybook category should the product screens belong to?** For
> clarity, product screens live in a separate section in Storybook than
> core components.
>
> - Use existing structure if it exists
> - `Products/<product name>/` (Default)
> - Provide your own Storybook category structure

When `STORYBOOK.md` found an existing product section, name it in the
first option (for example "Use existing structure: `Pages/we are here./`")
so the person knows what they're choosing. Record the section title and the
file path it maps to.

### 4. How do you want to handle non-system components?

> **How do you want to handle non-system components?**
>
> - **A. Import them as-is into the page** - This scopes the custom markup
>   & CSS so it won't leak into anything else, and is outlined so it's
>   obvious what's not in the system. (Recommended. You lose nothing and
>   you see the gaps.)
> - **B. Split each one into its own recipe or pattern.** - Each custom
>   component will be filed as a named piece next to the stories. This
>   doesn't turn them into design system components, but makes it easy to
>   turn into formal components later.
> - **C. Leave them out** - Replace custom components with a placeholder so
>   the page articulates only the system-powered components and reads as a
>   wireframe wherever the system currently has no answer.
> - **D. Something else**

Record the letter. Option C is the only one that hides UI, so if they pick
it, say plainly that the side-by-side report will show holes and that's
expected.

### 5. Would you like to file issues for gaps in the system?

> **Would you like to file issues for gaps in the system?** Every custom
> component is a potential gap in the design system. This process will keep
> a ledger of those gaps.
>
> - **A. Automatically file/update issues for gaps in the design system's
>   issue tracker** (recommended)
> - **B. Present the gaps for review before filing/updating any issues**
> - **C. Don't file/update gap issues; Only produce the gaps ledger
>   (`GAPS.md`)**

Record the letter and, for A or B, the repo the issues go to and the label
to use. Filing is always one issue per distinct gap, deduped against open
issues, never one per product; `phases/phase-4-proof.md` has the rule.

---

## When the product needs a login

Don't ask this up front. It comes up in phase 1 or 2 the moment a page
refuses to render without a session. When it does, say this:

<!-- WORDSMITH: draft -->
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
