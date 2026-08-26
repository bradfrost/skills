# Skills

Brad Frost's agent skills — installable, self-contained instructions for AI agents, spanning many dimensions of work and life.

Modeled on [mattpocock/skills](https://github.com/mattpocock/skills).

## Status

Early days. Skills live in `skills/<category>/<skill-name>/`, organized by category.

### Categories

- **mental-health** — healthy engagement with AI: limits, quiet hours, session endings, deliberate overrides
  - [`healthy-limits`](skills/mental-health/healthy-limits/SKILL.md) — a short guided interview that establishes *your* limits (smart defaults, your numbers), wires them into what your surface can actually enforce, and is honest about the rest
- **environment** — the environmental cost of AI usage, made visible
  - [`energy-awareness`](skills/environment/energy-awareness/SKILL.md) — rough per-session energy estimates as lightbulb time (💡), plus an optional weekly energy budget
- **design-systems** *(planned)* — design system inspection and health-check skills
- **product-design** *(planned)* — product analysis and inspection skills

More categories to come.

## Getting started

Install the skills, then ask your agent to **"set up healthy limits."** The interview takes a few minutes: what you want AI for, quiet hours, how sessions should end, usage rhythm, override costs, and environmental awareness — each with a sensible default you can accept or change. The output is your personal limits config, plus honest labels on every limit: **enforced**, **advisory**, or **nothing**, per surface. See [the enforcement matrix](skills/mental-health/healthy-limits/ENFORCEMENT.md).
