# Storybook intake

Learn the host Storybook once, then every product lands in it the same way.
This is the interview that teaches the skill how *this* Storybook writes a
story, where product screens belong, and how the design system loads inside
it.

Output: `product-to-storybook/STORYBOOK.md`, built from
`templates/storybook.md`.

Budget ten minutes. Nearly all of it is reading files the repo already has.

---

## Before you ask a single question

Look for work that already answers this:

- `product-to-storybook/STORYBOOK.md` — done, confirm it's current
- `vibe-killer/SYSTEM.md` or `ds-ascii/PROFILE.md` — the sibling skills'
  profiles. They carry the component vocabulary and the runtime with
  evidence tags. Read them and carry the bindings across. They don't cover
  the Storybook half, so you still need sections 2 through 4 below.
- The repo's own `CLAUDE.md`, `AGENTS.md`, or contributing guide. Teams
  write down how stories are supposed to look, and those rules outrank
  anything you'd infer.

Say what you found before asking anything.

---

## 1. Find the Storybook

Ask: *"Where's your design system's Storybook?"* Then confirm it yourself:

- The config folder (`.storybook/`, or wherever `main.*` lives)
- The framework and renderer (`@storybook/web-components-vite`,
  `@storybook/react-vite`, and so on)
- The Storybook version
- The command that runs it, and the command that builds it
- The `stories` globs in `main.*`, because those decide whether a new story
  file is even picked up

Record every one with the file it came from. **Run the dev server once** and
confirm it starts. A Storybook that won't boot is something to know before
you write sixteen stories into it.

---

## 2. How a story is written here

Open two or three existing stories, ideally one component story and one
page or template story if the repo has any. Record:

- **The CSF flavor.** CSF3 with `meta` and typed story objects, or older
  `export default` plus function stories. Match what's there.
- **The render function.** `html` from lit, JSX, a Vue template, a Svelte
  component. Copy the exact import.
- **How stories are titled.** `Pages/we are here./Marketing-Homepage` tells
  you this Storybook groups by section and product already. Copy the
  delimiter and the casing.
- **Tags and parameters that page stories carry.** `layout: 'fullscreen'`,
  `tags: ['!autodocs']`, a status parameter, a viewport default. Page-sized
  stories in this repo probably all set the same few things. Find them and
  use them.
  **Write `parameters` literally in every story file's default export.**
  Storybook reads `layout` statically, so a `parameters` block spread in
  from a shared meta object is ignored and the story renders with the
  padded canvas. Decorators and tags can come from the shared object;
  `parameters` cannot.
- **Where fixture data lives** when a story has any. A sibling JSON file, an
  inline object, a `data/` folder. Follow the local habit.

Paste one real story into the profile, verbatim. It's the reference every
generated story is checked against.

---

## 3. Where product screens should live

This is the question the product intake asks the user (default:
`Products/`). Your job here is to find out what the answer *costs* in this
repo so the user decides with real information:

- Does a section for product screens already exist? (Eddie has
  `Pages/we are here./`, for example.) If so, the default is that section,
  not `Products/`, and say why.
- Where do the story *files* go so the `stories` glob finds them? A
  `pages` package, a `stories/products/` folder, next to components. Name
  the path.
- Is there a monorepo boundary? A product's stories might need to live in a
  package that already depends on every component package, or they'll fail
  to import anything.
- **Is the existing product-pages location published?** Eddie's
  `Pages/<product>/` section lives in `eddie-pages`, an npm package of
  reference templates that the catalog indexes and the docs standard gates.
  Product screens carry frozen product content, which is data, and a
  published primitive package must not ship data. When the existing spot is
  published, the default flips to a new, unpublished section (`Products/`
  under the Storybook config folder), and you say why.

Record the candidate location, the file path it maps to, whether it is
published, and what has to be true for the glob to pick it up.

---

## 4. How the system loads inside Storybook

Read `preview.*` and record:

- **What it imports** before any story renders: tokens CSS, a base layer,
  fonts, component registrations, light-DOM stylesheets.
- **Theme activation.** A global toolbar, a decorator, a class on the
  preview `<html>`. If there's a theme switcher, product screens should
  respond to it, which means they must not hardcode a theme.
- **Existing decorators and globals.** You'll add a toolbar global (the
  Origins toggle from `reference/MARKERS.md`); the decorator itself goes in
  each product's story files, never here. Know what's there first.
- **Which components the preview registers.** Some systems register
  everything globally; some leave page-level components (Eddie's `ed-page`,
  `ed-stack`) for stories to import. The product shell imports what the
  preview doesn't.
- **Existing product CSS**, if any product screens already live here. How
  did they scope it? If they didn't, that's a finding for the report, not
  something to copy.

---

## 5. The component vocabulary

If a sibling profile exists, you have this already. If not, do the short
version: for the fifteen to twenty-five things a page is made of (shell,
header, footer, grid, card, heading, prose, button, form field, table, nav,
media), record the exact name, the props that matter, the slots, any
required wrapper, and an evidence tag: `[verified]` when you read it from
the catalog, MCP, manifest, or repo; `[reported]` when a human told you.

Phase 3 maps the product's components to these. A name you remember instead
of read is the failure that renders as an empty region with no error.

---

## 6. Write the profile

Fill `templates/storybook.md`, save it to
`product-to-storybook/STORYBOOK.md`, and read it back to the user in five
lines: Storybook version and framework, the story flavor, the proposed home
for product screens and what it maps to on disk, how the system loads, and
how much of the vocabulary is `[verified]`. Ask them to correct anything
wrong. A bad path here costs a whole run later.

---

## Keeping it honest

Re-run this intake when the Storybook or the renderer moves a major
version, when a generated story lands in the wrong section, or when a story
that used to render stops. Record `verified_on` and treat anything older
than a couple of months as suspect.
