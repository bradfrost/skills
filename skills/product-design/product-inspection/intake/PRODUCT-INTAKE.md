# Product Intake — Check the Vehicle In

Before any inspection, check the vehicle in. This step builds `product-inspection/GARAGE.md`: a profile of the product and a map of what evidence the agent can actually reach. Every station reads this file first — good intake is what makes the inspection specific instead of generic.

**Agent:** work through the sections below conversationally — a few questions at a time, not a wall of forms. Wherever you have live access (the running product, the repo, a docs URL), *discover* the answer yourself and confirm it instead of asking. Aim for 10–15 minutes, not an interrogation. Then write `GARAGE.md` using the template at the bottom and read it back for confirmation.

**First question, before anything else — get the product running in front of you.** A product inspection is worthless if it's about the product as *described* or as *coded* instead of as *shipped*. Open with: *"Is there a URL where this product is running — production or staging — or can I launch it locally? What does it take to get it up?"* Then check your own available tools for a browser bridge (in-app browser tools, Claude-in-Chrome, or similar) and actually load the product to confirm you can see and drive the real thing. Record the outcome either way. Skipping this is the #1 intake failure: six of the ten stations can only produce `[verified]` findings against a running instance, and if you find out at the end that you never had one, most of the report is `[reported]` guesswork.

## 1. The vehicle

- Product name, what it does, and who uses it (audience, rough scale)
- Team: who builds and owns it? How many people? Design/eng/product mix?
- Age & mileage: how old is the product? Any major rewrites or replatforms?
- Why now: what prompted this inspection? (Launch coming? Complaints? Redesign? AI-readiness push? Routine service?)
- Which design system does it build on, and which version? (This links the inspection to any `ds-inspection` run — note version drift.)

## 2. Intent & ideal (what is this product *supposed* to be?)

The inspection is sharper when it can measure the shipped product against the team's own stated ambition — not just generic quality bars. Ask like a mechanic taking down what the car is *for*: *"Say I've never seen this product — what's the one-pager? What does success look like? Is there anything written down — a pitch deck, a PRD, brand guidelines, north-star designs — I should read before I judge it?"*

- **The pitch:** what this product is supposed to be and do, in the team's own words (one or two sentences)
- **The core jobs:** the 2–5 things it exists to let people do — Station 7 scores against exactly these
- **The design ideal:** brand guidelines, design principles, reference products, or north-star mockups — Station 8 scores against these; "we want it to feel like X" counts
- **Success criteria:** stated goals or metrics ("launch by…", "cut support tickets", "every episode published in under an hour")
- **Sources:** collect links/paths to any decks, docs, or references offered — read what's reachable and cite it as evidence

If nothing written exists, record `none provided` honestly — the inspection then scores against general quality bars only, and "no stated ideal" is itself worth a line in the report (a team that hasn't named its ambition can't converge on it).

## 3. The assets

For each, capture *what exists* and *where it lives*:

- **Running instance** — production URL, staging URL, and/or local launch steps; does it need auth, seeded data, or services (DB, storage, workers) to run?
- **Codebase** — framework(s), repo location(s), how the design system is consumed (package, CDN, vendored)
- **Instrumentation** — analytics, error tracking, session tools, performance/real-user monitoring
- **Design source** — the intended design (Figma/spec) to compare as-shipped against, if any
- **Support & feedback** — where user complaints, tickets, reviews, and support requests land

## 4. Evidence access map (the critical part)

For each asset, establish what the agent can reach **right now**, and record it honestly:

| Asset | Access level to record |
|---|---|
| Running instance | `live` (loaded via a browser bridge / dev server — name it) / `screenshot` / `interview` |
| Codebase | `live` (repo open or reachable) / `export` (pasted files) / `interview` |
| Instrumentation | `live` (dashboard reachable) / `export` (pasted metrics) / `interview` |
| Design source | `live` (design-tool bridge) / `export` / `screenshot` / `interview` |
| Support & feedback | `live` (tracker/reviews reachable) / `export` / `interview` |

**Agent: test, don't assume.** If a browser bridge appears available, load the product and confirm you see the real thing. If repo access seems available, read one real file. If an analytics dashboard is reachable, pull one real view. Record what worked. If everything lands on `interview`, say so plainly: the inspection will run, findings will be `[reported]`, and the first work-order item should be getting the agent a running instance.

## 5. Known symptoms

Ask like a mechanic: *"What's it doing? When did it start?"*

- Where does the team already suspect the check engine light is coming from?
- Recent user complaints, drop-off points, or recurring support themes?
- Anything the team is proud of (probable greens — worth verifying and celebrating)?
- Any intentional deviations — from the design system or from convention — the inspection should respect?

## 6. Scope & frame

- What exactly is in scope — the whole product, or a specific flow/section?
- Which stations matter most right now? All 10, or a subset?
- Product-stage frame for scoring (prototype / early / mature / flagship)
- Anything explicitly out of scope this pass?

---

## GARAGE.md template

```markdown
# GARAGE.md — <Product Name>
_Checked in: <date> · Re-confirm at next inspection_

## Vehicle
- Product: <name>, does <what>, for <audience/scale>
- Team: <size, shape> · Owner: <who>
- Age: <how old, major rewrites>
- Reason for service: <why now>
- Design system: <name @ version in product> vs <latest>

## Intent & ideal
- The pitch: <what this product is supposed to be, in the team's words>
- Core jobs: <the 2–5 jobs it exists for — Station 7 scores these>
- Design ideal: <brand refs / principles / north-star designs — Station 8 scores against these, or "none provided">
- Success looks like: <stated goals/metrics, or "none provided">
- Sources: <links/paths to decks, PRDs, brand docs — or "none provided">

## Assets
- Running instance: <prod/staging URL or local launch steps; auth/data/services needed>
- Codebase: <framework, repo, how the design system is consumed>
- Instrumentation: <analytics / error tracking / RUM / none>
- Design source: <Figma/spec to compare against, or none>
- Support & feedback: <where complaints/tickets/reviews land>

## Evidence access map
| Asset | Access | Verified how |
|---|---|---|
| Running instance | live / screenshot / interview | <e.g. "loaded staging URL in the browser bridge"> |
| Codebase | live / export / interview | <e.g. "read src/pages/checkout.vue"> |
| Instrumentation | live / export / interview | <…> |
| Design source | live / export / screenshot / interview | <…> |
| Support & feedback | live / export / interview | <…> |

## Known symptoms
- <suspected reds/yellows, complaints, drop-off, support themes>

## Probable greens
- <what the team believes is healthy>

## Intentional deviations
- <deliberate, documented departures the inspection should respect>

## Scope & frame
- In scope: <whole product / specific flows> · Stations this pass: <all / subset>
- Scoring frame: <prototype / early / mature / flagship>
- Out of scope: <…>
```
