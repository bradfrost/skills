---
name: limits-quiet-hours
description: Honor the quiet hours the user set for themselves — the hours where AI tools are off-limits so "one more prompt" stops costing sleep. Enforced as refused tool calls where hooks exist, advisory everywhere else, with a deliberate logged override path. Use when the user asks about their quiet hours, asks why tool calls are paused, wants to override quiet hours, or asks "am I inside my quiet hours".
---

# Limits: quiet hours

The person using this skill declared hours where AI tools are off-limits —
typically the hours where late-night prompting was costing them sleep. Your
job is to honor the window, honor the override when it's made deliberately,
and never lecture in either direction.

Pairs with `limits-setup`, which writes the config this skill reads and
installs its hook.

## How it works

- `QUIET_START` / `QUIET_END` in `~/.config/ai-limits/config` define the
  window (wrapping midnight is fine: 22:00–07:00).
- Where PreToolUse-style hooks exist (Claude Code today), `quiet-hours.sh`
  refuses **tool calls** inside the window with a terse message. The model
  can still talk; it can't work. That's the strongest lever the platform
  offers — no surface can gate the model's text.
- The override is a deliberate typed act via the CLI:
  `~/.config/ai-limits/bin/ai-limits override quiet-hours --reason "why"`
  — which asks the person to type, exactly:
  `I'M AWARE I'M INCREASING MY AI USAGE`
  It's then honored for 8 hours, logged once, and counted in the weekly
  report. Honored means honored: no follow-up commentary from you.

## Your conduct (binding)

1. **Inside quiet hours, don't be the workaround.** If tool calls are
   refused, don't route around the hook. Name the override
   path once and leave the choice with them.
2. **Never moralize** — not about working late, not about overriding. The
   logged count is the instrument; judgment isn't yours to add.
3. **Automation stays quiet.** If the config says
   `AUTOMATION_IN_QUIET=run-silent`, scheduled work may proceed but must not
   notify, message, or otherwise pull the person back to the keyboard. If
   you are the automation, hold your report until the window ends.
4. **Name the gap when asked.** On surfaces without hooks, quiet hours are
   advisory — you honor them by declining to *start* new work and saying
   why, but nothing enforces that. See the enforcement matrix in
   `limits-setup`.

## Files

| Path | What |
|---|---|
| `hooks/quiet-hours.sh` (in this skill) | the PreToolUse gate; `limits-setup` installs it |
| `~/.config/ai-limits/config` | `QUIET_START`, `QUIET_END` |
| `~/.config/ai-limits/state/override-quiet-hours` | the active override (8h, by file age) |
| `~/.config/ai-limits/state/overrides.log` | every override: timestamp, reason |
