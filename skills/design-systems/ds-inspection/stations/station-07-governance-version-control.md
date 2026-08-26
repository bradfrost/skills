---
station: 7
name: Governance & version control
quality: Extensible (quality 4 of 5)
question: Are there formal, documented, and accurate processes for how system changes are made and managed?
---

# Station 7 — Governance & version control

**Quality: Extensible.** Growth should be repeatable, not heroic. This station checks the human processes that let the system evolve reliably: contribution, release, ownership, and the artifacts and rituals around them. The subtle failure mode isn't *no* governance doc — it's a governance doc that describes an ideal while the team lives a different reality. Symptoms of that gap: recurring support frustration, and users quietly detaching and drifting away.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Process artifacts | Repo: CONTRIBUTING, PR/issue templates, CHANGELOG, release docs, ecosystem guidelines | Docs site · interview |
| Tracker health | Issue tracker: duplicates, staleness, blocker age, triage cadence | Pasted issue list · screenshot |
| Release hygiene | Tags/versions, release cadence, migration notes for breaking changes | Changelog · npm versions |
| Ownership | Who's accountable, on paper and in practice | Interview |
| Lived reality | Support-channel themes, how the last few changes actually landed | Interview; pasted Slack/Teams themes |

## Inspection procedure

1. **Inventory the artifacts:** CONTRIBUTING guide, PR/issue templates, changelog, release process doc, ecosystem guidelines (when to build a local recipe vs. contribute to core). Existing *and findable*?
2. **Audit tracker health** (with GARAGE.md thresholds): duplicate and stale issues piling up? Blockers open past the team's tolerance? Backlog 30+ days overdue with no triage? A kinked hose here means contributions die in the queue.
3. **Check version hygiene:** semantic versioning (or a deliberate alternative)? A steady release cadence, or releases "happening all over the place"? Breaking changes shipped with versioning, migration guidance, and communication — or as surprises? Branch protection on the source of truth?
4. **Test paper vs. reality:** walk the documented process against the last 2–3 real changes. Did they follow the path? Where did reality diverge? That divergence *is* the finding — reconcile the doc or the behavior.
5. **Confirm ownership:** someone clearly accountable for the system's health and evolution — or diffuse "everyone's responsible" (i.e., no one's)?

## Warning lights

- No CONTRIBUTING guide or PR template
- No changelog — changes live only in git history
- Duplicate/stale issues; blockers open past your threshold
- No branch protection or clear release process
- Backlog overdue by 30+ days with no triage
- No clear ownership — no one accountable for the system's health and evolution
- Breaking changes ship with no versioning or migration communication

## Scoring anchors

- **Red (0–3):** No formal process, or a fictional one. Releases ad hoc, breaking changes unannounced, backlog abandoned, ownership unclear.
- **Yellow (4–7):** Process exists and is mostly real, but hygiene slips — changelog gaps, stale issues accumulating, cadence wobbly, contribution path documented but rarely walked.
- **Green (8–10):** Documented governance that matches lived reality; healthy triaged tracker; steady releases with clean versioning and migration comms; clear ownership; contributors know exactly how to get a change in.

## Turning off the light

- This is one of AI's most exciting governance uses: feed the **corpus of ephemera** — issues, PRs, meeting notes, support-channel threads, backlog, roadmap — into an LLM and get a cold-shower read on the *reality*: what's working, what's stuck, where the gaps are. That corpus was always too big to synthesize by hand.
- Then have AI **draft the missing artifacts** (CONTRIBUTING, templates, release process, workflow diagrams, a real changelog) and **triage the backlog** — dedupe, staleness flags, priority suggestions. Set thresholds so stale items trip the warning light automatically next inspection.
- Build feedback loops: recurring support questions should automatically become governance/doc fixes so the same question stops arriving. Automate release communications.
- Related deep tools: Design System Ops `contribution-workflow`, `deprecation-process`, `decision-record`, `version-bump-advisor`, `change-communication`, `governance-encoder`.

## Station record

```markdown
### Station 7 — Governance & version control: <RED|YELLOW|GREEN> (<n>/10)
- Inspected: <artifacts, tracker stats, releases reviewed>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <finding + evidence; flag paper-vs-reality gaps>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
