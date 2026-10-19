# Catch-up: carry what changed since the last handoff

The redesign ships, and then somebody tweaks a headline in Storybook, or
nudges a card's spacing, or adds a testimonial. The story is ahead of
production again. This mode carries just the difference, without running
the whole handoff from scratch.

Run it when the user says "catch up <product>", "carry the Storybook
changes over", "what changed in Storybook since we shipped", or on
whatever cadence they set.

**Output:** a branch and pull request with the changes, and
`storybook-to-product/catch-up/YYYY-MM-DD.md` from `templates/catch-up.md`.

---

## 1. Find what changed

Read `storybook-to-product/links.json`. For every link, diff the story's
folder from `story_commit` to the design system's current commit:

```bash
git -C <design-system-repo> log --oneline <story_commit>..HEAD -- <story folder>
git -C <design-system-repo> diff <story_commit>..HEAD -- <story folder>
```

Sort every change into one of four piles:

| Pile | What it is | Where it goes |
|---|---|---|
| **Copy** | A fixture value or a hardcoded string changed | Phase 2's rules: provenance, default, ask |
| **Markup** | A region's structure, component, or props changed | Phase 3's translation |
| **Style** | A pattern's CSS changed | Phase 3's styles section |
| **System** | The story now uses a component, prop, or version the product doesn't have | Phase 1's dependency ledger, and the release gate question if anything is unreleased |

## 2. Check the product side too

Find the handoff commit (the product commit that last touched `links.json`,
per `reference/LINKS.md`) and diff every linked product file from there to
the product's current commit. Somebody may have edited production directly: fixed a
typo, swapped a price, added a link. **Those edits win by default.** A
catch-up that overwrote a live fix with an older Storybook value would
quietly undo real work, so any field changed on both sides is a conflict,
shown side by side, and a person decides.

## 3. Carry it

Run the piles through the phases they belong to, at the size they
actually are: a copy-only catch-up is phase 2's ledger for the changed
fields, a find-and-replace, and phase 5's leak search and a side by side of
the affected pages. Don't re-run a full assessment for a changed headline.

Anything in the **System** pile, or any markup change that touches a
behavior hook, pulls in the full phase 4 and phase 5 checks for that
region.

## 4. Close

Move `story_commit` in `links.json` forward for every story that was
carried, in the same pull request as the changes, open it, and read the
counts back:

> Since the 2026-10-01 handoff: 7 story commits. 5 copy changes (4
> carried, 1 conflict with a production edit, kept the production copy), 1
> markup change (testimonial strip gained a heading), 0 style, 0 system.
> PR open, and it moves `links.json` to `9a1c77e0`.
