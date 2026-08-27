---
name: limits-setup
description: START HERE after installing the limits kit — say "set my limits" to begin. A short guided interview that establishes your personal limits for AI usage — quiet hours, a sessions-per-day ceiling, how sessions end — then wires them into whatever your tools can actually enforce and tells you plainly where enforcement stops. Use when the user says "set my limits", "set up my AI limits", "limits setup", "help me stop using AI at 2am", right after installing the limits skills, or when the limits skills are installed but no config exists yet at ~/.config/ai-limits/.
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

Open by saying how many questions are coming (six — or five, if Round 6
gets skipped), and number every question — "(1 of 6)" — so no single
screen ever implies the interview is over when it isn't. Client UI chrome
(a "Submit answers" button on a multi-select) can suggest completion;
the numbering is what counters it.

### Round 1 — Motivation

> "**(1 of 6)** Why do you want to be intentional about your AI usage? Check all that
> apply:
>
> - **My mental health** — I want AI in my life on my terms, not the tool's
> - **Sleep** — "one more prompt" at midnight keeps costing me
> - **Clarity around my work** — I want sessions that end cleanly, not
>   endless dangling next steps
> - **The environment** — every prompt burns real energy and water
> - **Something else** — tell me in your own words"

Multi-select; there's no wrong combination. Their picks shape the rest of
the interview: **sleep** → lean into quiet hours (Round 2); **mental
health** → give the session ceiling (Round 3) real attention; **clarity**
→ Round 4 endings is their headline; **environment** → the energy
footer in Round 5 is their headline. Quote their checked
reasons — plus any "something else" in their own words — at the top of the
contract, so the config always says why it exists.

### Round 2 — Quiet hours

> "**(2 of 6)** When do you want AI tools to be off-limits to protect sleep & balance?
> Default is **10pm to 7am daily**."

If they checked **Sleep** in Round 1, tie the default to their own words
instead of a generic pitch. Capture start and end — a window that wraps
midnight is fine. Then the honesty note, plainly: on Claude Code this
actually refuses to work during those hours; on chat and mobile it's
advisory, and the real tool there is Do Not Disturb on their phone.

### Round 3 — Sessions per day

> "**(3 of 6)** Do you want to set an upper limit on how many AI sessions you can start
> in a day? Default: **monitor usage for the first week** to get an honest
> count, and then you pick an upper limit number that you feel comfortable
> with."

If they pick a number now, take it. Explain the deal either way, in three
plain beats:

1. A session counts the first time you prompt in it — opening one costs
   nothing.
2. The day resets at 4am, so a late night doesn't hand you a fresh
   allowance at midnight.
3. At your limit, new sessions get the same short refusal every time — and
   raising the limit means typing a phrase that says you're doing it on
   purpose, with the change kicking in next session, not the one that just
   got refused.

### Round 4 — Session endings

> "**(4 of 6)** How should AI sessions end? Default: **definitively** — the task that
> started the session is seen through until completion, with additional
> tasks captured in your task tracker instead of dangled in front of you."

If they checked **Clarity around my work** in Round 1, this round is their
headline — say so. If they opt in, point to the `limits-endings` skill for
the full contract, including the Signal Flags close-out block. Then offer
the optional closing ritual: one fixed final beat at the end of a
wrapped-up session that points away from the machine — their own chosen
phrase, or quotes from a source they supply and can verify. Never invent
one.

### Round 5 — Energy

> "**(5 of 6)** Do you want to see the environmental cost of your AI usage? Default:
> **show a rough energy estimate at the end of working sessions** — built
> from published per-prompt figures, always labeled a floor, never a guilt
> trip. You can also set a weekly energy budget if you want a number to
> steer by."

If they checked **The environment** in Round 1, this is their headline.
The estimates come from the `limits-energy` skill; be honest up front that
they carry wide error bars and inform without ever blocking. If they want
the footer, set `ENERGY_FOOTER=yes`; if they name a weekly budget in
watt-hours, set `ENERGY_BUDGET_WH_WEEK` (useful scale: a full phone charge
is roughly 15 Wh; a published chat prompt is about a quarter of one).

### Round 6 — Automation

> "**(6 of 6)** Should scheduled/automated AI tasks keep running inside your quiet
> hours? Default: **scheduled/automated tasks run during your defined
> quiet hours, but they do not notify you**."

Skip this round entirely if they have no automation (and adjust the
question count you announced). If they take the
default, note it in the contract as `run-silent`: automations may proceed
inside quiet hours, but reports, pings, and messages hold until the window
ends.

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
ENERGY_FOOTER=yes      # end-of-session energy floor estimate (limits-energy)
ENERGY_BUDGET_WH_WEEK= # empty = no budget; informs, never blocks
AUTOMATION_IN_QUIET=run-silent
```

**2. `~/.config/ai-limits/limits.md`** — the human contract: their Round 1
motivations quoted at the top, then each limit with its honest enforcement label
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

4. **Ask whether other automated Claude sessions run under this account**
   — daemons, cron jobs, scheduled tasks. User-level hooks apply to ALL of
   them: quiet hours would block their tool calls and their prompts would
   eat the session allowance. Any session meant to run as automation must
   set `AI_LIMITS_AUTOMATION=1` in its environment (launchd plist, crontab,
   scheduler env) — the hooks stand aside for it, per the Round 5 deal.
   Skipping this step with automation present means their own quiet hours
   will strangle their automations tonight.

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
