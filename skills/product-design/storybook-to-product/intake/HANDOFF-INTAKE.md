# Handoff intake

Three questions, each with a default, asked in one batch. The answers go
into `storybook-to-product/HANDOFF.md` in the product repo, so a catch-up
never asks twice.

Budget five minutes. If the user already answered any of these in
conversation, don't ask again; write the answer down and say you did.

---

## Before you ask

Look for what's already known about this story and this product:

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
- **The product's own rules and workflow:** `CLAUDE.md`, `AGENTS.md`, a
  contributing guide, a process config, a pull request template, the branch
  names in its recent history, whether its host builds preview deploys.
  They outrank this skill. Read them now, and follow them for how the work
  branches, commits, and ships. **Never ask about it**, and depart from it
  only when the user explicitly says so. When the product states nothing,
  work on a new branch named `storybook-to-product/<date>` and open a pull
  request, and say that's what you'll do.
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

> This skill takes UI you've designed and built in your Storybook workshop
> environment and carries it into your production product. It assesses the
> work, integrates the front-of-the-front-end code into your product's
> codebase, and wires it up to your product back-of-the-front-end (data,
> functionality, business logic), so the screens you designed in Storybook
> become the screens your users actually see. Answer a few questions to get
> started.

## The three questions

Ask all three together, right after the opening. Lead with the defaults so a
person in a hurry can say "defaults are fine" and move on.

### 1. Which stories are going to production?

> **Which stories are going to production?** You can say “All stories in
> `<Storybook section>`,” or paste links to specific stories.

Fill in the real section when the design system's paper trail names one
(for example `Products/AI & Design Systems course/`). When none is known,
ask only the second half, unchanged: paste links to specific stories. Record the story IDs,
the story files, the design system repo, and the branch they live on. A
story on an unmerged branch is fine; say so, because it usually means the
release gate question is coming.

### 2. Where does the product live?

> **Where does the product live?** The handoff found the product’s
> repository at `/path/to/product/` and the live product at `https://…`.
> Confirm or provide a different path or URL.

Fill in the real values from the design system's paper trail or the
product's own files. When nothing names them, ask for both: the repo is
required (this skill changes code), the URL is for side by sides with
production.

### 3. How should content carry over?

> **How should copy and content carry over?** Copy/content in Storybook can
> be tricky; it's a blend of placeholder/hard-coded content and content
> captured from the live product.
>
> - **A. Decide field by field** - Every piece of content gets a default
>   based on where it came from: copy you edited in Storybook carries over,
>   the product's real content replaces anything invented, and anything
>   unclear gets asked about. (Recommended. Nothing fake ships, and you only
>   weigh in where it matters.)
> - **B. Storybook copy wins** - You've hand-crafted the copy in Storybook,
>   so it carries over everywhere it isn't a placeholder.
> - **C. Product content wins** - Keep the product's existing content and
>   use Storybook for the design only.
> - **D. Something else**
>
> Images and media always get asked about one at a time, whatever you pick
> here.

Record the letter. Even with B or C, invented content never ships;
`phases/phase-2-content.md` has the rule.

---

## Questions that wait for their moment

Don't ask these up front. They come up when the run reaches them.

**The release gate.** The moment phase 1 finds design system work the
product can't install yet. The exact wording is in
`phases/phase-1-assessment.md`.

**A page behind a login.** When a product page won't render without a
session:

> **This page requires a login.** Credentials are never handled by this
> process. Sign in with your own browser and say "Signed in," or say "Skip
> it" and this page's side by side gets marked "not captured."

**Retirements.** Every region the story dropped from the product gets its
own yes before anything is removed. Phase 1 asks.

---

## Write the handoff file

Fill `templates/handoff.md` and save it to
`storybook-to-product/HANDOFF.md` in the product repo, on the branch the
product's workflow calls for. Read the three answers back in three lines,
plus one line naming the workflow you'll follow and where it came from.
Then start phase 1.
