# Gap ledger — <product name>

**Built:** <date> · **Last refresh:** <date or never> · **Filed to:** <repo / ledger only>

Every region that isn't from the design system, everything the local
system no longer supports the way the product uses it, and every hole.
One row per distinct gap. Rows merge on name across products.

## Not from the system

| Name | Seen in (this product) | Seen in (other products) | Nearest system component | Screenshot | Issue |
|---|---|---|---|---|---|
| Site header | Post, Home, Note, Page, 404 | we-are-here (1) | `ed-site-header` [verified], missing search slot | `gaps/site-header.png` | <#n / none> |

## Version drift

| Product used | Local now | Templates affected | What the story does | Issue |
|---|---|---|---|---|
| `ed-card variant="raised"` (0.59) | `variant` dropped in 0.63; `elevation="2"` | Home, Post | renders `elevation="2"` | |

## Missing components (placeholders)

| Name | Seen in | Why it's a hole | Screenshot | Issue |
|---|---|---|---|---|

## Totals

<n> not from the system · <n> version drift · <n> placeholders · <n> issues filed, <n> updated.
