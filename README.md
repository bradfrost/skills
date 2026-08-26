# Brad Frost Skills

[Brad Frost](https://bradfrost.com/)'s agent skills are installable, self-contained instructions for AI
agents, spanning different dimensions of work and life. Inspired by [mattpocock/skills](https://github.com/mattpocock/skills).

## Limit your use of AI

AI companies are incentivized to keep you using AI, so the user experience is designed to keep you prompting. AI sessions always dangle next steps (e.g. "want me to tackle this next?") in front of you to keep you prompting, to the detriment of your [mental health](https://www.youtube.com/watch?v=iPUn1Fnfn0k) and the [environment](https://news.un.org/en/story/2026/06/1167658). 

"Just exercise more self discipline" is bullshit, especially when there's increasing pressure to rely on AI to work. That's why **this first family of AI skills helps you use AI on your own terms and set healthy limits to your AI use.** 

Here's how it works:
1. Install the skill
2. Answer a few questions to determine your own terms of engagement and define your own limits for AI usage.
3. AI will honor the your stated limits as far as is technically possible, and where it technically can't, this kit documents the gap loudly instead of papering over it with willpower.

> **It's important to say this cannot completely stop you from using AI, but it can provide a healthier user experience and > boundaries for working with AI.**

| Skill | What it does |
|---|---|
| [`limits-setup`](skills/mental-health/limits-setup/SKILL.md) | A short interview that establishes *your* limits — quiet hours, a sessions-per-day ceiling, how sessions end — then wires them into what your tools can actually enforce |
| [`limits-sessions`](skills/mental-health/limits-sessions/SKILL.md) | The sessions-per-day ceiling: honest counting, terse identical refusals past the limit, raises that cost a typed phrase and a logged reason |
| [`limits-quiet-hours`](skills/mental-health/limits-quiet-hours/SKILL.md) | Hours where AI tools are off-limits — enforced as refused tool calls where hooks exist, with a deliberate logged override |
| [`limits-endings`](skills/mental-health/limits-endings/SKILL.md) | Sessions end definitively: land it or park it, no trailing hooks, close with a Signal Flags block |

Every limit is labeled with what it honestly is on each surface —
**enforced**, **advisory**, or **nothing**. That's the
[enforcement matrix](skills/mental-health/limits-setup/ENFORCEMENT.md), and
it's the loudest document in this repo on purpose. Per-surface wiring
(including Cowork and claude.ai chat) is in
[SURFACES.md](skills/mental-health/limits-setup/SURFACES.md).

Fast-follow: `limits-energy` — making the environmental cost of usage
visible, with cited figures and honest error bars.

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

Then say **"set my limits"** to run the setup interview. It will walk you through one
question at a time, suggesting some sensible defaults that you can adopt or change based on your preferences and needs.

## Planned categories

- **design-systems** — design system inspection and health-check skills
- **product-design** — product analysis and inspection skills

More to come!

- Brad
