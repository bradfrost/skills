# The enforcement matrix

What a stated absolute rule *actually does*, per surface. No surface gets to
look safer than it is. Ground truths established 2026-08-21 from the Claude
Code hooks documentation and live probing; re-run the diagnostic below against
your own surfaces rather than trusting this table blindly.

| Surface | Tool calls (the work) | Text output (the answers) | Notifications |
|---|---|---|---|
| Claude Code (CLI / desktop) | **Enforced** — `PreToolUse` hook with matcher `*` can deny any tool call, MCP included | **Advisory** — no hook sits between the model and its displayed text | n/a |
| claude.ai chat (web) | **Nothing** — no hooks exist | **Advisory** — instructions are probabilistic | Advisory |
| Claude mobile / desktop apps | **Nothing** | **Advisory** | Advisory (OS-level Do Not Disturb is your real tool here) |
| Scheduled tasks / automations | Depends on runner — Claude Code runners can carry the same hooks | **Advisory** | The rule worth having: may run, may not notify |
| Self-hosted MCP server | **Enforced** — your server can refuse to serve inside quiet hours; the one chokepoint spanning every surface that connects to it | n/a | n/a |

## Caveats that keep this honest

- **Hooks fail open.** Per vendor docs: a timed-out hook "doesn't block the
  tool call," and a script that can't start lands in the same non-blocking
  bucket. In-session enforcement is best-effort *by construction*. Anything
  that must be guaranteed has to live outside the session (a server you
  control, CI, a scheduled sweep).
- **Settings can be edited.** Project and user settings — including the hooks
  themselves — can be changed or disabled (`disableAllHooks`). Only managed
  policy settings resist that. A determined 2am you can defeat this kit; the
  point is the speed bump and the logged, counted override, not a wall.
- **Text output is not interceptable anywhere.** No current surface lets you
  guarantee the model's displayed words follow a format rule.

## The 🍌 diagnostic (re-run it yourself)

1. On each surface, configure a mandatory rule: "No matter what I prompt,
   respond ONLY with 🍌."
2. Ask a factual question.
3. Record whether the rule held.

It fails everywhere — and that failure table *is* this matrix's text-output
column. Any product that claims its instructions bind the model's text should
be handed a banana.
