# Handoff report: <product name>

**<Ready to ship / Blocked on the design system release: <components>>**

<n> pages · <n> regions (<n> carried, <n> adapted, <n> retired, <n> kept) · <n> behaviors (<n> restored, <n> rebuilt, <n> new, <n> retired) · <n> content fields (<n> decided by you) · <n> assets · design system `<old>` → `<new>` · PR <link> · preview <link or none>

## What was proven

| Check | Result |
|---|---|
| Product build, from clean | <pass / fail> |
| Product tests and linters | <pass / none exist> |
| Storybook leak search (markers, scope, invented values) | <0 hits / n fixed> |
| Rendered in a browser, viewport confirmed | <yes, <width>px and <width>px / not rendered> |
| Every behavior exercised | <n of n; how> |
| Forms | <tested against <test setup> / checked up to the request, not submitted> |
| Axe | <0 violations / n, filed> |
| Pages the version bump touched | <n checked, n regressions> |
| Person looked at every page | <yes / no: nobody has looked yet> |

## Side by side

One section per page: the story and the product at each width, differences labeled.

### <page>

| Story | Product |
|---|---|
| ![](<story screenshot>) | ![](<product screenshot>) |

- **Content decision:** <difference> (CONTENT.md, <row>)
- **Integration error, fixed:** <difference>

## Accessibility fixed on the way in

| Bug (from product-to-storybook's ledger or axe) | Fix |
|---|---|
| <rule, where> | <what changed> |

## Filed to the design system

| Finding | Issue |
|---|---|
| <violation or gap inside a system component> | <link> |

## Connections

| Loop | Status |
|---|---|
| Link record (`storybook-to-product/links.json`) | <n stories, story commit `<sha>`> |
| Usage reporting | <runs / not set up> |
| Release propagation | <receiver present / missing: the next release will not reach this product on its own> |
