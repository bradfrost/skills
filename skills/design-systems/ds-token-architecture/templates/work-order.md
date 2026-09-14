# Work Order — <System Name>

_From: `reports/<date>-report.md` · Written: <date>_

Reds get fixed now. Yellows get scheduled. Greens get left alone. Every item
cites its check and its evidence; there are no vibes-based work items. The
team owns the order; this is the recommendation.

## 🔴 Fix now

<One block per red finding, the fix that unblocks the most other fixes
first. A missing tier 2 for a category almost always
goes first, because nothing downstream can be wired until it exists.>

### <n>. <Title in plain language>
- **Check:** <#, name> · **Evidence:** <[verified|reported] one-line citation with file and count>
- **Why it's first:** <what this blocks downstream>
- **First move:** <the concrete opening step, from the check's "Fixing it">
- **AI assist:** <what an agent can do mechanically vs. what needs a human decision>
- **Done when:** <observable condition a re-check will look for>
- **Effort:** S / M / L

## 🟡 Schedule

### <n>. <Title>
- **Check:** <…> · **Evidence:** <…>
- **First move:** <…> · **Done when:** <…> · **Effort:** S / M / L
- **Suggested timing:** <before the next theme / this quarter / before publishing 1.0>

## 🔧 Better evidence next time

<Access gaps from PROFILE.md worth closing: "connect a Figma bridge so the
design-side findings stop being [reported]," "point the agent at one product
so check 8 can run." Cheap items, big payoff.>

## 🟢 Keeping the greens green

<For each green check: the one habit that keeps it that way. Usually a CI
check, a lint rule, or a review ritual, not a project.>

## No guidance in the architecture

<Things the system does that the architecture has no opinion on (an opacity
scale, layout tokens, a data-viz palette structure). Described, not graded.
The team decides whether they're fine.>

## Cadence

- Re-check (all nine): <date>
- Wire into CI now: <checks>
- Owner of this work order: <person> · Reviewed in: <ritual>
