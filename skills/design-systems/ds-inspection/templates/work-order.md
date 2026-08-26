# Work Order — <System Name>

_From inspection: `reports/<date>-inspection.md` · Written: <date>_

Reds get fixed now. Yellows get scheduled. Greens get left alone (and celebrated). Every item cites its station and evidence — no vibes-based work items. The team owns prioritization; this is the technician's recommendation.

## 🔴 Fix now (reds)

<One block per red-station finding, ordered by leverage — the fix that unblocks the most other fixes goes first.>

### <n>. <Title in plain language>
- **Station:** <#, name> · **Evidence:** <[verified|reported] one-line citation>
- **Why it's first:** <what this blocks or breaks downstream>
- **First move:** <the concrete opening step, from the station's "Turning off the light">
- **AI assist:** <what to have the agent do vs. what needs human judgment>
- **Done when:** <observable condition — what re-inspection will check>
- **Effort:** S / M / L

## 🟡 Schedule (yellows)

### <n>. <Title>
- **Station:** <…> · **Evidence:** <…>
- **First move:** <…> · **Done when:** <…> · **Effort:** S / M / L
- **Suggested timing:** <this sprint / this quarter / before next inspection>

## 🔧 Access upgrades (sharper next inspection)

<Evidence-access gaps from GARAGE.md worth closing — e.g. "connect a design-tool bridge so Stations 1/2/6 stop relying on [reported] answers," "grant docs-site access." Cheap items, big diagnostic payoff.>

## 🟢 Keeping the greens green

<For each green station: the one habit or check that keeps it that way (usually a CI wiring or cadence item, not a project).>

## Cadence

- Re-inspect (deep, all stations): <date>
- Everyday checks to wire into CI now: <stations/checks>
- Owner of this work order: <person> · Review: <ritual/meeting where this gets triaged>
