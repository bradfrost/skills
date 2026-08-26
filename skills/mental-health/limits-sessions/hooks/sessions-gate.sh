#!/usr/bin/env bash
# sessions-gate.sh — Claude Code UserPromptSubmit hook: enforce the
# sessions-per-day ceiling the user set for themselves.
#
# How it counts: a session is "used" the first time you prompt in it —
# opening a session you never use costs nothing. Sessions admitted earlier
# today keep working. Session N+1 gets a terse, identical refusal on every
# prompt. A raised limit takes effect in NEW sessions only: a session
# refused today stays refused today.
#
# Honest limits of this mechanism (see ENFORCEMENT.md):
#   - Hooks fail open by platform design; this is a speed bump, not a wall.
#   - The user can always edit their own config. That's the point:
#     drifting past a limit should be deliberate, never frictionless.

DIR="${AI_LIMITS_DIR:-$HOME/.config/ai-limits}"
CONF="$DIR/config"
STATE="$DIR/state"

[ -f "$CONF" ] || exit 0
# shellcheck disable=SC1090
. "$CONF"

# Identify this session from the hook's stdin JSON; fail open if we can't.
input=$(cat 2>/dev/null)
sid=$(printf '%s' "$input" | sed -n 's/.*"session_id"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
[ -n "$sid" ] || exit 0

mkdir -p "$STATE"

# The limits day rolls over at DAY_BOUNDARY (default 04:00), not midnight,
# so a late-night session belongs to the day it started.
bh=4
case "$DAY_BOUNDARY" in
  [0-9][0-9]:[0-9][0-9]|[0-9]:[0-9][0-9]) bh=$((10#${DAY_BOUNDARY%%:*})) ;;
esac
if [ "$((10#$(date +%H)))" -lt "$bh" ]; then
  day=$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d yesterday +%Y-%m-%d)
else
  day=$(date +%Y-%m-%d)
fi

SESSIONS="$STATE/sessions-$day"
REFUSED="$STATE/refused-$day"
touch "$SESSIONS"

refuse() {
  grep -qxF "$sid" "$REFUSED" 2>/dev/null || echo "$sid" >> "$REFUSED"
  used=$(sort -u "$SESSIONS" | wc -l | tr -d ' ')
  cat >&2 <<MSG
You set a limit of $SESSIONS_PER_DAY sessions per day; all $used are used. This session stays closed.
The count resets at $(printf '%02d:00' "$bh"). To change the limit: edit ~/.config/ai-limits/config or run ~/.config/ai-limits/bin/ai-limits raise. Either way it takes effect in a new session, not this one.
MSG
  exit 2
}

# A session refused today stays refused today, even if the limit was raised.
if grep -qxF "$sid" "$REFUSED" 2>/dev/null; then
  refuse
fi

# Sessions already admitted today keep working.
grep -qxF "$sid" "$SESSIONS" 2>/dev/null && exit 0

# No ceiling set = measure first: count honestly, never block.
if [ -z "$SESSIONS_PER_DAY" ]; then
  echo "$sid" >> "$SESSIONS"
  exit 0
fi

used=$(sort -u "$SESSIONS" | wc -l | tr -d ' ')
if [ "$used" -lt "$SESSIONS_PER_DAY" ]; then
  echo "$sid" >> "$SESSIONS"
  exit 0
fi
refuse
