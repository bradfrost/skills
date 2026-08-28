#!/usr/bin/env bash
# energy-gate.sh — Claude Code UserPromptSubmit hook: the OPT-IN energy
# budget gate. Inert unless the user chose ENERGY_BUDGET_MODE=restrict in
# the limits-setup interview, eyes open about what the number is.
#
# Honest limits of this mechanism (see limits-setup ENFORCEMENT.md):
#   - The budget compares against FLOOR ESTIMATES, not measurements.
#   - This is the softest of the three gates: quiet hours read the clock
#     and the session gate reads hook-written state, but this one reads a
#     ledger the AI itself writes at session ends — real enforcement fed
#     by best-effort data.
#   - Hooks fail open by platform design. Overridable by a deliberate
#     typed act via the CLI — honored, logged, counted, never refused.

DIR="${AI_LIMITS_DIR:-$HOME/.config/ai-limits}"
CONF="$DIR/config"
LEDGER="$DIR/state/energy-ledger.log"
OVERRIDE="$DIR/state/override-energy-budget"

[ -f "$CONF" ] || exit 0
# shellcheck disable=SC1090
. "$CONF"
[ "${ENERGY_BUDGET_MODE:-}" = "restrict" ] || exit 0
case "${ENERGY_BUDGET_WH_WEEK:-}" in (*[!0-9]*|'') exit 0 ;; esac
[ "${AI_LIMITS_AUTOMATION:-}" = "1" ] && exit 0
[ -f "$LEDGER" ] || exit 0

# The budget week is fixed, not rolling: it starts Monday at the day
# boundary (default 4AM) and resets the following Monday, so the refusal
# can name the reset moment.
bh=4
case "${DAY_BOUNDARY:-}" in
  [0-9][0-9]:[0-9][0-9]|[0-9]:[0-9][0-9]) bh=$((10#${DAY_BOUNDARY%%:*})) ;;
esac
if [ "$((10#$(date +%H)))" -lt "$bh" ]; then
  today=$(date -v-1d +%Y-%m-%d 2>/dev/null || date -d yesterday +%Y-%m-%d)
else
  today=$(date +%Y-%m-%d)
fi
dow=$(date -j -f %Y-%m-%d "$today" +%u 2>/dev/null || date -d "$today" +%u)
weekstart=$(date -j -v-$((dow-1))d -f %Y-%m-%d "$today" +%Y-%m-%d 2>/dev/null || date -d "$today -$((dow-1)) days" +%Y-%m-%d)
resetday=$(date -j -v+7d -f %Y-%m-%d "$weekstart" "+%a %b %d" 2>/dev/null || date -d "$weekstart +7 days" "+%a %b %d")

# Sum the floor estimates from this week's ledger lines:
#   2026-08-27  wh=3+  turns=8  context
total=0
while read -r d whf _; do
  [ -n "$d" ] || continue
  [ "$d" \< "$weekstart" ] && continue
  n=${whf#wh=}
  n=${n%+}
  case "$n" in (*[!0-9]*|'') continue ;; esac
  total=$((total + n))
done < "$LEDGER"

[ "$total" -ge "$ENERGY_BUDGET_WH_WEEK" ] || exit 0

# A recent override (younger than 8h) was a deliberate typed act, already
# logged by the CLI that created it. Honor it without comment.
if [ -f "$OVERRIDE" ] && [ -n "$(find "$OVERRIDE" -mmin -480 2>/dev/null)" ]; then
  exit 0
fi

# No command paths in the refusal — see sessions-gate.sh for why.
cat >&2 <<MSG
🌍 You reached your weekly energy budget of $ENERGY_BUDGET_WH_WEEK Wh, which means tool calls are paused until the budget resets at ${bh}AM $resetday.

(You can adjust your settings if needed)
MSG
exit 2
