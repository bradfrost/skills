# Assessment: <product name>

**Date:** <date> · **Stories:** <n> · **Product pages:** <n> · **Confirmed by the user:** <date or pending>

> <The checkpoint paragraph from phase 1, section 7, with real numbers.>

## Story → page map

| Story | Product template | Includes it touches |
|---|---|---|
| `<story id>` | `<file>` | `<partials>` |

## Regions

One table per page, in render order.

### <page>

| # | Region | Disposition | What changes | Effort | Needs |
|---|---|---|---|---|---|
| 1 | <name> | Carry / Adapt / Retire / Keep | <one line> | XS–L | <dependency rows, behavior rows> |

## Retirements

Every row needs the user's explicit yes.

| Region | What goes with it (CSS, scripts, backend) | Anything else that uses those? | Confirmed |
|---|---|---|---|
| <name> | <files> | <no / yes: where> | <yes / no / pending> |

## System dependency ledger

| Component / recipe / token | Prop or variant that matters | State | Regions |
|---|---|---|---|
| `<name>` | `<prop>` | installed / published (bump to `<x.y.z>`) / unreleased (`<branch>`) / new dependency | <#s> |

## Behavior inventory

| Behavior | Trigger → target | Status | Source | Effort |
|---|---|---|---|---|
| <what it does> | `<trigger>` → `<target>` | Restore / Rebuild / New / Retire | <story comment, script, component state> | XS–L |

## Story comments collected

Verbatim, with file and line. Every "dropped", "cut", and "stays closed" is here.

- `<file>:<line>` <comment>

## Estimate

| | Regions | Behaviors | Total |
|---|---|---|---|
| Ready now | | | |
| Blocked on the release | | | |
