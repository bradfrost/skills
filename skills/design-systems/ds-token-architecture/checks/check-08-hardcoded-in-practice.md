---
check: 8
name: Tokenized in theory, hardcoded in practice
question: What's tokenized on paper but hardcoded where the pixels get painted?
---

# Check 8 — Tokenized in theory, hardcoded in practice

A token set is only as tiered as its consumers. This check leaves the token
files and reads the components and products that are supposed to use them,
looking for raw values where tokens exist, tier 1 leaking into components,
and tokens that nothing consumes. It's the check most likely to come back
`N/I` in plain chat, because it needs the consuming code; say so rather than
guessing.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Component stylesheets | Repo: the component library's source CSS/SCSS | Pasted files for 5 to 10 components |
| One product's stylesheets | Repo: a consuming app | Pasted files · interview |
| Which tokens are consumed | Grep the consumers for token names | Interview |
| Figma components | Bridge: detached instances, local styles, hardcoded fills | Screenshot · interview |

## Procedure

1. **Scan for raw values.** In the consumer source (not the token build
   output, not vendored libraries), find every hex, rgb, hsl, px font size,
   px spacing, px radius, and literal box shadow. Record file, line, value,
   and the token that should have been used if one exists. Sample if the
   codebase is large, and say exactly what you sampled.
2. **Separate the legitimate from the drift.** `1px` borders, `0`,
   `transparent`, `100%`, and values inside `var()` fallbacks are usually
   fine. A hex color is never fine. A px font size where a composite exists
   is drift. A `#fff` on a brand button is a missing pair (check 4).
3. **Find tier 1 in components.** Components should consume tier 2 (or tier
   3). A component reading `--ds-color-neutral-600` directly bypasses the
   theme. Count them.
4. **Find the orphans.** Tokens defined that no consumer references. Some
   are fine (tier 1 exists to be referenced by tier 2, not by components).
   Tier 2 or tier 3 tokens with zero consumers are either aspirational or
   dead; either way they cost maintenance.
5. **Find the ghosts.** Token names referenced in consumers that no theme
   defines (a `--ds-theme-color-content-muted` that someone reached for and
   nobody minted). These fail silently: the property gets no value and the
   browser falls back. A build-time check for bare `var()` references
   catches them.
6. **Check the design side, if reachable.** Detached instances, local
   styles, and hardcoded fills in Figma components are the same finding on
   the other side. Whole-file counts need a Console bridge; with the native
   bridge, scope the claim to the frames you were handed
   (`reference/FIGMA-ACCESS.md`).
7. **Check what the build ships.** If the built CSS resolves references to
   literals, consumers can't tell tier 2 from a literal anyway. Note
   whether the shipped artifact preserves references (`var()` chains) or
   flattens them.

## Warning lights

- Raw colors in components where tier 2 tokens exist
- Font sizes and spacing hardcoded where composites and a grid exist
- Components consuming tier 1
- Tier 2 / tier 3 tokens with no consumers
- References to tokens no theme defines
- Detached instances and local fills on the design side
- No automated check for any of the above

## Lights

- **Red:** tokens exist and most components ignore them, or ghost
  references are live in production.
- **Yellow:** most components use tokens, with a measurable minority of
  raw values, some tier 1 leakage, or a handful of orphans.
- **Green:** components consume tier 2/3, raw values are the documented
  exceptions, orphans and ghosts are zero, and a check enforces it.

## Fixing it

- Raw values → replace mechanically, guided by the token that should have
  been there. This is the work `ds-adoption-plan` schedules wave by wave;
  hand it the list.
- Tier 1 leakage → re-point at the tier 2 token; if none fits, that's a
  tier 2 gap.
- Ghosts → a CI check that every bare `var(--prefix-*)` in consumer source
  is declared by at least one built theme.
- Orphans → delete, or find the component that should have used them.
- Wire a raw-value lint into the component library's build. This is the
  check that keeps the rest honest.

## Record

```markdown
### Check 8 — Tokenized in theory, hardcoded in practice: <RED|YELLOW|GREEN> (or N/I)
- Consumers read: <n components / n product files> (sampled: <scope>)
- Raw values: <n> in <n> files (colors <n> · sizes <n> · spacing <n> · shadows <n>)
- Tier 1 consumed directly: <n> places
- Orphan tier 2/3 tokens: <n> · ghost references: <n> (<examples>)
- Design side: <detached n / local fills n / not reachable>
- Enforced by: <lint / CI check / nothing>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- First move: <…>
```
