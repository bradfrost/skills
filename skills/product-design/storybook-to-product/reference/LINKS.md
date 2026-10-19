# Links: the connective tissue

Once a story ships, the story and the product are two copies of the same
screen, in two repos, changing on two schedules. The links are how each
side knows the other exists, which version of the story shipped, and
what's changed since.

Build on what the design system already has before adding anything. Most
mature systems already connect to their products in a few ways, and each
one covers a different direction.

---

## What to look for first

| Direction | What it usually looks like | Eddie, for example |
|---|---|---|
| Story → product | The source file and URL a story was captured from | `product-to-storybook` fixtures carry `_meta.source_file`, `source_url`, and `captured_on`; the product's `GARAGE.md` has the repo path |
| Product → system (usage) | A usage reporter or adoption scanner that knows which products use which components at which version | `eddie-reporter` runs in the product's CI and feeds an activity ledger; an adoption scanner reads every org repo's pins |
| System → product (releases) | Something that tells products a new version shipped, or opens the upgrade for them | A publish beacon that dispatches to every repo pinning the package, received by a workflow in the product that opens the upgrade PR |

Record what you found in `HANDOFF.md`. **The gap is almost always the same
one:** nothing points from the product back to the story, and nothing
records *which version* of the story shipped. That's what this skill adds.

---

## 1. The link record

`storybook-to-product/links.json` in the product repo. One entry per story
that shipped, machine-readable so any later run (this skill's catch-up,
`product-to-storybook`'s refresh, a script) can read it without parsing
prose:

```json
{
  "design_system": {
    "repo": "Brad-Frost-Web/eddie-design-system",
    "storybook_url": "http://localhost:6006"
  },
  "links": [
    {
      "story_id": "products-ai-design-systems-course-home--default",
      "story_file": "packages/eddie-web-components/.storybook/products/ai-design-systems-course-website/home.stories.ts",
      "product_files": ["index.html", "_includes/hero.njk"],
      "live_url": "https://aianddesign.systems/",
      "story_commit": "5864f34a",
      "system_version": "0.69.0",
      "handed_off": "2026-10-01"
    }
  ]
}
```

`story_commit` is the heart of it. It says exactly which version of the
story is in production, so "what changed in Storybook since we shipped?" is
one `git log <story_commit>..HEAD -- <story folder>` away. The file changes
inside the handoff's own pull request, so merging the work is what makes
the record true, and every catch-up moves it forward the same way.

The product side needs no commit in the file: the product commit that last
touched `links.json` *is* the handoff, however the pull request was merged.
`git log -1 --format=%H -- storybook-to-product/links.json` finds it.

## 2. The file header

Every template and partial this skill creates or adapts gets a short
comment at the top, in the product's own comment syntax:

```njk
{# Story: Products/AI & Design Systems course/Home (products-ai-design-systems-course-home--default)
   Handed off from eddie-design-system@5864f34a by storybook-to-product. See storybook-to-product/links.json. #}
```

Two lines, no more. It's for the person who opens the file cold and needs
to know there's a Storybook version of it, and where to look. It never
renders into the page.

## 3. The note on the design system side

If the story came from `product-to-storybook`, add a **Handoffs** table to
that product's `GARAGE.md` in the design system repo (date, story commit,
product pull request) once the handoff merges. Now the design system side knows the product caught up, and
its next refresh can tell "the product drifted" apart from "the product
shipped the redesign."

Don't edit the stories themselves to add links. The story's fixture
already points at the product, and a story that changes every time the
product ships is noise in the design system's history.

## 4. The loops that already exist

Check each one and report it; fix only what's in the product's own repo:

- **Usage reporting.** If the design system has a usage reporter and the
  product runs it, confirm it still runs after the handoff. The first
  report after the merge is the system's own record that the new
  components are in production.
- **Release propagation.** If the design system announces releases to its
  products and the product has no receiver for it, say so plainly: the
  next release will not reach this product on its own. Offer to add the
  receiver as its own commit; never add it silently.
- **Adoption scanning.** Nothing to do. It reads the product's pins, which
  phase 3 just moved.

## How the two skills read each other

- **This skill's catch-up** reads `links.json`, diffs the story folder from
  `story_commit` to the design system's current commit, and carries what
  changed.
- **`product-to-storybook`'s refresh** reads `links.json` when it exists. A
  story that is ahead of `story_commit` is a pending handoff, not drift. A
  product that changed a linked file after the handoff commit is real
  drift, and it gets reported the usual way.
