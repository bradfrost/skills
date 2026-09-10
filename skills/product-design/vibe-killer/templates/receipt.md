# Receipt — <page name>

**<One-sentence headline with the real numbers.>**
*Example: 47 hardcoded values, 31 bespoke class names and 412 lines of CSS
became 11 components, 12 tokens and 0 lines of custom CSS.*

**System:** <name> @ <version> · **Posture:** <A | B> · **Date:** <date>
**Converted page:** `<path>` · **Autopsy:** `./autopsy.md`

---

## Before / after

| Measure | Before | After |
|---|---|---|
| Bespoke CSS class names | | 0 |
| Hardcoded color values | | 0 |
| Hardcoded lengths | | 0 |
| Font declarations | | 0 |
| Lines of custom CSS | | 0 |
| Design system components | 0 | |
| Design tokens in use | 0 | |
| Themeable | no | <yes, N themes> |

<If any "after" number isn't 0, it's named in "Still bespoke" below with a
reason. No exceptions.>

---

## Components used

| Component | Count |
|---|---|

**Evidence:** <n> of <n> mappings verified against the live catalog.
<If a meaningful share is `[reported]`, say so here, in the first screenful.>

---

## Accessibility fixed on the way through

| Was | Now |
|---|---|
| No focus styles (`outline: none`) | System focus treatment on every interactive element |
| `<div onclick>` × 4 | Real buttons, keyboard reachable |
| h1 → h3 → h2 | One h1, sequential levels |
| 3 images with no alt | Alt text written |
| No landmarks | `header` / `nav` / `main` / `footer` |

---

## Still bespoke

Everything the system didn't cover, named. This section being empty is a
great outcome; this section being *missing* is a broken receipt.

| What | Why | What's there now | Proposed upstream |
|---|---|---|---|

---

## Content a human needs to decide about

**Unverifiable claims carried across unchanged:**

<Every statistic, testimonial, logo and name from the original. These read as
real and were very likely invented. Nothing was deleted and nothing was
verified.>

**Copy tells noted, not touched:**

---

## What was proven, and what wasn't

| Check | Result |
|---|---|
| System validator | <output, or "no validator exists for this system"> |
| Rendered in a browser | <yes, at 320 / 768 / 1280, or **not rendered, and why**> |
| Deterministic counts | <measured, or estimated from a screenshot> |
| Contrast | <measured, or relying on the system's tested token pairs> |
| Automated a11y check | <output, or none available> |

---

## What to do next

1. <The one thing to look at first.>
2. <Whether to file the gap issues. This is the human's call.>
3. <Where this page should actually live, if it's still sitting in `kills/`.>
