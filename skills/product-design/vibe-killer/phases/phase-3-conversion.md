# Phase 3 — Conversion

Write the page. The mapping table decided what goes where, so this phase is
execution and discipline rather than design.

**Output:** the converted page, wherever the user said it goes.

---

## Where it lands

**Default: one standalone, runnable page.** A single file that loads the
system's real runtime from the URLs in `SYSTEM.md` and renders in a browser
with no build step. Save it next to the autopsy at
`vibe-killer/kills/<date>-<slug>/`.

**Or into their repo, if they asked.** Then the project's conventions
outrank everything here: its template syntax, its file layout, its import
style, its naming. Read a neighboring page before you write a new one, and
never introduce a folder or pattern the project doesn't already use. Ask
where it goes rather than choosing for them.

Ask once, early. Don't build it twice.

---

## Boot the runtime first

Get the page loading the system before you write a single region. Section 2
of `SYSTEM.md` has the block. Load order almost always runs:

1. Tokens
2. Fonts for the active theme
3. The base or reset layer, if the system ships one
4. Components
5. Any light-DOM stylesheets that particular components need
6. The theme class or attribute on `<html>`

**Render one component and confirm it looks right before continuing.** Ten
seconds here saves an hour of debugging a page where nothing is styled
because the tokens loaded after the base layer that consumes them.

Two failure modes worth naming, because both are silent:

- **Fonts.** A theme's tokens usually just *name* a family. Load tokens
  without the theme's font stylesheet and every heading renders in a
  fallback serif, with no error anywhere.
- **Version drift.** If the runtime floats on a `latest` tag and the profile
  was captured weeks ago, the model composing your markup and the browser
  loading the components may disagree about what exists. Pin the version for
  anything you're going to present.

---

## Write it top to bottom

Follow the mapping table in document order. For each region:

1. Reach for the canonical composition in `SYSTEM.md` and **copy its
   skeleton**, wrappers and all.
2. Pour in the content from the autopsy, unchanged.
3. Set only the props the mapping named, with values the catalog allows.
4. Move on. Don't tune it visually yet.

**The rules, which are the whole point:**

- **Zero bespoke classes.** If you're naming a class, something upstream is
  wrong. Go back to the mapping.
- **Zero hardcoded values.** No hex, no rgb, no px, no rem, no font stacks.
  Everything comes from a token by its custom property.
- **Zero style overrides on system components.** An override is a gap in
  disguise. Name it as a gap instead.
- **Never invent a slot, a prop, or a prop value.** When you're unsure, go
  read the catalog again. Every single time.
- **Keep every wrapper.** They carry the contract, and grid item wrappers in
  particular are load-bearing even when they look redundant.
- **Semantic HTML underneath.** Real landmarks, real heading order starting
  at one `<h1>`, real buttons and links, real labels on form fields, real
  alt text. You're rebuilding the markup, so rebuild it correctly.

When you genuinely need an inline style for something dynamic, use the
system's custom properties and nothing else:

```html
<div style="padding: var(--ds-space-md); background: var(--ds-color-surface)">
```

---

## What to do when it doesn't fit

Three legitimate moves, and one that isn't.

**Legitimate:**
1. **Take the system's answer.** The section is 8px roomier than the
   original. Good. That's the system's spacing doctrine working.
2. **Use the nearest component and note the difference** in the receipt.
3. **Leave a marked placeholder** for a real gap, with a comment saying what
   belongs there and what was proposed upstream:

```html
<!-- VIBE-KILLER GAP: pricing toggle. No toggle-group component exists.
     Proposed upstream (not yet filed). Placeholder below is two buttons. -->
```

**Not legitimate:** writing the CSS yourself. That is the failure this skill
exists to prevent, it will be invisible in six months, and it converts the
page's problem into your design system's problem.

---

## Content discipline

- **Carry the words across exactly.** Same copy, same order, same headings.
- **Carry the unverifiable claims across too**, unchanged, because they're
  already flagged in the autopsy and the human decides. Never present an
  invented statistic as fact in your own prose about the page, and never
  quietly delete one either.
- **Add real alt text** where images had none, describing what the image
  shows. If it's a placeholder gradient standing in for a screenshot, say
  that in a comment rather than writing alt text for an image that doesn't
  exist.
- **Fix the links you can.** A footer of `href="#"` stays `href="#"`; you
  don't know where those go. But if the nav says "Pricing" and the page has
  a pricing section, wire it up.
- **Emoji standing in for icons** become real icons from the system's icon
  set. When nothing is close, use the system's generic icon and note it.

---

## Close the phase

> Page written: 9 regions, 11 components, 1 marked gap. Standalone file at
> `vibe-killer/kills/2026-09-10-saas-landing/index.html`. Proving it next.
