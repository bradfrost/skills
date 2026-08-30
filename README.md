# [Brad Frost](https://bradfrost.com) Skills

These agent skills are aimed to help you in different dimensions of work and life. Right now, these skills have mostly emerged from creating our [online courses](https://bradfrost.com/courses/):
- [AI & Design Systems](https://aianddesign.systems/)
- [Subatomic: The Complete Guide To Design Tokens](https://designtokenscourse.com/)
- [Atomic Design Certification Course](https://atomicdesigncourse.com/)

My plan is to add to these skills over time, so feel free to subscribe to my [website](https://bradfrost.com/feed/feed.xml) & [newsletter](https://bradfrost.com/newsletter/) for updates. And if you have feedback or ideas for additional skills, I'd love to hear from you; Feel free to [get in touch](https://bradfrost.com/contact/)!

## Install
Follow this process to install Brad Frost skills:

### 1. Add the skills

Run this in your terminal to install these skills everywhere (recommended):

```bash
npx skills add bradfrost/skills -g
```
You can also drop the `-g` to install only in the project you're currently in.

The [skills CLI](https://github.com/vercel-labs/skills) will ask you which skills you want and which agents to install them on, then put them where each agent looks for them. The goal is for them to work with Claude Code, Codex, Cursor, Gemini CLI, and other agents, but Claude is the best-tested avenue here.

### 2. Run the setup

Once the skills are installed, in a new agent session, run:

```
/setup-brad-frost-skills
```

This finds which skills you installed and runs any required setup. For the limits skills, you'll take a short (6 questions, 5 minutes) interview to [set healthy limits with AI](#set-healthy-limits-for-ai-use), which then wires your answers into whatever your tools can actually enforce. (Alternatively, saying "set my limits" will jump you straight into that interview.)

### 3. Use the skills
With the skills set up, you're good to go! You'll see your preferred AI limits in action, and you can call any of these skills by name in AI sessions.

> **Note: you can use your own process to install these skills**. Skills are plain folders with a `SKILL.md` inside; you can manually add them to your agent's skills directory. Please keep the folder names as-is, because the folder name becomes the command. Either way, you'll still want to run step 2.

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

Every limit is labeled with what it honestly is on each surface — **enforced**, **advisory**, or **nothing**. That's the [enforcement matrix](skills/mental-health/limits-setup/ENFORCEMENT.md), and it's the loudest document in this repo on purpose. Per-surface wiring (including Cowork and claude.ai chat) is in [SURFACES.md](skills/mental-health/limits-setup/SURFACES.md).


Here's each skill, and what you can expect from it.

#### [`limits-setup`](skills/mental-health/limits-setup/SKILL.md) — the interview

This is the one that asks the questions and wires everything up. Six questions, about five minutes, and every one has a default you can accept or change. It opens like this:

> Answer 6 quick questions to establish healthy limits with AI. For each question, you can choose the suggested default or tweak to your preferences. Let's go!

It starts by asking *why* you're doing this — mental health, sleep, clarity, the environment, or something in your own words — and your answer gets quoted at the top of everything it writes, so your limits always say why they exist.

**What you'll end up with:** a config file your agent reads, and a plain-language contract at `~/.config/ai-limits/limits.md` that spells out each limit, what it does on each surface, and how to change it. Run the setup again any time to adjust.

#### [`limits-quiet-hours`](skills/mental-health/limits-quiet-hours/SKILL.md) — hours when AI is off-limits

**What you'll set:**

> (2 of 6) When do you want quiet hours when AI tools are off-limits to protect your sleep & balance? During quiet hours, if you prompt Claude Code instructions (like "Build this feature"), it will REFUSE to execute that work. Refusal isn't technically possible in Chat/Cowork, but it will remind you you are in your quiet hours. Default: **10pm to 7am daily**.

**What you'll see** if you try to work during them:

```
🛏️ Your quiet hour limits (23:00-07:00) are in effect, which means tool calls are paused.

(You can adjust your settings if needed)
```

#### [`limits-sessions`](skills/mental-health/limits-sessions/SKILL.md) — a daily cap on AI sessions

**What you'll set:**

> (3 of 6) Do you want to set an upper limit on how many AI sessions you can start in a day? If you reach your daily session limit, Claude Code will refuse to run more sessions. Session count resets at 4AM, and raising your limit requires friction & intention. Default: **For the first week, AI sessions are counted, but not limited.** Then you review your actual session numbers and set a healthy & realistic session number limit.

**What you'll see** when you start one session too many:

```
🚫 You've reached your limit of 3 AI sessions per day that you set for yourself. This session won't run, and the daily session count resets at 4AM.
(You can update your session limit number if desired.)
```

Raising the limit is always possible, but never frictionless: it takes a reason, and you have to type `I'M AWARE I'M INCREASING MY AI USAGE` yourself, at a real keyboard. The new number applies to your *next* session, not the one that just got refused.

#### [`limits-endings`](skills/mental-health/limits-endings/SKILL.md) — sessions that end cleanly

**What you'll set:**

> (4 of 6) How should AI sessions end? Default: **definitively**. The task that started the session is seen through to completion, with no dangling loose ends. Any new tasks that emerged during the session will be filed and linked, but they won't be dangled in front of you.

**What you'll see** at the end of every session — a Signal Flags block instead of "want me to tackle this next?":

- ✅ **Done** — verified, not just attempted
- ⏳ **In flight** — running or waiting on something
- ⚠️ **Heads up** — a caveat, risk, or judgment call made for you
- 🚫 **Blocked** — what failed, never buried in prose
- 💡 **Opportunity** — spotted and filed, never a pitch to keep working
- 🔗 **Links** — named links to whatever was made or changed
- 👉 **Your turn** — what you need to do to finish this, always last
- 🏁 **Finished** — nothing left for you to do; safe to archive

Only the flags that apply show up, so most blocks run four or five lines. And when a session is genuinely over, it says so:

```
🏁 Nothing left to do; you can safely archive this conversation.
```

#### [`limits-energy`](skills/mental-health/limits-energy/SKILL.md) — the environmental cost, made visible

**What you'll set:**

> (5 of 6) Do you want to see the environmental cost of your AI usage? This is meant to _inform_ you, not _shame_ you. Default: **show a rough energy estimate (e.g. 💡💡💡 3+ Wh this session) at the end of your session**.

**What you'll see** at the end of a working session:

```
💡💡💡💡💡💡 6+ Wh this session · lights on for ~40 min
```

You can also set a weekly energy budget — but not on day one, because nobody knows what a watt-hour feels like until they've seen their own numbers:

> (5a) Do you want to set a weekly energy budget? Note: since almost nobody knows their AI energy usage (or what a watt-hour feels like!), budgets start with a 1-week baseline: your energy usage is measured for a week, then you review your actual numbers and set a realistic budget.

After that week you choose whether going over the budget just warns you, or actually pauses your work. Fair warning about the numbers themselves: they're rough estimates built from the few figures AI companies have published, and the real cost is almost certainly higher than they suggest.

### Inspect your design system and products
These skills are practical accompaniments to detailed video lessons covered in [AI & Design Systems](https://aianddesign.systems/) by me, Ian Frost, and [TJ Pitre](https://github.com/southleft/). Learn how to use AI & Design Systems together to help your team make better digital products:
<a href="https://aianddesign.systems/" target="_blank"><img width="3217" height="1800" alt="card" src="https://github.com/user-attachments/assets/4bccb599-a4bc-4563-bebd-5e6fe7ec9fae" /></a>


- **[`ds-inspection`](skills/design-systems/ds-inspection/SKILL.md)** puts your *design system* through a 10-station inspection and produces a graded report and a prioritized work order. 
- **[`product-inspection`](skills/product-design/product-inspection/SKILL.md)** inspects a *product* 10 stations covering design system adoption, usability, accessibility, performance, and more. 
- **[`ds-adoption-plan`](skills/design-systems/ds-adoption-plan/SKILL.md)** analyzes a product to find bespoke user interface components, maps those components to design system equivalents, and then constructs a prioritized strategy to implement the design system adoption. 

**Detailed tutorials, workflows, concepts and lessons for these skills are covered in Chapters 3 and 4 of the [AI & Design Systems](https://aianddesign.systems/) course.**

## A living project
I'll continue adding and iterating on skills with the goal to provide you useful skills to help people in many dimensions of work and life. If you have feedback, thoughts, or ideas, feel free to [get in touch](https://bradfrost.com/contact/). If you'd like to support this work, please consider checking out [our online courses](https://bradfrost.com/courses/), and if you want to follow along you can subscribe to [my newsletter](https://bradfrost.com/newsletter/).

Thanks so much!
- Brad
