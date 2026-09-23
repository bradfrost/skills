# Report — <product name>

**<Headline with real numbers.>**
*Example: 5 templates and 11 stories are in Storybook under
`Products/bradfrost.com`. 14 regions render from the local system, 3 come
from the product (scoped), 0 placeholders, 2 version-drift entries, 3
issues filed.*

**Local system:** <x.y.z> · **Product pins:** <x.y.z> · **Source:** <repo / URL / both> · **Date:** <date>
**Stories:** `<path>` · **Ledger:** `./GAPS.md` · **Inventory:** `./INVENTORY.md`

> Note: these screens won't match the live product exactly because
> Storybook runs on the local design system (<x.y.z>) while the product runs
> on <x.y.z>. Each difference between renderings is labeled accordingly
> (version drift, relocation errors, omissions, etc).

---

## Scope check

| System story | Before | After | Identical |
|---|---|---|---|
| `Components/Header/Default` | `scope/header-before.png` | `scope/header-after.png` | yes |

<If any row says no: what leaked, what was fixed, re-run result.>

## What was proven, and what wasn't

| Check | Result |
|---|---|
| Renderer confirmed | <viewport and element count, or what failed> |
| Every story renders, no console errors | <11 of 11, or which failed> |
| Rendered widths | <e.g. 400 and 1280> |
| Visual regression suite | <ran clean / not available> |
| Human visual review | <who and what they found / **no human review**> |

---

## Side by side

### <Template> / <Permutation>

| Live (<width>) | Story (<width>) |
|---|---|
| `side-by-side/post-default-live-400.png` | `side-by-side/post-default-story-400.png` |

| Difference | Kind | Note |
|---|---|---|
| Card corners rounder | version drift | `GAPS.md` row 2 |
| Tag list wraps at 5 not 6 | relocation error, fixed | fixture had a trailing tag |
| Newsletter block missing | deliberate omission | question 4 option C |

<Repeat per permutation.>

---

## Issues filed

| Gap | Action | Link |
|---|---|---|
| Site header | filed | <url> |
| Newsletter signup | updated "seen in" to 3 | <url> |
