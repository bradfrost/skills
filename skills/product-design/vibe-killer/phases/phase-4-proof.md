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

If there is no validator, say so in the receipt in one line. Missing tooling
is a finding about the system, not something to paper over.

---

## 2. Render it

Open it. Look at it. If you have a browser tool, load the page, screenshot
it, and check at a narrow width too, since vibe-coded originals are usually
tested at exactly one desktop size and a converted page shouldn't inherit
that.

Watch for:

- Anything that didn't render at all. Empty regions are the signature of a
  slot name that doesn't exist, so go back to the catalog for that component.
- Unstyled text, which usually means tokens loaded in the wrong order or the
  theme class is missing.
- Fallback serif type, which means the theme's fonts didn't load.
- Anything wider than the viewport at 320px.

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
- Contrast: if you can measure it, measure it. If you can't, say which pairs
  you're relying on the system's tokens for, since a token pair the system
  ships and tests is genuinely stronger evidence than an eyeballed guess.

If you have an automated checker, run it and paste the output.

---

## 5. Write the receipt

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

## 6. Close it out

Show the user:

1. The headline number. Something like: *"47 hardcoded values, 31 bespoke
   classes, and 400 lines of CSS became 11 components, 12 tokens, and 0
   lines of custom CSS."*
2. Where the page is, and how to run it.
3. The gap list, with the drafted issues, and a direct question about
   whether to file them.
4. Anything you couldn't prove.

Then stop. The conversion is done. If they want another page, that's another
run.

---

## The honesty floor

Three things this phase must never do, because each of them makes every
future receipt worthless:

- **Report a count you estimated as if you measured it.** Say "estimated
  from a screenshot" when that's what happened.
- **Claim the page renders when you never rendered it.**
- **Report zero bespoke CSS when a gap got quietly hand-rolled.** If you
  wrote a rule, it's in the receipt.
