# The profile format

A profile is one markdown file that teaches this skill your design system's
vocabulary. It lives in the project you're rendering for, at
`ds-ascii/PROFILE.md`, and it gets built once and reused on every run.

Two rules govern everything in it. Every binding carries an evidence tag,
and nothing gets a name that wasn't read from somewhere real.

---

## The shape

```markdown
---
system: Your Design System
version: "2.4.0"
naming: web-components        # web-components | react | css-classes
tag_style: "<ds-button>"      # how a name should appear in labels
frame_width: 52               # optional, defaults to 52
source: https://…/custom-elements.json
source_kind: manifest         # manifest | mcp | repo | docs | figma | interview
verified_on: 2026-09-09
---

## Bindings

| Archetype | Component | Evidence |
|---|---|---|
| site-header | `ds-header` | [verified] |
| card | `ds-card` | [verified] |
| card.media | `slot="media"` | [reported] |
| button.primary | `ds-button variant="primary"` | [verified] |
| hero | unmapped | |

## Anatomy notes

Free prose about zones, slots, and props that the table can't hold.

## Anti-patterns

Structures your system refuses. The render will respect these.

## Unmapped

Which archetypes have no component, and how the render should compose them.
```

## The frontmatter fields

**`naming` and `tag_style`** decide how labels read. A web-components team
sees `<ds-card>`, a React team sees `<Card>`, and a CSS-classes team sees
`.ds-card`. Getting this right is most of what makes a render feel like it
belongs to your team.

**`frame_width`** defaults to 52, which never wraps in Slack or a PR body.
Set 80 if your prototypes live in READMEs or terminals. It's a hard ceiling
either way.

**`source` and `source_kind`** record where the vocabulary came from.
**`verified_on`** records when. Both exist so that drift is visible instead
of silent, which matters more than it sounds: the hand-written component
list this skill grew out of was 26% wrong against its own live catalog after
six weeks.

## The evidence tags

**`[verified]`** means you read the name out of a manifest, an MCP, a repo,
or a docs site. You could point at the line.

**`[reported]`** means a human told you, or you inferred it from a
convention, and you could not confirm it.

A profile made entirely of `[reported]` bindings is still useful. It is just
honest about being a memory of a design system rather than a reading of one,
and every render built on it inherits that caveat.

## Sub-archetype keys

Use dots for the parts of an archetype: `card.media`, `card.body`,
`card.actions`, `button.primary`, `button.secondary`, `button.tertiary`,
`field.text`, `field.select`, `field.radio`, `field.checkbox`,
`field.toggle`, `field.textarea`, `grid.item`, `table.row`, `table.cell`.

Bind what exists. Leave the rest out, or mark them `unmapped` when their
absence is worth knowing about.

## Keeping it honest

Re-verify when the system ships a major version, or any time a render
produces a name someone can't find. Re-running the intake against a manifest
takes a minute and it is the only thing that keeps a profile true.
