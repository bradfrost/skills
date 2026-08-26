# Skills

Brad Frost's agent skills — installable, self-contained instructions for AI
agents, spanning many dimensions of work and life.

Modeled on [mattpocock/skills](https://github.com/mattpocock/skills).

## The limits kit

The first family of skills here helps you set your own terms of engagement
with AI — and it makes you one promise, kept small on purpose:

> **It cannot stop you. It can make stopping the default and drifting
> deliberate.**

AI tools ship with affordances that keep you prompting — trailing "want me
to also…?" hooks, endless sessions, a fresh allowance every time you open a
new window. The standard advice ("use Screen Time, put the laptop away") is
the manufacturer telling you to hide your own cigarettes. The power is in
the tool, so the tool should honor your stated limits as far as is
technically possible — and where it technically can't, this kit documents
the gap loudly instead of papering over it with willpower.

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

Then say **"set my limits"** to run the setup interview. Ten minutes, one
question at a time, sensible defaults you can accept or change. Your
numbers, not mine.

## Planned categories

- **design-systems** — design system inspection and health-check skills
- **product-design** — product analysis and inspection skills

More to come.
