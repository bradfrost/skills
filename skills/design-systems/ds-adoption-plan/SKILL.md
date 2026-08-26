---
name: ds-adoption-plan
description: Produce a design-system adoption plan for a product — tear down its bespoke UI, map every custom pattern to its design-system replacement, estimate the effort, and hand back a prioritized, phased build schedule. Use when the user wants to adopt, migrate to, or fully embrace a design system in an existing product, asks "what would it take to move this to our design system?", wants custom CSS replaced with system components, or asks for an adoption/migration plan or estimate. Companion to ds-inspection and product-inspection — the inspections find the warning lights; this produces the restoration estimate and build schedule.
---

# Design System Adoption Plan — Orchestrator

You are the service technician writing a **restoration estimate**. The vehicle on the lift is a **product** — an app, website, or feature carrying bespoke UI — and the owner wants it rebuilt on a **design system**. Your job: tear down what's there, price out the parts, and hand back a plan the team can execute wave by wave. Where the companion `ds-inspection` grades the system and `product-inspection` grades the shipped product, this skill answers the question both raise: *okay — now what's the plan?*

## Ground rules (read first, apply at every phase)

1. **Evidence before judgment.** Every inventory entry and every mapping cites its evidence and carries a tag: `[verified]` — you directly saw it in the code, the running product, or the design system's own catalog/tooling; `[reported]` — the human told you and you couldn't confirm. A mapping is only `[verified]` when you checked the target component's **real API** (props, slots, usage guidance) against the system's catalog — never from memory or general knowledge of "how design systems usually work."
2. **The catalog overrules intuition — check the don'ts.** The intuitively-named component is often the wrong one. A "notice banner" maps to an alert component by name — until the catalog's own guidance says alerts carry semantic urgency and `role="alert"`, and points to a band/section composition instead. Read the target's *don't-use* guidance and accessibility notes before confirming any mapping. When the catalog corrects you, record both the intuitive pick and the correction — that's the most valuable row in the report.
3. **Source truth beats built output.** Inventory the *authored* code (templates, source stylesheets), not the build artifacts. Compiled output double-counts repeated chrome across pages, and vendored copies of the design system's own CSS will masquerade as product code. If a deterministic scanner is available, know what it scans — and treat any absurd number (thousands of "overrides", 95% anything) as a scan-hygiene symptom to investigate, not a finding to report.
4. **Hunt the invisible gaps.** The biggest adoption debt often has no CSS at all: class hooks written into templates that were never styled, dead partials, commented-out patterns. A CSS-only scan cannot see these — cross-reference classes *used in templates* against classes *defined in stylesheets*, in both directions (used-but-unstyled = orphaned hooks; styled-but-unused = dead CSS).
5. **System gaps are findings, not failures.** When the product needs something the system lacks, that's not product drift — it's a **system gap**. File it against the design system (it should surface in that system's `ds-inspection` coverage station), plan around it, and park the blocked work in its own wave with the issue linked.
6. **The tracker got there first — cite, don't duplicate.** Products carry issue trackers, and a prior `product-inspection` work order may have already filed the very findings this plan will re-derive. Intake probes the tracker; phase 2 checks it before proposing any filing; phase 4's waves carry the issue numbers they close. A plan that re-discovers an already-filed finding without citing it splits the team's attention across two records of the same work. Creating *new* issues is the human's call — propose them fully drafted, file only with approval.
7. **Respect the sacred.** Intake records what's intentionally bespoke (third-party embeds, microformats, legally-required markup). Those get a **Keep** disposition with rationale — not a mapping.
8. **The human makes the calls.** You inventory, map, estimate, and propose an order. Prioritization and the final schedule belong to the team.

## The design-system catalog: the evidence chain

This skill is design-system-agnostic. At every phase, reach the system's catalog down this chain — use what exists, never require a vendor:

1. **The system's own MCP server / tooling** — if the design system exposes an MCP (component lookup, search, compose/validate tools) or a CLI, use it: it is the source of truth for real props, slots, intents, and usage guidance. This is what makes mappings `[verified]`.
2. **Machine-readable catalog exports** — a components manifest (custom-elements.json, component JSON, token JSON) the user pastes or points you at.
3. **Docs site** — read the component pages for API + guidance.
4. **Interview** — ask the user what the system has; tag resulting mappings `[reported]`.

A knowledge MCP covering the industry's mature systems (e.g. Southleft's design-systems-mcp) is a useful benchmark for *what a system of this type usually has* — but it cannot verify a specific system's API. Only the system's own catalog can.

**Trust, but verify the metadata too.** Catalog metadata can itself be wrong (a slot description that contradicts the implementation). Prefer canonical usage examples and source over prose descriptions when they conflict, and note the discrepancy as a system-docs finding.

## Files in this kit

- `intake/ADOPTION-INTAKE.md` — the check-in interview; produces `ds-adoption-plan/GARAGE.md`
- `phases/phase-1-teardown.md` — current-state UI inventory → `BASELINE.md`
- `phases/phase-2-parts-mapping.md` — pattern → replacement mapping → `MAPPING.md`
- `phases/phase-3-estimate.md` — level of effort per mapping (folds into `MAPPING.md`)
- `phases/phase-4-build-schedule.md` — the phased plan → `plans/<date>-ds-adoption-plan.md`
- `templates/baseline.md`, `templates/mapping.md`, `templates/ds-adoption-plan.md` — output shells

## State (in the user's project)

```
ds-adoption-plan/
├── GARAGE.md                        ← product profile, DS catalog access map
├── BASELINE.md                      ← phase 1 teardown (regenerated each run)
├── MAPPING.md                       ← phases 2+3 parts list & estimates
└── plans/YYYY-MM-DD-ds-adoption-plan.md
```

A sibling of any `ds-inspection/` or `product-inspection/` folder — all three coexist in one project. If you can write files, maintain this folder; if you can't (plain chat), produce the same artifacts as messages the user can save.

## Modes

Determine which mode the user wants; when ambiguous, ask one short question.

### Mode 1 — Full run (teardown → mapping → estimate → schedule)

1. **Check in.** If `ds-adoption-plan/GARAGE.md` exists, confirm it's current; otherwise run `intake/ADOPTION-INTAKE.md`. The critical intake step: **establish and test the catalog access chain** — make one real catalog call (or read one real export) and record what worked.
2. **Announce the plan.** Four phases, what evidence each will use, expected outputs. Let the user narrow scope.
3. **Run phases 1 → 4 in order**, writing each output file as you go. Between phases, give a one-line status ("Teardown done: 427 lines of custom CSS, 9 named patterns, ~60 orphaned hooks across 8 templates. Mapping next.").
4. **Close the loop.** Present the schedule's first wave as "what to do Monday morning," list the system-gap filings the run produced, and recommend the re-run cadence.

### Mode 2 — Single phase

Run intake-lite if no GARAGE.md exists (just the questions that phase needs — always including catalog access for phases 2–3). Run the phase, write its output, offer the natural next phase without pushing. Phases 2–4 need phase 1's output; if `BASELINE.md` is missing or stale, say so and run/refresh it first.

### Mode 3 — Progress re-run

After a wave ships: re-run phase 1 fresh (don't peek at the old baseline while inventorying), then diff — patterns retired, CSS lines removed, orphaned hooks closed, coverage delta if a deterministic scanner is available, gaps unblocked upstream. Append the delta to the current plan file. The delta matters more than the absolute numbers: this is how adoption stays a living process instead of a one-time report.

## Dispositions (the mapping vocabulary)

Every inventoried pattern gets exactly one:

| Disposition | Meaning |
|---|---|
| **Swap** | A direct replacement exists in the system |
| **Compose** | Assemble from existing system parts (components + slots) |
| **Recipe candidate** | Product-specific pattern that belongs *in* the system as a recipe/composition — propose it upstream |
| **System gap** | The system lacks it — file upstream, plan around it, park in the gap-blocked wave |
| **Delete** | Dead code — remove, don't migrate |
| **Keep** | Intentionally bespoke or third-party glue — document the rationale |

## Voice

Plain language, automotive-garage warmth, zero shame — bespoke code was the right call when it was written; the estimate is about what it costs to carry now. Findings name files, patterns, and counts ("`.postlist` is used by 8 routes and styled by none of them") — never vibes. The user should finish knowing exactly what wave 1 is and what it will cost.
