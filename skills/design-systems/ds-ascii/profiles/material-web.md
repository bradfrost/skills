---
system: Material Web
version: "@material/web (latest on unpkg)"
naming: web-components
tag_style: "<md-filled-button>"
frame_width: 52
source: https://unpkg.com/@material/web/custom-elements.json
source_kind: manifest
verified_on: 2026-09-09
---

# Material Web

The reference profile. Anyone can re-run the ingestion that produced it,
which is the point of shipping it.

Every tag name below was read out of Material Web's published Custom
Elements Manifest, which declares 54 elements. Nothing here was typed from
memory.

**Seven of the fourteen archetypes bind. Seven do not.** That is not a
knock on Material Web, and it is the most useful thing this profile
teaches: Material Web is a component library, not a page-layout system. It
ships buttons, fields, cards, lists, and dialogs, and it ships nothing for
heroes, sections, grids, tables, or page chrome. Most component libraries
look like this. A render against this profile will say so on the page
instead of inventing names.

## Bindings

| Archetype | Component | Evidence |
|---|---|---|
| page-shell | unmapped | |
| site-header | unmapped | |
| hero | unmapped | |
| section | unmapped | |
| grid | unmapped | |
| card | `md-outlined-card` | [verified] |
| card (variants) | `md-elevated-card`, `md-filled-card` | [verified] |
| button.primary | `md-filled-button` | [verified] |
| button.secondary | `md-outlined-button` | [verified] |
| button.tertiary | `md-text-button` | [verified] |
| button (icon) | `md-icon-button`, `md-fab` | [verified] |
| field.text | `md-outlined-text-field`, `md-filled-text-field` | [verified] |
| field.select | `md-outlined-select`, `md-filled-select` | [verified] |
| field.select.option | `md-select-option` | [verified] |
| field.radio | `md-radio` | [verified] |
| field.checkbox | `md-checkbox` | [verified] |
| field.toggle | `md-switch` | [verified] |
| field.textarea | `md-outlined-text-field type="textarea"` | [reported] |
| form | unmapped | |
| table | unmapped | |
| list | `md-list` | [verified] |
| list.item | `md-list-item` | [verified] |
| media | unmapped | |
| overlay.modal | `md-dialog` | [verified] |
| overlay.drawer | `md-navigation-drawer` | [verified] |
| footer | unmapped | |

## Anatomy notes

**Card zones are not in the manifest.** Material Web's cards are containers
with no declared slots, so the three-zone card pattern has to be composed by
hand from a media element, headings, and buttons. Draw the zones, and note
in the legend that they are a composition rather than named slots.

**The manifest carries tag names reliably and slot anatomy hardly at all.**
Several of these elements ship with an empty description, and none of the
ones checked declare slots. This is the normal state of a Custom Elements
Manifest, and it is why a good profile pairs tier-2 ingestion for names with
a short interview for anatomy.

**`field.textarea` is the one `[reported]` row here.** Material's text field
is documented as taking a `type="textarea"`, but the attribute is inherited
rather than declared on the element, so it did not survive the manifest
read. Confirm it against your version before relying on it.

**`md-navigation-drawer` is a navigation drawer**, not a general-purpose
drawer. It's bound to `overlay.drawer` because it's the closest real thing,
and a render should say which one it means.

## Anti-patterns

None declared. The manifest carries no containment rules, so this profile
cannot tell you what Material Web refuses. If you know of one, add it here
and every render will respect it.

## Unmapped

`page-shell`, `site-header`, `hero`, `section`, `grid`, `form`, `table`,
`media`, and `footer` have no Material Web component.

Compose them from what exists and mark them in the legend:

- **hero, section** → a heading plus body content in a plain container
- **grid** → CSS grid or flexbox in your own layer
- **table** → a plain HTML `<table>`
- **media** → a plain `<img>`; `md-icon` is icons only
- **site-header, footer** → your own page chrome
- **form** → an `md-*-text-field` plus an `md-filled-button`

Every one of those is a real gap between a component library and a page. The
render marks them `<unmapped: …>` so the gap shows up in the artifact rather
than being papered over.
