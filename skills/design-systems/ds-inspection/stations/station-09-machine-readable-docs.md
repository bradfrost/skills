---
station: 9
name: Machine-readable docs & context
quality: AI-Ready (quality 5 of 5)
question: Can a machine actually consume the system's knowledge, not just a human?
---

# Station 9 — Machine-readable docs & context

**Quality: AI-Ready.** Stations 1–8 sturdied the foundations; the last two check whether machines can use them. "Docs exist" (Station 1) is not "a machine can pick up those docs and use them properly." This station asks whether all that hard-earned infrastructure has an explicit, AI-facing context surface that works with the grain of how LLMs operate — because the symptom of failure is painfully concrete: agents misusing your components and producing off-system output. Caveat from the course: formats and techniques here are emerging and changing constantly — carry the spirit (make your system's knowledge available to LLMs), hold the specifics loosely.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Machine-consumable formats | Repo: tokens as JSON/CSS vars, typed component APIs, component metadata files | Pasted samples · interview |
| AI-facing context surfaces | llms.txt, agent rules files (CLAUDE.md/AGENTS.md/.cursorrules), schemas, component descriptions written for machines | Repo/docs scan · interview |
| Structure of the docs | Docs source: structured/parseable, or prose-only walls? | Pasted pages |
| The proof | A generation test — see procedure step 4 | Interview about past AI attempts |

## Inspection procedure

1. **Inventory machine-consumable formats:** tokens published as JSON / CSS custom properties / design-tool variables (not just a styles page)? Component APIs in a parseable form (TypeScript types, JSON schema, custom-elements manifest)? Usage rules encoded anywhere a machine can read — or living only in paragraphs and Slack lore?
2. **Look for explicit AI-facing surfaces:** llms.txt or equivalent index; agent rules files; component metadata with purpose, anti-patterns, composition rules, a11y contracts; docs published in a structured, chunkable format. None of these = the system speaks only human.
3. **Judge machine-legibility of the docs themselves:** consistent structure per component (an agent can find props/usage/don'ts in the same place every time)? Guidance phrased as rules ("never place a button inside a link") or vibes ("use judiciously")? Cross-links resolvable?
4. **Run the proof (the test that matters):** give an agent the system's docs/context and ask it to build a small composition — a settings form, a card grid. Watch where it trips: wrong component choice, invented props, hardcoded values, missed conventions. Every stumble marks a context gap. No live agent available? Ask the team what happened last time someone tried (`[reported]`).
5. **Check freshness wiring:** is the machine-readable layer generated from source (types, tokens, stories) so it stays true — or hand-maintained and quietly rotting (which re-fails Station 6)?

## Warning lights

- Docs that read fine for humans but have no machine-readable structure
- No AI-facing context surface (no llms.txt, schemas, or metadata)
- Component metadata that confuses agents
- Agents misuse components because rules aren't machine-readable
- Tokens and props aren't published in a machine-consumable format (JSON, CSS variables, Figma Variables)

## Scoring anchors

- **Red (0–3):** Knowledge lives in human-only prose and habit. No structured metadata, no AI-facing surface. Agents guess — badly.
- **Yellow (4–7):** Raw materials are machine-friendly (typed APIs, token JSON) but no deliberate AI-facing layer: no llms.txt, no usage rules, no anti-patterns encoded. Agents get the *what*, miss the *how* and *when*.
- **Green (8–10):** A deliberate, current context surface: structured metadata (purpose, props, anti-patterns, composition, a11y), machine-consumable tokens, encoded usage rules — generated from source, and the generation test passes with minor stumbles at most.

**No generation test, no confirmed green.** If procedure step 4 wasn't run, record a would-be green as *provisional green* with the reason — the test is the proof, and running it becomes the station's first move.

## Turning off the light

- It's a bit meta, and it works: **use LLMs to assess your docs' AI-readiness** — feed in docs and metadata, ask what an agent can and can't determine — then have AI **author the machine-readable layer**: component descriptions (purpose, props, anti-patterns, composition, accessibility, examples), llms.txt, metadata schemas. Human-review everything; this layer steers every future agent.
- **Iterate through failure.** There's no arriving at this in one pass: generate compositions, pages, whole flows; watch where AI trips; feed each failure back into the context. The failure log *is* the roadmap.
- Generate from source wherever possible — metadata derived from types, tokens, and stories can't silently drift the way hand-written context does.
- Related deep tools: Design System Ops `ai-component-description`, `metadata-schema-generator`, `codebase-index`, `context-engine-builder`, `component-decision-tree`.

## Station record

```markdown
### Station 9 — Machine-readable docs & context: <RED|YELLOW|GREEN> (<n>/10)
- Inventoried: <formats, surfaces found> · Generation test: <run/not run, result>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
