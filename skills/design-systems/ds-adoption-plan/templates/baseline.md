# Phase 1 — Teardown: <Product> current-state UI inventory

_Inventoried <date> from source (not built output) · findings tagged `[verified]` / `[reported]` · run: `plans/<date>-ds-adoption-plan.md`_

**Headline:** <one paragraph: greenfield or mid-adoption? total custom surface? the single largest gap category?>

## 1. Foundation (already adopted)

<DS packages + versions · token/font wiring · shell · distinct DS components in use with occurrence counts and heaviest files. "None" is a valid, important answer.>

## 2. Custom CSS surface — <n> lines total

| File | Lines | Loaded |
|---|---|---|
| <path> | <n> | <how/where> |

Patterns defined (with line ranges): <named list — each pattern family, its range, one-line description of what it is on screen. Group trivial utilities. Note token usage vs hardcoded values.>

## 3. Orphaned class hooks — used in templates, styled nowhere

| Family | Where used | Notes |
|---|---|---|
| <class family> | <template(s) + route count> | <…> |

Dead code (inverse): <styled-but-unused CSS · dead partials no route includes>

## 4. UI JavaScript

<behavior scripts with lines + purpose · glue with documented expiry (+ issue links) · non-UI scripts noted and excluded>

## 5. Templates & routes

<layouts · partials (with consumer counts) · page types · content volume per type — the numbers phase 3 prices against>

## 6. Content archaeology

<legacy markup in stored content: pattern → instance count. Transform territory, not hand-edits.>

## Scanner cross-check (if a deterministic analyzer ran)

<its headline numbers · discrepancies vs this source-level teardown · hygiene notes (built output? vendored DS CSS?)>
