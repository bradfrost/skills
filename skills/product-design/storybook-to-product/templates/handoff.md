# Handoff: <product name>

**Intake:** <date> · **Last catch-up:** <date or never>

## Source

| | |
|---|---|
| Stories | `<story IDs or Storybook section>` |
| Story files | `<design system repo>/<path>` on `<branch>` |
| Design system version the stories render on | `<x.y.z>` (`<branch>`, commit `<sha>`; contained in `<release branch / tag, or none yet>`) |
| Checkouts at intake | product: <current / behind <n> / dirty: <files>>; design system: <current / behind <n>>; <fetched / pulled / worked from what was there> |
| Product repo | `<path>` |
| Live URL | `<url or none>` |
| Product's pinned design system version | `<package@range>` from `<manifest>`; `<x.y.z>` in the lockfile |
| Product's own rules read | <CLAUDE.md / AGENTS.md / contributing guide / process config / none> |
| Sibling files read | <product-to-storybook/<product>/*, ds-adoption-plan/MAPPING.md, none> |

## Intake answers

| # | Question | Answer |
|---|---|---|
| 1 | Which stories? | <every story in `<section>` / the list> |
| 2 | Where's the product? | <above> |
| 3 | Content | <A field by field / B Storybook wins / C product wins / D: …> |
| 4 | Where the work lands | `<branch>` off `<base>`; previews: <yes, <host> / no> |

## Release gate

<n/a: every dependency is published / A wait / B local link: <what is linked, and how> / C released regions only>

## Existing connections

| Loop | Found | Notes |
|---|---|---|
| Story → product (fixture source) | <yes / no> | <where> |
| Usage reporting | <yes / no> | <workflow, endpoint> |
| Release propagation | <yes / no> | <receiver present in the product or not> |

## Login handling

<n/a / user signed in for <pages> / live check skipped for <pages>>

## Runs

| Date | Mode | Result |
|---|---|---|
| <date> | handoff | <3 pages, PR #<n>, REPORT.md> |
