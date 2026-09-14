# The Subatomic token architecture

What this skill checks a token set against. This is the architecture Ian and I
teach in [Subatomic: The Complete Guide To Design Tokens](https://designtokenscourse.com/),
condensed to the rules that can actually be checked. Lesson numbers point at
the course so you can go deeper; you don't need the course to use the skill.

Two things to know before you check anything against this:

1. **The words are a guide, not gospel.** The course says so itself: "pick the
   right algorithm that works for you" (3.39, 3.43). A system that calls tier
   2 "semantic" instead of "theme," or uses `on-brand` where we'd say
   `knockout`, is following the architecture. A system where nobody can say
   which tier a token lives in is not. Check the structure, not the vocabulary.
2. **Tier 2 and tier 3 are the API.** Tier 1 names "can be loose"; tier 2 and
   3 "need to be strictly defined" because they're what every component and
   every product consumes (3.45). Spend your scrutiny where the contract is.

## The three tiers

| Tier | Also called | Holds | References |
|---|---|---|---|
| **Tier 1: definitions** | primitives, core, global | Every raw ingredient: `red-100` through `red-900` with hex values, the type scale, the spacing grid, durations, easings | Nothing. Tier 1 is where raw values live and the only place they should. |
| **Tier 2: usage** | semantic, alias, theme | Jobs for those ingredients: `color-background-brand`, `typography-body-md`, `spacing-section` | Tier 1, always by alias, never by raw value |
| **Tier 3: components** | component, override | Component-specific decisions: `button-color-background-primary`, `focus-ring-color` | Tier 2 by preference; tier 1 is allowed ("doesn't hurt anything, we've seen it both ways," 2.3) |

Taught in 2.2 (the MVP walk-through), 2.3, 2.4, and 2.10.

The heavy lifting happens in tier 2: "you wanna be able to do most of your
heavy lifting by mapping your tier one variables to your tier two tokens"
(2.3). Components are wired to tier 2 by default. A component reaching past
tier 2 into tier 1 for a color is a smell; a product reaching into tier 1 is
a finding.

**A theme is the three tiers operating as a group**: "a collection of tokens
that define a specific visual language" (2.4). The architecture makes sense
even for a single-brand system, because a redesign is a second theme waiting
to happen.

## Tier 3 discipline

The course is blunt here: use tier 3 "really sparingly," and "when you find
yourself adding tier three tokens, you should feel bad" (2.3). The cautionary
tale is a client with 4,000 tokens from minting one per property per variant
per component.

Sanctioned uses (2.3, 6.27):

- Heavily variable components (buttons)
- Component *categories* (one input border token shared by text input,
  textarea, and select)
- Special cases: focus ring, a highlighted data-table row, charts
- Components whose mapping legitimately changes per theme (links: brand color
  in one theme, interactive blue in another)

Tier 3 disabled states can fall back to tier 2 `content-disabled` instead of
minting new tokens (6.27). Tier 3 typography is rare and mostly for nudging a
size or setting a line height to 1 (2.19, 3.52). Tier 3 animation: "we've
never done this in production" (3.57).

## The naming algorithm

Every name is assembled in the same order (3.43 through 3.49):

```
[global prefix] - [tier identifier] - [category] - [category-specific segments]
     ds             theme               color        background-brand-hover
```

- **Global prefix** (`ds`, `sub`, your system's initials): code only, not
  needed in Figma (3.44, 3.32).
- **Tier identifier** (`theme`, `semantic`, optionally `component` for
  tier 3): tier 2 and 3 only, code only (3.45). Tier 1 carries no tier
  identifier, which is itself the signal that it's raw material.
- **Category**: `color`, `typography`, `spacing`, `border`, `box-shadow`,
  `animation`, `breakpoint`, `z-index` (3.46).

Then the category decides the rest.

### Color, tier 2 (3.48, 2.10, 6.19 through 6.26)

```
color - [property] - [intention] - [variant] - [state]
```

- **Property** (what it paints): `background`, `content`, `border`. Content
  covers text and icons together; split into `text`/`icon` "only if you need
  to" (2.10).
- **Intention** (why): `default`, `brand`, `accent`, `disabled`, `utility`,
  `dataviz`, `transparent`. `disabled` sits at the intention level on purpose,
  "to prevent a bunch of duplicative color definitions" (3.48, 6.23).
- **Variant** (which flavor of that intention): `subtle` / `strong` /
  `extra-strong` as dial-down and dial-up (6.26); `error` / `success` /
  `warning` / `info` under utility (6.24); `knockout` (or `inverted`) for the
  paired color that sits on top of a filled surface (6.25); `primary` /
  `secondary` / `tertiary`; `accent-1` / `accent-2` as interchangeable
  siblings (6.22).
- **State**: `hover`, `focus`, `active`, `pressed`.

`default` is the baseline everywhere: page background, body text, hairline
border (6.20). Figma can't express an unnamed default, so `default` is spelled
out in both places rather than implied in one (3.36).

**Knockout pairs.** A filled surface needs a content color that reads on it:
`background-brand` pairs with `content-brand-knockout`; `background-knockout`
pairs with `content-knockout`. Other systems name the same idea `on-brand`,
`on-default`, `on-dark`: "accomplishing the same thing, different language"
(6.25). Whichever word you use, every filled surface needs its pair, and the
pair has to pass contrast.

### Color, tier 3 (3.49)

```
[component or category] - [variant] - color - [property] - [state]
button - primary - color - background - hover
```

Component first, so a component's tokens sort together.

### Typography (2.16 through 2.19, 3.50 through 3.53)

Typography is a composite token (the W3C community group definition, 2.16).
Tier 1 enumerates the ingredients: `font-family`, `font-size`, `font-weight`,
`font-style`, `line-height`, `text-transform`, `letter-spacing`. Tier 1 names
can be descriptive ("Helvetica 64") because they exist only to be mapped
(2.17). Tier 1 typography "should not be published to consumers" (3.50).

Tier 2:

```
typography - [intention] - [size] - [screen?] - [property]
typography - body - md - font-size
```

Intentions: `display`, `headline`, `title`, `body`, `label`, `meta` (the
eyebrow/overline register). Sizes are T-shirt and abbreviated (`lg`, not
`large`). The optional screen segment (`mobile`, `tablet`, `desktop`) applies
only where a size actually changes per viewport, and the whole thing rolls up
into one composite (`typography-body-sm`) consumed as a Figma text style or a
Sass mixin (2.18, 3.51, 4.42, 4.55).

### Spacing (2.20 through 2.22, 3.54)

Tier 1 is the 4pt or 8pt grid as integers: `spacing-0`, `spacing-4`,
`spacing-8`... Unlike color and typography, "tier one spacing units can be
used directly" (3.54). Tier 2 spacing is optional and named by intention
(`spacing-section`, `spacing-stack`); tier 3 is `button-padding-x`-shaped.

### Border, shadow, animation (2.23 through 2.25, 3.55 through 3.57)

- **Border**: tier 1 holds radius, width, and (rarely) style values; tier 2 is
  `border-radius-lg`-shaped with T-shirt sizes.
- **Shadow**: a composite (color, x, y, blur, spread), described at tier 2
  in practice: `box-shadow-md`.
- **Animation**: a composite of duration and easing; tier 1 lists the
  durations and eases, tier 2 names the effects (`animation-fade-quick`).

### Breakpoints and z-index (3.58, 3.59)

`breakpoint-sm/md/lg`. Device names (`mobile`, `tablet`) are allowed
"although we don't recommend them." Z-index is "questionable whether or not
to even include," and if included, `z-index-100` through `900`.

## Themes, core, vanilla, modes

- **A second theme is a clone plus a remap** (4.78): a new tier 1 palette,
  tier 2 and 3 re-pointed, everything else inherited.
- **Core tokens** are the fourth collection (4.76, 4.77, 4.79): the universal
  decisions shared across every theme. Neutrals, utility colors,
  transparents, data-viz colors, the type scale, the spacing grid, animation,
  z-index. Create core "as soon as you start making a second theme," because
  that's the moment duplication starts.
- **The vanilla theme** is a brandless internal theme that acts as "x-ray
  vision for your token system" (4.74, 7.14). Its job is to prove the
  architecture works with the brand stripped out.
- **Dark mode** is a child theme that overrides its parent at tier 2 and tier
  3 and "generally only touches color as well as box shadow values" (8.02).
  It loads on top of the parent, it doesn't fork it.
- **Sub-brands** follow the same override pattern and stay cosmetic: color,
  font face, radius. Not structural: font size, spacing (8.06).
- **Switching**: in Figma, themes are modes on the tier 2 and tier 3
  collections, applied to a page frame (4.80). In code, a class on `<html>`
  swaps the custom properties (4.81, 8.03).

## The build and what gets published

- Source of truth is JSON, built by Style Dictionary or an equivalent into
  per-platform outputs (4.05). Aliases use dot notation: `{color.brand.pink}`
  (2.3, 4.13). JSON nesting mirrors the Figma slash groups (4.09).
- Folders mirror tiers: `tier-1-definitions/`, `tier-2-usage/`,
  `tier-3-components/`, one directory per theme, plus `core/` (4.11, 4.13,
  4.78, 4.79). The tier identifier is added by a build transform keyed on the
  directory, not typed by hand (4.15).
- **Should you publish tier 1?** The course leans no (5.06): consumers who can
  reach raw palette values will build contrast failures and bypass the
  theme. Hide tier 1 from Figma scopes and from publishing (4.26, 5.10).
- Scope Figma variables once the categories settle: `color/content` to text
  and shape fills, `color/background` to frame and shape fills,
  `color/border` to strokes (4.26).

## Governance

- Semantic versioning (7.15): additive tokens are minor, renames are major,
  `0.x` means emerging and `1.0` means stable. Keep a changelog (7.19).
- Fix bad names and brittle structure while only one product is consuming
  (7.19). Every extra consumer makes a rename more expensive.
- The governance workflow (7.26): a product team hits a snag and talks to the
  token czars, who classify it as education, a bug, a new or modified token,
  or a visual discrepancy. Bugs (wrong mapping, design/code drift, contrast,
  inconsistent names, missing docs) are "a five alarm fire." New tokens get
  asked whether they belong in the core system at all before anything is
  minted.

## What the course does not cover (and this skill therefore reports, not grades)

- A formal deprecation mechanism for tokens beyond a semver major
- Layout and grid tokens (container widths, columns, gutters)
- Sizing tokens as a category (icon sizes, control heights)
- An opacity scale or a naming scheme for transparent colors
- Structured data-viz palettes (categorical, sequential, diverging)
- A DTCG `$value` / `$type` file format walkthrough

When a check touches one of these, the finding says "no guidance in the
architecture" and describes what the system does, instead of pretending the
architecture has an opinion it doesn't.
