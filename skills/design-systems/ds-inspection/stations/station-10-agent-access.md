---
station: 10
name: Agent access
quality: AI-Ready (quality 5 of 5)
question: Is the design system exposed to AI agents so it can be used successfully in AI-assisted product work?
---

# Station 10 — Agent access

**Quality: AI-Ready.** The final station. Station 9 made the knowledge machine-readable; this one asks whether agents can actually *reach* it from inside the tools where product work happens — and whether anyone knows it's there. Machine-readable context is the first step; the real success is connection into the org's actual tooling environments. And the goal isn't access for its own sake — it's **habitual, trusted use**: agents producing on-system results in real product work, in repeatable workflows teams actually run. (Same caveat as Station 9: this landscape is moving fast — revisit as tools evolve, not set-and-forget.)

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Query surfaces | MCP server(s), knowledge graph, API for the system | Try connecting/calling one · interview |
| Design ↔ code bridge | Code Connect or equivalent mappings | Config in repo · interview |
| Tool integration | Reachability from IDEs (Claude Code, Cursor, Copilot) and design tools the org actually uses | Interview: "what's in your team's daily tooling?" |
| Discoverability | Docs/onboarding telling downstream teams the AI tooling exists and how to wire it in | Docs scan · interview |
| Output quality | Live test: agent builds real UI through the access surface | Team's account of recent attempts |

## Inspection procedure

1. **Map the access surfaces:** is there an MCP server, knowledge graph, or equivalent an agent can query for components, tokens, usage rules? Try it live if you can: search for a component, look up a token. No surface = agents freelance from training data, and the output looks like it.
2. **Check the design↔code bridge:** Code Connect (or similar) mapping design components to real code — so design-to-code flows land on-system instead of generating lookalikes?
3. **Check integration into the actual toolchain:** whatever the org really uses (from GARAGE.md) — is the system reachable *there*, configured and working, not just theoretically available?
4. **Run the live test (the proof):** ask an agent, through the org's access surfaces, to rebuild a small page with the system's components. Grade the output: right components? correct props/tokens? conventions followed? **Weak, generic output is this station's warning light** — even with everything technically wired.
5. **Check discoverability and communication:** if the tooling exists but isn't documented or announced, teams can't use it. "We have an MCP" nobody knows about scores like no MCP.
6. **Check for repeatable workflows:** documented, shared AI-assisted workflows (scaffold a page, generate a variant, run this inspection) with a shared sense of where agents can and can't be trusted — or one person's private experiments?

## Warning lights

- No MCP or knowledge-graph surface to query
- No design-to-code bridge (no Code Connect)
- Not reachable from the IDE or design tool
- Agents produce weak, generic results
- No repeatable AI-assisted workflow in daily practice — AI use is one-off, with no shared sense of where it can and can't be trusted

## Scoring anchors

- **Red (0–3):** No exposure. Agents in the org's tools know nothing about the system; AI-assisted work is generic and off-system by default.
- **Yellow (4–7):** Some access exists (an MCP, partial Code Connect) but it's spotty, unintegrated into daily tools, undocumented, or produces mediocre results — capability without adoption.
- **Green (8–10):** System exposed via well-integrated surfaces; agents in the org's real tools produce on-system results; the tooling is documented and communicated; teams run repeatable AI-assisted workflows with shared, earned trust.

**No live test, no confirmed green.** Same rule as Station 9: if procedure step 4 wasn't run, a would-be green is *provisional green*, and running the test is the first move.

## Turning off the light

- Have AI **assess the current access story** (existing MCPs, Code Connect, metadata, docs) and report: can agents reach and successfully wield the ingredients? Then have it **help build what's missing** — standing up a design system MCP server, authoring skills and agent-facing ephemera, wiring integrations into each tool environment. This work is dramatically cheaper than a year ago.
- Test-drive relentlessly: agent rebuilds a page → weak output → trace whether it's an access problem (this station) or a context problem (Station 9) → fix → re-run. That loop is the tuning mechanism.
- Announce it and teach it: integration docs, onboarding, a lunch-and-learn. Then turn wins into named, repeatable workflows the team actually runs — the goal is habitual, trusted use, not a demo.
- Watch where your org's tooling goes next — wherever product work happens, the system needs to be reachable there too.
- Related deep tools: Design System Ops `context-engine-builder`, `governance-encoder`, `mcp-setup-guide` knowledge note; Figma Code Connect.

## Station record

```markdown
### Station 10 — Agent access: <RED|YELLOW|GREEN> (<n>/10)
- Surfaces mapped: <MCP/bridge/integrations> · Live test: <run/not run, output grade>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
