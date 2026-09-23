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

The answer to question 4 decides what happens here. Whatever the
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
each region becomes its own file next to the stories, with the product's
name for it. The shape that worked (Content Brain, 35 files):

- `patterns/<kebab-name>.ts` exports one render function returning the
  region's markup, with `data-origin="product"` and `data-p2s-name` on its
  root. Eddie-wrapping components (a file that is mostly `<ed-*>` tags with
  a few product classes) are still pattern files: the product owns them.
- `patterns/<kebab-name>.css` holds that region's own stylesheet verbatim,
  wrapped in `@scope ([data-p2s-product="<slug>"]) { … }`. Rules the region
  takes from a global product stylesheet stay in the product's scoped file.
- The product shell globs `patterns/*.css` and hands the lot to the
  decorator, so adding a pattern never touches the shell.
- A layout wrapper that is nothing but a class on a `div` (a page padding
  wrapper, a flex row, a spacer) stays inline in the story, marked. Pattern
  files are for things a person would call a component.

Set up the files and nothing more: no props API, no docs page, no
registration in the system's package. Turning one into a real component is
a decision for a person and a different session.

**Translating from a framework template.** The product's markup rarely
arrives as plain HTML. Carry the structure, drop the behaviour:

| Product wrote | Story writes |
|---|---|
| `v-if` / `{#if}` / `{cond && …}` | a ternary, one branch per permutation |
| `v-for` / `{#each}` / `.map` | `.map` over the fixture |
| `:prop="…"` / `{prop}` | an attribute, `?attr` for booleans, `.prop` for arrays and objects |
| `@click` / `on:click` / `onClick` | dropped; stories are static (keep `aria-*`) |
| `<style scoped>` | the pattern's `.css`, plain selectors inside `@scope` |
| a child component | its own pattern file |

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

Declare the decorator in each product story file's meta (a shared
`hubStoryMeta`-style object next to the shell keeps that to one line), not in
`preview.*` with a title-prefix check. Declared per file, it is structurally
impossible for it to run on a system story. Phase 4 still proves it.

**Expect the host's validator to reject the product's classes.** A design
system's naming rule (`ed-c-*` only, say) will flag every `cw-*` class the
product brought along. That is the origin marker doing its job in a
different voice. Record the count in the ledger; never rename a product
class to satisfy the rule, and check whether the host's CI scans the folder
the stories live in (Eddie's does not scan `.storybook/`).

---

## Write the first pass at the ledger

Scrape every `data-origin="product"` and `data-placeholder` region across
the stories you just wrote, plus every version-drift note, into
`templates/gaps.md`. Phase 4 adds the screenshots and the nearest-component
column. Close the phase in one line:

> 5 story files, 11 stories, all rendering. 14 regions from the local
> system, 3 from the product (scoped), 0 placeholders, 2 version-drift
> entries. Proof next.
