# The tells

A field guide to pages that came out of a prompt.

Models have taste, and it's remarkably consistent taste. Ask a dozen
different assistants for a landing page and you get a dozen versions of the
same page: violet gradient at the top, three cards with emoji in rounded
squares, a strip of big numbers nobody measured, a footer with four columns
of links that go nowhere. Once you can see it, you can't unsee it.

**This file is a decoder, not a hit list.** Every tell below carries a
"what it means" line, because that's the part you actually convert. A
gradient band is not a design requirement, it's a model reaching for the
only way it knows to say "this is the top of the page." The top of the page
is the thing you map. The gradient is an artifact.

Two rules for using this:

- **A tell is evidence, not a verdict.** Real designers use gradients.
  Plenty of hand-built pages have a three-up feature grid, because a
  three-up feature grid is a good pattern. What identifies a vibe-coded page
  is the *stack*: six or eight of these at once, all at their default
  values, with no CSS that couldn't have been generated.
- **Count them.** The count goes in the receipt, and the count is what makes
  a before/after persuasive. "This page had 14 of the 30 tells" lands
  harder than "this page was AI-generated."

---

## 1. The visual signature

### The violet gradient hero

**What you'll see:** A full-bleed band at the top of the page, usually
`linear-gradient(135deg, ...)`, running from indigo or violet through purple
into pink or blue. `#6366f1`, `#8b5cf6`, `#a855f7`, `#667eea`, `#764ba2` are
the recurring hex values. White text on top, centered, with one or two
buttons underneath.

**What it means:** This is the page's primary entry point. Map it to your
hero, banner, or page-header component. If your system doesn't have one,
that's a real gap worth naming, because most component libraries ship
nothing for page-level layout.

### Gradient text

**What you'll see:** `background-clip: text` with
`-webkit-text-fill-color: transparent` on the headline, or on two or three
words inside it.

**What it means:** Emphasis on a phrase. Your system almost certainly has an
opinion about how a headline gets emphasis, and it's almost certainly not
this. Use the system's heading component at the right level and let its
type scale carry the weight.

### Glassmorphism

**What you'll see:** `backdrop-filter: blur(10px)` with
`background: rgba(255, 255, 255, 0.1)` and a translucent 1px border. Usually
on cards sitting over the gradient, sometimes on a sticky header.

**What it means:** "This is a surface floating over something." Map it to
your card or surface component and take whatever elevation treatment your
system uses. Do not try to reproduce the blur unless your system ships it.

### The emoji icon tile

**What you'll see:** A 48px or 56px rounded square with a pastel background,
holding a single emoji, sitting above a small heading. Three or six of them
in a row. 🚀 ⚡ 🎯 🔒 📊 ✨ are the usual cast.

**What it means:** An icon slot, and the emoji is standing in for an icon
the model didn't have. Use your system's icon component with a real icon
name from your icon set. When your icon set has nothing close, say so in the
receipt rather than shipping the emoji, because emoji render differently on
every platform and get announced out loud by screen readers.

### The three-up feature grid

**What you'll see:** Three (occasionally four, occasionally six) equal cards
in a row, each with icon, then a heading, then two lines of body copy.
Collapses to one column at 768px if it's responsive at all.

**What it means:** A collection of peer items. This is the single most
common composition in the wild and the one that breaks most often on
conversion, because most grid components require an explicit item wrapper
around each child. Check that requirement in the catalog before you write
it. Cards dropped straight into a grid usually stack into one sad column,
and it looks like a CSS bug rather than a missing wrapper.

### The stat strip

**What you'll see:** Three or four big numbers with small labels
underneath. `10,000+ Users`, `99.9% Uptime`, `4.9★ Rating`, `24/7 Support`.
Frequently on a dark or tinted band.

**What it means:** A row of stat or metric tiles. Also: **these numbers are
almost always fabricated.** Flag every one of them in the receipt so a human
can replace or delete them. Never carry an invented statistic into a real
page just because it was in the source.

### Testimonials from nobody

**What you'll see:** Two or three quote cards, each with a circular avatar
holding two initials, a name, and a job title at a company that may not
exist. "Sarah Chen, Head of Product at TechFlow."

**What it means:** Same as above. Map the shape to your quote or testimonial
component, and flag every attribution as unverified. Fabricated endorsements
are a legal and ethical problem, not a copy problem.

### The pill badge above the headline

**What you'll see:** A small rounded capsule with a tiny dot or a sparkle,
reading `✨ Now in beta` or `🎉 v2.0 is here`, sitting directly above the
`<h1>`.

**What it means:** An eyebrow or badge. Check whether your hero or page
header already has a slot for this before you reach for a standalone badge
component.

### The dark-light-dark sandwich

**What you'll see:** Dark hero, white body, dark footer. Sometimes an
additional dark band around the call to action near the bottom.

**What it means:** Alternating section surfaces. Most systems handle this
with a variant or an inverted flag on a band or section component, not with
three hand-set background colors.

### Hover lift on everything

**What you'll see:** `transform: translateY(-4px)` and a heavier shadow on
card hover, with `transition: all 0.3s ease`.

**What it means:** Interactive affordance. Your card or link component has
its own hover treatment. Take it, drop this, and notice that `transition:
all` is one of the clearest fingerprints there is; almost nobody writes it
deliberately.

---

## 2. The CSS signature

Look at the source, not the render. These are the fastest confirmations.

- **A single `<style>` block, 200 to 600 lines**, holding the entire page's
  CSS, opening with `* { margin: 0; padding: 0; box-sizing: border-box; }`.
- **The Tailwind Play CDN** (`<script src="https://cdn.tailwindcss.com">`),
  frequently alongside hand-written CSS doing the same job twice.
- **The Tailwind default card**: `rounded-2xl shadow-lg border
  border-gray-200 p-6`, repeated on every card with no shared class.
- **A palette of four to eight hardcoded hex values**, indigo and violet and
  slate, repeated inline dozens of times rather than declared once. Count
  these. The count is your best single before/after number.
- **Inter, or a Google Fonts `<link>`**, usually Inter, Poppins, Plus Jakarta
  Sans, or Space Grotesk. Sometimes a bare `font-family: -apple-system,
  BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif` stack copied from a
  reset.
- **Suspiciously round numbers everywhere**: section padding of exactly
  `80px` or `5rem`, container `max-width: 1200px`, border radius of exactly
  `12px` or `16px`, gaps of exactly `2rem`.
- **Class names that describe appearance**, not meaning: `.gradient-bg`,
  `.card-hover`, `.big-text`, `.section-dark`, `.flex-center`.
- **A media query at 768px and nothing else.** Sometimes literally one.
- **Inline SVG icons lifted from Lucide or Heroicons**, pasted in full,
  often the same icon repeated four times with slightly different stroke
  widths.

---

## 3. The markup signature

- **Divs doing a button's job.** `<div class="btn" onclick="...">` with no
  `role`, no `tabindex`, no keyboard handler.
- **Headings chosen by size, not by level.** An `<h3>` following an `<h1>`
  because h3 looked right. Or worse, `<div class="heading">`.
- **No landmarks.** No `<header>`, `<nav>`, `<main>`, or `<footer>`, just
  a stack of sections and divs.
- **Every link goes to `#`.** A four-column footer of links, every one of
  them `href="#"`.
- **Images that are gradient divs**, or `<img>` tags pointing at
  `via.placeholder.com`, or an emoji standing in for a product screenshot.
- **`alt=""` on meaningful images**, or no `alt` attribute at all.
- **Repeated markup with no abstraction.** Three cards written out three
  times, character for character, because there was no component to reach
  for. This is the whole problem in miniature.

---

## 4. The copy signature

The words have tells too, and they matter because you're deciding what to
carry over.

- **The tricolon headline.** "Beautiful. Fast. Yours." Three words, three
  periods, no verb.
- **Em dashes stacked up.** Two or three in a single paragraph.
- **Empty superlatives with no object**: "seamless," "effortless,"
  "powerful," "intuitive," "beautifully designed," "blazing fast."
- **"Everything you need to..."** as a section heading, roughly always.
- **Feature copy in exactly two lines**, every card the same length, because
  the model was balancing the layout rather than saying something.
- **Sparkles as punctuation.** ✨ prefixing headings and button labels.
- **A call to action that promises nothing specific**: "Get Started Free" /
  "No credit card required" on a page for something that doesn't exist yet.

**What to do with this:** Nothing, unilaterally. Carry the copy across as
written and list the tells in the receipt under a heading the human can act
on. Rewriting somebody's words while claiming you converted their page is a
different job that nobody asked you to do.

---

## 5. What's missing (the accessibility signature)

Vibe-coded pages fail in a consistent pattern, and it's worth checking each
one explicitly because you're rebuilding the markup anyway:

- No visible focus styles, often `outline: none` with nothing replacing it
- No skip link
- Contrast that was never checked, especially white or light-gray text on a
  mid-tone gradient
- Heading levels that skip or repeat
- Interactive elements that aren't reachable by keyboard
- No `lang` on `<html>`
- Form fields with placeholder text instead of labels
- Icon-only buttons with no accessible name
- Animation with no `prefers-reduced-motion` guard

Every one of these that your system's components fix for free is a line in
the receipt, and collectively they're the most persuasive argument in it.

---

## 6. Things that look like tells but aren't

Be fair. Don't report these as evidence:

- **A three-up grid.** It's a good pattern with a long history.
- **A gradient.** Designers use gradients on purpose all the time.
- **Inter.** It's a genuinely excellent typeface that many real teams chose
  deliberately.
- **Tailwind in a build.** A Tailwind project with a config, a build step,
  and a shared component layer is a real project with a real system. The
  Play CDN script tag is the tell, not the framework.
- **A page that's just simple.** Not every plain page came from a model.
  Some pages are plain because somebody made them plain.

If your evidence is one item from this section, you don't have evidence. Say
so, and convert the page anyway if that's what was asked, since a page
carrying bespoke CSS is worth moving onto the system regardless of who
typed it.

---

## Using this in phase 1

For each tell you find, write one row:

| Tell | Where | What it means | Maps to |
|---|---|---|---|
| Violet gradient hero | `index.html:41-68` | Page entry point | `[phase 2]` |
| Emoji icon tiles ×3 | `index.html:88-140` | Icon slot in a card | `[phase 2]` |
| 47 hardcoded hex values | throughout `<style>` | Color tokens | `[phase 2]` |

Leave "maps to" empty until phase 2 fills it. The count at the bottom of
this table is the number that opens the receipt.
