# Phase 2 — Mapping

Every region from phase 1 gets exactly one disposition and, where it's being
built, a real component name read from the catalog. This is where the
conversion is actually decided. Phase 3 is typing.

**Output:** the mapping table in `autopsy.md`.

---

## Start at the top of the hierarchy

Work down, not up. In order:

1. **Is there a page template?** Some systems ship whole-page starting
   points. If one fits, start there and pour the content in. This eliminates
   the entire class of bugs that comes from composing a page shell out of
   primitives.
2. **Is there a recipe or a published composition?** A site header, a
   product card, a footer. Use it rather than assembling the parts yourself.
3. **Is there a canonical composition in the docs?** Copy its skeleton
   exactly, including every wrapper.
4. **Compose from components.** Only now.
5. **Is it a gap?** Say so. Don't build it.

Most conversions go wrong at step 4 because nobody checked 1 through 3.

---

## The dispositions

Every region gets exactly one:

| Disposition | Meaning |
|---|---|
| **Swap** | A single component replaces it directly |
| **Compose** | Assemble from existing parts, following a canonical composition |
| **Template** | This region comes from a whole-page template the system publishes |
| **Delete** | Decorative, dead, or duplicated. Removing it is the right answer |
| **Gap** | The system doesn't cover it. Name it, propose it, placeholder it |
| **Keep** | Intentionally outside the system: a third-party embed, a legally required block, a piece of custom art direction the human asked to preserve |

**Delete and Keep both need a one-line reason.** A deletion nobody can
account for looks like an accident, and a Keep with no rationale is just
bespoke CSS wearing a badge.

---

## Verify before you write it down

For every component you name, read its catalog entry and confirm four
things. This is the step that gets skipped and it's the step that breaks
pages.

1. **The tag or import name**, in exact casing.
2. **The props you're going to set**, and their allowed values. `variant`
   and `appearance` are different axes in many systems and folding one into
   the other produces a value that silently does nothing.
3. **The slots or children**, exactly as declared. Most component libraries
   silently drop content projected into a slot name that doesn't exist. No
   error, no warning, just an empty region. Slot names are the single most
   common thing to remember wrong.
4. **Required wrappers.** Does this grid need an item element around each
   child? Does this section want its heading in a named slot rather than as
   a direct child? Check, every time.

Then check the **don'ts**. If the catalog's own guidance warns against the
component you picked, take the correction and record both: what you reached
for first and what the catalog said instead. That row is the most
interesting one in the autopsy and it's a genuine finding about how the
system teaches itself.

---

## The mapping table

| # | Region | Disposition | Target | Props / slots | Evidence |
|---|---|---|---|---|---|
| 1 | Sticky top bar | Compose | `ds-header` > `ds-nav` | default slot; nav takes `ds-nav-item` children | `[verified]` |
| 2 | Gradient band | Swap | `ds-hero` | `variant="feature"`; slots: `default`, `actions` | `[verified]` |
| 3 | Icon card row | Compose | `ds-grid` > `ds-grid-item` > `ds-card` | grid `cols="3"`; **item wrapper required** | `[verified]` |
| 4 | Gradient blob divider | Delete | — | Decorative only | — |
| 5 | Pricing toggle | Gap | — | No toggle-group in the system. Filing proposed | — |

Carry the evidence tag on every row. A table that's mostly `[reported]`
isn't a failure, it's a conversion built on a memory of the system rather
than a reading of it, and the receipt will say so at the top.

---

## Tokens

Same job at the value level. Map the page's hardcoded values to real tokens,
and do it once here rather than improvising during phase 3.

| Original | Nearest token | Note |
|---|---|---|
| `#6366f1` | `--ds-color-action-primary` | |
| `#1e293b` | `--ds-color-content-default` | |
| `80px` section padding | `--ds-space-region` | |
| `12px` radius | `--ds-radius-md` | |
| `#a855f7` gradient stop | — | No equivalent. Region uses a surface variant instead |

Use the semantic tier when the system has tiers. Reaching into primitives to
get an exact color match is how a converted page ends up just as unthemeable
as the original, which defeats the entire point.

**When there's no near match, don't force one.** Take the system's closest
sensible value and note the shift. A page that's 4% off the original's
purple and fully themeable is the win. A page that matches the purple
exactly by hardcoding it is not.

---

## Gaps are findings

When the system genuinely lacks something:

- Name it precisely: what the page needs, what the closest existing
  component is, and why it doesn't cover the case.
- Propose it upstream. Draft the issue. **File it only if the human says
  to.** Filing is their call.
- Decide what phase 3 does in the meantime: use the nearest component and
  accept the difference, or leave a clearly marked placeholder. Never
  hand-roll a replacement component quietly. A gap that gets silently filled
  with bespoke CSS is the exact thing this skill exists to stop, and it will
  be invisible to everyone in six months.

Gaps go in the receipt with the rest, because a conversion that surfaces
three real holes in the design system did something valuable beyond
converting a page.

---

## Close the phase

> Mapping done: 9 regions. 5 swap, 2 compose, 1 delete, 1 gap. 11 components,
> 10 verified against the catalog, 1 reported. 47 hardcoded values map to 12
> tokens; 2 have no equivalent. Writing the page next.
