# The markers

Every region in a relocated story says where it came from. The convention
is three data attributes and one small stylesheet, so it works in any
Storybook, any renderer, and any design system, and it comes out cleanly
when you're done with it.

The gap ledger is scraped from these attributes. An unmarked region is a gap
nobody will ever see.

---

## The attributes

| Attribute | Values | On what |
|---|---|---|
| `data-origin` | `system` \| `product` | Every region that renders something |
| `data-placeholder` | `missing-component` | A stand-in for a region that isn't built (question 4 option C, or a template branch nobody finished) |
| `data-p2s-name` | the product's name for the region | Every `product` region and every placeholder |
| `data-p2s-product` | the product slug | The wrapper the decorator puts around the whole story |
| `data-p2s-outline` | present or absent | The same wrapper; set by the toolbar toggle |

Rules:

- **`system` regions** are the local design system's components. Mark the
  outermost element of the region, not every component inside it.
- **`product` regions** are markup the product owns. Always carry a
  `data-p2s-name`, spelled the way the product's own code or team spells
  it. That name is the dedupe key across products, so "Site header" in one
  product and "site-header" in another should be made to match on
  purpose.
- **Placeholders** are visible even with the outline off. They're a hole
  in the page and the page should look like it has a hole.
- **Nothing is unmarked.** If you can't decide, it's `product`.

---

## The stylesheet

`product-to-storybook/markers.css`, loaded by the product decorator only:

```css
/* Placeholders are always visible. */
[data-placeholder="missing-component"] {
  min-height: 4rem;
  display: grid;
  place-items: center;
  background: repeating-linear-gradient(
    45deg, transparent 0 8px, rgba(0 0 0 / 0.06) 8px 16px
  );
  outline: 1px dashed currentColor;
  outline-offset: -1px;
}
[data-placeholder="missing-component"]::before {
  content: "Missing: " attr(data-p2s-name);
  font: 600 0.875rem/1 system-ui, sans-serif;
  opacity: 0.7;
}

/* Product regions are outlined only when the toggle is on. */
[data-p2s-outline] [data-origin="product"] {
  position: relative;
  outline: 2px solid #d6336c;
  outline-offset: -2px;
}
[data-p2s-outline] [data-origin="product"]::after {
  content: "Not from the system: " attr(data-p2s-name);
  position: absolute;
  inset: 0 auto auto 0;
  padding: 0.25rem 0.5rem;
  background: #d6336c;
  color: #fff;
  font: 600 0.75rem/1 system-ui, sans-serif;
  z-index: 1;
  pointer-events: none;
}
```

Hardcoded colors on purpose. The markers must look the same in every
design system, and they must never inherit a theme, or a product's dark
mode could hide them.

---

## The decorator and the toggle

Added to the host Storybook's `preview.*`, in the host's own syntax. What it
has to do, in any renderer:

1. **Run only on the product section.** Check the story's title prefix
   against the section from `GARAGE.md`. The system's own stories never
   see this decorator; phase 4 proves it.
2. **Wrap** the story in `<div data-p2s-product="<slug>">`.
3. **Load** `markers.css` and `<slug>.scoped.css` once, on first use.
4. **Read the `Origins` global** and set `data-p2s-outline` on the wrapper
   when it's on.

The toolbar global:

```js
export const globalTypes = {
  origins: {
    description: 'Outline regions that are not from the design system',
    toolbar: {
      title: 'Origins',
      icon: 'component',
      items: [
        { value: 'off', title: 'Origins: off' },
        { value: 'on', title: 'Origins: on' },
      ],
      dynamicTitle: true,
    },
  },
};
export const initialGlobals = { origins: 'off' };
```

If the host Storybook already has a global for something similar, extend
it rather than adding a second toolbar item. If the host has its own
placeholder component (Eddie has `f-po`), it can read these same attributes
so there's one convention, not two; that's the host's change to make, not
this skill's.

---

## Scraping the ledger

The first pass at `GAPS.md` is a query over the rendered stories:

```js
[...document.querySelectorAll('[data-origin="product"], [data-placeholder]')]
  .map(el => ({
    name: el.dataset.p2sName,
    type: el.dataset.placeholder ? 'missing-component' : 'product',
    story: window.location.search,
  }));
```

Run it per story, merge on `name`, and you have the "seen in" column
before anyone screenshots anything.
