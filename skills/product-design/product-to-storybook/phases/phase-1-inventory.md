# Phase 1 — Inventory

Find the product's core page templates and the permutations of each that
matter. Then stop and show the user, because everything after this phase is
built on this list, and a wrong grouping here costs the whole run.

**Output:** `product-to-storybook/<product>/INVENTORY.md`, confirmed by the
user.

---

## From a repo (best case)

Templates are in the source. Find them:

- **Layouts and templates.** `_includes/layouts/*.njk`, `layouts/`,
  `templates/`, `app/**/layout.*`, `pages/**`, route files. A content site
  usually has three to eight. An app has one shell plus a screen per route.
- **What each one wraps.** Read the front matter or the route config to see
  which content types use which layout. That's the grouping, straight from
  the product's own rules.
- **Permutations.** Inside one template, what varies? Conditionals in the
  template (`{% if video %}`), optional front matter fields, content types
  that share a layout but render differently. Every branch that changes
  what's on screen is a candidate permutation.
- **Design system usage per template.** Which system components each
  template renders, by tag or import. This is the list phase 3 rebuilds
  from local components, so get the exact names.
- **The pinned version.** From `package.json` or the lockfile. Compare it to
  the local system's version and write both down.
- **The installed tree, too.** The lockfile is the declaration; what is
  under `node_modules` is what the product last ran on, and the two can be
  months apart (eddie-diagrams declared 0.67 and had 0.25 installed, the
  dependabot bumps merged and never installed). Read both. When they differ,
  install from the lockfile before capturing screens, say so in the garage,
  and never edit the product's own files.
- **Props spelled in a way the system does not read** (`tag-name` for
  `tagName`, `hide-text` for `hideText`) are a product bug, not drift, when
  the system never declared that spelling on any version. Check the
  component's `attribute:` declarations before calling it drift; the story
  sets the property the system reads, and the bug goes to the product.

**When the product is a client-rendered app**, there are no layouts in the
11ty sense. The templates are the view renderers: find the router (the
route table, the dispatch function) and the function each route calls, and
group by the skeleton those functions emit. The shell is whatever static
markup wraps every view. bf-brain's hub was 21 view renderers behind one
`index.html`, grouped into 6 templates.

## From a live URL

Templates are inferred from the pages. Be honest about that: tag every
template `[inferred]` in the inventory.

- **Get the page list.** `sitemap.xml`, `robots.txt`, the site's nav, an
  RSS feed. For an app, the routes you can reach.
- **Sample widely, then cluster.** Fetch a spread of pages: the homepage,
  three or four from each nav section, the oldest and newest items in any
  list, a 404. Group them by rendered structure: the landmarks, the order of
  regions, the classes on `<body>` or `<main>`. Pages with the same skeleton
  are one template.
- **Permutations** are pages in a cluster whose skeleton matches but whose
  regions differ: an embed, a sidebar, a gallery, an empty state.
- **Design system usage** from the rendered DOM: custom element tags, the
  system's class prefix, its token custom properties in computed styles.

If a URL needs a login, handle it per `intake/PRODUCT-INTAKE.md` before you
go further.

---

## Deciding what's "within reason"

The goal is a set of screens the design system can be designed against,
not a museum of every page. Some rules that hold up:

- **One template = one story file.** Five templates is typical. Fifteen
  means you're counting pages, not templates; regroup.
- **One is a real answer.** A one-page marketing site or a single-route
  dashboard is one template with permutations for its states; don't invent
  section-level templates to reach a bigger number. Five of the nine fleet
  products came in at one to three templates.
- **A permutation earns its place by changing what the system has to
  support.** A post with a YouTube embed, a post with a code block, a post
  with a 90-character title: yes. A post from 2019 versus a post from 2024:
  no, unless the layout changed between them.
- **Two to five permutations per template** is the usual range. More than
  that and the template is probably two templates.
- **Empty and overflow states count** when the product actually has them:
  the listing with zero results, the profile with no avatar, the nav with
  too many items.

---

## Write the inventory

Fill `templates/inventory.md`. One row per template:

| Template | Source | Pages using it | Permutations | System components | Not from the system |
|---|---|---|---|---|---|
| Post | `_includes/layouts/post.njk` | ~1,900 | Default, With video embed, With code block, Long title | `ed-page-header`, `ed-prose`, `ed-tag-list` | Site header, site footer, webmentions block |

The last two columns are a first pass. Phase 3 confirms them against the
render. Tag each template `[source]` or `[inferred]`.

---

## The checkpoint

**Stop here.** Show the user the inventory in this shape and wait. One
numbered line per template, biggest first; name a template's permutation
count only when it has more than one:

> The inventory found 5 templates and 11 permutations:
>
> 1. Post is the biggest, containing about 1,900 pages and 4 permutations
> 2. Page has 2 permutations
> 3. Home
> 4. Note
> 5. 404
>
> Three custom components show up on every template and aren't from the
> design system: the site header, the site footer, and the newsletter
> signup.
>
> To continue, select one of the following:
>
> - Go ahead and build this
> - Make revisions (add, edit, drop, etc)

Take their corrections, update `INVENTORY.md`, and only then move to phase
2. Do not build a single story before this is confirmed. On a repo-sourced
inventory the user is usually confirming; on a URL-sourced one they're
usually fixing, and that's exactly what the checkpoint is for.
