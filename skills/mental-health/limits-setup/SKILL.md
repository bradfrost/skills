---
name: limits-setup
description: The AI limits interview — run by /setup-brad-frost-skills, or directly any time. A short guided interview that establishes your personal limits for AI usage — quiet hours, a sessions-per-day ceiling, how sessions end — then wires them into whatever your tools can actually enforce and tells you plainly where enforcement stops. Use when the user says "set my limits", "set up my AI limits", "limits setup", "help me stop using AI at 2am", when /setup-brad-frost-skills routes here, or when the limits skills are installed but no config exists yet at ~/.config/ai-limits/.
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

**The script is the whole script.** The quoted copy below is everything
you say — the user's voice, not yours. Acknowledge an answer in five words
or fewer ("Got it — 11pm to 7am."), then ask the next question. No
commentary, no restating what an answer means, no encouragement, no
honesty notes beyond the ones scripted into a round. Number every question
— "(1 of 6)" — so no single screen ever implies the interview is over when
it isn't (client UI chrome like a "Submit answers" button can suggest
completion; the numbering counters it).

Open with exactly:

> "Answer 6 quick questions to establish healthy limits with AI. For each
> question, you can choose the suggested default or tweak to your
> preferences. Let's go!"

(Say 5 if Round 6 will be skipped.)

### Round 1 — Motivation

> "**(1 of 6)** Why do you want to be intentional about your AI usage? Check all that
> apply:
>
> - **Mental health:** I want to establish healthier boundaries with AI
> - **Sleep:** I want to prioritize sleep and not feel pulled into
>   prompting through the night
> - **Clarity around AI sessions:** I want sessions that end cleanly
>   without never-ending, confusing, dangling next steps
> - **The environment:** I want better awareness of how my AI use impacts
>   the environment
> - **Anything else?** Feel free to share anything else around why you
>   want to be intentional about your AI use."

Multi-select; there's no wrong combination. Their picks shape the rest of
the interview SILENTLY — never narrate what a pick means: **sleep** →
lean into quiet hours (Round 2); **mental health** → the session ceiling
(Round 3); **clarity** → endings (Round 4); **environment** → the energy
footer (Round 5). Quote their checked reasons — plus anything else in
their own words — at the top of the contract, so the config always says
why it exists. Spoken response to their answer: "Got it." and the next
question.

### Round 2 — Quiet hours

> "**(2 of 6)** When do you want quiet hours when AI tools are off-limits to protect
> your sleep & balance? During quiet hours, if you prompt Claude Code
> instructions (like "Build this feature"), it will REFUSE to execute
> that work. Refusal isn't technically possible in Chat/Cowork, but it
> will remind you you are in your quiet hours. Default: **10pm to 7am
> daily**."

Capture start and end — a window that wraps midnight is fine. The
enforcement note is already in the script; add nothing to it.

### Round 3 — Sessions per day

> "**(3 of 6)** Do you want to set an upper limit on how many AI sessions you can start
> in a day? If you reach your daily session limit, Claude Code will refuse
> to run more sessions. Session count resets at 4AM, and raising your
> limit requires friction & intention. Default: **For the first week, AI
> sessions are counted, but not limited.** Then you review your actual
> session numbers and set a healthy & realistic session number limit."

If they pick a number now, take it. If they decline entirely ("no
thanks"), honor it fully: set `SESSIONS_TRACKING=off` — no ceiling AND no
counting; declining measurement is a real choice, not a lesser
measure-first. The mechanics are already in the script; add nothing to
them. (Fine print you know but don't recite: a
session counts on its first prompt, refused sessions stay refused after a
raise, raises go through `ai-limits raise` with a typed phrase.)

### Round 4 — Session endings

> "**(4 of 6)** How should AI sessions end? Default: **definitively**. The task that
> started the session is seen through to completion, with no dangling
> loose ends. Any new tasks that emerged during the session will be filed
> and linked, but they won't be dangled in front of you."

If they opt in, the `limits-endings` skill carries the full contract,
including the Signal Flags close-out block — apply it; don't narrate it.
The closing ritual is no longer offered in the interview: it stays
available in `limits-endings` for anyone who asks, with its guardrail
intact — their own chosen phrase, or quotes from a source they supply and
can verify. Never invent one.

### Round 5 — Energy

> "**(5 of 6)** Do you want to see the environmental cost of your AI usage? This is
> meant to _inform_ you, not _shame_ you. Default: **show a rough energy
> estimate (e.g. 💡💡💡 3+ Wh this session) at the end of your session**."

If they decline: `ENERGY_FOOTER=no`, skip 5a, go to Round 6. If they
accept, `ENERGY_FOOTER=yes` and follow up:

> "**(5a)** Do you want to set a weekly energy budget? Note: since almost nobody
> knows their AI energy usage (or what a watt-hour feels like!), budgets
> start with a 1-week baseline: your energy usage is measured for a week,
> then you review your actual numbers and set a realistic budget."

There is no set-a-number-now path — the baseline week is the on-ramp, by
design; never link out to calculators. If no: footer only, leave all
budget keys empty, skip 5b. If yes, ask 5b:

> "**(5b)** Once you have an energy baseline after a week of use, you can then
> set your energy budget limit. How would you like to enforce your energy
> limit?
>
> - ⚠️ **Warn only:** you get a heads-up when you exceed your budget
> - 🚫 **Restrict:** Claude Code will refuse to continue working once your
>   budget is exceeded (you can always deliberately adjust)
> - **I'm not sure right now;** ask me again when I see my actual numbers"

Record intent only: `ENERGY_BUDGET_MODE=warn` or `restrict` (leave empty
for "not sure"), and leave `ENERGY_BUDGET_WH_WEEK` empty — nothing warns
or gates until the number is set at the baseline review, which the
`limits-energy` skill runs when a week of ledger data exists. Say nothing
more here.

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
SESSIONS_TRACKING=     # off = don't even count (declined in Round 3)
QUIET_START=22:00
QUIET_END=07:00
DAY_BOUNDARY=04:00     # the day rolls over at 4am, not midnight
DEFINITIVE_ENDINGS=yes
ENERGY_FOOTER=yes      # end-of-session energy floor estimate (limits-energy)
ENERGY_BUDGET_WH_WEEK= # empty = no budget
ENERGY_BUDGET_MODE=    # warn = heads-up only; restrict = opt-in gate
AUTOMATION_IN_QUIET=run-silent
```

**2. `~/.config/ai-limits/limits.md`** — the human contract. Fixed
template below: fill the brackets from their answers, drop table rows for
limits they declined, pick the matching energy-row variant, and quote
their Round 1 reasons verbatim (the one first-person section — their
words quoted back; everything else stays second person). Add nothing.

````markdown
# Your AI Limit Preferences

You deliberately set these limits on [date] at [time] using Brad Frost's
[AI limits skill](https://github.com/bradfrost/skills)

## Why I set these limits

- [their checked Round 1 reasons, verbatim, one per line]
- [anything else they shared, in their own words]

## The limits

| Limit | Your setting | Claude Code | Chat & Cowork |
|---|---|---|---|
| Quiet hours | [23:00-07:00 daily] | 🚫 tool calls refused | ⚠️ reminded of limits |
| Sessions per day | [measuring this week / limit of N] | 🚫 new sessions refused [add "(once a number is set)" while measuring] | — (can't count sessions) |
| Session endings | [Definitive] | loaded into every session | loaded once pasted into settings |
| Energy | [footer on, no budget / budget of N Wh/week, warn / budget of N Wh/week, restrict] | [estimate shown at session end / ⚠️ warned when budget exceeded / 🚫 tool calls refused when budget exceeded] | shown via pasted preference |
| Automation in quiet hours | [runs, but can't notify me] | honored by exempted automations | n/a |

## Changing your limits

You can update any of your limits by editing `~/.config/ai-limits/config`.
It's important to know that loosening a limit requires going through some
deliberate friction.

- You need to provide a reason for raising your `SESSIONS_PER_DAY` limit
  or shortening your `quiet-hours` window
- You'll need to type `I'M AWARE I'M INCREASING MY AI USAGE`
- The updated settings will take effect in the next new session
- Every raise and override is logged and shows up in your weekly AI
  session count.

```
ai-limits raise SESSIONS_PER_DAY <n> --reason "why"
ai-limits override quiet-hours --reason "why"
```

## You control your own limits

- These gates are merely speed bumps to steer you to healthier limits;
  the point isn't to make it impossible to venture outside of your
  limits, it's just that it should be an intentional and documented act
  rather than an impulsive override
- Claude Code can refuse work, but that isn't technically possible in
  Chat & Cowork. But by pasting your limit preferences into your
  settings, sessions will adhere to your session endings format and
  remind you of your limits
- The energy numbers are rough estimates; AI companies don't publish how
  much energy each prompt actually burns 🥵. The real cost is almost
  certainly higher than the numbers suggest.

## Checking in

In any session, you can say "limits report" to see your:

- weekly session number
- raises & overrides
- energy usage

Again, this is about understanding, not shaming.
````

## Wiring enforcement (Claude Code)

If they use Claude Code and want the enforced layer:

1. Copy the tools into place and make them executable:
   - `bin/ai-limits` (from this skill's directory) → `~/.config/ai-limits/bin/ai-limits`
   - `limits-sessions/hooks/sessions-gate.sh` → `~/.config/ai-limits/hooks/sessions-gate.sh`
   - `limits-quiet-hours/hooks/quiet-hours.sh` → `~/.config/ai-limits/hooks/quiet-hours.sh`
   - `limits-energy/hooks/energy-gate.sh` → `~/.config/ai-limits/hooks/energy-gate.sh`
     (inert unless they chose the restrict budget mode)
   - `limits-endings/hooks/endings-context.sh` → `~/.config/ai-limits/hooks/endings-context.sh`
     (loads the endings contract into every session; inert unless
     `DEFINITIVE_ENDINGS=yes`)

   (The hooks ship with their skills; install what they installed.)

2. Merge into `~/.claude/settings.json`:

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          { "type": "command", "command": "$HOME/.config/ai-limits/hooks/sessions-gate.sh" },
          { "type": "command", "command": "$HOME/.config/ai-limits/hooks/energy-gate.sh" }
        ]
      }
    ],
    "SessionStart": [
      {
        "hooks": [
          { "type": "command", "command": "$HOME/.config/ai-limits/hooks/endings-context.sh" }
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

## The chat & Cowork paste

Claude Code is now enforced; the other surfaces need one manual step. Say
exactly:

> "Your limits are now live in Claude Code. Only one step is left to
> apply them to Chat & Cowork:
>
> ⚠️ Chat & Cowork can't refuse work the way Claude Code can, but will
> honor your session ending preferences and remind you of your set limits.
> 👉 Paste the following into claude.ai → Settings → Profile → personal
> preferences."

Then generate this block FROM THEIR ANSWERS (fill the brackets, drop any
line for a limit they didn't set) and show it ready to copy:

```
My AI limits, set deliberately on [date] (bradfrost/skills limits kit):
- Quiet hours [23:00-07:00] daily: if I start something in this window,
  remind me once, briefly, and keep it short.
- Sessions: [limit of N per day / measuring my count this week].
- End every session definitively: the task that started it is the task
  that ends it; no trailing "want me to also...?" offers; file loose ends,
  don't dangle them. Close substantive responses with a Signal Flags
  block. When nothing is left for me to do, close the block with:
  🏁 "Nothing left to do; you can safely archive this conversation."
- Energy: end working sessions with a one-line energy floor estimate.
Honor these limits; never lecture me about them.
```

## The close

The spoken part of finishing is the paste step above plus the scripted
close below — nothing else. The hooks-fail-open and
settings-stay-editable honesty lives in the written contract, not the
speech.

After the files are written and wiring is done, end with exactly:

> "Alright, your limits are set! Here's what you can expect:
>
> - All future AI sessions will read your limit preferences, which are
>   saved as a plain-language contract in a config file
>   (`~/.config/ai-limits/`)
> - Any quiet hours and session limits you just set are now actually
>   enforced in Claude Code. When your limit conditions are met, Claude
>   Code will refuse to continue performing work.
> - Claude Chat & Cowork can't technically refuse to work, but will alert
>   you when you've exceeded your limits
> - None of this is set in stone; you can adjust your limits at any point.
>   Edit the config file (`~/.config/ai-limits/`) or say "set/adjust my
>   limits" to tune your preferences. Note that _loosening_ your limits
>   requires some intentional friction in the form of a typed phrase.
> - You can say "limits report" anytime to see how you're doing.
>
> By setting these limits, I hope you arrive at a healthy, balanced
> relationship with AI. Wishing you health, happiness, balance, and
> satisfaction in your work and life. - Brad"

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
