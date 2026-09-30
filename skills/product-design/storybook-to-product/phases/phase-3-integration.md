# Phase 3: Integration

Bring the markup and the styles into the product, in the product's own
language and conventions. By the end of this phase every page renders the
new UI with the content decided in phase 2. Nothing is wired to a backend
yet; that's phase 4.

**Output:** the product's templates, partials, and stylesheets, changed on
the branch from `HANDOFF.md`, plus the design system version bump.

---

## 1. Branch first, bump first

Work on the branch recorded in `HANDOFF.md`, never on the default branch.

Then move the design system pin, because every region after this depends
on it:

- **Installed and published rows:** bump the product's pins to the version
  the ledger named, install, and commit the bump on its own. A version bump
  that rides along with markup changes is impossible to review.
- **Unreleased rows:** follow the release gate answer. Option B links the
  local design system for development (`npm link`, a `file:` path, a
  workspace alias, whatever this product's toolchain supports) and records
  in `HANDOFF.md` exactly what was linked, so phase 5 can prove it's gone.
- **New dependencies** (a recipes package the product never used): add them
  and say so.

Then read the release notes for everything between the old pin and the new
one. A bump from 0.63 to 0.69 can change components the story never
touched, and those changes land on pages this run isn't redesigning. List
them for phase 5 to check.

## 2. Translate each region

`reference/TRANSLATION.md` is the table: how a story's constructs map to
the product's templates. The rules that matter most:

- **Match the product, not the story.** The product's partial naming, its
  indentation, its CSS architecture, its class naming. The story is the
  spec for *what* renders; the product decides *how* it's written.
- **Strip every Storybook-only construct.** Origin markers
  (`data-origin`, `data-p2s-*`), `@scope` wrappers, decorators, fixture
  imports. Phase 5 sweeps for leftovers.
- **Keep every hook the product's scripts need.** When an **Adapt** region
  gets new markup, the `js-` classes, IDs, and `data-*` attributes the
  existing scripts reach for go back on the right elements. Phase 1's
  behavior inventory lists them.
- **System components go in by their real name and API**, read from the
  design system's catalog for the version the product now pins, not the one
  the story rendered on.

Work in this order: **Adapt** regions first (they carry existing wiring,
and breaking them is the costliest mistake), then **Carry**, then
**Retire**.

## 3. Retire what was confirmed, completely

For every retirement the user confirmed in phase 1, remove the region's
markup, its partial, its stylesheet, its scripts, and its script tags. Then
search the whole product for its class names, IDs, and partial name, and
remove anything that only existed for it.

A backend a retired region used (a serverless function, a form endpoint)
is removed only when phase 1 proved nothing else calls it, and the removal
is its own commit so it's easy to put back.

## 4. Bring the styles home

A story from `product-to-storybook` carries the product's CSS wrapped in
`@scope`, often reorganized one file per pattern, often edited during the
redesign. Bring it back into the product's own stylesheet architecture:

- **Unwrap the scope.** `@scope ([data-p2s-product="…"]) { … }` becomes the
  plain rules, in the partial for that region.
- **A per-page scope** (`[data-p2s-page="…"]`) becomes whatever the product
  uses to keep page styles apart: a page class on `<body>`, a
  framework's scoped styles, a page-specific stylesheet.
- **Variables that were moved onto the story's root class** (because
  `:root` never matches inside `@scope`) go back to `:root`, or wherever the
  product defines its theme layer.
- **Rules the redesign deleted get deleted in the product too.** Diff the
  story's CSS against the product's for each region; a rule that only
  exists in the product's old version is dead weight.
- **Inline styles in the story** (custom properties set with `style=""`)
  move to a class when the product's content security policy forbids inline
  styles. Check before assuming.

Every product stylesheet still has to compile with the product's own build
(Sass, PostCSS, a bundler), so build after each region, not at the end.

## 5. Register what the story registered

A story imports each component it uses, one line at a time, and Storybook's
preview registers the rest. The product has its own list. Walk every system
tag in the translated templates and confirm the product's component
registration covers it. An unregistered custom element renders as an empty
inline box with no error, which is the most common "it worked in
Storybook" bug there is.

## 6. Keep the paper trail out of the build

A static site generator publishes whatever it finds, and
`storybook-to-product/*.md` is Markdown it knows how to render. Add the
folder to the generator's ignore list before the first build, or the
assessment ships as a page on the live site. (Eleventy rendered all three
files on the first run.) If the repo tracks compiled output (a built
stylesheet, a bundle), rebuild before each commit so the artifact matches
the source.

## 7. Leave a trail

Put the link header from `reference/LINKS.md` at the top of each template
and partial this phase created or adapted, so anyone who opens the file
knows which story it came from and at which commit.

Close the phase in one line:

> 3 pages integrated: 6 regions carried, 5 adapted, 2 retired (1 function
> removed). Eddie 0.63.0 → 0.69.0, 4 components linked locally until the
> release. 12 system tags checked against the component registry, 2 added.
> Wiring next.
