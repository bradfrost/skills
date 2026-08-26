---
station: 6
name: Orchestration
quality: Synchronized (quality 3 of 5)
question: Are design, code, and docs assets actually connected, and are workflows synchronized?
---

# Station 6 — Orchestration

**Quality: Synchronized.** Your Figma button, coded button, and docs should describe the same button — the moment they drift, every downstream decision is built on a lie. Stations 1–5 checked each asset; this one checks the *connections*. And it's as much a human-workflow question as a technical one: disconnected assets are usually the fingerprint of disconnected teams — handoff energy instead of genuine cross-disciplinary collaboration. Be rightly skeptical of any tool that claims to "solve" sync automatically; culture and workflow do the heavy lifting, tooling assists.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Design ↔ code parity | Both sides live: diff 3–5 components' variants/props/tokens/visuals | Exports of both · screenshots vs. rendered components |
| Docs ↔ reality parity | Docs pages vs. current component APIs | Pasted docs + API tables |
| Token sync | Token pipeline: single source flowing to design + platforms, or parallel manual copies? | Interview + both exports |
| Published vs. repo | Latest package vs. repo head — how stale is what consumers get? | Changelog · npm metadata |
| Workflow reality | How a change actually travels: who touches what, in what order | Interview; recent change post-mortem |

## Inspection procedure

1. **Diff design against code** for 3–5 components: same variants? same prop/property names and values? same token bindings? same visual result? Small mismatches here are the early smoke of big drift.
2. **Diff docs against reality:** do documented props/guidance match the shipping component, or describe a previous version?
3. **Trace the token pipeline:** one source of truth flowing everywhere (e.g. tokens → Style Dictionary → platforms + design variables), or parallel copies maintained by hand? Do web/iOS/Android agree?
4. **Check for duplicated sources of truth:** the same guidance copy-pasted into design files, code comments, and a docs site is three things to maintain and a drift generator. Cross-linking beats copying.
5. **Trace one real change end to end** (interview): when a component changed recently, how did design, code, and docs each get updated? Deliberate workflow with a definition of done spanning all three — or heroics and memory?
6. **Look for sync mechanisms:** Code Connect or similar bridges, drift-detection checks, CI parity tests, agentic cross-referencing — anything that *notices* divergence before users do.

## Warning lights

- Design, code, and docs have visibly drifted apart
- Changes flow one way only — design updates never reach code, or code never reaches docs
- No mechanism to propagate a change across all three; syncing is manual and ad hoc
- Tokens diverge across platforms (web, iOS, Android)
- Detached instances or competing forks drifting on their own
- Figma component names and variants don't match their code counterparts

## Scoring anchors

- **Red (0–3):** The three legs describe different systems. Nobody can say which is canonical. Changes routinely ship to one asset and never reach the others.
- **Yellow (4–7):** Mostly aligned, but sync is manual and personality-dependent; drift accumulates between deliberate cleanup pushes.
- **Green (8–10):** Sampled components trace cleanly across design, code, and docs; tokens flow from one source; the workflow's definition of done spans all three; something automated notices drift.

## Turning off the light

- Point AI at **any two assets and have it diff them** — design vs. code, docs vs. behavior, tokens across platforms — then propagate the reconciled change back across all three. Pairwise diffing at scale is something humans simply couldn't do before.
- Fix the *workflow*, not just the artifacts: make "represented in design, code, and docs" the definition of done, and add an AI check for it at PR time.
- Consolidate duplicated sources of truth into cross-links. With agentic workflows and scheduled tasks, agents can also cross-reference assets and pull the right context into the right workflow automatically — a genuinely new dimension of connective tissue.
- Adopt a context-based workflow: one shared context source (conventions, tokens, component intent) informing design work, code work, docs work, and the agents assisting each.
- Related deep tools: Design System Ops `drift-detection`, `design-to-code-check`; Figma Code Connect.

## Station record

```markdown
### Station 6 — Orchestration: <RED|YELLOW|GREEN> (<n>/10)
- Diffed: <components/assets compared>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <drift/connection finding + evidence>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
