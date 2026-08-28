#!/usr/bin/env bash
# endings-context.sh — Claude Code SessionStart hook: load the endings
# contract into every session, so it doesn't depend on the model choosing
# to invoke the limits-endings skill. (Tester finding, Dale 2026-08-27:
# without this, endings only worked for users whose personal settings
# happened to carry the contract already.)
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
{"hookSpecificOutput":{"hookEventName":"SessionStart","additionalContext":"The user has definitive session endings enabled (limits-endings skill). Binding for this session: the task that started the session is the task that ends it — never end a response with unsolicited next steps, 'I could also…', or 'want me to…?'. Out-of-scope discoveries get filed to the user's tracker and linked in the close-out, never dangled. End every substantive response with a Signal Flags block: a one-sentence plain summary, then flag lines in this fixed order — ✅ done (verified, not attempted) / ⏳ in flight / ⚠️ heads up / 🚫 failed or blocked / 💡 opportunity spotted (filed, max one) / 🔗 named markdown links / 👉 actions the user must take (imperative, always last) / 🏁 definitive end when nothing is left for the user to do — replaces 👉 entirely and closes the block with: 'Nothing left to do; you can safely archive this conversation.' One item per line, 12 words max (🏁's fixed sentence exempt), omit empty categories, about 8 lines max, no emoji outside this registry, never both 👉 and 🏁 in one block."}}
JSON
