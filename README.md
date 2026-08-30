# [Brad Frost](https://bradfrost.com) Skills

These agent skills are aimed to help you in different dimensions of work and life. Right now, these skills have mostly emerged from creating our [online courses](https://bradfrost.com/courses/):
- [AI & Design Systems](https://aianddesign.systems/)
- [Subatomic: The Complete Guide To Design Tokens](https://designtokenscourse.com/)
- [Atomic Design Certification Course](https://atomicdesigncourse.com/)

This will continue to be an organic and iterative adventure, so if you have feedback, thoughts, or ideas, feel free to [get in touch](https://bradfrost.com/contact/).

## Install
Follow this process to install Brad Frost skills:

### 1. Add the skills

Run this in your terminal:

```bash
npx skills add bradfrost/skills -g
```

The [skills CLI](https://github.com/vercel-labs/skills) will ask you which skills you want and which agents to install them on, then put them where each agent looks for them. The `-g` makes them available in every project — drop it to install into just the one you're in. The goal is for them to work with Claude Code, Codex, Cursor, Gemini CLI, and other agents, but Claude is the best-tested avenue here.

### 2. Run the setup

Once the skills are installed, in a new agent session, run:

```
/setup-brad-frost-skills
```

This finds which skills you installed and runs the setup they need. For the limits skills, that's a short (6 questions, 5 minutes) interview to [set healthy limits with AI](#set-healthy-limits-for-ai-use), which then wires your answers into whatever your tools can actually enforce. (Saying "set my limits" jumps straight to that interview.)

### 3. Use the skills

Once you're set up, you can say **"limits report"** any time to see how you're doing, or **"adjust my limits"** to change them.

Design system and product design skills can be called by name (`/ds-inspection`, `/product-inspection`, `/ds-adoption-plan`) from inside the project you want inspected.

> **You can use your own process to install these skills**. Skills are plain folders with a `SKILL.md` inside; you can manually add them to your agent's skills directory. Please keep the folder names as-is, because the folder name becomes the command. Either way, you'll still want to run step 2.

## Available skills

**Start here**

| Skill | What it does |
|---|---|
| [`setup-brad-frost-skills`](skills/setup-brad-frost-skills/SKILL.md) | Sets up whichever of these skills you installed. Run it once. |

**Mental health**

| Skill | What it does |
|---|---|
| [`limits-setup`](skills/mental-health/limits-setup/SKILL.md) | A brief interview to set and wire up your AI limits |
| [`limits-sessions`](skills/mental-health/limits-sessions/SKILL.md) | Caps how many AI sessions you can start in a day |
| [`limits-quiet-hours`](skills/mental-health/limits-quiet-hours/SKILL.md) | Sets hours where AI tools are off-limits |
| [`limits-endings`](skills/mental-health/limits-endings/SKILL.md) | Ends sessions definitively, with no dangling next steps |
| [`limits-energy`](skills/mental-health/limits-energy/SKILL.md) | Shows you the environmental cost of your AI usage |

**Design & development**

| Skill | What it does |
|---|---|
| [`ds-inspection`](skills/design-systems/ds-inspection/SKILL.md) | Runs your design system through the 10-station inspection, detailed in Chapter 3 of our [AI & Design Systems course](https://aianddesign.systems) |
| [`product-inspection`](skills/product-design/product-inspection/SKILL.md) | Runs your product through a multi-point health inspection, detailed in Chapter 4 of [AI & Design Systems](https://aianddesign.systems/) |
| [`ds-adoption-plan`](skills/design-systems/ds-adoption-plan/SKILL.md) | Establishes a plan to migrate your product's existing UI over to your design system, detailed in Chapter 4 of [AI & Design Systems](https://aianddesign.systems/) |

---

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
These skills are practical accompaniments to detailed video lessons covered in [AI & Design Systems](https://aianddesign.systems/) by me, Ian Frost, and [TJ Pitre](https://github.com/southleft/). Learn how to use AI & Design Systems together to help your team make better digital products:
<a href="https://aianddesign.systems/" target="_blank"><img width="3217" height="1800" alt="card" src="https://github.com/user-attachments/assets/4bccb599-a4bc-4563-bebd-5e6fe7ec9fae" /></a>

The following skills are 

- **[`ds-inspection`](skills/design-systems/ds-inspection/SKILL.md)** puts your *design system* through a 10-station inspection and produces a graded report and a prioritized work order. 
- **[`product-inspection`](skills/product-design/product-inspection/SKILL.md)** inspects a *product* 10 stations covering design system adoption, usability, accessibility, performance, and more. 
- **[`ds-adoption-plan`](skills/design-systems/ds-adoption-plan/SKILL.md)** analyzes a product to find bespoke user interface components, maps those components to design system equivalents, and then constructs a prioritized strategy to implement the design system adoption. 

**Detailed tutorials, workflows, concepts and lessons for this skill are is covered in Chapters 3 and 4 of the [AI & Design Systems](https://aianddesign.systems/) course.**

## A living project
I'll continue adding and iterative over skills with the goal to provide you useful skills to help people in many dimensions of work and life. If you have feedback, thoughts, or ideas, feel free to [get in touch](https://bradfrost.com/contact/). If you'd like to support this work, please consider checking out [our online courses](https://bradfrost.com/courses/), and if you want to follow along you can subscribe to [my newsletter](https://bradfrost.com/newsletter/).

Thanks so much!
- Brad
