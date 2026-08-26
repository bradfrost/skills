---
phase: 1
name: Teardown
question: What UI-specific code does this product actually own — components, styles, JS, templates, routes — and how much of it is already on the system?
output: ds-adoption-plan/BASELINE.md
---

# Phase 1 — Teardown

Dump every UI-specific thing the product owns on the table, with file paths and counts. The teardown is the denominator for everything that follows: mapping rows, effort estimates, and the schedule all cite it. A teardown that misses a category (orphaned hooks, stored-content markup) silently shrinks the estimate — the classic underquote.

## Evidence to gather

| What | Best source | Fallbacks |
|---|---|---|
| Authored stylesheets | Repo: every CSS/SCSS file that isn't the design system's own | pasted CSS · interview |
| Markup patterns as used | Repo: templates/components — custom classes, custom elements, DS components in use | rendered HTML · screenshots |
| UI JavaScript | Repo: behavior scripts vs non-UI tooling | interview |
| Templates & routes | Repo: layouts, partials, page types, content volume per type | sitemap · interview |
| Already-adopted surface | Repo: DS package versions, DS component usage counts, tokens/fonts wiring | package.json paste |
| Deterministic scan | The system's analyzer tool, if any (per GARAGE.md, with its blind spots noted) | skip |

## Teardown procedure

1. **Foundation first.** Establish what's *already* adopted: DS packages + versions, token/font wiring, DS components in use (distinct + occurrence counts, heaviest files). Partial adoption is normal; the plan measures the remaining gap.
2. **Walk the authored CSS.** Total lines per file. Then enumerate the **named patterns**: for each, its selector family, line range, and a one-line description of what it is on screen. Group trivial utilities. Flag hardcoded values vs token usage as you go. **Exclude the design system's own CSS** — vendored bundles, node_modules, build output are not product code.
3. **Cross-reference classes both directions.** Extract the classes *used in templates* and the classes *defined in stylesheets*, then diff: **used-but-unstyled** (orphaned hooks — templates reference them, no CSS anywhere; invisible to CSS-only scans and often the largest hidden gap) and **styled-but-unused** (dead CSS). Note dead partials/templates too — files no route includes.
4. **Inventory UI JS.** Behavior scripts (toggles, embeds, hydration glue) with line counts and purpose; separate from non-UI tooling (analytics, build scripts). Note anything with a documented expiry.
5. **Map templates & routes.** Layouts, partials, page types — and **content volume per type** (a pattern in a partial used by 8 routes, or baked into 700 stored posts, prices differently than a one-pager).
6. **Content archaeology scan.** Stored content (markdown, CMS bodies) carrying legacy markup — old embed wrappers, raw iframes, generator-era classes. Count instances; these usually become build-time transforms, not hand-edits.
7. **Run the deterministic scanner** if one exists — then sanity-check its numbers against what you just saw at source level. Report discrepancies as scanner-hygiene notes, not findings.

## Warning signs while you work

- Absurd scanner numbers (thousands of overrides, ~100% of anything) → it's scanning built output or the system's own vendored CSS
- A styles directory that's small and clean → the debt may be hiding in templates (orphaned hooks) instead
- Classes following a *different* naming convention than the rest → archaeological layer from an earlier era; probable dead code
- One template powering many routes → leverage (cheap wins); one pattern baked into stored content → cost (transform territory)

## Output

Write `BASELINE.md` from `templates/baseline.md`. Every entry `[verified]` or `[reported]`. Close with the headline: total custom surface, the single largest gap category, and what's already adopted.
