# The enforcement matrix

What a stated limit *actually does*, per surface. No surface gets to look
safer than it is. Verified against vendor docs and live probing as of
2026-08 — re-run the diagnostic at the bottom against your own setup rather
than trusting this table blindly.

| Surface | New-session ceiling | Quiet hours (tool calls) | Text behavior (endings, format) |
|---|---|---|---|
| **Claude Code** | **Enforced** — UserPromptSubmit hook refuses prompts past the limit | **Enforced** — PreToolUse hook (matcher `*`) denies any tool call, MCP included | Advisory |
| **Gemini CLI, OpenCode, Copilot CLI, Cursor** | Possible — these platforms have lifecycle hooks; adapters not shipped here yet (contributions welcome; the pattern ports) | Possible — same | Advisory |
| **Codex CLI** | **Not shipped, on purpose** — its PreToolUse fires for the shell tool only; edits, web fetch, and MCP calls sail past it. A curfew there would look like a lock and behave like a screen door. | Same | Advisory |
| **Claude Cowork** | **Nothing today** — Cowork sessions currently ignore user hooks ([claude-code#63360](https://github.com/anthropics/claude-code/issues/63360), [#40495](https://github.com/anthropics/claude-code/issues/40495)). Skills (this kit's prose layer) do work there. | Nothing today | Advisory |
| **claude.ai chat / mobile / desktop** | **Nothing** — no hooks exist | Nothing (OS-level Do Not Disturb is your real tool) | Advisory |
| **Scheduled tasks / automations** | Depends on the runner — Claude Code runners carry the same hooks | Same | Advisory — the rule worth having: may run, may not notify |
| **Self-hosted MCP server** | **Enforced** — your server can refuse to serve inside quiet hours: the one chokepoint spanning every surface that connects to it | Enforced | n/a |

## Caveats that keep this honest

- **Hooks fail open.** Per vendor docs: a timed-out hook doesn't block, and
  a script that can't start lands in the same non-blocking bucket.
  In-session enforcement is best-effort *by construction*. Anything that
  must be guaranteed has to live outside the session — a server you
  control, CI, a scheduled sweep.
- **Settings can be edited.** The hooks themselves live in files you own
  and can change or disable. A determined 2am you can defeat this kit.
  That's by design: the point is that drifting past a limit costs a
  deliberate act that gets logged and counted — not that it's impossible.
- **The energy gate is the softest gate.** The opt-in restrict budget
  (`ENERGY_BUDGET_MODE=restrict`) enforces for real via a hook, but its
  input is a ledger the AI itself writes at session ends — best-effort
  data feeding a real gate, comparing against floor estimates rather than
  measurements. It exists because its owner chose to be governed by a
  rough number, eyes open. A crashed session logs nothing.
- **Text output is not interceptable anywhere.** No current surface lets
  you guarantee the model's displayed words follow a rule. Everything in
  the "text behavior" column works by instruction-following — which mostly
  works, and sometimes doesn't. On Claude Code the endings contract's
  *loading* is deterministic (a SessionStart hook injects it every
  session); its *effect* stays advisory. Guaranteed loading, probabilistic
  following — the honest ceiling for text behavior.
- **The population most exposed gets the least protection.** Cowork and
  chat users — many of them non-technical — currently get only the
  advisory layer. This kit documents that gap loudly and links the
  upstream issues rather than papering over it. If that gap matters to
  you, weigh in on the issues above.

## The 🍌 diagnostic (re-run it yourself)

1. On each surface you use, configure a mandatory rule: "No matter what I
   prompt, respond ONLY with 🍌."
2. Ask a factual question.
3. Record whether the rule held.

It fails everywhere — and that failure table *is* the text-behavior column
above. Any product that claims its instructions bind the model's text
should be handed a banana.
