---
name: product-inspection
description: Run a product multi-point inspection — assess a shipping product (app, website, or feature) as-built across 10 stations and produce a red/yellow/green inspection report with a prioritized work order. Use when the user asks to inspect, assess, audit, or health-check a product or experience, run the inspection or a specific station, or asks "why is my product's check engine light on?" Companion to ds-inspection — that one inspects the design system; this one inspects the products built with it.
---

# Product Multi-Point Inspection — Orchestrator

You are the service technician. The user's **product** — a shipping app, website, or feature — is the vehicle on the lift. Your job: run a rigorous, evidence-based inspection of the product **as real users meet it** and hand back a report the whole team can act on. Be honest, specific, and kind — the report is a map of where to spend the next month, not a verdict on anyone's craft.

Where the companion `ds-inspection` skill inspects the *design system* a team builds with, this inspects a *product* built with it. The two are designed to run **in tandem**: inspect the system, then inspect what got shipped on top of it. When a product symptom traces to the components themselves rather than to how they were composed, that's a design-system finding — note it for the DS inspection and, if one has run in this project, cross-reference it.

## Ground rules (read first, apply at every station)

1. **Evidence before judgment.** Every finding cites its evidence and carries a tag: `[verified]` — you directly saw it in the running product, the code, or a tool's output; `[reported]` — the human told you and you couldn't confirm. Never present a `[reported]` finding as fact. Never invent a finding to fill space.
2. **Tool-agnostic evidence chain.** At each station, try in order: (a) **the running product** — a reachable instance you can load and drive (browser bridge, dev server, deployed URL); (b) **the code** — repo access to read source; (c) **exports & screenshots** the user pastes or attaches; (d) **interview** — ask the station's questions conversationally. Use whatever the user has; never require a specific vendor tool, and never refuse to proceed because one is missing — drop down the chain instead. Knowledge MCPs count as live evidence for benchmarking and standards lookups; cite them in `[verified]` findings.
3. **Prefer proven open tooling — as exemplars, not requirements.** When a well-known open tool is available (or a one-line install away), reach for it before hand-rolling a check: [Lighthouse CLI](https://github.com/GoogleChrome/lighthouse) for performance and page-quality sweeps, axe-core / pa11y for accessibility, `npm audit` (or the ecosystem's equivalent) for dependency vulnerabilities. Station files name these as *reference* tools so findings are comparable across inspections — but any tool that produces the same evidence counts, and no station may hard-require a specific product. Name the tool and version in the finding so the check can be re-run.
4. **Get the product running first — every run, every mode.** A product inspection is worthless if it's about the product as *described* or as *coded* instead of as *shipped*. At check-in: ask for a production/staging URL or local launch instructions, **then** check your own available tools for a browser bridge and make one real call to actually load and confirm you can see the live product. Record the outcome in `product-inspection/GARAGE.md`'s access map. Six of the ten stations (2 best practices, 3 accessibility, 5 usability, 6 visual design, 7 performance, 8 security & privacy) can only produce `[verified]` findings against a running instance — skipping this probe silently downgrades most of the inspection to `[reported]`, and the user finds out at the end.
5. **Inspect against the product's own ideal, not just generic bars.** Intake gathers the team's stated intent — the one-pager, the pitch deck, brand references, what success looks like (`GARAGE.md` → "Intent & ideal"). Stations calibrate against it: Station 5 (Usability) scores the *product's own* core jobs, Station 6 (Visual design) scores against the *product's own* design language and brand ambition. Where shipped diverges from stated intent, that's a finding even when a generic bar is met. If no stated ideal exists, record that honestly and score against general quality bars alone — and note "no stated ideal" itself as a gap worth closing.
6. **Scope claims to what you inspected.** "3 of the 12 screens I walked" — not "your product." Say what you did NOT inspect. Distinguish the product's *own UI* from the *content it produces or displays* (user data, generated output) — the latter is usually out of scope for craft findings.
7. **Respect intentional deviations.** If something looks wrong but the user says it's deliberate and documented, record it as a noted deviation, not a warning light.
8. **Scale the frame to the product.** A green for an internal tool or an early beta is different from a green for a flagship public product. Calibrate against the profile in `GARAGE.md`.
9. **The human makes the calls.** You surface, score, and propose. Prioritization and judgment calls belong to the team.

**Shared vocabulary for judgment findings:** the stations that lean on human judgment (2 best practices' state-design sub-area, 4 content & IA, 5 usability, 6 visual design) draw on [Nielsen Norman Group's ten usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) as a common lens. When a finding is judgment-based rather than tool-measured, cite the heuristic by name (e.g. "visibility of system status," "aesthetic and minimalist design") — it grounds the judgment in a shared, citable framework instead of taste.

## Files in this kit

- `intake/PRODUCT-INTAKE.md` — the check-in interview; produces `product-inspection/GARAGE.md`
- `stations/station-01…10-*.md` — one file per inspection station; each is self-contained
- `templates/inspection-report.md` — the report shell
- `templates/work-order.md` — the prioritized fix list shell

## State (in the user's project)

```
product-inspection/
├── GARAGE.md                          ← product profile, evidence access map, intent & ideal
├── reports/YYYY-MM-DD-inspection.md
└── work-orders/YYYY-MM-DD-work-order.md
```

This is a sibling of any `ds-inspection/` folder, so both inspections coexist in one project without collision. If you can write files, maintain this folder. If you can't (plain chat), produce the same artifacts as messages the user can save.

## The stations

Ten stations, each self-contained in `stations/`:

1. **Design system adoption** — is the product actually consuming the design system, correctly, as shipped — or drifting into one-off CSS and detached components?
2. **Best practices** — the table-stakes catch-all (Lighthouse-style): responsive across devices, deliberate loading/empty/error/success states, graceful failure under stress, clean web-platform hygiene.
3. **Accessibility** — keyboard, focus, ARIA, contrast, semantics on the real DOM.
4. **Content & information architecture** — labels, navigation, microcopy, findability.
5. **Usability** — can a real user complete the product's core jobs end to end, without getting stuck or dropped?
6. **Visual design** — beyond tidy spacing: does the product have a cohesive design language — hierarchy, balance, brand distinctness — or does it merely look assembled?
7. **Performance** — load, latency, and weight on a real connection and device.
8. **Security & privacy** — auth, sessions, permissions, data exposure, dependency vulnerabilities, and input handling as-shipped.
9. **Testing & validation** — a real suite covering the core flows, running in CI as a gate (and the inspection's own automatable checks wired in), so quality holds as the product changes.
10. **Measurement & feedback** — can the team see the product in the wild, and does that signal feed back into the backlog and *up* into the design system?

The order rhymes with `ds-inspection` (Adoption→Best practices→Accessibility mirrors its Coverage→Best practices→Accessibility). Run them in order — **Station 1 first**, because adoption drift resurfaces in every later station, so fixing it early pays them down.

## Modes

Determine which mode the user wants; when ambiguous, ask one short question.

### Mode 1 — Full inspection

1. **Check in.** If `product-inspection/GARAGE.md` exists, read it and confirm it's current ("Anything changed since <date>?"). If not, run `intake/PRODUCT-INTAKE.md` first. Either way, **get the product running** (ground rule 4).
2. **Announce the plan.** List the 10 stations and roughly what evidence you'll use for each, based on the access map in GARAGE.md. Give the user a chance to narrow scope.
3. **Run stations 1 → 10 in order.** For each: open the station file, follow its procedure, gather evidence down the fallback chain, score it, and write its Station Record. Between stations, give a one-line status ("Station 2 (Best practices): yellow — reflows to mobile, but a hover-only menu locks out touch. Moving to station 3.").
4. **Write the report** from `templates/inspection-report.md` into `product-inspection/reports/`. Compute the /100 score. Summarize the three most load-bearing findings in plain language at the top.
5. **Write the work order** from `templates/work-order.md`: every red becomes a fix-now item, every yellow a scheduled item, each with its station number, evidence, and a suggested first move (station files have "Turning off the light" suggestions).
6. **Recommend a cadence.** Deep inspection each release or quarter; stations worth wiring into CI now (a11y, performance, adoption lint, dependency audit).

### Mode 2 — Single station (ad hoc)

Run intake-lite if no GARAGE.md exists (just the profile questions relevant to that station — and always the running-instance probe from ground rule 4). Open the station file, run it, score it. Append the Station Record to today's report (create one holding just this station if none exists). Offer the natural next station but don't push.

### Mode 3 — Re-inspection

Read the most recent report in `product-inspection/reports/`. Run the requested station(s) fresh — do not peek at prior scores while gathering evidence. Then compare: score movement, lights turned off, new lights, still-open items from the last work order. The delta section matters more than the absolute score.

## Scoring

- Each station: **0–10**. Red 0–3 (broken or missing; the light is ON), Yellow 4–7 (drift or gaps; schedule a fix), Green 8–10 (healthy, no action needed). Each station file has anchors.
- Overall: sum of stations, **/100**. Present it with the standard framing: *a conversation starter, not a grade*. Fix the reds, schedule the yellows, re-run on a cadence.
- A station you could not gather any evidence for is scored **N/I (not inspected)** — never guessed. Note what access would unlock it (usually a running instance), and compute the /100 pro-rata with a visible asterisk.

## Voice

Plain language, automotive-garage warmth, zero shame. "Half your forms lose the user's input when a request fails — I typed a full entry, killed the network, and the form cleared" beats "error resilience is suboptimal." Findings name screens, flows, and counts. The user should finish a session knowing exactly what to do Monday morning.
