---
name: limits-sessions
description: Enforce the sessions-per-day ceiling the user set for themselves — count sessions honestly, refuse new ones past the limit with the same terse message every time, and make raising the limit a deliberate, logged act. Use when the user asks "how many sessions have I used", "am I at my limit", "raise my session limit", "limits report", or asks why a session was refused.
---

# Limits: sessions

The person using this skill set a ceiling on how many AI sessions they start
in a day — the same way someone allows themselves one glass of wine or one
cheat day. Your job is to honor it, count it honestly, and never talk them
past it.

Pairs with `limits-setup`, which writes the config this skill reads and
installs its hook. Without setup, this skill has nothing to enforce.

## How it works

- **A session counts the first time the person prompts in it.** Opening a
  session and never using it costs nothing.
- **The day rolls over at 4am** (configurable as `DAY_BOUNDARY`), not
  midnight — a late-night session belongs to the day it started, and 12:01am
  never hands out a fresh allowance.
- **At the ceiling, new sessions are refused** by the `sessions-gate.sh`
  hook (UserPromptSubmit, exit 2): the limit, the reset time, how to change
  it. Same words every time. A vending machine that's out of stock isn't
  nagging you; it's just out.
- **A refused session stays refused for the day**, even if the limit is
  raised afterward. The raise applies to new sessions — that's the deal the
  person agreed to at setup.
- **No ceiling set means measure-first**: sessions are counted, never
  blocked, so the person can pick a number grounded in a week of honest data.

## Your conduct around the gate (binding)

1. **Never help circumvent it.** If the person is refused and asks you to
   find a way around, don't. Tell them the two legitimate paths: edit
   `~/.config/ai-limits/config` by hand, or run
   `~/.config/ai-limits/bin/ai-limits raise SESSIONS_PER_DAY <n> --reason "why"`
   — which asks them to type, exactly:
   `I'M AWARE I'M INCREASING MY AI USAGE`
   That friction is theirs, chosen at setup. Respect it.
2. **Never moralize.** Not when they're near the limit, not when they raise
   it, not in the weekly report. State counts; skip commentary.
3. **Report honestly.** For "limits report" or "how many sessions": read
   `~/.config/ai-limits/state/` — `sessions-YYYY-MM-DD` files (one session
   id per line) and `changes.log` (raises, with reasons). Distinct lines per
   day = sessions used. Present the week's counts and any raises, plainly.
4. **Name the gap when asked.** This works where UserPromptSubmit hooks run
   (Claude Code today). On surfaces without hooks it doesn't exist, and you
   say so. See the enforcement matrix in `limits-setup`.

## Files

| Path | What |
|---|---|
| `hooks/sessions-gate.sh` (in this skill) | the UserPromptSubmit gate; `limits-setup` installs it |
| `~/.config/ai-limits/config` | `SESSIONS_PER_DAY`, `DAY_BOUNDARY` |
| `~/.config/ai-limits/state/sessions-<day>` | session ids used that day |
| `~/.config/ai-limits/state/refused-<day>` | sessions refused that day (stay refused) |
| `~/.config/ai-limits/state/changes.log` | limit raises: timestamp, old → new, reason |
