---
phase: 4
name: Build schedule
question: In what order does the work land, what does "done" mean per wave, and what's parked behind upstream gaps?
output: ds-adoption-plan/plans/<date>-ds-adoption-plan.md
---

# Phase 4 — Build schedule

Turn the priced parts list into waves the team can ship. Order by **dependency and leverage**, not by category: the fix that unblocks or de-risks the most other fixes goes first. Every wave gets a definition of done and a verification step — a wave without a "done when" is a vibe, not a plan.

## The canonical wave shape

Adapt to the product — most adoptions want some version of:

1. **Foundation** — tokens, fonts, theme wiring, page shell, DS package current. Skip what's already adopted (per the baseline); if foundation is missing, nothing else lands cleanly, so it's always wave 1.
2. **Quick swaps & deletes** — the XS/S rows with `[verified]` targets, plus all Delete rows. Visible wins, builds momentum, shrinks the surface before the harder work. **Also: file every upstream issue now** (System gaps, Recipe candidates) — filing early means later waves aren't waiting on triage.
3. **Compositions** — the M rows: listing pages, grids, cards, the slot-contract work. Sequence within the wave by leverage: shared partials first (one edit, many routes), most-bespoke pages last (they reuse the motifs the earlier items establish).
4. **Content archaeology** — stored-content transforms (build-time rewrites + verification scripts, not hand-edits). Can start in parallel once its target patterns exist; gate on any upstream gap it depends on.
5. **Gap-blocked & upstream-paced** — a parking table, not a wave: each row names its blocking issue and the local action when unblocked. Reviewed at each re-run; items graduate into waves as upstream ships.

## Per wave, write

- The mapping rows it contains (by ID — the plan cites the mapping, never restates it)
- **The issues it closes:** existing tracker issues covered by this wave's rows (from the phase 2 tracker check) — the wave's PR carries `Closes #N` so the tracker and the plan converge instead of drifting apart
- **Done when:** observable conditions — lines deleted, hooks closed, routes visually verified, scanner delta
- **Verification:** what gets run (build, visual check against prod, a11y/perf scripts, the deterministic scanner re-run)
- Ship unit: a wave should be a mergeable PR (or a small stack) — no long-lived adoption branches

## End state, stated up front

Open the plan with the measurable end state: e.g. "custom CSS from 427 → under 120 lines (sanctioned reset + documented Keeps); zero orphaned hooks; every remaining custom line carries a comment linking its Keep rationale or upstream issue." The re-run mode measures against exactly this.

## Cadence & the living loop

- **Re-run after each wave** (skill Mode 3): fresh teardown, delta against the plan — patterns retired, lines removed, hooks closed, gaps unblocked. Append deltas to the plan file.
- **Upstream watch:** the gap-blocked table lists its issues; check them each re-run.
- **Tracker sweep:** at each re-run, re-list the product's open issues — confirm the closed ones actually closed, catch new filings that belong in the plan, and flag plan items still missing from the tracker.
- **Telemetry, if the system has it:** confirm the product's usage shows up in the system's adoption/activity tracking after the first post-wave deploy — adoption the system can't see didn't happen, as far as the flywheel is concerned.

## Output

Write `plans/<date>-ds-adoption-plan.md` from `templates/ds-adoption-plan.md`. Close the session by presenting wave 1 as "Monday morning": the concrete first items, their mapping rows, and the done-when.
