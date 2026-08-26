---
station: 5
name: Testing & validation
quality: Sound (quality 2 of 5)
question: Is quality tested and validated across the system, and is testing built into workflows?
---

# Station 5 — Testing & validation

**Quality: Sound.** Out of all the quality checks, are there actual testing and validation steps in place so ongoing work *keeps* embodying them? Traditional deterministic testing (unit, visual regression, integration, E2E) is still very much a good idea — and in a world where more code is AI-generated, this station also asks the new question: are there **evals** judging the output of non-deterministic workflows? Green checkboxes aren't the goal; *trust* is. Humans validate at the end before anything goes out the door.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Test suites | Repo: test files next to components, coverage config | Pasted directory listing · interview |
| CI wiring | CI config: what runs on every PR (tests, lint, a11y, build) | Screenshot of a PR's checks · interview |
| Visual regression | Chromatic/Percy/Playwright screenshot config | Interview |
| Test *meaning* | Read tests for 2–3 core components — what do they assert? | Pasted test files |
| Evals / AI validation | Eval skills, LLM-as-judge rubrics, design linting (FigmaLint-style), agent QA loops | Interview: "how do you judge AI-produced work?" |

## Inspection procedure

1. **Does CI exist at all?** Tests, linting, and build running on every change — or local-only, "by vibes," where silent component bugs sail into the codebase and come back later as bug reports?
2. **Read the tests, don't count them.** For 2–3 core components: do tests assert key *behaviors* — keyboard interaction, state changes, edge cases — or just "it renders"? A wall of green checkboxes asserting nothing is a warning light with extra steps.
3. **Visual regression:** is anything watching for visual breakage when tokens or CSS change? A token system with no visual regression net makes every token change a gamble.
4. **Design-side validation:** any linting of the design library itself (token usage, a11y properties, structure — FigmaLint-style deterministic checks)?
5. **Evals for the non-deterministic era:** are there rubric-based evaluations for components and AI-assisted output — deterministic checks scripted where possible, LLM-as-judge for the subjective parts, with the judge grounded in real context (conventions docs, design.md)? Anything like a Playwright self-healing loop where the agent tests, screenshots, and fixes until acceptance criteria pass?
6. **Workflow integration:** is validation in the definition of done and enforced at PR time — or dependent on someone remembering?

## Warning lights

- No CI; tests and linting are local-only
- Silent component bugs that don't fail loudly
- No visual regression testing
- Tests exist but key behaviors (keyboard, states) aren't asserted
- No evals judging AI-produced output despite AI being in the workflow

## Scoring anchors

- **Red (0–3):** No CI. Whatever tests exist run on someone's laptop, sometimes.
- **Yellow (4–7):** CI runs and tests pass, but coverage is shallow (render-only assertions), no visual regression, nothing evaluating AI-generated work.
- **Green (8–10):** The whole suite — meaningful unit/behavior tests, visual regression, lint, a11y checks — runs on every change; evals exist for AI-assisted workflows; humans give the final blessing. The team *trusts* the system because the system earns it.

## Turning off the light

- Have AI produce a **test-coverage report of what's *not* tested** — untested surfaces, unasserted behaviors, silent failure modes — then generate the missing test cases and the CI/DevOps wiring. Standing up testing architecture used to be prohibitive for non-specialists; it isn't anymore.
- Add visual regression before your next token change, not after.
- Start evals small: one rubric-based component eval (deterministic checks + LLM-as-judge, 0–100 with pass/fail gates) that you run before promoting any AI-generated component. Grow from there. Keep humans at the end of the loop.
- Related deep tools: Design System Ops `cicd-integration`; Playwright (MCP or CLI) for self-healing browser loops; axe-core in CI (Station 3).

## Station record

```markdown
### Station 5 — Testing & validation: <RED|YELLOW|GREEN> (<n>/10)
- Inspected: <suites, CI config, tests read>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
