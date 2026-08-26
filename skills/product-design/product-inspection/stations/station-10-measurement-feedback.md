---
station: 10
name: Measurement & feedback
quality: Measured (quality 10 of 10)
question: Can the team see how the product performs in the wild — errors, usage, drop-off, feedback — and does that signal feed back into the backlog and up into the design system?
---

# Station 10 — Measurement & feedback

**Quality: Measured.** A product that ships without instrumentation is a car with no dashboard — you can't tell it's overheating until it dies on the shoulder. This final station checks whether the team can *observe* the running product — errors captured, meaningful usage tracked, drop-off visible, a path for user feedback — **and whether that signal actually goes somewhere**: into the product's own backlog, and *up* into the higher systems the product depends on. When real-world usage reveals a component gap or a token that doesn't hold, that's not just a local bug — it's feedback the **design system** needs (the mirror image of `ds-inspection`'s *Feedback & adoption* station, which asks the same question from the system side). Measurement without a loop is just a dashboard nobody reads; this station grades the whole loop, from captured signal to the system that acts on it.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Error monitoring | Repo/config: Sentry/Rollbar/etc. wired; live errors reaching it | Dashboard access · interview |
| Analytics | Repo/config: analytics present; events beyond pageviews | Dashboard · interview |
| Key-flow tracking | Are the core jobs (Station 5) instrumented as funnels? | Interview |
| Performance monitoring | Real-user monitoring / web-vitals reporting in place | Interview |
| Feedback channels | In-product feedback, support path, review monitoring | Live instance · interview |
| Loop-closing (backlog) | Does captured signal actually reach the team's backlog? | Interview |
| Loop-closing (upstream) | Do product findings feed *up* into the design system / shared platform? | Interview · cross-ref `ds-inspection` |

## Inspection procedure

1. **Check for error monitoring.** Is a service wired (Sentry/Rollbar/etc.)? Are unhandled errors and promise rejections captured with enough context (user action, release, stack) to act on? If possible, trigger a test error and confirm it lands.
2. **Check analytics depth.** Is anything tracked beyond raw pageviews? Are *meaningful events* — the core actions from Station 5 — instrumented, so the team can answer "how many people actually complete the primary job?"
3. **Check funnel visibility.** For each core job, can the team see where users drop off? Without this, Station 5 findings can never be confirmed by real data.
4. **Check performance monitoring.** Is there real-user monitoring (web vitals from the field), or only occasional lab tests? Field data is what catches the regression Station 7 can't predict.
5. **Check feedback channels.** Is there an in-product way for users to report problems or request things? A support path? Is anyone watching app-store/marketplace reviews if relevant?
6. **Check the loop closes — both directions.** Captured errors and feedback are only worth the wiring if they *go somewhere*. **Down into the backlog:** is there a route from "signal captured" to "issue triaged," or does it pile up unseen? **Up into the higher system:** when field signal reveals a component gap, a token that doesn't hold, or a pattern that keeps breaking, does that finding reach the **design system** (or shared platform) that could fix it once for everyone — or does each product re-discover it alone? This is the product side of the tandem: `ds-inspection` asks whether product context feeds *into* the system; this asks whether the product is *sending* it.

## Warning lights

- No error monitoring — failures in production are invisible until a user complains
- Analytics limited to pageviews; core actions uninstrumented
- No funnel visibility — the team can't see where users drop off
- Only lab performance checks; no field/real-user data
- No feedback channel, or feedback captured but never routed anywhere
- Signal collected but not connected to the backlog — a dashboard nobody reads
- Field findings that implicate the design system never make it upstream — every product re-discovers the same gap alone

## Scoring anchors

- **Red (0–3):** The product is flying blind — no error capture, no meaningful analytics, no feedback path. Problems are invisible until they escalate.
- **Yellow (4–7):** Partial visibility — errors captured but usage thin, or analytics present but core flows uninstrumented, or signal captured but not routed to the backlog.
- **Green (8–10):** The team can honestly say: *"We can see errors, usage of core flows, drop-off, and real-user performance in production; users have a way to tell us things; that signal reaches our backlog; and when it implicates the design system, it feeds back upstream."*

## Turning off the light

- Error monitoring is the highest-leverage, lowest-effort add — a single SDK wire-up turns production from invisible to observable; do it first.
- Instrument the core jobs from Station 5 as events/funnels — that's what lets future inspections check claims against real behavior instead of interview.
- Add a lightweight in-product feedback path and, critically, a ritual that routes what it captures into triage — instrumentation without a loop is just noise.
- Establish the upstream channel too: a standing way for product findings that implicate the design system to reach it (an issue label, a shared triage, the dual-filing pattern) so the loop closes all the way up, not just locally.

## Station record

```markdown
### Station 10 — Measurement & feedback: <RED|YELLOW|GREEN> (<n>/10)
- Error monitoring: <tool/none> · Analytics depth: <pageviews/events/funnels> · RUM: <yes/no> · Feedback path: <what> · Loop-closing: <backlog? upstream to DS?>
- Evidence level: <live / dashboard / code / interview, per check>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
