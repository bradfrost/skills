#!/usr/bin/env bash
# quiet-hours.sh — Claude Code PreToolUse hook: refuse tool calls inside
# the quiet hours declared in ~/.claude/healthy-limits.conf.
#
# Honest limits of this mechanism (see ENFORCEMENT.md):
#   - Blocks tool calls (the work), not model text (the answers).
#   - Claude Code hooks FAIL OPEN: a timed-out or broken hook does not block.
#     This is best-effort enforcement, not a guarantee.
#   - Overridable by a deliberate typed act, by design. The override is
#     honored, logged, and counted — never refused.

CONF="${HEALTHY_LIMITS_CONF:-$HOME/.claude/healthy-limits.conf}"
OVERRIDE="$HOME/.claude/healthy-limits-override"
LOG="$HOME/.claude/healthy-limits-overrides.log"
STAMP="$HOME/.claude/.healthy-limits-override-logged"

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

# A recent override (younger than 8h) is a deliberate typed act: honor it,
# log it once per act, never lecture.
if [ -f "$OVERRIDE" ] && [ -n "$(find "$OVERRIDE" -mmin -480 2>/dev/null)" ]; then
  if [ ! -f "$STAMP" ] || [ "$OVERRIDE" -nt "$STAMP" ]; then
    printf '%s override: %s\n' "$(date '+%Y-%m-%dT%H:%M:%S')" \
      "$(head -c 200 "$OVERRIDE" | tr '\n' ' ')" >> "$LOG"
    touch "$STAMP"
  fi
  exit 0
fi

cat >&2 <<MSG
Quiet hours ($QUIET_START-$QUIET_END): tool calls are paused per your healthy-limits config.
To override deliberately, write your reason to $OVERRIDE:
  echo "why you are choosing to continue" > $OVERRIDE
It will be honored for 8 hours, logged, and counted in your weekly report.
MSG
exit 2
