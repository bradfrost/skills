# Handoff intake

Four questions, each with a default, asked in one batch. The answers go
into `storybook-to-product/HANDOFF.md` in the product repo, so a catch-up
never asks twice.

Budget five minutes. If the user already answered any of these in
conversation, don't ask again; write the answer down and say you did.

---

## Before you ask

**First, make sure both checkouts are current.** Run `git status` and
`git log --oneline HEAD..@{u}` in the product repo and in the design system
repo. A product checkout that's behind its remote, or carries uncommitted
edits, is a stale destination: the whole assessment gets built against
code that may already be gone. (The first dry run of this skill found the
product six commits behind, and upstream had already removed two of the
regions the assessment was about to retire.) If either one is behind or dirty, stop
and ask whether to fetch, pull, or work from what's there, and record the
answer.

Then look for what's already known about this story and this product:

- **`storybook-to-product/HANDOFF.md` in the product repo.** A handoff has
  already happened. This is probably a catch-up (`phases/catch-up.md`), not
  a new handoff. Say so and ask which one they want.
- **`product-to-storybook/<product>/` in the design system repo.**
  `GARAGE.md` has the product's repo path, live URL, and pinned version;
  `INVENTORY.md` maps every story to the product template it came from;
  `GAPS.md` lists the product bugs found on the way in. This is the richest
  source there is, and when it exists most of the questions below already
  have answers. It describes the product **as it was captured**, though,
  and a redesign moves on from there: patterns get deleted, forks become
  recipes, permutations get cut. Where the paper trail and the story's
  current code disagree, the paper trail says what the product *had*, and
  the story says what ships.
- **`ds-adoption-plan/` or `product-inspection/` in the product repo.** The
  mapping and the effort grades carry straight into phase 1.
- **The product's own rules:** `CLAUDE.md`, `AGENTS.md`, a contributing
  guide, a process config. They outrank this skill. Read them now.
- **Both version numbers.** For the story: the design system's package
  version, the commit of the story's last change, and which release
  branches and tags contain that commit (`git branch -a --contains <sha>`,
  `git tag --contains <sha>`). A package that says 0.68.0 can carry work
  that only exists on `release/0.69.0`. For the product: the range in its
  manifest and the exact version in its lockfile and installed tree.

Say what you found first.

---

## The opening

Say this first, before any question, in exactly these words:

> This skill takes UI you designed and built in your Storybook workshop and
> carries it into your production product. It assesses the work, brings
> the markup and styles over in the product's own language, wires them up
> to the product's data and functionality, and proves the product matches
> what you designed. Answer a few questions to begin the handoff.

## The four questions

Ask all four together, right after the opening. Lead with the defaults so a
person in a hurry can say "defaults are fine" and move on.

### 1. Which stories are going to production?

> **Which stories are going to production?** Please provide a link to the
> story in your Storybook, and/or the path to the story files in your
> design system repo.
>
> - Every story in `<Storybook section>` (Default)
> - Only the stories I list

Fill in the real section when the design system's paper trail names one
(for example `Products/AI & Design Systems course/`). Record the story IDs,
the story files, the design system repo, and the branch they live on. A
story on an unmerged branch is fine; say so, because it usually means the
release gate question is coming.

### 2. Where does the product live?

> **Where does the product live?** The handoff identified the product repo
> as `/path/to/product/` and the live product as `https://…`.
>
> - This is correct (Y)
> - Provide another path or URL

Fill in the real values from the design system's paper trail or the
product's own files. When nothing names them, ask for both: the repo is
required (this skill changes code), the URL is for side by sides with
production.

### 3. How should content carry over?

> **How should content carry over?** Copy in Storybook is a mix of real
> copy you edited there, content captured from the live product, and
> placeholder content invented to fill out the design.
>
> - **A. Decide field by field.** Every piece of content gets a default
>   based on where it came from: your Storybook edits carry over, the
>   product's real content replaces anything invented, and anything unclear
>   gets asked about. (Recommended)
> - **B. Storybook content wins** wherever it isn't invented.
> - **C. The product's content wins** everywhere, and Storybook supplies the
>   design only.
> - **D. Something else**
>
> Images and media are always asked about one at a time, whatever you pick
> here.

Record the letter. Even with B or C, invented content never ships;
`phases/phase-2-content.md` has the rule.

### 4. Where should the work land?

> **Where should the work land?** Production code changes happen on a
> branch and arrive as a pull request, so nothing reaches your live product
> until you merge it.
>
> - **A. A new branch and pull request** named
>   `storybook-to-product/<date>` (Default)
> - **B. A branch you name**
> - **C. Something else**

Record the branch and the base branch. If the product's host builds a
preview for every pull request, say so now: the report will link to it.

---

## Questions that wait for their moment

Don't ask these up front. They come up when the run reaches them.

**The release gate.** The moment phase 1 finds design system work the
product can't install yet. The exact wording is in
`phases/phase-1-assessment.md`.

**A page behind a login.** When a product page won't render without a
session:

> **This page requires a login.** Credentials are never handled by this
> process.
>
> - **A. Sign in yourself.** Log in with your own browser, and the page is
>   checked from there. (Recommended)
> - **B. Skip the live check for this page.** The side by side for it is
>   marked "not captured."

**Retirements.** Every region the story dropped from the product gets its
own yes before anything is removed. Phase 1 asks.

---

## Write the handoff file

Fill `templates/handoff.md` and save it to
`storybook-to-product/HANDOFF.md` in the product repo, on the branch from
question 4. Read the four answers back in four lines. Then start phase 1.
