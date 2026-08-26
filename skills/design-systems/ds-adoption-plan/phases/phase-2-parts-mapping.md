---
phase: 2
name: Parts mapping
question: For every custom pattern in the baseline, what replaces it — a system part, a composition, a new recipe, or nothing yet?
output: ds-adoption-plan/MAPPING.md (rows; phase 3 adds the estimates)
---

# Phase 2 — Parts mapping

The heart of the estimate. Every pattern from the teardown gets exactly one **disposition** and, where applicable, a verified system target. This is where catalog access earns its keep — and where intuition goes to get corrected.

## Dispositions

| Disposition | Meaning | Test |
|---|---|---|
| **Swap** | Direct replacement exists | One component covers the pattern's whole job |
| **Compose** | Assemble from system parts | The pattern is chrome + content that existing components + slots express |
| **Recipe candidate** | Belongs *in* the system | The pattern is product-shaped but reusable — propose it upstream; map to the composition it would formalize |
| **System gap** | The system lacks it | Nothing covers it and it isn't a recipe of existing parts — file upstream, plan around |
| **Delete** | Dead code | Nothing uses it (teardown's dead-CSS / dead-partial list) |
| **Keep** | Intentionally bespoke | On the GARAGE.md sacred list, or third-party glue — record rationale + any expiry issue |

## Mapping procedure — per pattern

1. **Look it up for real.** Query the system's catalog (MCP lookup/search, manifest, docs — per the GARAGE.md access chain) for the candidate target. Get its **actual** props, slots, and usage guidance. A mapping sourced this way is `[verified]`; anything from memory or general DS knowledge is `[reported]`.
2. **Read the don'ts before the dos.** Check the target's don't-use guidance, accessibility notes, and semantics. The intuitively-named component is often wrong: a "notice" banner maps to `alert` by name — until the catalog says alerts carry semantic urgency and announce via `role="alert"` on load, and a band/section composition is the real match. **When the catalog overrules the intuitive pick, record both** — "notice → ~~alert~~ band composition, because…" is the most instructive row in the report.
3. **Verify the composition shape.** For Compose rows, confirm every slot name and required child against the catalog (invented slot names silently drop content in most component models; missing required wrappers break layout). If the system publishes canonical usage examples, copy their skeleton. If catalog metadata contradicts a canonical example or the source, trust the example/source and note the docs discrepancy as a system finding.
4. **Check the tracker before proposing anything.** GARAGE.md's tracker probe lists the product's open issues — a prior inspection work order may have already filed this exact finding. If an issue exists, the row **cites it** (and the wave that fixes it will close it); if the issue references an upstream DS issue you didn't know about, add it to the row's dependencies. Only findings absent from both trackers become new filings — drafted for the human to approve, never filed unilaterally.
5. **Search before declaring a gap.** A System gap row must cite the search that came up empty ("no video/embed component in catalog; nearest prior art: X"). Name what the proposed component/recipe would be, so the upstream filing is concrete.
6. **Route the recipe candidates.** A pattern used across many routes (a dated post list, a bio block) that the system *almost* covers is a proposal, not a gap: map it to the composition it would formalize, and note the upstream proposal.
7. **Honor the sacred list.** Keep rows cite their GARAGE.md rationale or expiry issue. Don't map what the team has declared intentional.

## Cross-cutting checks

- **Semantics & a11y parity:** the replacement must preserve landmarks, heading order, link/button semantics, and any microformats/structured data the pattern carries. A visual match that loses semantics is a regression, not an adoption.
- **State coverage:** if the custom pattern handled states (active, error, empty), confirm the target covers them or note the delta.
- **Behavioral JS:** patterns with behavior map to components that own that behavior — or the JS delta goes in the row's notes (it prices into phase 3).

## Output

Fill the tables in `templates/mapping.md` — grouped as the baseline groups them (styled patterns / orphaned hooks / content archaeology / JS & glue). Close with the **upstream filings list**: every System gap and Recipe candidate this mapping produced, ready to file against the design system. Cross-link: these belong in the DS's backlog and should surface in its next `ds-inspection` coverage station.
