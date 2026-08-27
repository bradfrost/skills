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

# Sum the floor estimates from the last 7 days of ledger lines:
#   2026-08-27  wh=3+  turns=8  context
cutoff=$(date -v-6d +%Y-%m-%d 2>/dev/null || date -d '6 days ago' +%Y-%m-%d)
total=0
while read -r d whf _; do
  [ -n "$d" ] || continue
  [ "$d" \< "$cutoff" ] && continue
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

cat >&2 <<MSG
Energy budget ($ENERGY_BUDGET_WH_WEEK Wh/week): this week's floor estimate is ${total}+ Wh, past the budget you set. Pausing per your own config.
These are rough estimates, and this gate is yours: to override, run ~/.config/ai-limits/bin/ai-limits override energy-budget --reason "why". Honored for 8 hours, logged, counted.
MSG
exit 2
