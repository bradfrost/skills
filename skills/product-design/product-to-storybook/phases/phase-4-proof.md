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

> These won't match pixel for pixel, and they shouldn't. The stories run on
> your local design system (0.67.0) and the product pins 0.59.0. Every
> difference below is labeled: version drift you'll want to know about, or
> something I got wrong and fixed.

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
