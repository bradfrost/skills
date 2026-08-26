# Adoption Intake — Check the Vehicle In

Before the teardown, check the vehicle in. This step builds `ds-adoption-plan/GARAGE.md`: a profile of the product, the target design system, and a map of what evidence the agent can actually reach. Every phase reads this file first.

**Agent:** work through the sections conversationally — a few questions at a time. Wherever you have live access (the repo, the system's MCP, a docs URL), *discover* the answer yourself and confirm it instead of asking. Aim for 10–15 minutes. Then write `GARAGE.md` using the template below and read it back for confirmation.

**First question, before anything else — can you reach the design system's catalog?** An adoption plan whose mappings aren't checked against the system's real APIs is a guess with a table of contents. Open with: *"Which design system are we adopting, and how can I reach its catalog — an MCP server, a components manifest, a docs site?"* Then **make one real call**: look up one component you expect to exist and confirm you get real props/slots/guidance back. Record the outcome. If the chain bottoms out at interview, say so plainly: the plan will still run, mappings will be `[reported]`, and the first work-order item is getting the agent catalog access.

## 1. The vehicle

- Product name, what it does, audience and rough scale (pages/screens/routes)
- Stack: framework, templating, build pipeline, where source lives vs build output
- Team: who will execute the adoption? Appetite: big-bang or wave-by-wave?
- Why now: what prompted the adoption push?

## 2. The target system

- Design system name and version; is the product already partially on it? (Check `package.json` / imports — partial adoption changes the whole plan: you're measuring the *remaining* gap.)
- How is it consumed — package, CDN, vendored? Version drift from latest?
- Where do system-gap findings get filed (issue tracker)? Who owns triage?

## 2b. The product's own tracker (probe it — don't just ask)

If you can reach the product's issue tracker (`gh issue list`, an MCP, or a pasted export), **list the open issues now** and pull out the adoption-relevant ones — especially anything filed by a prior `product-inspection` work order (unstyled templates, DS-fidelity findings, component bugs, upstream DS issue references). Record them in GARAGE.md. These are pre-existing records of the plan's findings: phase 2 cites them instead of re-deriving them, wave PRs close them, and issues that reference *upstream DS issues* seed the known-gaps list. A plan written blind to the tracker will duplicate it.

## 3. Evidence access map (the critical part)

Test, don't assume — make one real probe per row and record what worked:

| Asset | Access level to record |
|---|---|
| DS catalog | `live-mcp` (name the tools) / `export` (manifest pasted) / `docs` (URL readable) / `interview` |
| Product codebase | `live` (repo open) / `export` (pasted files) / `interview` |
| Running instance | `live` (browser bridge / dev server) / `screenshot` / `interview` |
| Issue tracker | `live` (gh/MCP — list the open issues) / `export` (pasted list) / `interview` |
| Deterministic scanner | `live` (an analyzer tool exists — name it, note its known blind spots) / `none` |

**Scanner honesty:** if the system ships a product-analyzer tool, record what it actually scans (source or built output? does it exclude vendored DS assets?). A scanner with hygiene blind spots still helps — but its numbers get sanity-checked against the source-level teardown, never reported raw.

## 4. The sacred list

What must survive the adoption untouched?

- Third-party DOM you don't control (ads, embeds, comment widgets)
- Semantic/legal markup (microformats, structured data, compliance text)
- Deliberate brand moments that intentionally sit outside the system
- Temporary glue with a known expiry (polyfills, hydration bridges) — record the linked issue

## 5. Scope & frame

- Whole product or a section/flow first?
- Target end state: "zero custom component CSS" or a defined residue?
- Anything explicitly out of scope this pass (e.g. stored legacy content)?

---

## GARAGE.md template

```markdown
# Adoption Plan — Garage Profile: <Product>
_Checked in: <date> · Method: ds-adoption-plan · Technician: <agent + catalog access>_

## Product profile
| | |
|---|---|
| Product | <name, what, audience, scale> |
| Stack | <framework, templating, build, source vs output paths> |
| Design system | <name @ version declared> vs <latest> · consumed via <package/CDN/vendored> |
| Target | <end state> |
| Sacred / intentional | <the keep-list, each with rationale or linked issue> |

## Evidence access map
| Source | Status |
|---|---|
| DS catalog | <live-mcp: tool names / export / docs / interview> — verified by <the real probe you made> |
| Repo | <access + branch> |
| Running instance | <URL / local / none> |
| Issue tracker | <live via gh/MCP · export · interview — note open-issue count> |
| Deterministic scan | <tool + known blind spots, or none> |

## Adoption-relevant open issues (from the tracker probe)
<issue# + title, especially prior inspection work-order filings — phase 2 cites these instead of re-deriving them>

## Known upstream gaps already tracked
<issue links found in code comments, the tracker probe, prior inspections, or team knowledge>

## Files in this run
- `BASELINE.md` — phase 1 teardown
- `MAPPING.md` — phases 2+3 parts list & estimates
- `plans/<date>-ds-adoption-plan.md` — phase 4 build schedule
```
