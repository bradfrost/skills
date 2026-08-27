---
name: limits-energy
description: Make the environmental cost of AI usage visible — floor estimates built from published per-prompt figures, rendered as lightbulb time (💡), with an optional weekly energy budget that informs but never blocks. Use when the user asks "how much energy did this session cost", "what's the environmental cost", "show the energy footer", "set an energy budget", "energy report", or enables environmental awareness in the limits-setup interview.
---

# Limits: energy

Every prompt burns real electricity and water in a real data center. This
skill makes that cost visible — as an honest floor estimate, not a guilt
trip and not a fake precision instrument.

Pairs with `limits-setup`, which writes the config this skill reads.

## The honesty contract (binding on you, the agent)

1. **Inform, never gate.** Energy numbers never block work — not at the
   budget line, not anywhere. Blocking on a number with error bars this
   wide would be fake precision with consequences. Sessions and schedules
   enforce; energy informs.
2. **Cited figures only, provenance inline.** The two published anchors,
   with what they cover:
   - **~0.24 Wh** — Google's published median for a Gemini Apps text
     prompt (2025). Includes accelerator, host CPU/memory, backup
     equipment, and datacenter overhead including cooling; excludes
     training.
   - **~0.34 Wh** — OpenAI's figure for an "average" ChatGPT query
     (2025, from Sam Altman's blog). Not peer-reviewed; "average query"
     is undefined.

   Both are vendor self-reported. Say so when asked.
3. **Never invent a conversion.** There is no published per-token energy
   figure — do not create one. Nobody has published figures for agentic
   coding sessions either; they involve far more computation per turn than
   a median chat prompt, which is exactly why every estimate here is a
   **floor**.
4. **No shame mechanics.** The footer is information; the budget is
   theirs; crossing it changes what you *say*, never what you *do*.

## Estimating: count turns, multiply, call it a floor

A "turn" is one model call — each response, including each tool-use step in
an agentic session, is one. Turns are countable; per-turn cost is not
knowable, so:

> estimated floor = (turns you can count) × 0.24 Wh (the conservative
> anchor)

The footer shows only the result (see Rendering); the method stays one
question away — when they ask "how was this measured", give the math, the
turn count, and both anchors with provenance. When you cannot count turns
on a surface, estimate the count conservatively and say you did. Never
present a result without its floor marker: a trailing `+` on the number
(`36+ Wh`), which reads naturally and stays true — the real cost is
higher, never lower.

## Rendering: keep it light

One terse line, emoji that scale with the magnitude, no method talk.
End-of-session footer (only when `ENERGY_FOOTER=yes` in
`~/.config/ai-limits/config`, or on request; skip it in automated
sessions):

> 💡💡💡💡💡💡 6+ Wh this session · lights on for ~40 min

At bigger totals, switch units so the emoji stay meaningful:

> 📱📱📱 51+ Wh this week · 3 full phone charges · lights on for ~5 hours

Rules:

- **The number:** counted turns × 0.24 Wh, rounded, with a trailing `+`
  carrying the floor.
- **💡** one per Wh, capped at ten. **📱** one per full phone charge
  (~15 Wh), capped at ten — use phones once bulbs stop being legible.
- **Felt equivalents:** lights-on time = Wh ÷ 10 W LED; a phone charge
  ≈ 15 Wh. Month- and year-scale equivalences (✈️ flights and beyond)
  need cited energy-to-carbon conversions — that's the energy tracker's
  job, not this footer's.
- Nothing else on the line. Method and provenance are answers, not
  furniture.

Like everything text-shaped, the footer is **advisory on every surface**
(see the enforcement matrix in `limits-setup`). It works by being followed.

## The weekly budget (optional, inform-only)

If `ENERGY_BUDGET_WH_WEEK` is set in the config:

- Where a filesystem exists, append one line per session to
  `~/.config/ai-limits/state/energy-ledger.log`:
  `2026-08-27  wh=2+  turns=8  <one-word context>` — keep this format
  stable and parseable; it is the data source for reviewing usage over
  time
- When the week's running floor crosses the budget, say so **once**,
  plainly: the tally, the budget, nothing else. No gate, no lecture, no
  repeat. The count is the instrument.
- Useful scale for picking a number: a full smartphone charge is roughly
  15 Wh; an hour of a 10 W LED is 10 Wh; a published chat prompt is about
  a quarter of a watt-hour.

## Weekly report

When asked ("energy report", or as part of a limits report): sum the
ledger's ranges, render the lightbulb row, compare to the budget if one is
set, and state what the number is: **a floor estimate of one slice of the
true cost** — it excludes training, embodied hardware, idle capacity, and
anything the providers don't publish. Never let the report imply
completeness it doesn't have; where the ledger has gaps, say "not measured"
rather than backfilling.
