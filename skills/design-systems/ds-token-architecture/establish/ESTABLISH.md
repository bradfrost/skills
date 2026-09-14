# Establish: from a production codebase to a tier ladder

For the team that has a product but no tokens. The values are all there,
sitting in stylesheets and Tailwind configs and inline styles; what's missing
is the structure. This procedure gets from "every color in production" to a
tier ladder the nine checks can grade, without letting a scanner make the
design decisions.

The course teaches the same move at a smaller scale: the MVP lesson starts
from hardcoded hex values and abstracts them tier by tier (2.2), and the
AI-assisted version runs a site through CSS Stats, groups the results, and
scaffolds the theme (8.31). This is that procedure, with the judgment steps
made explicit.

## Ground rules for this mode

1. **Extraction preserves the mess.** Pull every color out of production and
   you get fourteen grays as fourteen tokens. The consolidation step (E2) is
   where the design work happens, and a scanner cannot do it. Neither can
   you, alone: the merges are the team's decisions, and every one of them
   changes pixels.
2. **Tiers before names.** Decide what's tier 1, what's core, and what jobs
   tier 2 needs to do *before* naming anything. A name assigned by value
   (`gray-437`, `blue-1a5fb4`) breaks the moment a second theme shows up.
3. **Production values record what someone meant, not what the spec says.**
   `#f4f4f4` and `#f5f5f5` are probably the same intent. `#1a5fb4` and
   `#0d47a1` might be two intents. Compare screenshots before and after every
   merge that isn't obviously safe.
4. **Keep provenance for every value.** Which files, how many uses, what it
   was merged from. That record is what makes replacing the hardcoded
   values mechanical later (`ds-adoption-plan` consumes it), and it's the
   only way to answer "why is this token this color?" in six months.
5. **Code-first still leaves Figma behind.** Tokens that only exist in code
   turn the design file into a second, drifting source. The ladder isn't
   established until the design side has the same variables; E6 covers the
   import.

## E1. Extract

Get every raw value out of the product, with provenance.

**Best tool: a real extractor.** If [Figma Console MCP](https://docs.figma-console-mcp.southleft.com/)
is available in local mode, its `figma_ds_analyze` and
`figma_ds_extract_tokens` tools do this deliberately: framework detection, a
usage-ranked inventory, and DTCG tokens with per-token source tracking for
CSS custom properties, SCSS variables, Tailwind values, and shadcn HSL. Use
them and skip to E2. It's important to know what they don't do: their docs
say consolidation is a human decision, and they don't document naming rules.
That's E2 through E4.

**Fallback: scan it yourself.** Read the authored source, not the build
output (compiled CSS double-counts and vendored libraries masquerade as
product code). Walk the stylesheets, config files, and inline styles for:

- Colors (hex, rgb/rgba, hsl, named)
- Font families, sizes, weights, line heights, letter spacing
- Spacing values in padding, margin, gap
- Radii, border widths
- Box shadows
- Transition durations and easings
- Breakpoints in media queries
- Z-index values

For each value record: the value, every file it appears in, the count, and
the CSS property it was used on (a `#fff` used as `color` and a `#fff` used
as `background` are two different jobs; that's E4's input). Write it to
`ds-token-architecture/extraction/<category>.json`.

**From a Figma file instead of (or as well as) code.** The same extraction
works on a design file that has styles but no variables, or local fills
everywhere. With the Console bridge, `figma_execute` can walk every fill,
stroke, text style, and effect in the file and count them; with the native
bridge you're reading the frames the user links you to, so say so. Record
provenance as node ids and frame names instead of files and lines, and the
property the value was applied to (fill, stroke, text) the way you'd record
the CSS property. If both a codebase and a Figma file exist, extract both
and keep them as separate columns through E2; a value that appears on only
one side is its own finding before it's a token.

Report the raw counts before doing anything else. "214 distinct colors, 38
font sizes, 61 spacing values" is the sentence that gets a team to fund the
next step.

## E2. Consolidate

Group near-duplicates and propose merges. Decide nothing.

- **Cluster by perceptual distance for color** (ΔE under roughly 3 is
  usually the same intent; between 3 and 8 needs a human; above that,
  leave them apart). Cluster by rounding for sizes (`15px`, `16px`, `1rem`
  are probably one value; `14px` and `18px` probably aren't).
- **Rank each cluster by total usage** so the survivor is the value the
  product actually wears, not the first one found.
- **Flag the ambiguous ones** with the evidence: the values, the usage
  split, and a screenshot pair if you can render. Two blues with a 40/12
  usage split is a question, not a merge.
- Write `consolidation.md`: every proposed merge with survivor, absorbed
  values, and usage counts, and a decision column the team fills in.

Then stop and get the decisions. Don't proceed with defaults; a default merge
is a design decision made by a script.

## E3. Tier 1 and core

From the approved survivors, mint tier 1. Names can be loose here (the
course is explicit: tier 1 exists to be mapped, 2.17, 3.45). Ramps by
lightness (`neutral-100` … `neutral-900`), type sizes by scale step,
spacing by the grid.

Split core from theme now, even with one theme. Neutrals, utility colors,
the type scale, the spacing grid, animation, and z-index are core; the
brand's colors and font faces are the theme (4.76). It costs nothing today
and it's the step everyone regrets skipping when the second theme arrives.

If the grid the product actually uses isn't 4pt or 8pt, say so. Snapping
sixty spacing values to an 8pt grid is a redesign, and the team should
choose it knowing that.

## E4. Tier 2

Assign jobs. This is the design work, and the naming algorithm in
`reference/SUBATOMIC-ARCHITECTURE.md` is the tool.

For color, start from the CSS property each value was used on (E1 recorded
it): values used on `background` become candidates for `color-background-*`,
values on `color` become `color-content-*`, values on `border-color` become
`color-border-*`. Then the intention: which one is `default`, which is
`brand`, which are `utility` (they're usually the reds, greens, and ambers),
which is `disabled`.

Pair every filled surface with its content color and compute the contrast
ratio right there in the table. A `background-brand` with no knockout pair
is the most common gap in an established-from-code system, because in the
old CSS the white text was just `#fff` on the button.

For typography, find the composites: which font-size, line-height, weight,
and family actually occur *together* in the source. Those clusters are your
`display` / `headline` / `title` / `body` / `label` / `meta` candidates.
Name by intention, size by T-shirt.

Spacing tier 2 is optional. Only mint intentions the product demonstrably
has (a section gap that recurs, a stack rhythm). Border, shadow, and
animation get tier 2 names by size or effect.

Write the proposal to `templates/ladder.md` → `ladder.md`. Every decision
the codebase couldn't settle goes in "Decisions the team still owns."

## E5. Tier 3

Sparingly. Read the sanctioned uses in the reference. The extraction will
tempt you: a button with six colors looks like six tier 3 tokens. Ask
whether each one is a tier 2 reference in disguise (`button-color-background`
→ `color-background-brand`). Mint tier 3 only where a component's mapping
genuinely differs from the semantic one, or where a category of components
shares a decision (input borders).

An empty tier 3 at establish time is a good result.

## E6. Wire and prove

1. **Build.** Put the JSON through Style Dictionary or the team's equivalent
   with the prefix and tier-identifier transforms (4.14, 4.15). Output CSS
   custom properties at minimum.
2. **Replace, mechanically.** Using the provenance from E1, replace the
   hardcoded values in the consumers with the tokens. This is exactly the
   work `ds-adoption-plan` schedules; hand it off there for anything bigger
   than a pilot component, and do one component here to prove the ladder.
3. **Prove no pixels moved that weren't supposed to.** Screenshot the pilot
   before and after. Every diff is either an approved merge from E2 or a
   bug.
4. **Import to Figma.** Console MCP's `figma_import_tokens` closes the loop;
   otherwise a Tokens Studio or Design Tokens Manager import (4.86, 4.87).
   Until this is done, the design file is a second source.
5. **Run the nine checks** against what you built. Establish mode ends with
   an assessment, because a ladder you never checked is a claim.

## What you hand back

- `extraction/` with provenance
- `consolidation.md` with the team's decisions recorded
- `ladder.md`, the proposal, with open decisions listed
- One converted pilot component with a before/after
- A first `reports/<date>-report.md` from the nine checks
