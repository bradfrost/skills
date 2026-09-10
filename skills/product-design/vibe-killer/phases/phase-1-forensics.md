# Phase 1 — Forensics

Read the page. Work out what it's made of and, more importantly, what each
part of it is *for*. You are not judging the page here, you're taking
inventory so phase 2 has something real to map.

**Output:** the top half of `vibe-killer/kills/<date>-<slug>/autopsy.md`.

---

## Get the source

Best available, in this order:

1. **A file or a paste.** The whole HTML, ideally with its CSS. Best case.
2. **A URL you can fetch.** Get the served HTML plus any linked stylesheets.
   Read the CSS, not just the markup; roughly half of the tells live there.
3. **A URL you can render.** Some pages are empty HTML shells that build
   themselves in JavaScript. If you have a browser tool, load it and read
   the rendered DOM. If you don't, say so now rather than converting a
   skeleton.
4. **A screenshot.** Workable, and worse than it sounds. You'll get layout
   and content and you will not get markup, class names, hardcoded values,
   or any accessibility signal. Everything in the autopsy becomes
   `[reported]` and the receipt's before-numbers become estimates. Say this
   out loud rather than producing counts that look measured.

**When you can't reach it at all, stop and say so.** Pages behind auth, an
app that needs a login, a Figma prototype, a video of a page. Ask for a file
or a screenshot instead of guessing at what's probably there.

Record the source and its fidelity at the top of the autopsy. Every number
downstream inherits it.

---

## Catalog the tells

Work through `reference/THE-TELLS.md` and record every hit. One row each:

| Tell | Where | What it means |
|---|---|---|

Then get the deterministic counts, because these are the before-numbers that
make the receipt land. If you can run commands, count them; if you're
reading a paste, count them by hand and say which.

- **Hardcoded color values.** Hex, `rgb()`, `hsl()`, and named colors, in
  CSS and in inline styles and in `<svg fill>`.
- **Hardcoded lengths.** `px` and `rem` values in spacing, sizing, and
  radius.
- **Bespoke class names.** Distinct classes defined in the page's own CSS.
- **Font declarations.** `font-family` rules plus any Google Fonts `<link>`
  or `@import`.
- **Total CSS lines** the page ships that aren't a framework's.
- **Elements with no accessible name**, interactive elements that aren't
  focusable, and heading-level jumps.
- **`!important` count**, when there is one. It's a good proxy for how much
  the page was fighting itself.

Handy starting points when you have a shell:

```bash
# every color value, ranked by how often it repeats
grep -oE '#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)' page.html | sort | uniq -c | sort -rn

# distinct class names the page's own CSS defines
grep -oE '^\s*\.[a-zA-Z][a-zA-Z0-9_-]*' page.html | tr -d ' .' | sort -u | wc -l

# hardcoded lengths
grep -oE '[0-9.]+(px|rem|em)\b' page.html | wc -l

# font declarations and any web-font link
grep -oE 'font-family|fonts\.googleapis' page.html | wc -l
```

**Use `grep -o … | wc -l`, not `grep -c`.** `grep -c` counts *matching
lines*, so a minified stylesheet or a footer with four links on one line
reports 1 when the real answer is 4. That mistake makes the before-numbers
quietly too small, which is the wrong direction to be wrong in.

Adjust for the page. The exact regex matters less than getting a real number
you can defend, and a class-name count in particular needs a second look
when the CSS is minified onto one line.

---

## Map the regions

This is the part that actually feeds phase 2. Walk the page top to bottom
and write one row per region, in document order:

| # | Region | What it's for | Content it carries | Notes |
|---|---|---|---|---|
| 1 | Sticky top bar | Site navigation | Logo, 4 nav links, 1 CTA button | Links all `href="#"` |
| 2 | Gradient band | Page entry point | H1, one line of body copy, 2 buttons | Contrast unchecked |
| 3 | Icon card row | Three peer feature summaries | 3 × (emoji, h3, 2 lines) | Emoji standing in for icons |

**"What it's for" is the column that matters.** Write it in plain language,
describing the job, not the appearance. "Three peer feature summaries" is
convertible. "Purple cards with rounded corners" is not.

Some judgment calls that come up every time:

- **A region doing two jobs** gets two rows. A hero with a signup form
  inside it is an entry point plus a form, and those map to different
  components.
- **Decorative-only regions** (a divider made of gradient blobs, a spacer
  div) get a row with "decorative" in the notes. Most will be deleted in
  phase 2, and deleting something is a decision that should be visible.
- **Repeated markup** gets one row with a count, not N rows. Three
  hand-written identical cards are one pattern that happened three times,
  and saying so is half the argument for the conversion.

---

## Flag the content

Two lists the human will want, kept separate from everything else:

**Unverifiable claims.** Every statistic, testimonial, logo, name, award,
and press mention. Vibe-coded pages invent these freely and they read as
real. Carry them across as written, and put every one in this list so a
person decides what happens to them. Never present an invented number as a
fact in a converted page and never quietly delete one either.

**Copy tells.** The tricolon headline, the empty superlatives, the sparkles.
Note them, don't touch them. Rewriting the words is a different job.

---

## Close the phase

One line to the user, with real numbers:

> Forensics done: 14 of 30 tells, 47 hardcoded colors, 31 bespoke classes,
> 9 regions, 0 focus styles, 4 unverifiable claims. Mapping next.

Then ask the posture question from `SKILL.md` if you haven't yet, and record
the answer at the top of the autopsy.
