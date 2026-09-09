---
system: Eddie Design System
version: "0.63.0"
naming: web-components
tag_style: "<ed-card>"
frame_width: 52
source: https://ds.bradfrost.com/catalog.json
source_kind: mcp
verified_on: 2026-09-09
---

# Eddie

Brad Frost Web's own design system, and the one this skill grew up in. Read
live from Eddie's catalog, which declares 164 components.

Included as the contrast case to `material-web.md`. **All fourteen
archetypes bind**, because Eddie ships page-level composition alongside its
primitives. Put the two profiles side by side and you can see the difference
between a component library and a system that also covers the page.

## Bindings

| Archetype | Component | Evidence |
|---|---|---|
| page-shell | `ed-page` | [verified] |
| site-header | `ed-r-site-header` | [verified] |
| site-header.brand | `ed-logo` | [verified] |
| site-header.nav | `ed-primary-nav`, `ed-primary-nav-item` | [verified] |
| site-header.utility | `ed-utility-nav` | [verified] |
| hero | `ed-hero` | [verified] |
| section | `ed-section` | [verified] |
| section.container | `ed-layout-container` | [verified] |
| grid | `ed-grid` | [verified] |
| grid.item | `ed-grid-item` | [verified] |
| card | `ed-card` | [verified] |
| card.media | `slot="header"` | [verified] |
| card.body | default slot | [verified] |
| card.actions | `slot="footer"` | [verified] |
| button.primary | `ed-button variant="primary"` | [verified] |
| button.secondary | `ed-button variant="secondary"` | [verified] |
| button.tertiary | `ed-text-link` | [verified] |
| button.group | `ed-button-group` | [verified] |
| field.text | `ed-text-field` | [verified] |
| field.textarea | `ed-textarea-field` | [verified] |
| field.select | `ed-select-field` | [verified] |
| field.radio | `ed-radio-field`, `ed-radio-field-item` | [verified] |
| field.checkbox | `ed-checkbox-field`, `ed-checkbox-field-item` | [verified] |
| field.toggle | `ed-toggle` | [verified] |
| form | `ed-single-field-form` | [verified] |
| form.search | `ed-search-form` | [verified] |
| form.newsletter | `ed-r-newsletter-signup` | [verified] |
| table | `ed-table` | [verified] |
| table.wrapper | `ed-table-object` | [verified] |
| table.row | `ed-table-row` | [verified] |
| table.cell | `ed-table-cell`, `ed-table-header-cell` | [verified] |
| list | `ed-list`, `ed-list-item` | [verified] |
| list.links | `ed-link-list`, `ed-link-list-item` | [verified] |
| media | `ed-image` | [verified] |
| media.figure | `ed-figure` | [verified] |
| media.video | `ed-r-video-embed` | [verified] |
| overlay.modal | `ed-modal` | [verified] |
| overlay.drawer | `ed-drawer` | [verified] |
| footer | `ed-r-site-footer` | [verified] |

## Anatomy notes

**The card's three zones are real slots**, which is what makes Eddie render
cleanly in ASCII: `header` is the media band, the default slot is the body,
and `footer` is actions. The media band is media only.

**The hero owns the page's h1** and there is one per page. `height` sets its
size and `align` sets which side the media lands on.

**Grids need their item wrapper.** `ed-grid` only lays out `ed-grid-item`
children; anything else stacks in a single column.

## Anti-patterns

Read from the catalog's own `@antipattern` tags. The render respects all of
these.

- A heading or a text passage in the card's `header` slot. That slot is
  media only, and prose there paints as an image band and drops out of the
  document outline.
- Anything but a grid item as a direct child of a grid.
- A grid item inside a grid item.
- A layout container inside a hero, or a hero inside a layout container.
- An anchor wrapping a button, or a link inside a button. Give the button an
  href instead.

## Variants worth binding

`ed-r-stat-card` is the card variant for a KPI tile: label, display-size
value, meta line. `ed-r-promo-block` is the section variant for a closing
call to action. `ed-r-speaking-card` covers event and talk listings.

## Unmapped

None. Every archetype binds.
