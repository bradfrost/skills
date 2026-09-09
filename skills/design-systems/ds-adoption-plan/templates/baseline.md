# Phase 1 — Teardown: <Product> current-state UI inventory

_Inventoried <date> from source (not built output) · findings tagged `[verified]` / `[reported]` · run: `plans/<date>-ds-adoption-plan.md`_

**Headline:** <one paragraph: greenfield or mid-adoption? total custom surface across code *and* design? the single largest gap category? If the design side couldn't be inventoried, say so here — it changes how the estimate should be read.>

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

## 7. Design file surface

_Access: <live-figma (name the bridge) / screenshot / interview — per `reference/FIGMA-ACCESS.md`> · scope: <whole file, or the frames linked>_

| What | Count | Notes |
|---|---|---|
| Detached instances | <n> | <which components they drifted from> |
| Local components duplicating the library | <n> | <names> |
| Local styles / hardcoded values where variables exist | <n> | <color, type, spacing…> |
| Off-library frames built from scratch | <n> | <which screens> |

Cross-reference with sections 2 and 3: <which named patterns exist on both sides (one problem, two costs) · design-only (unbuilt work) · code-only (design-undocumented)>

## Scanner cross-check (if a deterministic analyzer ran)

<its headline numbers · discrepancies vs this source-level teardown · hygiene notes (built output? vendored DS CSS?)>
