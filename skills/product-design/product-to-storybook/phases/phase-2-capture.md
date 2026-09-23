# Phase 2 — Capture

Choose the content that goes into each story and freeze it. The stories
exist so the design system can be designed against real content shapes, so
the sample is chosen for *diversity*, not for being recent or popular.

**Output:** one fixture file per permutation, next to where the story file
will live, plus the "Content sample" section of `INVENTORY.md`.

---

## Choosing the cross-section

For every permutation in the confirmed inventory, pick one real page (or
one real record) that shows the shape the permutation exists for. Then, for
the template's `Default`, pick the page that's most *representative*: the
median case, not the best-looking one.

Go looking for the awkward ones on purpose:

- The longest title the product actually has, and the shortest
- A list or tag set at its real maximum
- Media the template supports: an embed, a gallery, a wide image, no image
  at all
- Rich content the prose region has to handle: blockquotes, code, tables,
  nested lists, a footnote
- Empty states and missing fields: no excerpt, no author photo, zero
  comments
- Dates and numbers at their real widths

A story built from the prettiest page teaches the system nothing. A story
built from the page with the 90-character title and the 40-item tag list
finds the bug.

---

## Freezing it

One fixture per permutation, in whatever format the host Storybook already
uses for data (see `STORYBOOK.md`). JSON is the default. Every fixture
carries a header:

```json
{
  "_meta": {
    "product": "bradfrost-com",
    "template": "post",
    "permutation": "with-video-embed",
    "source_url": "https://bradfrost.com/blog/post/example/",
    "captured_on": "2026-09-22",
    "product_version": "eddie-web-components@0.59.0",
    "source": "repo"
  },
  "title": "…",
  "body": "…"
}
```

`captured_on` and `source_url` are what the refresh mode diffs against.
Never leave them out.

**Content is content.** Carry the words across as written. If the product's
copy has problems, that's not this skill's job to fix, and the fixture is
not the place to fix it.

**Media.** Reference images by their live URL when the product is public,
and note it in `_meta`. When it isn't, or when you'd rather the stories
work offline, copy the asset next to the fixture and record the original
URL. Never hotlink from a logged-in product.

---

## The stop condition

Before you write a fixture, read it. If it contains a real person's data
(a name that isn't the product owner's, an email, an address, an order,
anything from an account), stop:

1. Delete the fixture.
2. Tell the user what you found and where it came from.
3. Rebuild it from the data's *shape* with invented values in the real
   widths, and say that's what you did in `_meta.source`.

A product owner's own public content (their blog posts, their bio) is fine.
Their customers' content is not. When you can't tell, ask. A third party
named inside the product's own copy (a quoted expert, the author of a
cited document, a byline) gets the same treatment as customer data: the
name and its link are replaced and `_meta.source` says so. It's the one
edit the "content is content" rule allows, and it's applied the same way
every run (Subatomic's attributed quotes, we are here.'s charter citation).

**A signed-in product's data reaches you through the browser, not the
repo.** Read the live screens for shape, counts and widths; write fixtures
from the source's types and seed files with invented values in those
widths; every person comes from one shared `fixtures/members.json` of
invented members so the same invented people recur across templates.

---

## Record the sample

Add a "Content sample" section to `INVENTORY.md`: one line per permutation
naming the source page and *why* it was chosen ("longest title on the
site", "only post with a table"). Then close the phase in one line:

> This phase collected 11 fixtures across 5 templates. The default for the
> Post template is the 2024 design tokens post (median length, one image,
> six tags). Moving onto relocation next.
