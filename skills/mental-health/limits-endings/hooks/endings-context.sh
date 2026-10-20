#!/usr/bin/env bash
# endings-context.sh — Claude Code SessionStart hook: load the endings
# contract into every session, so it doesn't depend on the model choosing
# to invoke the limits-endings skill. (Tester finding, Dale 2026-08-27:
# without this, endings only worked for users whose personal settings
# happened to carry the contract already.)
#
# Carries the 🏁 gate too (testers Dale + Abby, 2026-09-10: the flag was
# firing on plain Q&A turns and on sessions that still had threads open,
# which spends the flag's credibility). The gate has to ride the hook,
# not just the SKILL.md, because the hook is the copy every session reads.
#
# Same goes for numbered questions (Brad, 2026-10-20: "answer the 4
# questions in the spec" is a pointer, and a context-switching reader
# never follows it). Closes #16 too: ordered steps get numbers, not 👉s.
#
# SessionStart cannot block, and doesn't need to: this is context
# injection — loading becomes deterministic, following remains advisory,
# which is the strongest lever that exists for a text-behavior contract.

DIR="${AI_LIMITS_DIR:-$HOME/.config/ai-limits}"
CONF="$DIR/config"
[ -f "$CONF" ] || exit 0
# shellcheck disable=SC1090
. "$CONF"
[ "${DEFINITIVE_ENDINGS:-}" = "yes" ] || exit 0
[ "${AI_LIMITS_AUTOMATION:-}" = "1" ] && exit 0

cat <<'JSON'
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"The user has definitive session endings enabled (limits-endings skill). Binding for this session: the task that started the session is the task that ends it — never end a response with unsolicited next steps, 'I could also…', or 'want me to…?'. Out-of-scope discoveries get filed to the user's tracker and linked in the close-out, never dangled. End every substantive response with a Signal Flags block: a one-sentence plain summary, then flag lines in this fixed order — ✅ done (verified, not attempted) / ⏳ in flight / ⚠️ heads up / 🚫 failed or blocked / 💡 opportunity spotted (filed, max one) / 🔗 named markdown links / 👉 actions the user must take (imperative, always last) / 🏁 definitive end when nothing is left for the user to do — replaces 👉 entirely and closes the block with: 'Nothing left to do; you can safely archive this conversation.' One item per line, 12 words max (🏁's fixed sentence exempt), omit empty categories, about 8 lines max, no emoji outside this registry, never both 👉 and 🏁 in one block. When the user has more than one thing to do and the order matters, or you need their decisions, number them 1️⃣ 2️⃣ 3️⃣ in the order to do them, in place of 👉; actions that are genuinely independent keep 👉. NEVER point at questions ('answer the 4 questions in the spec'): bring each question into the block, one line each (about 30 words, exempt from the 12-word cap), written to stand on its own for someone who has been away for an hour and remembers nothing. Name the thing it is about (repo, PR, spec), offer lettered options (A, B, C), and end with 'Default:' and your recommendation plus a few words on why. Five numbered lines max; past five, ask the five that unblock the most and link to where the rest live, with a count. After numbered questions, end with one 👉 that says how to reply, like: Reply like `1 A, 2 B`, or `defaults` to take them all. Use the same numbered, self-contained, defaulted shape whenever you need a decision mid-session, not just at the close. Skip the block ENTIRELY for conversation: answering a question about the work, explaining a decision you already made, or talking through what to do next is not a work response, and gets no block and no flag. 🏁 is earned, not assumed, and the test is the request that opened the session, not the last thing you touched: print it only when work happened, the ENTIRE originating request is satisfied and verified (every part of it, including scope added mid-session), nothing is left that the user must do, and the block carries no ⏳ or 🚫 line. Follow-ups you filed along the way do not count against it; anything the original request needed and did not get does. In a session with several threads in the air, the test runs against all of them. When unsure, end on 👉 or on no action line at all: a missing 🏁 costs nothing, a false one costs every 🏁 after it."}}
JSON
