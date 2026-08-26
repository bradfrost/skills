#!/usr/bin/env bash
# quiet-hours.sh — Claude Code PreToolUse hook: refuse tool calls inside
# the quiet hours the user set for themselves.
#
# Honest limits of this mechanism (see ENFORCEMENT.md):
#   - Blocks tool calls (the work), not model text (the answers).
#   - Hooks fail open by platform design: a timed-out or broken hook does
#     not block. This is a speed bump, not a wall.
#   - Overridable through a deliberate typed act (ai-limits override),
#     which is honored for 8 hours, logged, and counted — never refused.

DIR="${AI_LIMITS_DIR:-$HOME/.config/ai-limits}"
CONF="$DIR/config"
OVERRIDE="$DIR/state/override-quiet-hours"

[ -f "$CONF" ] || exit 0
# shellcheck disable=SC1090
. "$CONF"
[ -n "$QUIET_START" ] && [ -n "$QUIET_END" ] || exit 0

to_min() { IFS=: read -r h m <<EOF
$1
EOF
echo $((10#$h * 60 + 10#$m)); }

now=$((10#$(date +%H) * 60 + 10#$(date +%M)))
start=$(to_min "$QUIET_START")
end=$(to_min "$QUIET_END")

in_quiet=0
if [ "$start" -le "$end" ]; then
  [ "$now" -ge "$start" ] && [ "$now" -lt "$end" ] && in_quiet=1
else # window wraps midnight, e.g. 22:00-07:00
  { [ "$now" -ge "$start" ] || [ "$now" -lt "$end" ]; } && in_quiet=1
fi
[ "$in_quiet" -eq 1 ] || exit 0

# An override younger than 8 hours was a deliberate typed act, already
# logged by the CLI that created it. Honor it without comment.
if [ -f "$OVERRIDE" ] && [ -n "$(find "$OVERRIDE" -mmin -480 2>/dev/null)" ]; then
  exit 0
fi

cat >&2 <<MSG
Quiet hours ($QUIET_START-$QUIET_END): tool calls are paused per your own config.
To override deliberately: ~/.config/ai-limits/bin/ai-limits override quiet-hours --reason "why". Honored for 8 hours, logged, counted.
MSG
exit 2
