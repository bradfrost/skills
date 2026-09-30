# Phase 1: Assessment

Work out exactly what it takes to carry the Storybook screens into the
product, before a single file in the product changes. Every region of every
story gets a disposition, every behavior the story left behind gets named,
and every piece of the design system the story leans on gets checked against
what the product can actually install.

**Output:** `storybook-to-product/ASSESSMENT.md`, built from
`templates/assessment.md`. Then **stop and show the user.**

---

## 1. Read the story like source code

The story is the spec. Read all of it, not just the render:

- **The story file and its shell.** Every region, in order, with its
  component names, props, slots, and inline styles.
- **The pattern files** the story imports (a `patterns/` folder, if the
  story came from `product-to-storybook`). Each one is a region the product
  owns.
- **The comments.** Storybook work leaves a trail in the code: "the FAQ was
  cut", "js/scripts.js is dropped", "the modal stays closed". Every one of
  those is a finding for this phase. Collect them verbatim with file and
  line. Read them carefully, though: in a story from
  `product-to-storybook`, **"dropped" means "not carried into a static
  story," never "remove from the product."** Only a comment saying a region
  was *cut* (or a commit that removed it) is evidence of a retirement.
- **The git history of the story folder** since the product was last
  captured or handed off. `git log --oneline -- <story folder>` tells you
  what the redesign actually changed, and the commit messages usually say
  why.
- **The fixtures**, including any `_meta` block. Phase 2 does the content
  work; here you only need to know which fields exist and which regions
  they feed.

If a `product-to-storybook/<product>/` paper trail exists in the design
system repo, read `GARAGE.md`, `INVENTORY.md`, and `GAPS.md` now. The
inventory maps every story back to a product template, and the gap ledger's
"product bugs found by relocating" section is a list of things this run can
fix on the way in.

## 2. Read the product like a destination

For each story, find the product template it lands in (the story's comments
or the fixture's `_meta.source_file` usually say). Record:

- **The template and every partial it includes**, in render order.
- **How the product gets its data:** data files, front matter, a CMS, an
  API, hardcoded strings in the template.
- **How the product loads the design system:** which components it
  registers (a `components.js` barrel, individual imports, a CDN script),
  which CSS it imports, which theme it activates.
- **Every script that touches the page**, and which classes, IDs, and
  `data-*` hooks each one reaches for.
- **Every form and where it posts:** serverless functions, third-party
  endpoints, email service providers.
- **Its own rules.** A `CLAUDE.md`, `AGENTS.md`, contributing guide, or
  process config in the product repo outranks this skill. Read it first and
  say you did.

## 3. Map every region

Walk each story top to bottom and give every region exactly one
disposition:

| Disposition | Meaning |
|---|---|
| **Carry** | The region is new or rebuilt in Storybook, and it moves into the product as a new partial. |
| **Adapt** | The product already has this region, and it changes to match the story. Edit the existing partial so its wiring survives, rather than replacing it. |
| **Retire** | The product has a region the story dropped (a section that was cut, a gate that went away). It comes out of the product, along with its CSS, its scripts, and any backend it alone used. Always confirmed by the user, region by region. |
| **Keep** | The product has something the story never represented (analytics, head metadata, a third-party widget, a skip link). It stays exactly as it is. |

A region that is **Adapt** gets a one-line diff in words: "same cards, now
a 3-up `ed-grid` instead of a flex row, eyebrow above the title."

**Retire is where production breaks.** A retired email gate can orphan a
serverless function, an analytics event, and a query-string branch in
another page. Trace every retired region's dependencies before proposing
it, and list them in the row: its partial, its stylesheet, its scripts,
the component registrations only it used, and any build configuration
that names its files (a bundler's entry points, a copy step).

**A retired region's content often moves rather than disappears.** A cut
"about" section whose list of inclusions reappears in a new bento is a
**Retire** and a **Carry**, linked. Write both rows and say where the
content went, so phase 2 treats it as the same content.

**Partials are shared.** Before adapting or retiring a partial, find every
page that includes it. A hero partial the homepage redesign rebuilds may
also render, smaller, on the order page. Every other page it touches goes
in the row, and phase 5 renders it.

## 4. The system dependency ledger

The story renders on the design system checked out next to it. The product
renders on whatever version it pins. Those are rarely the same, and in a
redesign the story almost always leans on system work the product can't
install yet.

Check at the level of detail the story actually uses. A component that
exists in every version can still carry a new prop, variant, or styling
hook that doesn't, and in a redesign that's most of the ledger. So check
every component and recipe, **every attribute and variant value the story
sets, every custom property it sets (`--ed-*` and the like), every icon
name, including the ones read from fixture data**, and every token:

- **Is it in the product's installed version?** Read the installed tree
  (`node_modules`: the type declarations, the CSS, the icon sprite), not
  just `package.json`.
- **Is it in the latest published version?** `npm view <package> version`
  tells you the number, not the contents. Read the published contents: the
  design system's release tag (`git show v<x.y.z>:<path>`) or the package
  tarball (`npm pack <package>@<x.y.z> --dry-run` lists its files).
- **Is it only on a branch?** New components, new props, new variants made
  during the redesign often live in unreleased work. `git branch -a
  --contains` and `git tag --contains` on the commit that added it tell
  you.

A build step that copies assets out of the design system (an icon sprite,
a font folder) turns every icon name and font file into a version
dependency too.

Each row lands in one of three states: **installed**, **published** (the
product needs a version bump), or **unreleased** (the product can't have it
until the design system ships a release). Record the component, the prop or
variant that matters, the state, and the regions that need it.

A recipe or package the product doesn't depend on at all (a recipes
package, an icon set) is its own row: the product needs a new dependency,
not just a bump.

**Runtime third parties get a row too.** A component that fetches its
configuration from another site at runtime, a video embed, a hosted font:
each one needs the product's content security policy to allow it, and each
one is a way for the page to break when somebody else's server does.

### When something is unreleased, ask

The moment the ledger has an **unreleased** row, say this:

> **This UI depends on design system work that hasn't been released yet.**
> The product can't install these until a new version of the design system
> is published: <list>.
>
> - **A. Wait for the release.** Nothing in the product changes until a
>   version with all of these is published.
> - **B. Build against the local design system now.** The product links to
>   the local design system during development, and the work is marked not
>   ready to ship until the product pins a published release that contains
>   every one of these. (Recommended when a release is already on its way.)
> - **C. Build what's released.** Regions whose dependencies are published
>   move now; the rest keep the product's current version until the release
>   lands.

Record the answer in `HANDOFF.md`. Option B never ships on a local link:
phase 5 refuses to call the work ready while the product's manifest points
anywhere but a published version.

## 5. The behavior inventory

Storybook is static on purpose, so a story carries the *look* of an
interaction and none of the behavior. Every behavior the product needs gets
a row:

| Status | Meaning |
|---|---|
| **Restore** | The product already does this. The existing script needs to find its hooks in the new markup. |
| **Rebuild** | The behavior exists, but the new markup changed enough that the old script doesn't fit. Prefer the system component's own API (a modal's open property, a component's events) over porting the old script. |
| **New** | The story implies a behavior the product never had: a play button over a thumbnail, a "copy" button, a tab set. Somebody has to decide what it does. |
| **Retire** | The behavior belonged to a retired region. Delete the script, not just the markup. |

Find them in four places: the story's own comments about what was dropped,
every script in the product, every trigger in the story (buttons, links
with `#` hrefs, anything with an `aria-controls` or a `js-` class), and
every component in the story that has an open, closed, or active state
(modals, drawers, accordions, tabs, toasts).

**One script often carries several behaviors, and they fail together.**
Before changing or retiring any script, list every page that loads it,
every region it touches, and every query it runs at the top level. A
module that calls `addEventListener` on an element the redesign removed
throws before it reaches the next behavior, so removing one form can
silently break a modal three functions further down.

Modal triggers are the classic miss: the modal is in the story, closed, and
nothing on the page opens it.

## 6. Estimate

Grade each region and each behavior row with the effort vocabulary the user
already knows. If `ds-adoption-plan` has run on this product, use its
grades. Otherwise:

| Grade | Rough size |
|---|---|
| **XS** | Under an hour. A copy swap, a prop change. |
| **S** | A couple of hours. A partial adapted, a script's selectors updated. |
| **M** | Half a day to a day. A new partial with its data wiring, a behavior rebuilt. |
| **L** | More than a day. A new data source, a new backend endpoint, a region that needs a design decision first. |

Sum it, and say how much of the total is blocked behind the release gate.

## 7. The checkpoint

Show the user the assessment in this shape, then stop and wait:

> **3 stories → 3 product pages.** 14 regions: 6 carry, 5 adapt, 2 retire,
> 1 keep. 9 behaviors: 4 restore, 2 rebuild, 1 new, 2 retire. System
> dependencies: 11 installed, 3 need a version bump, 4 unreleased (release
> gate: option B). Estimate: about 3 days, 1 of it waiting on the release.
>
> Retiring: the FAQ section (and `js/faq.js`), the email gate (and
> `netlify/functions/subscribe.mjs`, which nothing else uses). **Confirm
> each retirement before I touch it.**

A wrong retirement here deletes something the business still needs, so
every **Retire** row gets an explicit yes. Everything else can be confirmed
as a batch.
