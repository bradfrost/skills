# What this skill can and can't do

Read this before promising anybody a result. Every limit here is real and
each one has a workaround or an honest thing to say instead.

---

## It can

- Convert a page it can read: a pasted file, a fetched URL, a rendered DOM,
  or (with real caveats) a screenshot.
- Work against any design system it can reach through the evidence chain,
  including one it's never seen. That's what the profile is for.
- Produce a standalone runnable page, or write into a repo in that project's
  own conventions.
- Count what changed, deterministically, and show the before/after.
- Find real gaps in a design system and draft the proposals.
- Fix the accessibility failures the original was carrying.

## It can't

- **See a page it can't reach.** Behind auth, inside an app, in a Figma
  prototype, in a video. Ask for a file or a screenshot instead of guessing.
- **Read markup from a screenshot.** You'll get layout and content; you will
  not get class names, hardcoded values, slot usage, or any accessibility
  signal. The before-numbers become estimates and the receipt has to say so.
- **Verify what a page looks like without a browser.** Source that reads
  correctly is not a rendered page. When there's no browser in the
  environment, the receipt says "not rendered" and means it.
- **Trust a browser that isn't really rendering.** A hidden or headless
  browser can report a 0px viewport or serve a stale snapshot and still hand
  back plausible numbers. Phase 4 confirms the renderer first, and reads the
  source instead when it can't.
- **Tell you the page looks right.** Validators and DOM checks confirm how
  the page is built, not whether it looks correct. A person has to look
  before the receipt calls it done.
- **Invent a component the system doesn't have.** By design. That's a gap,
  and naming it is the useful output.
- **Know a system it can't read.** With no catalog access, every mapping is
  `[reported]` and the conversion inherits that. Still worth doing, still has
  to say so.
- **Decide what happens to invented content.** Fabricated statistics and
  testimonials get carried across and flagged. A human decides.
- **Rewrite the page's copy.** Different job, and nobody asked for it.
- **File issues on its own.** Gaps get drafted. Filing is the human's call.

---

## Where it degrades, and what to say

| Situation | What still works | What to say |
|---|---|---|
| No catalog access | Full conversion from an interview | "Every component name here is `[reported]`. Verify before shipping." |
| Screenshot only | Regions, content, mapping, conversion | "Before-numbers are estimates. No markup or a11y signal was available." |
| No browser | Everything through phase 3, plus the greps | "Not rendered. Counts are from source." |
| Browser that isn't really rendering | Structural checks from source: heading outline, slots, nesting | "The browser couldn't be trusted, so these checks came from source." |
| No person to review it | Everything automated | "No human review. Nobody has looked at this page yet." |
| No validator | The deterministic counts | "This system ships no validator. Counts are grep-based." |
| JS-rendered page, no browser | Nothing useful | Stop. Ask for the rendered HTML or a screenshot. |

---

## The one thing that makes a run worthless

Reporting an estimate as a measurement, or a page as working when it was
never rendered. Every number in a receipt is a number somebody might repeat
in a meeting. If it isn't real, label it.
