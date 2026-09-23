# Refresh — the drift check

The day after a backfill, the product changes, and the Storybook copy is
out of date. Nobody notices until they design against a screen that no
longer exists. This mode notices.

Run it when the user says "check for drift", "is Storybook still current
for <product>", "refresh <product>", or on whatever cadence they set.

**Output:** `product-to-storybook/<product>/drift/YYYY-MM-DD.md`. Nothing
else changes. Not a story, not a fixture, not `INVENTORY.md`.

---

## What it does

1. **Re-read the product** the same way the original run did (`GARAGE.md`
   says whether it was a repo, a URL, or both). Same intake answers, no
   questions asked.
2. **Rebuild the inventory in memory** per phase 1, without the checkpoint.
3. **Re-capture the fixture sources** per phase 2: fetch each
   `_meta.source_url` again and compare to the frozen fixture.
4. **Diff** against what's in Storybook, and write the report.

## The four sections

Every drift report has exactly these, in this order, each ending with the
choice the user has to make.

### Templates added or removed

Templates in the fresh inventory that have no story, and stories whose
template is gone from the product.

> The product has templates that Storybook doesn't (or the other way
> around). What should happen?
>
> - Update Storybook to match the product
> - Leave Storybook as it is for now
> - File an issue to deal with it later

### Permutations changed

For each existing permutation: the source page changed (content diff
against the fixture), the source page is gone (404), or a new branch
appeared in the template that no story covers.

> The content behind these screens has changed since it was captured. What
> should happen?
>
> - Re-capture the content so the screen matches the product again
> - Keep the captured content as it is
> - File an issue to deal with it later

### Pinned version bumped

`package.json` now pins a different design system version than
`GARAGE.md` recorded. List what moved, and re-check every `version-drift`
row in `GAPS.md`: some will have closed (the product caught up), some will
be new.

> The product moved to a newer version of the design system. What should
> happen?
>
> - Record the new version and update the version-drift ledger
> - Leave it as it is for now

### New UI that isn't from the system

Regions in the fresh render that carry no system component and match no
existing `data-p2s-name`. Each one is a candidate `GAPS.md` row.

> The product has new custom components that aren't from the design
> system. What should happen?
>
> - Add them to the gap ledger
> - Add them to the gap ledger and file issues
> - Leave them out for now

---

## Why it never overwrites

A story that differs from the live product might be *ahead* of it: someone
redesigned that screen in Storybook on purpose and the product hasn't
caught up yet. That's the whole workflow working. A refresh that
overwrote it would destroy the design work to match the old product. So it
reports, and a person decides, every time.

When the user answers "update," do the update as a normal phase 2 or phase
3 step, record it in the drift report, and leave the rest alone.

---

## Close

Read the four counts back:

> Drift since 2026-09-22: 0 templates changed, 2 permutations changed (both
> source pages edited), version pin moved 0.59.0 → 0.62.0 (1 drift entry
> closed, 0 new), 1 new region not from the system (a cookie banner).
> Report at `product-to-storybook/bradfrost-com/drift/2026-10-15.md`.

Then wait for the answers.
