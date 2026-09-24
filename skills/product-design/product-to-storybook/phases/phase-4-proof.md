# Phase 4 — Proof

Render everything, compare it to the live product, prove the system's own
stories didn't change, finish the gap ledger, and write the report. A story
you never rendered is a claim, not a result.

**Output:** `product-to-storybook/<product>/GAPS.md` (finished),
`product-to-storybook/<product>/REPORT.md`, and any issues the intake
asked for.

---

## 1. Confirm the renderer

Before trusting a single screenshot, confirm the browser is really
rendering: a viewport of a known width, an element count that matches what
the story should contain. A headless browser reporting a 0px viewport hands
back plausible screenshots of nothing. If you have no browser, the report
says "not rendered" and every check below is done from source, and it says
that too.

## 2. Every story renders

Open each story. It renders with no console errors, every fixture field
lands somewhere on screen, and no region is empty that shouldn't be. An
empty region with no error is the classic symptom of a slot name that
doesn't exist locally, so check the version-drift entries first when you
see one.

**Restart the Storybook dev server before this phase** if you added story
files after it booted. Storybook's watcher missed every file created after
boot in the Eddie run; the stories only existed in `index.json` after a
restart.

**When axe fails, where it fails decides what happens.** A failure inside a
`data-origin="product"` region is the product's: exclude that selector for
that story (`parameters.a11y.context.exclude = ['[data-origin="product"]']`),
name the rule in a comment, and file it to the product. A failure inside a
system region is the system's: keep the story gated on everything else, run
it at `test: 'todo'` so the violation stays visible, and file it to the
system. Never "fix" the markup to pass in either case. (Eddie: the hub's
Court story and `ed-r-chunky-checkbox`'s hardcoded `<h3>`, #2170.)

**Look at every Default screen before writing the report, at the width the
product is designed for, and compare its silhouette to the live page.** A
render that "passes" (no errors, no overflow, regions counted) can still be
wrong in the way a person sees first: a full-bleed hero sitting in a 70rem
box, a band that lost its background, a rail that became a row. The fleet
run shipped two heroes boxed by the local `ed-main` (a newer version caps
non-bleed children; the products' pins did not) with clean probes and a
report that never said so; Brad saw it in one glance. Silhouette first,
then counts.

## 3. Side by side with the live product

For every permutation, screenshot the live page and the story at two
widths (a phone width and a desktop width; use the host Storybook's
viewport presets if it has them). Put them next to each other in the
report.

**There is no pass/fail number here, on purpose.** The story runs on the
local system and the product runs on the version it pins, so they *should*
differ wherever the system moved. Your job is to sort the differences:

- **Version drift:** the local component looks or behaves differently from
  the pinned one. Expected. Point at the `GAPS.md` entry.
- **Relocation error:** something you mapped wrong, a fixture field in the
  wrong place, a region missing. Fix it now, then re-screenshot.
- **Deliberate omission:** placeholders from question 4 option C. Expected, say
  so.

**When the live product can't be captured**, say so and describe the expected
differences from source instead. A local server can be wedged, throttle a
headless browser, or answer curl and time out a page load (the hub did all
three). Never fake a capture, and never commit a live capture that carries
real people's data, even when you got one.

Say this plainly at the top of the report, in roughly these words:

> Note: these screens won't match the live product exactly because
> Storybook runs on the local design system (0.67.0) while the product runs
> on 0.59.0. Each difference between renderings is labeled accordingly
> (version drift, relocation errors, omissions, etc).

## 4. The system's own stories didn't change

This is the promise from rule 6. Pick three of the system's component
stories, ideally ones the product's scoped CSS could plausibly hit (a
header, a card, a button). Screenshot them with the product's stories
absent from the build, then with them present. They must be identical. If
the host Storybook has visual regression (Chromatic, Loki, a Playwright
suite), run it instead of eyeballing.

Any difference means the product's CSS escaped its scope. Fix the scope,
don't ship the leak, and record what happened in the report. A product
restyling the system's Storybook is the one outcome worse than not doing
this at all.

**Run the scope check alone.** With 88 screenshot renders hitting the same
dev server at the same time, one system story came back as a page that had
loaded without its styles (Times, no tokens): not a leak, a starved server.
Re-run in isolation before calling it either way, and say in the report
that you did.

## 5. Finish the ledger

Add to every `GAPS.md` row:

- **A screenshot** of the region, cropped, from the story with the outline
  on.
- **The nearest system component**, if one exists, with an evidence tag.
  "Site header, nearest `ed-site-header` [verified], missing the search
  slot" is a backlog item somebody can pick up. "Custom header" is not.
- **Seen in:** which templates in this product. When other products already
  have a ledger in `product-to-storybook/`, check theirs for the same gap
  (match on the `data-p2s-name`, then by eye) and count across products.

Then file, if the intake asked for it (question 5):

- **One issue per distinct gap**, on the repo from `GARAGE.md`. Search open
  issues for the gap's name first. If one exists, add a comment updating
  "seen in" instead of opening another.
- Title: `[product-to-storybook] <name>: seen in <N> product(s)`.
- Body: the ledger row, the screenshot, the nearest component, and a link
  back to the story.
- Option B: show the list, wait for a yes, then file. Option C: ledger
  only, file nothing.

The same site header in six products is one issue that says six. Six
issues that each say one is noise.

## 6. Write the report

Fill `templates/report.md`. The first screenful carries:

- The headline with real numbers: templates, stories, regions from the
  system, regions from the product, placeholders, version-drift entries,
  issues filed.
- The version line: local system version versus the product's pin.
- The shift disclaimer from step 3.
- The scope check result from step 4.
- What was proven and what wasn't: rendered or not, viewport confirmed or
  not, whether a person looked.

Then the side-by-sides, one permutation per section, differences labeled.

## 7. Close

Read the headline back to the user, tell them where the stories are and
how to open them, and stop. If the report says "no human review," say that
out loud: nobody has looked at these screens yet, and somebody should
before designing against them.
