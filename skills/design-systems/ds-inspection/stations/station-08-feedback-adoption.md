---
station: 8
name: Feedback & adoption
quality: Extensible (quality 4 of 5)
question: Is system adoption tracked, and is product context feeding back into the system?
---

# Station 8 — Feedback & adoption

**Quality: Extensible.** Two questions, and the second matters more: is adoption measured, and is real product work *informing* the system's ongoing work? The healthiest systems have a virtuous cycle — product context flows in, system improvements flow out. The saddest signal in design systems is the team learning after the fact that a product team scrapped, hacked, or detached from the system. Distance between system and product is the thing to measure here — numbers are only part of the picture; the real story is *how* teams use the system, where they're succeeding, and what frustrates them.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Usage data | Import/dependency scan across consumer repos; design-library analytics; npm downloads | Pasted stats · interview |
| Feedback mechanisms | Support channel, intake form, office hours — and their actual activity | Interview |
| Detachment signal | Detached instances, local forks/overrides, hardcoded workarounds in product code | Drift findings from Station 6 · interview |
| Roadmap connection | System backlog vs. product roadmaps: does one reflect the other? | Interview |
| The "this is broke, please fix" index | Quality of incoming issues — context-rich or one-liners? | Tracker sample |

## Inspection procedure

1. **Measure what you can reach.** Even a simple grep across consumer projects shows which components are actually used, which are ignored, and where local forks live. Design-side: library analytics, detach rates if available. No access? Record the team's estimate as `[reported]` and note that instrumentation itself is a work-order item.
2. **Distinguish coverage from adoption:** teams that *can* use the system vs. teams that *do*. High coverage + low adoption is a different problem (trust, fit, awareness) than low coverage (distribution).
3. **Audit the feedback loop:** does a mechanism exist, and is it *alive*? An empty feedback channel isn't success — it usually means people stopped bothering. Where do complaints actually go, and does anything change because of them?
4. **Check the roadmap connection:** does the system team know what product teams are building next quarter? Does product work show up in the system backlog? Or is the system team standing on its back feet, finding out after the fact?
5. **Look for the breakup signs:** teams that quietly stopped upgrading, forked components, or built parallel ones. Each is data about unmet needs — treat them as intel, not betrayal.
6. **Check the cadence:** is *this inspection itself* on a schedule, or a one-off? Reviews ad hoc = drift by default.

## Warning lights

- No adoption/usage analytics
- A feedback mechanism that exists but is empty
- No deprecation/migration announcements
- Reviews are ad hoc; inspection treated as one-and-done
- No regular cadence for this inspection

## Scoring anchors

- **Red (0–3):** No idea who uses what. No live feedback path. System team detached from product reality; discovers scrapped adoptions after the fact.
- **Yellow (4–7):** Some numbers (downloads, rough counts) but not the story behind them; feedback arrives informally and irregularly shapes the roadmap.
- **Green (8–10):** Adoption tracked with meaning (coverage vs. adoption, trends, at-risk teams); an active feedback loop demonstrably shapes the backlog; product and system roadmaps know about each other; inspection runs on a cadence.

## Turning off the light

- AI is a genuinely new tool for this station: plug it into the **product landscape** — repos, backlogs, roadmaps, support threads — and have it surface how teams actually use (and work around) the system: the eyes-in-the-sky view that was never practical manually. Let AI ooze into the cracks between system and product and act as mortar.
- Turn that intel into a **feedback report** that reshapes the system backlog — and flows back out: on-system suggestions in product-team terms, migration nudges, "you hand-rolled X; the system has it" notes.
- Start embarrassingly simple: a dependency-version scan across consumer repos this week beats an analytics platform next year.
- Announce deprecations and migrations like you mean it, and put this inspection on the calendar — quarterly deep pass, everyday checks in CI.
- Related deep tools: Design System Ops `adoption-report`, `drift-detection`, `stakeholder-brief`.

## Station record

```markdown
### Station 8 — Feedback & adoption: <RED|YELLOW|GREEN> (<n>/10)
- Measured: <repos scanned, analytics reviewed, teams interviewed>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <finding + evidence; separate coverage vs. adoption>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
