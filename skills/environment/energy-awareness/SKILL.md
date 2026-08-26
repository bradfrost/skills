---
name: energy-awareness
description: Make the environmental cost of AI usage visible — rough per-session energy estimates rendered as lightbulb time (💡), plus an optional weekly energy budget with deliberate, logged overrides. Use when the user asks "how much energy did this session cost", "what's the environmental cost", "show the energy footer", "set an energy budget", or enables environmental awareness in the healthy-limits interview.
---

# Energy Awareness

Every prompt burns real electricity and water in a real data center. This
skill makes that cost visible — as an honest estimate, not a guilt trip and
not a fake precision instrument.

## The honesty contract (binding on you, the agent)

1. **These are estimates with at least ±3× error bars.** No provider exposes
   per-request energy. Published anchors: Google reported a median of
   ~0.24 Wh per Gemini text prompt (2025); OpenAI cited ~0.34 Wh for an
   average ChatGPT query. Agentic coding sessions consume orders of
   magnitude more tokens than a chat prompt.
2. **Never present an estimate as a measurement.** Always mark it `~` and
   say "estimate" on first use per session.
3. **No shame mechanics.** The footer is information, the budget is theirs,
   the override is honored and counted — never refused, never lectured.
4. **If you can't see token counts on this surface, say so** and use the
   per-message rough anchor instead of inventing precision.

## Estimating

- **When token counts are visible** (Claude Code exposes session token
  usage): estimate **~0.3 Wh per 1,000 output tokens** as the anchor, and
  say the true figure may be several times higher or lower.
- **When they aren't** (chat surfaces): estimate **~0.3 Wh per substantial
  response**, same caveat.
- Include thinking/tool-use turns in agentic sessions — they're output too.

## Rendering: lightbulb time

Translate watt-hours into something felt: **1 Wh ≈ running a 10 W LED bulb
for 6 minutes.** Render one 💡 per Wh (round up, cap the row at 10 with a
`×N` multiplier).

End-of-session footer format (only when `ENERGY_FOOTER=yes` in
`~/.claude/healthy-limits.conf`, or the user asks):

> 💡💡💡 ~3 Wh this session (estimate) — a 10 W LED burning for ~18 min

Honesty note: on every surface, this footer is **advisory** — an instruction
the model follows probabilistically, not a platform guarantee (see the 🍌
diagnostic in the mental-health/healthy-limits skill's ENFORCEMENT.md).

## The weekly budget (optional)

If `ENERGY_BUDGET_WH_WEEK` is set in `~/.claude/healthy-limits.conf`:

- Keep a running tally where the surface allows (Claude Code: append
  `date  estimated_Wh  note` lines to `~/.claude/energy-ledger.log`).
- When a session would cross the budget, **say so before continuing** and ask
  for a deliberate go-ahead; log the override to the same ledger. The count
  is the instrument — surface it in the weekly report, plainly, no judgment.
- Useful scale for choosing a number: a full smartphone charge is ~15 Wh;
  an hour of a 10 W LED is 10 Wh; published estimates put a single chat
  prompt around 0.3 Wh.

## Weekly report

When asked ("energy report", "how much did I burn this week"): sum the
ledger, render the lightbulb row, compare to their budget if set, and state
what the number is: **a rough estimate of one slice of the true cost** —
it excludes training, embodied hardware, cooling water, and idle capacity.
Never let the report imply completeness it doesn't have.
