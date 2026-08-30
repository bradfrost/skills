# Brad Frost Skills

These agent skills by [Brad Frost](https://bradfrost.com/) have mostly emerged from creating our [online courses](https://bradfrost.com/courses/):
- [AI & Design Systems](https://aianddesign.systems/)
- [Subatomic: The Complete Guide To Design Tokens](https://designtokenscourse.com/)
- [Atomic Design Certification Course](https://atomicdesigncourse.com/)

But the goal is to provide skills to help you in many dimensions of work and life. This will continue to be an organic and iterative adventure, and I hope you find them useful.

## Install

Works with Claude Code, Codex, Cursor, Gemini CLI, and other agents.

### 1. Add the skills

Run this in your terminal:

```bash
npx skills add bradfrost/skills -g
```

The [skills CLI](https://github.com/vercel-labs/skills) will ask you which skills you want and which agents to install them on, then put them where each agent looks for them. The `-g` makes them available in every project — drop it to install into just the one you're in.

### 2. Run `/setup-brad-frost-skills`

In your agent, run it once:

```
/setup-brad-frost-skills
```

Installing the skills doesn't do anything on its own — this is the step that sets them up. It finds which ones you installed and runs the setup they need. For the limits skills that's a short interview (6 questions, about 5 minutes) that wires your answers into whatever your tools can actually enforce.

### 3. That's it!

If you set limits, they're live now. Say **"limits report"** any time to see how you're doing, or **"adjust my limits"** to change them.

The inspection skills need no setup at all — run `/ds-inspection`, `/product-inspection`, or `/ds-adoption-plan` from inside the project you want inspected.

> **Already have your own way of installing skills?** Use it. Skills are plain folders with a `SKILL.md` inside — however they get into your agent's skills directory, symlinks and all, they'll work. Just keep the folder names as-is, because the folder name becomes the command. You'll still want step 2.

## Available skills

**Start here**

| Skill | What it does |
|---|---|
| [`setup-brad-frost-skills`](skills/setup-brad-frost-skills/SKILL.md) | Sets up whichever of these skills you installed. Run it once. |

**Mental health**

| Skill | What it does |
|---|---|
| [`limits-setup`](skills/mental-health/limits-setup/SKILL.md) | The interview that establishes your limits and wires them up |
| [`limits-sessions`](skills/mental-health/limits-sessions/SKILL.md) | Caps how many AI sessions you can start in a day |
| [`limits-quiet-hours`](skills/mental-health/limits-quiet-hours/SKILL.md) | Sets hours where AI tools are off-limits |
| [`limits-endings`](skills/mental-health/limits-endings/SKILL.md) | Ends sessions definitively, with no dangling next steps |
| [`limits-energy`](skills/mental-health/limits-energy/SKILL.md) | Shows you the environmental cost of your AI usage |

**Design & development**

| Skill | What it does |
|---|---|
| [`ds-inspection`](skills/design-systems/ds-inspection/SKILL.md) | Puts your design system through a 10-station inspection |
| [`ds-adoption-plan`](skills/design-systems/ds-adoption-plan/SKILL.md) | Plans a product's move onto your design system |
| [`product-inspection`](skills/product-design/product-inspection/SKILL.md) | Inspects a shipping product the way real users meet it |

## Skill details

### Set healthy limits for AI use

AI companies are incentivized to keep you using AI, so the user experience is designed to keep you prompting. AI sessions always dangle next steps (e.g. "want me to tackle this next?") in front of you to keep you prompting, to the detriment of your [mental health](https://www.youtube.com/watch?v=iPUn1Fnfn0k) and the [environment](https://news.un.org/en/story/2026/06/1167658).

"Just exercise more self discipline" is bullshit, especially when there's increasing pressure to rely on AI to work. That's why **this first family of AI skills helps you use AI on your own terms and set healthy limits to your AI use.**

Here's how it works:
1. Install the skills (see [Install](#install) above)
2. Run **`/setup-brad-frost-skills`**, then answer a few questions to determine your own terms of engagement and define your own limits for AI usage.
3. AI will honor your stated limits as far as is technically possible, and where it technically can't, this kit documents the gap loudly instead of papering over it with willpower.

> **It's important to say this cannot completely stop you from using AI, but it can provide a healthier user experience and boundaries for working with AI.**

What you get after the interview:

- **Quiet hours** — the hours you've declared off-limits. In Claude Code, prompting during them gets refused; in Chat & Cowork you get reminded.
- **A daily session limit** — start with a week of just counting, then set a number you're comfortable with. Past it, new sessions are refused.
- **Definitive endings** — the task that started the session is the task that ends it, and anything new gets filed instead of dangled in front of you.
- **Energy estimates** — a one-line estimate at the end of your sessions, with an optional weekly budget once you've seen what your usage actually looks like.
- **Friction where it counts** — tightening a limit is easy. Loosening one takes a reason, a typed phrase, and a new session. That's the whole point.

Every limit is labeled with what it honestly is on each surface — **enforced**, **advisory**, or **nothing**. That's the [enforcement matrix](skills/mental-health/limits-setup/ENFORCEMENT.md), and it's the loudest document in this repo on purpose. Per-surface wiring (including Cowork and claude.ai chat) is in [SURFACES.md](skills/mental-health/limits-setup/SURFACES.md).

### Inspect your design system and products

These skills walk your design system — and the products built with it — through a multi-point inspection, as detailed in [AI & Design Systems](https://aianddesign.systems/), the course by Brad Frost, Ian Frost, and TJ Pitre. They're designed to run in sequence: inspect the system, inspect what got shipped on top of it, then plan the rebuild.

- **[`ds-inspection`](skills/design-systems/ds-inspection/SKILL.md)** puts your *design system* on the lift: a 10-station inspection producing a graded report and a prioritized work order.
- **[`product-inspection`](skills/product-design/product-inspection/SKILL.md)** inspects a *product* as real users meet it — 10 stations covering adoption, usability, accessibility, performance, and more.
- **[`ds-adoption-plan`](skills/design-systems/ds-adoption-plan/SKILL.md)** hands back the restoration estimate: it tears down a product's bespoke UI, maps every custom pattern to its design-system replacement, and gives you a phased build schedule.

More to come!

- Brad
