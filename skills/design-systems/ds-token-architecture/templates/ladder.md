# Ladder Proposal — <System Name>

_Establish mode · Written: <date> · From: `PROFILE.md`, `extraction/` (E1), `consolidation.md` (E2)_
_Architecture reference: `reference/SUBATOMIC-ARCHITECTURE.md`_

This is a proposal, not a token set. Every row below is a decision the team
makes; the agent's job was to lay the decisions out with evidence so they can
be made in an afternoon instead of a quarter.

## What the extraction found

- Sources scanned: <paths, file counts>
- Raw values found: <n> colors · <n> font sizes · <n> font families · <n>
  spacing values · <n> radii · <n> shadows · <n> durations
- After consolidation (E2): <n> colors · <n> sizes · … (<n> merges approved,
  <n> declined, <n> pending)

## Tier 1: definitions

<One table per category. Tier 1 names can be loose; they only exist to be
mapped. Provenance is the column that matters most: it's what lets the
hardcoded values be replaced mechanically later.>

### Color

| Proposed token | Value | Came from (files, count) | Merged from |
|---|---|---|---|
| `color-neutral-100` | `#f4f4f4` | 31 uses across 9 files | `#f4f4f4`, `#f5f5f5`, `#f3f3f4` |

### Typography · Spacing · Border · Shadow · Animation

<Same shape.>

### Core vs theme

<Which tier 1 values are universal (neutrals, utility, the type scale, the
grid) and belong in `core/`, and which are this brand's and belong in the
theme directory. Say why for anything non-obvious.>

## Tier 2: usage

<The jobs. Every tier 2 token aliases a tier 1 token by name. This is the
API, so the names follow the algorithm strictly. Include the knockout (or
`on-`) pair for every filled surface, and the contrast ratio of that pair.>

### Color

| Proposed token | Aliases | Job | Pair | Contrast |
|---|---|---|---|---|
| `color-background-brand` | `{color.brand.500}` | Primary filled surfaces | `color-content-brand-knockout` | 7.2:1 |

### Typography

| Composite | Ingredients (tier 1) | Job |
|---|---|---|
| `typography-body-md` | `font-family-primary`, `font-size-16`, `line-height-normal`, `font-weight-regular` | Default body copy |

### Spacing · Border · Shadow · Animation

<Only where a tier 2 intention earns its keep. Spacing tier 2 is optional;
say so if you skipped it.>

## Tier 3: components

<Sparingly. One row per token, each with the reason it can't be a tier 2
reference. If this section is empty, that's a fine result.>

| Proposed token | Aliases | Why tier 3 |
|---|---|---|

## Decisions the team still owns

<Numbered. Each one is a question with the options and the trade-off in a
sentence. These are the things the agent could not decide from the
codebase.>

1. <e.g. "Two brand blues survived consolidation (`#1a5fb4` on 40 uses,
   `#1b60b5` on 12). Same color with drift, or a deliberate secondary? Merging
   changes 12 pixels' worth of UI.">

## Next

- Wire and prove: `establish/ESTABLISH.md` E6
- Then run the nine checks against what you built:
  `reports/<date>-report.md`
- Then hand the hardcoded-value replacement to `ds-adoption-plan`, which
  schedules it wave by wave.
