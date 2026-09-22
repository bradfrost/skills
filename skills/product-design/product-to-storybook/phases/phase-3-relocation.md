# Phase 3 — Relocation

Write the stories. Every region of every template lands in one of three
buckets, and the bucket is visible in the markup: built from the local
system, brought in from the product, or a marked placeholder.

**Output:** one story file per template plus its fixtures, in the location
from `GARAGE.md`; the origin outline toggle wired into the host Storybook;
a first pass at `GAPS.md`.

---

## The story file

Match the host Storybook exactly. `STORYBOOK.md` has a verbatim story to
copy from; use its CSF flavor, its render import, its title delimiter, and
the parameters its page stories already set. A story that ignores local
convention is the first thing a maintainer deletes.

The shape, in whatever syntax the host uses:

- **Title:** `<section>/<product>/<Template>`, from `GARAGE.md`. For
  example `Products/bradfrost.com/Post`.
- **`Default` first.** The representative permutation, always named
  `Default`, always the first export.
- **One named story per permutation**, named for the content that makes it
  different: `WithVideoEmbed`, `WithCodeBlock`, `LongTitle`,
  `EmptyResults`. Storybook's sidebar then reads as a list of the content
  shapes the system has to support, which is half the value of this whole
  exercise.
- **Fullscreen layout** and whatever else the host's page stories set.
- **A product wrapper** around the whole story:
  `<div data-p2s-product="<product>">`. This is what the scoped CSS and the
  outline toggle hang off. The decorator below adds it, so the story itself
  doesn't have to.

---

## Bucket 1 — Regions the product builds from the system

The inventory says which system components each template uses. Rebuild
those regions with the *local* component, by its real local name, with its
real local props and slots, read from the catalog (`STORYBOOK.md` section
5). Mark the region `data-origin="system"`.

**Version drift is a finding, not a fix.** The product pins one version and
you're rendering with another. When a prop, slot, variant, or component the
product uses no longer exists locally:

- Use the local API so the story renders.
- Record the drift in `GAPS.md` with type `version-drift`: what the product
  used, what's local now, which templates it affects.
- Don't paper over it in the story with custom CSS. If the local component
  can't do what the product's version did, that's exactly what the ledger
  is for.

This is the ripple working as intended. The product's screen, rendered on
the newer system, shows what the next product release is going to look
like. Some of what it shows will be a regression, and now it's in a ledger
instead of a surprise.

## Bucket 2 — Regions that aren't from the system

The intake answer (question 4) decides what happens here. Whatever the
answer, mark the region `data-origin="product"` and give it a name:
`data-p2s-name="Site header"`. The gap ledger is built from these
attributes.

**A. Bring them in as-is (default).** The product's markup goes into the
story, and the product's CSS for it goes into
`<product>.scoped.css` next to the stories, wrapped:

```css
@scope ([data-p2s-product="bradfrost-com"]) {
  /* the product's own rules, unchanged */
}
```

Load that file from the product decorator only, never from `preview.*`
globally. `@scope` is what stops a product's `.header` rule from restyling
the system's own header story two sections over. It's supported in every
current browser; if the host Storybook has to run somewhere it isn't, say
so in the report and fall back to prefixing every selector with the product
wrapper.

Carry the product's real markup, including its classes. Don't tidy it. The
point of A is that the story shows the product as it is, outlined so
everyone can see which parts the system doesn't own.

**B. Split each one into its own recipe.** Same markup and CSS as A, but
each region becomes its own file next to the stories (a partial, a small
component, a template fragment, whatever the host renderer calls that) with
the product's name for it. The story imports them. Set up the files and
nothing more: no props API, no docs page, no registration in the system's
package. Turning one into a real component is a decision for a person and a
different session.

**C. Leave them out.** A placeholder in the region's place, marked
`data-placeholder="missing-component"` with the same `data-p2s-name`, sized
roughly to the region it stands in for so the layout holds. Say in the
report that the side-by-side will show holes on purpose.

**D.** Do what they said, and record it in `GARAGE.md`.

## Bucket 3 — Regions the template needs and nobody has built

Rare on a backfill, since the product exists, but it happens: a template
branch that renders nothing today because the feature was never finished, a
region the source references and the render omits. Placeholder, marked
`data-placeholder="missing-component"`, named, and a `GAPS.md` row of type
`missing-component`.

---

## Wire the outline toggle

One decorator and one toolbar global, added to the host Storybook per
`reference/MARKERS.md`:

- The decorator wraps every story under the product section in
  `<div data-p2s-product="…">`, loads `product-to-storybook/markers.css`
  and that product's scoped CSS, and sets `data-p2s-outline` on the wrapper
  when the toggle is on.
- The toolbar global is named `Origins`, off by default. On, every
  `data-origin="product"` region gets an outline and a badge with its
  `data-p2s-name`; every placeholder gets a hatched fill. Off, the story
  looks like the product.

Scope the decorator to the product section (by title prefix) so it never
runs on the system's own stories. That's a promise phase 4 checks.

---

## Write the first pass at the ledger

Scrape every `data-origin="product"` and `data-placeholder` region across
the stories you just wrote, plus every version-drift note, into
`templates/gaps.md`. Phase 4 adds the screenshots and the nearest-component
column. Close the phase in one line:

> 5 story files, 11 stories, all rendering. 14 regions from the local
> system, 3 from the product (scoped), 0 placeholders, 2 version-drift
> entries. Proof next.
