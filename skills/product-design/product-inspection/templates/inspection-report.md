# Multi-Point Inspection Report — <Product Name>

_Inspected: <date> · Technician: <agent + model> · Previous inspection: <date or "first inspection">_
_Vehicle profile: `product-inspection/GARAGE.md` (checked in <date>)_

## The short version

<Three to five plain-language sentences: overall condition, the most load-bearing problems, and the single most important thing to do next. Write it for a teammate who reads nothing else.>

**Overall: <n>/100** — a conversation starter, not a grade. Fix the reds, schedule the yellows, re-run on a cadence.
<If any station is N/I: "Score is /<max> pro-rata — <n> station(s) not inspected for lack of evidence access (usually a running instance).">

## Inspection sheet

<!-- Agent formatting rules — these are what make the sheet scannable:
     1. PAD every cell with spaces so all pipes line up vertically. This report
        is read as plain text in terminals and editors at least as often as
        it's rendered; an unaligned table is unreadable there.
     2. Keep the alignment markers exactly as below (right-align #, center
        Light, right-align Score).
     3. One row per station, in order, then the Overall row, then the Lights
        tally. No extra columns.
     4. The lights and scores below are EXAMPLE values demonstrating the target
        formatting — replace all of them with this inspection's real results.
        For a not-inspected station, put N/I in both Light and Score. -->

|  # | Station                       | Quality    | Light |      Score |
|---:|:------------------------------|:-----------|:-----:|-----------:|
|  1 | Design system adoption        | Adopted    |  🟡   |       6/10 |
|  2 | Best practices                | Sound      |  🟡   |       6/10 |
|  3 | Accessibility                 | Accessible |  🟡   |       6/10 |
|  4 | Content & IA                  | Clear      |  🟢   |       8/10 |
|  5 | Usability                     | Usable     |  🟢   |       8/10 |
|  6 | Visual design                 | Refined    |  🟡   |       7/10 |
|  7 | Performance                   | Fast       |  🟡   |       7/10 |
|  8 | Security & privacy            | Secure     |  🔴   |       3/10 |
|  9 | Testing & validation          | Validated  |  🟡   |       5/10 |
| 10 | Measurement & feedback        | Measured   |  🟡   |       5/10 |
|    | **Overall**                   |            |       | **56/100** |

**Lights:** 🟢 <n> green · 🟡 <n> yellow · 🔴 <n> red · <n> not inspected

**Key:** 🔴 Red (0–3) — broken or missing; the light is ON · 🟡 Yellow (4–7) — drift or gaps; schedule a fix · 🟢 Green (8–10) — healthy, no action needed · **N/I** — not inspected (no evidence access; never guessed)

## Evidence basis

- Access used this pass: <running instance / code / exports / screenshots / interview, per asset>
- Findings tagged `[verified]`: <n> · `[reported]`: <n>
- <If reported-heavy: "Large share of findings are [reported] — getting the agent a running instance (see work order) will make the next inspection sharper.">

## Station records

<Append each station's completed Station Record block here, in order.>

## What changed since last inspection

<Re-inspections only: score movement per station, lights turned off, new lights, work-order items completed/still open. Delete for first inspections.>

## Next service

- Work order: `product-inspection/work-orders/<date>-work-order.md`
- Recommended cadence: deep inspection <each release / quarterly>; everyday checks to wire into CI: <a11y, performance, adoption lint, dependency audit>
- Re-inspect by: <date>
