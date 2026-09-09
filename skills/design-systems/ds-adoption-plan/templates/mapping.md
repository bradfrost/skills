# Phases 2+3 — Parts mapping & estimate: <Product> → <Design System>

_Mapped <date> · targets verified against the system's catalog via <access method from GARAGE.md> · `[verified]` = real API checked; `[reported]` = unconfirmed_

Dispositions: **Swap** · **Compose** · **Recipe candidate** · **System gap** · **Delete** · **Keep**
Effort: XS / S / M / L — basis: instances × templates touched × API distance × behavioral risk (see phase 3).

## A. Styled patterns

| # | Pattern | Disposition | Target & evidence | Design side | Effort (code / design) |
|---|---|---|---|---|---|
| A1 | <pattern> | <disposition> | <system target, the `[verified]` evidence, and — when the catalog overruled the intuitive pick — both: "→ ~~intuitive~~ actual, because <the catalog's own guidance>"> | <library component the design file should use · "no counterpart" · "n/a, code-only"> | <XS/S/M/L> / <XS/S/M/L or —> |

_Roll-up: <n> rows — <n> S, <n> M, <n> blocked… · design effort: <n> rows carrying design work_

## B. Orphaned hooks (templates only — no CSS today)

| # | Pattern | Disposition | Target & evidence | Effort |
|---|---|---|---|---|

## C. Content archaeology (stored content)

| # | Pattern | Disposition | Approach (transform, not hand-edits) | Effort |
|---|---|---|---|---|

## D. JS & glue

| # | Item | Disposition | Notes (expiry issues for temporary glue) |
|---|---|---|---|

## E. Design-only patterns (in the design file, not in code)

_Detached instances, local components duplicating the library, off-library frames. Design effort, no engineering effort._

| # | Pattern | Disposition | Library target & evidence | Effort |
|---|---|---|---|---|

## Upstream filings this mapping produces

1. **New:** <each System gap → the concrete component/recipe proposal, with the empty-search evidence>
2. **New:** <each Recipe candidate → the proposal + which rows it would formalize>
3. **Existing, now load-bearing:** <already-tracked upstream issues this plan depends on>

<These belong in the design system's backlog and should surface in its next ds-inspection coverage station.>
