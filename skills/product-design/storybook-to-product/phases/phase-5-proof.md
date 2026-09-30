# Phase 5: Proof

Prove the product now does what the story shows, and everything the story
couldn't. Then open the pull request and stop. A page nobody rendered is a
claim, not a result.

**Output:** `storybook-to-product/REPORT.md` from `templates/report.md`, and
a pull request on the product repo.

---

## 1. It builds

Run the product's own build command, from clean. It passes with no new
warnings. Then run the product's own tests and linters, whatever it has.

## 2. Nothing from Storybook leaked through

Search the built output (not the source) for anything that belongs to
Storybook:

- Origin markers: `data-origin`, `data-p2s-`, `data-placeholder`
- Scope wrappers: `@scope`, `[data-p2s-product`
- Fixture leftovers: `example.com`, `lorem`, `_meta`, and every value
  `CONTENT.md` tagged `invented`, searched for by its exact text

Any hit is a bug. Fix it and search again. Invented content on a live page
is the one outcome this whole phase exists to prevent.

## 3. Side by side with the story

Confirm the renderer first: a viewport of a known width and an element
count that matches the page. A headless browser reporting a 0px viewport
hands back plausible screenshots of nothing.

Then screenshot every page and its story at two widths (a phone width and
the desktop width the product is designed for) and put them next to each
other.

**This time they should match.** `product-to-storybook` expects
differences, because the story runs on a newer system than the product.
After a handoff, the product pins the version the story needs, so every
difference is one of these, and gets labeled:

- **A content decision:** `CONTENT.md` chose the product's copy or asset.
  Expected. Point at the row.
- **A retired or kept region:** expected. Point at the phase 1 row.
- **An integration error:** a region translated wrong, a style that didn't
  come home, a component that isn't registered. Fix it now and
  re-screenshot.

**Silhouette first, then details.** Look at every page whole before
counting anything: a full-bleed band that got boxed, a rail that became a
row, a section that lost its background. A person sees those in one glance,
so look for them first.

## 4. Every behavior works

Walk the behavior inventory in a real browser and do each one: open every
modal and close it with the keyboard, submit every form against the test
setup from phase 4, follow every in-page anchor, tab through every page.
Record each one as done, and how.

## 5. Accessibility

Run axe on every page. If `product-to-storybook` recorded product bugs when
it relocated this product (its `GAPS.md` usually has a section for them),
check each one: the handoff is the natural moment to fix them, and every
one that's fixed goes in the report. A violation inside a system component
gets filed to the design system, not patched in the product.

## 6. The pages this run didn't redesign

The version bump in phase 3 touched every page, not just the redesigned
ones, and every shared partial phase 1 flagged renders on pages this run
never meant to change. Render each page the release notes put at risk, and compare it to
production. A regression on a page nobody meant to change is still a
regression.

## 7. The release gate

If the release gate answer was B, the work is **not ready to ship** while
the product's manifest or lockfile points at a local link. Check both. When
the design system release is published, swap the link for the published
version, reinstall, rebuild, and re-run steps 1 through 3. Until then, the
report and the pull request say "blocked on the design system release" in
their first line.

## 8. Write the report and open the pull request

Fill `templates/report.md`. The first screenful carries:

- The headline with real numbers: pages, regions by disposition,
  behaviors by status, content decisions, assets, system version before and
  after.
- Ready to ship, or blocked, and on what.
- What was proven and what wasn't: rendered or not, viewport confirmed or
  not, forms tested against what, whether a person looked.

Open the pull request on the branch from `HANDOFF.md`, with the report's
headline as its description and the side by sides attached or linked. If
the product's host builds preview deploys, link the preview.

**Merging and deploying belong to the person.** This skill opens the pull
request and stops there, every time, even when every check is green.

## 9. After the merge

When the user says it merged, add the handoff to the design system side
per `reference/LINKS.md` and record the run in `HANDOFF.md`. That's the
whole close.
