# Wiring your limits into each surface

The hooks only run on Claude Code (today). Everywhere else, your limits
travel as *instructions* — the advisory layer. Advisory mostly works; it
isn't guaranteed. Both facts matter.

## Claude Code

Full wiring — hooks, CLI, settings — is in [SKILL.md](./SKILL.md). This is
the one surface where refusals are real.

## claude.ai chat (web, mobile, desktop)

Paste your limits block into **Settings → Profile → personal
preferences** (it rides along in every conversation). The setup interview
generates this block from your answers at the end — the template lives in
[SKILL.md](./SKILL.md)'s "The chat & Cowork paste" section; ask any
session to regenerate it from `~/.config/ai-limits/config` if you've
tuned your limits since.

Label it honestly: this is advisory. Nothing on this surface can refuse.

## Claude Cowork

Install this kit's skills — the prose layer works in Cowork. The hooks
currently do not: Cowork sessions ignore user hooks
([claude-code#63360](https://github.com/anthropics/claude-code/issues/63360),
[#40495](https://github.com/anthropics/claude-code/issues/40495)). Until
that changes, Cowork is advisory-only, and your quiet hours there depend on
the model honoring the instruction. If you want that to change, the issues
above are where to say so.

## Other agent CLIs (Gemini CLI, OpenCode, Copilot CLI, Cursor)

Install the skills with `npx skills add` — the interview, the endings
contract, and the config all work as prose. These platforms have hook
systems, so the enforced layer is *possible*; this kit doesn't ship
adapters for them yet. The Claude Code hooks in `limits-sessions/hooks/`
and `limits-quiet-hours/hooks/` are small, commented bash scripts —
porting one is an afternoon, and contributions are welcome.

## Codex CLI

Skills work as prose. No hook adapter is shipped, deliberately: Codex's
PreToolUse only intercepts the shell tool, so a "curfew" there would let
edits, web fetches, and MCP calls straight through while looking locked.
A gate that leaks is worse than a documented gap.

## Your phone at 11pm

No skill reaches it. iOS Screen Time / Android Digital Wellbeing app limits
on the Claude app, plus OS-level Do Not Disturb during your quiet hours,
are the honest tools here. This kit can't do it for you, so it says so.
