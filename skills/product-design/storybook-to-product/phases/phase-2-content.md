# Phase 2: Content

Decide, field by field, whose content ships: the story's, the product's, or
a blend of the two. This is the blurriest line in the whole handoff, which
is exactly why it gets its own phase and its own ledger instead of a guess
buried in a template.

**Output:** `storybook-to-product/CONTENT.md`, built from
`templates/content.md`, with a decision on every row.

---

## Why this is hard

A story's fixture is a mix of three very different things, and they all
look the same in JSON:

- **Real copy that was edited in Storybook.** Somebody did a copy pass
  right there in the fixture, because that's where the design was
  happening. This is the new copy, and it should ship.
- **Content captured from the live product.** It was true on the day it was
  captured. The product may have moved since.
- **Content invented to fill a shape.** Made-up students, sample prices,
  `example.com` links, a testimonial nobody said. It exists so the layout
  has something to hold, and it must never reach production.

Getting any one of these wrong is a real problem: shipping invented content
puts fake people on a live page, and dropping a Storybook copy pass throws
away somebody's work.

## 1. Tag every field

Walk every fixture and every hardcoded string in the story and its
patterns. Give each one a provenance tag:

| Tag | How you know |
|---|---|
| `storybook-edit` | The fixture's git history changes this value after it was first captured, or `_meta` says it was edited. |
| `captured` | The value matches the product's current source, or `_meta` says it was copied from the live product. |
| `invented` | The value is a placeholder (`example.com`, lorem, a sample name), or the evidence below says it was invented and nothing replaced it since. |
| `sourced` | The value came from outside both codebases: a content doc, a transcript, a CMS, a spreadsheet. A commit message or a `_meta` key usually says so. |
| `new` | The region is new in Storybook, so there's nothing in the product to compare against. |
| `unknown` | None of the above holds up. Ask. |

Read the evidence, not the vibe, and weigh it in this order:

1. **`git log -p -- <fixture>`** shows exactly which values changed after
   capture, in which commit, and usually why.
2. **Field-scoped `_meta` notes** (a key that names a section, like
   `course_structure`) describe that section.
3. **The file-level `_meta.source`** describes the fixture *on the day it
   was captured*, and nothing after. A fixture whose `_meta` says "values
   invented" may be mostly real copy by the time it ships.

"The product" means the product's **fetched default branch**, never just
the local working tree. A value that matches it character for character is
`captured`, whatever the history says. A value that only matches an
uncommitted edit in the product checkout is in flight: flag it, don't
count it as a match.

Then compare every `captured` value against the product *now*. If the
product changed it since the capture, the row is a **conflict**, and a
person decides.

**Time-bound content is always asked.** Prices, deadlines, "increases on
September 30th," sale banners, dates in copy. Content like this is right
for a window of time, and the window may have closed between the capture,
the redesign, and the merge.

## 2. Propose a default for every row

| Tag | Default |
|---|---|
| `storybook-edit` | **Carry** the story's copy. |
| `captured`, unchanged | **Keep** the product's (they're the same). |
| `captured`, conflict | **Ask.** Show both. |
| `invented` | **Keep** the product's real content. If the product has no real equivalent, **ask**: invented content never ships. |
| `sourced` | **Carry**, and say where it came from. |
| `new` | **Ask.** It's probably real copy written in Storybook, and it might be a placeholder. |
| `unknown` | **Ask.** |

"Blend" is a real answer, and a common one: the story's new heading and
intro paragraph, over the product's real list of testimonials, for
example. Record it per field, not per region.

## 3. Images and media

Every image, video, embed, icon, and background gets its own row, and
**media is always asked, never defaulted.** Files have to physically move,
and a picture carries rights, alt text, and page weight with it.

For each asset, record:

- Where the story's asset lives (the design system repo, a Storybook
  static folder, an external URL, a config file for a generated background)
  and where the product's equivalent lives, if it has one.
- The story's alt text and the product's alt text. Alt text is content, so
  it gets decided like any other copy.
- The file size and dimensions, when the asset is a file.

The choices:

> - **Carry the story's asset** (copied into the product's own asset
>   folder, never hotlinked from the design system's Storybook)
> - **Keep the product's asset**
> - **Replace it** with something else the user provides

## 4. Where the content lives in the product

Deciding *whose* content ships is half of it; deciding *where it lives* is
the other half. The story kept everything in a fixture. The product has its
own habits:

- **The product has a data source for it** (data files, front matter, a
  CMS, an API): the content goes there, and the template reads it.
  Fixtures never ship.
- **The product hardcodes it in the template:** it stays in the template,
  unless a region repeats (a list of cards, a set of tiers), in which case
  propose moving it to the product's data source and say why.
- **The content belongs to someone else's system** (a CMS, a course
  platform, a checkout): the template reads it from there, and the story's
  copy becomes a note for whoever edits that system.

## 5. Ask once, in a batch

Present only the rows that need a person, grouped by page, each with its
default. Lead with the count so a person in a hurry can accept the
defaults:

> **Content decisions: 74 fields, 58 defaulted, 16 need you.** 9 are new
> copy written in Storybook (defaulting to carry), 4 are conflicts where the
> product changed after capture, 3 are invented values with no real
> equivalent in the product. Plus 7 images, which I always ask about.

Write every answer into `CONTENT.md`. Phase 3 builds from that file and
nothing else, and phase 5 checks the build against it.
