---
check: 7
name: Themes, core, and modes
question: Would a second theme (or dark mode, or a sub-brand) be a remap, or a rewrite?
---

# Check 7 — Themes, core, and modes

A theme is the three tiers operating as a group (2.4). The test of the
architecture is what happens when there are two of them. The course's model:
a new theme is a clone plus a remap (4.78); universal decisions live once in
core (4.76); a vanilla theme proves the structure with the brand stripped
out (4.74); dark mode is a child that overrides its parent at tier 2 and 3
and touches only color and shadow (8.02); sub-brands stay cosmetic (8.06).
This check runs even for a single-theme system, because the answer to
"could you add one?" is the answer to "is this tiered?"

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Theme list and structure | Repo: theme directories, a themes registry, build config | Figma modes on the tier 2 / tier 3 collections |
| What differs between two themes | `diff` the theme directories | Interview |
| Core / shared tokens | `core/` or equivalent | Interview |
| Dark theme structure | The dark theme's files: does it hold only what changes? | Interview |
| Switching mechanism | CSS: `:root` vs `.theme-x` selectors; Figma: mode on a frame | Interview |

## Procedure

1. **Count the themes** and name what each is for (brand, sub-brand, dark
   mode, client, internal vanilla).
2. **Diff two themes.** What actually differs? In the architecture it's tier
   1 brand values and the tier 2/3 aliases that point at them. If tier 2
   *structure* differs (a token exists in one theme and not the other), the
   themes have drifted and components will break when switched. List the
   tokens present in one theme and absent in another.
3. **Check for core.** Neutrals, utility colors, transparents, data-viz
   colors, the type scale, the spacing grid, animation, z-index: are they
   defined once or per theme (4.76)? With one theme, note whether the split
   exists. With two or more and no core, that's a finding.
4. **Check the dark theme, if any.** The architecture's dark mode is a
   *variant*: it holds only the color and shadow tokens that change, and
   inherits everything else from its parent (8.02). A dark theme that is a
   full copy of the light theme will drift (typography tokens added to
   light and not dark is the classic symptom). Count the non-color tokens
   the dark theme declares; the right number is zero or close to it.
5. **Check dark-theme direction.** Ramps reverse on dark: brand and link
   colors step lighter, hover brightens rather than darkens, `subtle` and
   `surface` step up from the page instead of down. A dark theme built by
   copying light values and swapping black for white usually gets one of
   these backwards (check 4 computes the contrast; here you check the
   direction).
6. **Check sub-brands.** Cosmetic changes (color, font face, radius) are
   what a sub-brand should touch; structural changes (font sizes, spacing)
   are a different product, not a sub-brand (8.06).
7. **Check for vanilla.** An internal brandless theme is the architecture's
   x-ray (4.74, 7.14). Its absence isn't a red, but its presence is strong
   evidence the tiers are real.
8. **Check the switching mechanism.** Code: one class on `<html>` swaps the
   custom properties (4.81). Figma: one mode change on a frame swaps the
   theme (4.80). Anything that requires touching components to switch
   themes is a finding.

## Warning lights

- Themes with different tier 2 structures (drift)
- Universals duplicated per theme
- Dark mode as a full copy, declaring non-color tokens
- Dark hover moving the wrong direction
- Sub-brands changing structure
- Switching that requires component edits
- Single theme with no core split and no way to add a second

## Lights

- **Red:** themes have drifted structurally, or a second theme would be a
  rewrite.
- **Yellow:** themes hold together but core is missing, the dark theme is a
  full copy, or a few tokens exist in some themes only.
- **Green:** a second theme is a remap; core exists; dark mode is a variant
  holding only what changes; switching is one class or one mode.

## Fixing it

- Drift → diff the theme key sets in CI so a token added to one theme has
  to be added to all (or inherited).
- No core → create it now, before the next theme.
- Dark mode as a copy → convert it to a variant: delete every non-color
  token it declares and load it on top of its parent. Then gate it: a
  variant declares no non-color token.
- Wrong direction → write the rules down (lighter on dark, hover increases
  separation from the page) and derive the values from them.

## Record

```markdown
### Check 7 — Themes, core, and modes: <RED|YELLOW|GREEN> (or N/I)
- Themes: <n> (<names and purposes>) · vanilla: <yes / no>
- Structural drift between themes: <n tokens present in some themes only>
- Core: <present, n tokens / absent> · universals duplicated: <yes / no>
- Dark theme: <variant / full copy / none> · non-color tokens it declares: <n>
- Dark direction: <holds / brand steps down / hover darkens>
- Switching: <one class / one mode / requires component edits>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- First move: <…>
```
