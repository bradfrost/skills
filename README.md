# Brad Frost Skills

[Brad Frost](https://bradfrost.com/)'s agent skills are installable, self-contained instructions for AI
agents, spanning different dimensions of work and life. Inspired by [mattpocock/skills](https://github.com/mattpocock/skills).

## What's inside

- **Mental health**
  - [`limits-setup`](skills/mental-health/limits-setup/SKILL.md)
  - [`limits-sessions`](skills/mental-health/limits-sessions/SKILL.md)
  - [`limits-quiet-hours`](skills/mental-health/limits-quiet-hours/SKILL.md)
  - [`limits-endings`](skills/mental-health/limits-endings/SKILL.md)
  - [`limits-energy`](skills/mental-health/limits-energy/SKILL.md)
- **Design systems**
  - [`ds-inspection`](skills/design-systems/ds-inspection/SKILL.md)
  - [`ds-adoption-plan`](skills/design-systems/ds-adoption-plan/SKILL.md)
- **Product design**
  - [`product-inspection`](skills/product-design/product-inspection/SKILL.md)

## Limit your use of AI

AI companies are incentivized to keep you using AI, so the user experience is designed to keep you prompting. AI sessions always dangle next steps (e.g. "want me to tackle this next?") in front of you to keep you prompting, to the detriment of your [mental health](https://www.youtube.com/watch?v=iPUn1Fnfn0k) and the [environment](https://news.un.org/en/story/2026/06/1167658). 

"Just exercise more self discipline" is bullshit, especially when there's increasing pressure to rely on AI to work. That's why **this first family of AI skills helps you use AI on your own terms and set healthy limits to your AI use.** 

Here's how it works:
1. Install the skill (see [Install](#install) below)
2. Say **"set my limits"** to your AI agent, then answer a few questions to determine your own terms of engagement and define your own limits for AI usage.
3. AI will honor the your stated limits as far as is technically possible, and where it technically can't, this kit documents the gap loudly instead of papering over it with willpower.

> **It's important to say this cannot completely stop you from using AI, but it can provide a healthier user experience and boundaries for working with AI.**

| Skill | What it does |
|---|---|
| [`limits-setup`](skills/mental-health/limits-setup/SKILL.md) | A short interview that establishes *your* limits — quiet hours, a sessions-per-day ceiling, how sessions end — then wires them into what your tools can actually enforce |
| [`limits-sessions`](skills/mental-health/limits-sessions/SKILL.md) | The sessions-per-day ceiling: honest counting, terse identical refusals past the limit, raises that cost a typed phrase and a logged reason |
| [`limits-quiet-hours`](skills/mental-health/limits-quiet-hours/SKILL.md) | Hours where AI tools are off-limits — enforced as refused tool calls where hooks exist, with a deliberate logged override |
| [`limits-endings`](skills/mental-health/limits-endings/SKILL.md) | Sessions end definitively: land it or park it, no trailing hooks, close with a Signal Flags block |
| [`limits-energy`](skills/mental-health/limits-energy/SKILL.md) | Makes the environmental cost visible: floor estimates from published per-prompt figures, rendered as lightbulb time, with an optional weekly energy budget that informs but never blocks |

Every limit is labeled with what it honestly is on each surface —
**enforced**, **advisory**, or **nothing**. That's the
[enforcement matrix](skills/mental-health/limits-setup/ENFORCEMENT.md), and
it's the loudest document in this repo on purpose. Per-surface wiring
(including Cowork and claude.ai chat) is in
[SURFACES.md](skills/mental-health/limits-setup/SURFACES.md).

## Install

Using the [skills CLI](https://github.com/vercel-labs/skills), which
detects which agents you use and installs where each one looks:

```bash
npx skills add bradfrost/skills
```

While this repo is private, that command works for collaborators whose
git/GitHub CLI auth can already reach it. (Manual fallback: clone the repo
and copy `skills/mental-health/<skill>/` into your agent's skills
directory, e.g. `~/.claude/skills/<skill>/`.)

**Then, the step the installer won't tell you about:** open your agent and
say **"set my limits"** (in Claude Code, `/limits-setup` also works). That
runs the setup interview — one question at a time, with sensible defaults
you can adopt or change based on your preferences and needs. Installing
the skills does nothing on its own; the interview is where your limits get
set and wired up.

## Inspect your design system and products

These skills walk your design system — and the products built with it —
through a multi-point inspection, as detailed in
[AI & Design Systems](https://aianddesign.systems/), the course by Brad
Frost, Ian Frost, and TJ Pitre. They're designed to run in sequence:
inspect the system, inspect what got shipped on top of it, then plan the
rebuild.

| Skill | What it does |
|---|---|
| [`ds-inspection`](skills/design-systems/ds-inspection/SKILL.md) | Puts your *design system* on the lift: a 10-station inspection producing a graded report and a prioritized work order |
| [`ds-adoption-plan`](skills/design-systems/ds-adoption-plan/SKILL.md) | The restoration estimate: tears down a product's bespoke UI, maps every custom pattern to its design-system replacement, and hands back a phased build schedule |
| [`product-inspection`](skills/product-design/product-inspection/SKILL.md) | Inspects a *product* as real users meet it — 10 stations covering adoption, usability, accessibility, performance, and more |

More to come!

- Brad
