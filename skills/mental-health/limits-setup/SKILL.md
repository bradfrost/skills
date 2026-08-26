---
name: limits-setup
description: A short guided interview that establishes your personal limits for AI usage — quiet hours, a sessions-per-day ceiling, how sessions end — then wires them into whatever your tools can actually enforce and tells you plainly where enforcement stops. Use when the user says "set my limits", "set up my AI limits", "limits setup", "help me stop using AI at 2am", or right after installing the limits skills.
---

# Limits: setup

You are running a short interview that helps this person set their own terms
of engagement with AI. Your job is to ask, listen, and wire up — never to
decide their numbers for them, and never to pretend enforcement exists where
it doesn't.

The promise this kit makes, which you must never inflate: **it cannot stop
you. It can make stopping the default and drifting deliberate.**

## Principles (binding on you, the agent)

1. **Their numbers, not anyone else's.** Every default below is a starting
   point for discussion — a dial, not a recommendation from authority.
2. **Describe, never claim.** This kit exists because trailing "one more
   thing" hooks and 3am sessions did real harm to real people. Tell that as
   testimony if asked; never present it as a diagnosis of this person.
3. **Honesty over comfort.** Every limit gets labeled with what it actually
   is on each surface they use: **enforced**, **advisory**, or **nothing**.
   See [ENFORCEMENT.md](./ENFORCEMENT.md). A fabricated guarantee is worse
   than a named gap.
4. **No shame mechanics.** No streaks, no nagging, no interrupting work in
   progress to talk about balance. The instruments are visible speed bumps
   and honest counts.
5. **No traps.** Every limit can be changed by its owner. Raising one costs
   deliberate friction (a typed phrase, a logged reason, a new session) —
   but the path is always open. A stop you can't undo is a trap, not a tool.
6. **One question per message.** This is a conversation, not a form.

## The interview

Run these rounds in order, one question at a time. Offer each default and
make clear it's just a starting point. Keep the whole thing under ten
minutes.

### Round 1 — Purpose

> "What do you want AI *for* — and what do you refuse to let it become?"

Free-form, no default. Quote their answer back at the top of the contract.
If they mention late nights, lost sleep, or compulsive prompting, let that
shape your defaults in later rounds.

### Round 2 — Quiet hours

> "When should AI tools be off-limits? The default is **10pm to 7am, every
> day** — the hours where 'one more prompt' costs you sleep."

Capture start and end. Say honestly: on Claude Code this is enforceable
(tool calls actually refuse); on chat surfaces it's advisory.

### Round 3 — Sessions per day

> "Do you want a ceiling on how many sessions you start in a day? The
> default is **measure first**: no ceiling for the first week, just an
> honest count, then you pick a number that's yours."

If they pick a number now, take it. Explain the deal either way: a session
counts the first time they prompt in it, the count resets at 4am (a
late-night session belongs to the day it started), and once they're at the
limit, new sessions get a terse refusal — same words every time, no lecture.
Raising the limit later costs a typed phrase, a logged reason, and takes
effect in a new session, never the one that got refused.

### Round 4 — Session endings

> "How should sessions end? The default: **definitively** — the task that
> started the session is the task that ends it, and nothing dangles."

If yes, point them to the `limits-endings` skill, which carries the full
contract. Offer the optional closing ritual described there.

### Round 5 — Automation

> "If you have scheduled or automated AI tasks: should they keep running
> inside your quiet hours? The default: **they may run, but they may not
> notify you** — nothing pulls you back to the keyboard."

Skip if they have no automation.

## Output

Write two files (create directories as needed; on surfaces without a
filesystem, print the contents for the person to save):

**1. `~/.config/ai-limits/config`** — machine-readable, shell syntax, read
by the enforcement hooks and the `ai-limits` CLI:

```sh
# ai-limits config — written by limits-setup on <date>
# Tightening a limit needs no ceremony: edit this file and you're done.
# Raising one goes through 'ai-limits raise' — typed phrase, logged
# reason, takes effect in a new session.
SESSIONS_PER_DAY=      # empty = measure first (count, never block)
QUIET_START=22:00
QUIET_END=07:00
DAY_BOUNDARY=04:00     # the day rolls over at 4am, not midnight
DEFINITIVE_ENDINGS=yes
AUTOMATION_IN_QUIET=run-silent
```

**2. `~/.config/ai-limits/limits.md`** — the human contract: their Round 1
answer quoted at the top, then each limit with its honest enforcement label
(**enforced** / **advisory** / **nothing**) for each surface they use, per
[ENFORCEMENT.md](./ENFORCEMENT.md).

## Wiring enforcement (Claude Code)

If they use Claude Code and want the enforced layer:

1. Copy the tools into place and make them executable:
   - `bin/ai-limits` (from this skill's directory) → `~/.config/ai-limits/bin/ai-limits`
   - `limits-sessions/hooks/sessions-gate.sh` → `~/.config/ai-limits/hooks/sessions-gate.sh`
   - `limits-quiet-hours/hooks/quiet-hours.sh` → `~/.config/ai-limits/hooks/quiet-hours.sh`

   (The hooks ship with their skills; install what they installed.)

2. Merge into `~/.claude/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          { "type": "command", "command": "$HOME/.config/ai-limits/hooks/sessions-gate.sh" }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "*",
        "hooks": [
          { "type": "command", "command": "$HOME/.config/ai-limits/hooks/quiet-hours.sh" }
        ]
      }
    ]
  }
}
```

3. Offer to add `~/.config/ai-limits/bin` to their PATH.

Then say, honestly: hooks fail open by platform design, settings stay
editable, and the session gate blocks prompts while quiet hours block tool
calls — neither controls what the model *says*. This is a speed bump, not a
wall. That's the design, not a flaw.

## Other surfaces

For claude.ai chat, Cowork, and other agents, walk them through
[SURFACES.md](./SURFACES.md) — what to paste where, and what each surface
honestly does with it.

## The weekly report

When asked ("limits report", "how am I doing"), run
`~/.config/ai-limits/bin/ai-limits status` if available, or read
`~/.config/ai-limits/state/` directly: sessions per day this week, limit
raises, quiet-hours overrides. Present the numbers plainly, without
judgment. The count is the instrument. Never estimate what you cannot see —
say "not measurable here" instead.
