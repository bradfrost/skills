---
station: 5
name: Usability
quality: Usable (quality 5 of 10)
question: Can a real user actually complete the product's core jobs, end to end, without getting stuck, confused, or dropped?
---

# Station 5 — Usability

**Quality: Usable.** Every prior station inspects an attribute — adoption, best practices, a11y, clarity. This one inspects the *whole*: put yourself in the user's shoes and try to accomplish what they came to do, start to finish. A product can pass every component-level check and still fail here because the *flow* is broken — a dead end, a missing step, a confirmation that never comes, a path that assumes knowledge the user doesn't have. This is the station that most resembles a lightweight usability test, and it leans hardest on [NN/g's usability heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/) as its judgment vocabulary — "user control and freedom," "error prevention," "flexibility and efficiency of use." Cite the heuristic by name when a finding is judgment-based.

**Calibrate against the product's own intent.** The core jobs come from `GARAGE.md` → "Intent & ideal" — the team's stated purpose, not your inference. Score the product against what *it* says it exists to do; where the shipped flow diverges from the stated goal, that's a finding even if the flow technically completes.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| The core jobs | GARAGE profile ("Intent & ideal") + interview: what are users here to do? | Product docs · your own inference |
| Flow walkthrough | Live instance: complete each core job end to end, as a user | Screen recording · interview |
| First-run experience | Live instance from a fresh/empty account | Screenshots · interview |
| Drop-off points | Analytics/funnels if reachable | Interview: "where do people get stuck?" |
| Recovery paths | Live: can users undo, go back, fix a mistake mid-flow? | Interview |
| Friction & dead ends | Observed during the walkthrough | Interview |

## Inspection procedure

1. **Name the core jobs** — the 2–5 things this product exists to let people do (from intake). Score against these, not every feature.
2. **Complete each job end to end, as a first-time user would.** Don't use insider knowledge. Note every point of hesitation, every "wait, how do I…," every step that required a guess.
3. **Start from empty.** Run the primary job from a fresh account/blank state — the first-run experience is where products lose people. Is there orientation, or a cold blank?
4. **Count the steps and the friction.** Is the path as short as it can be? Unnecessary steps, redundant confirmations, re-entered data, context switches?
5. **Test recovery.** Mid-flow, can the user go back, undo, edit a prior step, or abandon cleanly — without losing work or hitting a dead end?
6. **Find the dead ends.** Anywhere the user can land with no clear next action, no way forward, or an error they can't get past.
7. **Cross-reference analytics** if reachable: where do real funnels drop? That's evidence pointing at the broken step.

## Warning lights

- A core job that can't be completed, or only with insider knowledge
- Cold first-run: empty state with no path to the first success
- Excess steps, re-entered data, or forced context switches in a common flow
- No way to go back, undo, or fix a mistake without starting over
- Dead ends — screens with no clear next action
- Analytics showing consistent drop-off at a specific step

## Scoring anchors

- **Red (0–3):** A core job is broken, blocked, or completable only by someone who already knows the product. Users get stuck.
- **Yellow (4–7):** Jobs are completable but with real friction — a confusing step, a rough first-run, a missing recovery path, avoidable length.
- **Green (8–10):** The team can honestly say: *"A first-time user can complete every core job end to end, understands each step, can recover from mistakes, and never hits a dead end."*

## Turning off the light

- The walkthrough notes *are* the punch list — each hesitation point is a fix, ranked by how core the job is.
- First-run and recovery paths are usually the biggest wins; fixing a cold empty state lifts the whole funnel.
- Where a step's necessity is unclear, that's a product-design question for the human — surface it, don't silently prescribe.
- If real users are available, a 5-person hallway test beats any inspection here; recommend it.

## Station record

```markdown
### Station 5 — Usability: <RED|YELLOW|GREEN> (<n>/10)
- Core jobs tested: <list> · Completed end-to-end: <n/n> · Worst friction: <where>
- Evidence level: <live / recording / analytics / interview, per job>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
