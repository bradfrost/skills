# Translation: from a story to the product's templates

Read the product's build config before translating anything: the
engine that parses a file is not always the one its extension names.

A story is written in whatever the Storybook renders with (lit's `html`,
JSX, a Vue template). The product is written in whatever *it* uses
(Nunjucks, Liquid, JSX, Vue, PHP, Rails views). This is the table for
getting from one to the other, in either direction the two happen to
differ.

`product-to-storybook` has the same table pointing the other way. When the
story came from that skill, its phase 3 notes say what it dropped, and
this is where it comes back.

---

## Structure

| The story wrote | The product writes |
|---|---|
| `.map()` over a fixture array | The product's loop (`{% for %}`, `v-for`, `.map`, `each`) over the product's data |
| A ternary, one branch per story permutation | The product's conditional, with every branch the permutations showed |
| A pattern function (`patterns/site-header.ts`) | A partial, include, or component named the way the product names them |
| A pattern function's arguments | The partial's parameters, or the variables it reads from the page's data |
| The shell (`shell.ts`) | The product's layout or base template, **adapted, never replaced**: it carries the head, analytics, and scripts the story never had |
| A helper that renders trusted HTML (`unsafeHTML`, a `rich()` helper) | The template's raw or safe filter, and only for content the product controls |

## Attributes and properties

| The story wrote | The product writes |
|---|---|
| `attr=${value}` | A plain attribute |
| `?attr=${bool}` | The attribute, present or absent, behind a conditional |
| `.prop=${array or object}` | **Check the component first.** Static HTML can't set a property. If the component accepts the value as a JSON attribute, use that; if it only takes a property, set it from a script after the element upgrades, and say so in the report |
| `@event=${handler}` | Never in a story from `product-to-storybook` (they're static). If a story has one, it's a behavior row for phase 4 |
| `style="--custom-prop: …"` | Keep it inline when the product allows inline styles; otherwise a class in the product's stylesheet |

## Storybook-only constructs

Everything in this list is removed, and phase 5 searches the build to
prove it:

| The story wrote | The product writes |
|---|---|
| `data-origin="system"` / `"product"` | Nothing |
| `data-p2s-name`, `data-p2s-product`, `data-p2s-page`, `data-p2s-outline` | Nothing |
| `data-placeholder="missing-component"` | Nothing: a placeholder means the region isn't built. Stop and ask what goes there |
| A product decorator (`withProduct`, a wrapper `div`) | Nothing |
| Side-effect imports that register one component each | The product's own registration (a components barrel, a bundle entry, a CDN script). Phase 3 checks every tag against it |
| Fixture imports and `_meta` blocks | Nothing; content comes from `CONTENT.md` decisions |
| `parameters`, `tags`, `a11y` excludes | Nothing. An axe exclude in a story is a known accessibility bug: find it in the ledger and fix it on the way in |

## Styles

| The story wrote | The product writes |
|---|---|
| `@scope ([data-p2s-product="…"]) { rules }` | The rules, unwrapped, in the partial's stylesheet |
| `@scope ([data-p2s-product="…"] [data-p2s-page="…"]) { rules }` | The rules under whatever keeps page styles apart in the product: a page class, framework-scoped styles, a page stylesheet |
| Variables set on the story's root class (because `:root` never matches inside `@scope`) | Back on `:root`, or the product's theme layer |
| `import.meta.glob('./patterns/*.css')` | The product's stylesheet imports, in its own order |
| A pattern's `.css` file | The product's own stylesheet language and file layout (a Sass partial, a CSS module, a `<style>` block) |

Carry the redesign's CSS *changes*, not just the final file. Diff each
region's story CSS against the product's current CSS for the same region,
so a rule the redesign deleted gets deleted in the product too.

## Worked example: a lit pattern to a Nunjucks partial

The story's pattern:

```ts
export const chapterCard = (c: Chapter) => html`
  <ed-card data-origin="product" data-p2s-name="Chapter card">
    <ed-heading tagName="h3" variant="title-md">${c.title}</ed-heading>
    ${c.videoId ? html`<ed-button class="js-chapter-video-trigger" data-video=${c.videoId}>Watch the intro</ed-button>` : nothing}
  </ed-card>
`;
```

The product's partial, `_includes/chapter-card.njk`:

```njk
{# Story: Products/AI & Design Systems course/Home. See storybook-to-product/links.json. #}
<ed-card>
  <ed-heading tagName="h3" variant="title-md">{{ chapter.title }}</ed-heading>
  {% if chapter.videoId %}
    <ed-button class="js-chapter-video-trigger" data-video="{{ chapter.videoId }}">Watch the intro</ed-button>
  {% endif %}
</ed-card>
```

Markers gone, the conditional in the product's syntax, the data from the
product's own `chapter` object, the behavior hook kept, and a header that
says where it came from.
