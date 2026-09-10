---
system: <Design System Name>
version: "<version live right now>"
naming: web-components        # web-components | react | vue | css-classes
tag_style: "<ds-button>"      # how a name appears in this system
token_prefix: "--ds-"
catalog_source: <URL, command, or path>
catalog_rung: mcp             # mcp | manifest | repo | docs | figma | interview
runtime_tested: true          # did you actually render a component?
verified_on: 2026-09-10
---

# <Design System Name> — vibe-killer profile

One paragraph: what this system is, who maintains it, and anything a
converter needs to know before touching it.

---

## 1. Catalog access

**Rung that answered:** <which one, and the exact command or URL>

**Proof:** <the component you looked up, and one real prop or slot you read
back from it>

Everything below is `[verified]` unless tagged otherwise.

---

## 2. Runtime (how a page loads this system)

**Packages:** `@org/tokens@x.y.z`, `@org/components@x.y.z`

**Load order matters.** This block goes in `<head>`, in this order:

```html
<link rel="stylesheet" href="…/tokens.css">
<link rel="stylesheet" href="…/<theme>/fonts.css">
<link rel="stylesheet" href="…/base.css">
<script type="module" src="…/components.js"></script>
```

**Theme activation:** `<html class="<theme>">` | `data-theme="<theme>"` |
`<Provider theme="…">`

**Available themes:** …  **Default:** …

**Light-DOM stylesheets** (components that style content outside their own
shadow root, easy to miss, page looks broken without them): …

**Version pinning:** floating `@latest` | pinned. <Which, and why.>

**Tested:** <yes, rendered `<ds-button>` and it looked right> | `[untested]`
<and why not>

---

## 3. Vocabulary

Mark anything absent as `unmapped`. Absence is a finding.

| Need | Component | Props | Slots / children | Required wrapper | Evidence |
|---|---|---|---|---|---|
| Page shell | | | | | |
| Header | | | | | |
| Main | | | | | |
| Footer | | | | | |
| Section / band | | | | | |
| Layout container | | | | | |
| Grid | | | | | |
| Grid item | | | | | |
| Heading | | | | | |
| Prose passage | | | | | |
| Text link | | | | | |
| Image / media | | | | | |
| Icon | | | | | |
| Button | | | | | |
| Button group | | | | | |
| Card | | | | | |
| Card zones | | | | | |
| Badge / tag | | | | | |
| Hero / page header | | | | | |
| Form field(s) | | | | | |
| Alert / notice | | | | | |
| Navigation | | | | | |
| Table | | | | | |
| Modal / dialog | | | | | |

### Page templates

Whole-page starting points this system publishes. Always check here first.

### Recipes and published compositions

### Canonical compositions

Copy the real skeletons in, verbatim. These are worth more than any prose.

```html
<!-- page shell -->

<!-- card grid -->

<!-- section with heading -->
```

---

## 4. Tokens

**Prefix:** `--ds-`

**Tiers:** <primitive → semantic → component, or whatever this system uses>

**Which tier consumers may use:** <and which are off-limits>

| Family | Pattern | Example |
|---|---|---|
| Background | `--ds-color-background-*` | |
| Content | `--ds-color-content-*` | |
| Border | | |
| Spacing | | |
| Radius | | |
| Shadow | | |
| Type | | |

---

## 5. The rules

**Naming convention:**

**Spacing doctrine** (who owns the space between two things):

**Accessibility baseline** (level, what's automatic, what the consumer supplies):

**Anti-patterns this system forbids:**

**The don'ts worth remembering** (catalog guidance that corrects an obvious
but wrong mapping):

---

## 6. Validation

**Command:** `<exact command>` | none

**What it catches:**

---

## 7. Known gaps

Things this system doesn't cover, found during conversions. Each one is a
proposal waiting to happen.
