# Phase 4 — Proof

A converted page you never checked is a claim. This phase turns it into a
result, or says honestly that it couldn't.

**Output:** `vibe-killer/kills/<date>-<slug>/receipt.md`, from
`templates/receipt.md`.

---

## 1. Run the system's own validator

If `SYSTEM.md` section 6 recorded one, run it now and paste the real output
into the receipt. A design system's own validator knows things no generic
check can: its slot contracts, its anti-patterns, its placement rules.

Fix what it flags, then run it again. Never report a validator's complaint
as "expected" without saying why.

**A clean validator is necessary, not sufficient.** Validators check how the
markup is written: slot names, anti-patterns, placement rules. They can't
see a caption rendering as a black bar or a paragraph sitting right on top
of its buttons. Don't lead the receipt with a clean run.

If there is no validator, say so in the receipt in one line. Missing tooling
is a finding about the system, not something to paper over.

---

## 2. Render it

Open it. Look at it. If you have a browser tool, load the page, screenshot
it, and check at a narrow width too, since vibe-coded originals are usually
tested at exactly one desktop size and a converted page shouldn't inherit
that.

**Confirm the renderer before you trust a single number from it.** Some
browser tools run hidden or headless, and a hidden page can report a 0px
viewport, skip repainting after a scroll, never fire an
`IntersectionObserver`, or hand you a stale snapshot after a reload. Every
measurement still comes back looking plausible. Before you record anything,
check that:

- the viewport width is the width you asked for, not 0
- the element count is roughly what the source holds (a page with 200
  components shouldn't report 11)
- the page reflects your last edit, not a cached copy

When the renderer fails those checks, say so, and read the source directly
for anything structural. A heading outline, a slot contract, and a nesting
check can all be verified from the file without a browser.

Watch for:

- Anything that didn't render at all. Empty regions are the signature of a
  slot name that doesn't exist, so go back to the catalog for that component.
- Unstyled text, which usually means tokens loaded in the wrong order or the
  theme class is missing.
- Fallback serif type, which means the theme's fonts didn't load.
- Anything wider than the viewport at 320px.
- Siblings with no space between them. Measure the gap between adjacent
  elements in each region. 0px almost always means the element that owns the
  spacing isn't the direct parent anymore, because something got wrapped
  around the content.
- Every region that got a catalog correction in phase 2. Look at each one,
  then mark the correction confirmed or overturned in the autopsy.

**If you cannot render in this environment, say exactly that in the
receipt.** Do not imply a page works because it looks right in source. This
is the single easiest place in the whole procedure to quietly overstate, and
the receipt is worth less than nothing if it does.

---

## 3. Count what changed

These are deterministic and they're what makes the receipt persuasive. Run
them against the converted page:

```bash
# Hardcoded colors: should be 0
grep -oE '#[0-9a-fA-F]{3,8}\b|rgba?\([^)]*\)|hsla?\([^)]*\)' converted.html | wc -l

# Hardcoded lengths outside var(): should be 0
grep -oE '[0-9.]+(px|rem|em)' converted.html | wc -l

# Font declarations: should be 0
grep -oE 'font-family|fonts\.googleapis' converted.html | wc -l

# Token usage: should be the only styling in the file
grep -oE 'var\(--<prefix>[a-z0-9-]+\)' converted.html | sort | uniq -c | sort -rn

# System components used
grep -oE '<ds-[a-z-]+' converted.html | sort | uniq -c | sort -rn
```

Swap in the real prefix and tag pattern from `SYSTEM.md`. Adapt for a
class-based or React system; the point is a real number, not this exact
regex. Count occurrences with `grep -o … | wc -l` rather than `grep -c`,
which counts matching lines and will happily report 1 for a minified file
holding forty violations.

**Any non-zero count in the first three is a bug in your conversion, not a
result to report.** Go fix it before writing the receipt. The one exception
is a marked gap placeholder, and it has to be marked in the code and named
in the receipt.

---

## 4. Check accessibility

Walk the list, because these are the wins the original almost certainly
didn't have:

- One `<h1>`, no skipped levels
- Real landmarks: `header`, `nav`, `main`, `footer`
- Every interactive element reachable and visibly focused by keyboard
- Every image has alt text, or is properly marked decorative
- Every form field has a real label
- Icon-only buttons have accessible names
- `lang` on `<html>`
- Line length: long prose stays under about 80 characters per line. That's
  WCAG 1.4.8 (a AAA criterion, and a good default at any level). Measure the
  widest paragraph at desktop width; anything wider belongs in the system's
  reading-width container
- Contrast: if you can measure it, measure it. If you can't, say which pairs
  you're relying on the system's tokens for, since a token pair the system
  ships and tests is genuinely stronger evidence than an eyeballed guess.

If you have an automated checker, run it and paste the output.

---

## 5. Have a person look at it

Everything above can pass on a page a person would reject in seconds. So
before the receipt is final, put the rendered page in front of a human.

Send screenshots region by region, at desktop and narrow widths, and ask
them to scan for anything that looks wrong: text jammed against an edge,
type that doesn't match its job, spacing that collapsed, a treatment that
doesn't fit the region. If nobody is available, say that in the receipt's
proof table. "No human review" is a legitimate result; leaving the row out
is not.

Fix what they find. When a problem traces back to the system itself, draft
it as a gap like any other.

---

## 6. Write the receipt

Fill in `templates/receipt.md`. It has to carry, at minimum:

- **The before/after table** with the real counts from phase 1 and step 3
- **The posture** that was chosen, and one line on what it meant
- **The evidence position**: how many mappings were `[verified]`
- **Components used**, with counts
- **What's still bespoke**, every gap and every placeholder, named
- **Accessibility fixed**, itemized
- **Content flagged**, the unverifiable claims list, carried forward
- **What wasn't proven**, plainly. Anything you couldn't render, validate,
  or measure

---

## 7. Close it out

Show the user:

1. The headline number. Something like: *"47 hardcoded values, 31 bespoke
   classes, and 400 lines of CSS became 11 components, 12 tokens, and 0
   lines of custom CSS."*
2. Where the page is, and how to run it.
3. The gap list, with the drafted issues, and a direct question about
   whether to file them.
4. Anything you couldn't prove.
5. What the human review turned up, and what changed because of it.

Then stop. The conversion is done. If they want another page, that's another
run.

---

## The honesty floor

Four things this phase must never do, because each of them makes every
future receipt worthless:

- **Report a count you estimated as if you measured it.** Say "estimated
  from a screenshot" when that's what happened.
- **Claim the page renders when you never rendered it.**
- **Report zero bespoke CSS when a gap got quietly hand-rolled.** If you
  wrote a rule, it's in the receipt.
- **Count a catalog correction as a win before you've looked at the
  region.** Until it renders the way the catalog promised, it's a claim.
