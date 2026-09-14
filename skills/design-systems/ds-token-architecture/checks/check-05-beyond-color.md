---
check: 5
name: Beyond color
question: Is the ladder built for every category, or is it color-only with everything else hardcoded?
---

# Check 5 — Beyond color

Most systems tokenize color first and stop. The architecture covers
typography (2.11 through 2.19), spacing (2.20 through 2.22), border, shadow,
and animation (2.23 through 2.25), plus breakpoints and z-index (3.58,
3.59). Each has its own shape; this check walks them one at a time and asks
whether the tiers exist for each, not just whether a few values do.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Tier 1 and tier 2 files per category | Repo or pasted JSON | Figma collections (`typography/`, `spacing/`, and so on) |
| How typography is consumed | Sass mixins, CSS classes, Figma text styles | Interview |
| Spacing usage in components | Component source | Interview |
| SCSS variables that never became tokens | `_variables.scss` and friends | Interview |

## Procedure

Per category, record: tier 1 present? tier 2 present? consumed by
components? Then:

1. **Typography.** Tier 1 should enumerate the ingredients: family, size,
   weight, style, line height, letter spacing, transform (2.17). Tier 2
   should be *composites* named by intention (`display`, `headline`,
   `title`, `body`, `label`, `meta`) and T-shirt size (2.18, 3.51). Check
   that a composite carries all of its properties (a `body-md` with only a
   font size is half a token). Check how it's consumed: a Sass mixin, a
   CSS class, or a Figma text style that maps to it (4.55). Responsive
   variants: the `-mobile` sibling pattern or a viewport mode (4.42, 4.44).
   Tier 1 typography should not be published to consumers (3.50).
2. **Spacing.** Tier 1 is the grid as integers (3.54). Confirm there is a
   grid (4pt or 8pt) and that the values on it are the values components
   use. Tier 2 spacing is optional; if it exists, it should be named by
   intention (section, stack, inline). A `size()` Sass function with no
   tokens behind it means spacing is not tokenized on the design side and
   can't be themed. Flag it.
3. **Border.** Tier 1 radius and width scales; tier 2 T-shirt names (3.55).
   A `round` / `full` / `pill` value for circular corners is normal.
4. **Shadow.** A composite (color, x, y, blur, spread) described at tier 2
   by size (3.56). Check whether the shadow color is a literal (`#00000040`)
   or a reference to a tier 2 color; literals won't follow a theme.
5. **Animation.** Tier 1 durations and easings; tier 2 named effects (3.57).
   Often the smallest category and often missing entirely; note it either
   way.
6. **Breakpoints and z-index.** Breakpoints as tokens (`breakpoint-sm/md/lg`)
   or as SCSS variables only. Z-index as a numeric ladder, optionally with a
   semantic layer on top (`layer-modal`). The course is ambivalent about
   z-index (3.59), so a missing ladder is a note, not a light.
7. **What's not in the architecture.** Opacity, icon sizes, control
   heights, container widths, grid columns. Record what the system has;
   don't grade it. Put it in the report's "no guidance" section.

## Warning lights

- Typography tokens that are ingredients only, with no composites
- Composites consumed nowhere (defined, but components set font-size by
  hand)
- No spacing grid, or spacing as a function with no tokens behind it
- Shadow colors as literals
- Whole categories absent while their values are hardcoded in components
- SCSS variables doing the job of tokens for a category, invisible to design

## Lights

- **Red:** color only. Everything else hardcoded or SCSS-only.
- **Yellow:** typography and spacing tokenized, one or more of border /
  shadow / animation missing or half-built, or composites defined but not
  consumed.
- **Green:** every category has its tiers, composites are consumed through a
  mixin or style, spacing is on a grid, shadows follow the theme.

## Fixing it

- Composites → build them from the ingredients you already have and give
  components one thing to consume (4.55).
- Spacing → mint the grid at tier 1 even if you skip tier 2. It's the step
  that makes density a theme concern instead of a rewrite.
- Shadow colors → reference a tier 2 background or border token so the
  shadow changes with the theme.
- SCSS-only categories → promote to tokens so the design side can see them;
  the SCSS can keep consuming them.

## Record

```markdown
### Check 5 — Beyond color: <RED|YELLOW|GREEN> (or N/I)
| Category | Tier 1 | Tier 2 | Consumed via | Note |
|---|---|---|---|---|
| Typography | <n / none> | <n composites / none> | <mixin / class / style / hand> | |
| Spacing | <grid: 4 / 8 / none> | <n / optional-skipped> | | |
| Border | | | | |
| Shadow | | | color: <ref / literal> | |
| Animation | | | | |
| Breakpoints | <tokens / SCSS only / none> | | | |
| Z-index | | | | |
- No guidance in the architecture: <opacity, sizing, layout: what exists>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- First move: <…>
```
