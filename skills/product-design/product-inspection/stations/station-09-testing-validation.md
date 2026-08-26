---
station: 9
name: Testing & validation
quality: Validated (quality 9 of 10)
question: Is the product's quality tested and validated — a real suite covering the core flows, running in CI as a gate — so it keeps working as it changes?
---

# Station 9 — Testing & validation

**Quality: Validated.** Every other station is a snapshot of quality *right now*; this one asks whether that quality is *defended over time*. It's the product-side rhyme of `ds-inspection`'s **Testing & validation** station — same question, pointed at the app instead of the system: does a real test suite exist, does it cover the core flows (the jobs from Station 5), does it run in CI as a gate that blocks bad merges, and — the new question in an AI-assisted world — are there **evals** judging non-deterministic output? Green checkboxes aren't the goal; *trust* is. This is also where the inspection eats its own cooking: the automatable stations (a11y, performance, best-practices, security) each recommend a CI check — this station verifies those checks actually exist and run.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Test suite exists & passes | Repo: run the suite (`npm test`/equivalent); read the config | Pasted test output · interview |
| Coverage of core flows | Do the tests exercise the Station 5 jobs end-to-end, or just utilities? | Read test files · interview |
| CI wiring | CI config: what runs on every PR — tests, lint, build, and the inspection's own gates (axe, Lighthouse, `npm audit`)? | Screenshot of a PR's checks · interview |
| E2E / integration | Playwright/Cypress driving real flows in a browser | Interview |
| Test *meaning* | Read 2–3 tests on core surfaces — what do they assert? | Pasted test files |
| The inspection's checks, wired | Are a11y/perf/security checks CI gates, or one-off manual runs (and do they even work)? | CI config · interview |
| Evals / AI validation | Rubric-based evals for AI-produced features, LLM-as-judge, self-healing agent loops | Interview |

## Inspection procedure

1. **Run the suite.** Don't take "we have tests" on faith — run it. Does it pass? How long, how many, how flaky? (A suite nobody can run green is worse than none.)
2. **Read the tests, don't count them.** For 2–3 core surfaces: do they assert real *behavior* — a flow completes, an error state renders, an edge case is handled — or just "it mounts"? A wall of green asserting nothing is a warning light with extra steps.
3. **Check coverage against the core flows.** Map the Station 5 jobs to tests. The primary job the product exists for should have an end-to-end test; if the happy path can silently break and no test fails, that's the gap.
4. **Does CI exist, and is it a gate?** Tests + lint + build running on every PR and *blocking merge* — or local-only "by vibes," where breakage sails in and comes back as a bug report later?
5. **Are the inspection's own checks wired — and do they run?** The a11y (axe), performance (Lighthouse), best-practices, and dependency-audit (`npm audit`) checks each station recommends: are they CI gates? And critically — **do they actually execute?** (A configured-but-broken checker — e.g. an a11y CLI pinned to a Chrome version that no longer exists — is a silent gap: it looks covered and isn't.)
6. **Evals for the non-deterministic era:** if AI generates features or content, is there rubric-based evaluation before it ships — deterministic checks where possible, LLM-as-judge for the subjective parts, humans at the end of the loop?

## Warning lights

- No test suite, or one that can't be run green
- Tests exist but assert only "it renders" — core flows have no coverage
- No CI, or CI that runs but doesn't block merge
- The primary job has no end-to-end test — it can break silently
- Recommended a11y/perf/security checks are manual-only, or configured but **broken** (silently not running)
- AI-generated features/content ship with no eval or human validation gate

## Scoring anchors

- **Red (0–3):** No CI, or no meaningful tests. Whatever exists runs on someone's laptop, sometimes; core flows can break silently.
- **Yellow (4–7):** CI runs and tests pass, but coverage is shallow (utilities tested, core flows not), or the inspection's checks are manual/partial/broken, or nothing evaluates AI-produced work.
- **Green (8–10):** The team can honestly say: *"Meaningful tests cover our core flows, they run in CI and block bad merges, our a11y/performance/security checks are gates that actually execute, and AI-assisted work passes an eval before it ships. We trust changes because the pipeline earns it."*

## Turning off the light

- Have an agent produce a **coverage report of what's *not* tested** — untested core flows, unasserted behaviors, silent failure modes — then generate the missing tests and the CI wiring. Standing up a test/CI pipeline used to be a specialist job; it isn't anymore.
- Wire the inspection's cheap automatable stations into CI as gates first: axe on real routes (Station 3), a Lighthouse budget (Station 7), `npm audit` (Station 8), a best-practices/console-error check (Station 2). That's the guardrail that keeps every other station from regressing between inspections.
- **Verify the checks run**, not just that they're configured — a green pipeline that skips a broken step is a false sense of safety.
- Add one end-to-end test for the single most important flow before the next feature, not after.
- Related deep tools: Design System Ops `cicd-integration`; Playwright (MCP or CLI) for self-healing browser loops.

## Station record

```markdown
### Station 9 — Testing & validation: <RED|YELLOW|GREEN> (<n>/10)
- Suite: <ran? n tests, pass/fail, duration> · Core-flow coverage: <which jobs have E2E> · CI gate: <yes/no, what runs> · Inspection checks wired: <axe/lighthouse/audit — gate/manual/broken>
- Evidence level: <live / export / screenshot / interview, per check>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
