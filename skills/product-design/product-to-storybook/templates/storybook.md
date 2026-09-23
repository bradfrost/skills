# Storybook profile — <design system name>

**Built:** <date> · **Verified on:** <date> · **By:** product-to-storybook intake
**Sibling profiles read:** <vibe-killer/SYSTEM.md, ds-ascii/PROFILE.md, none>

---

## 1. The Storybook

| | |
|---|---|
| Config folder | `<path>` |
| Framework / renderer | `<package>` |
| Storybook version | `<x.y.z>` |
| Run | `<command>` |
| Build | `<command>` |
| `stories` globs | `<from main.*>` |
| Boots clean | <yes on <date> / no: <error>> |

## 2. How a story is written here

- CSF flavor: <CSF3 typed / legacy>
- Render import: `<exact import line>`
- Title delimiter and casing: `<example title>`
- Parameters page stories set: `<layout, tags, status, viewport…>`
- Fixture habit: <sibling JSON / inline / data folder>

**Reference story, verbatim:**

```
<paste one real page or template story>
```

## 3. Where product screens live

| | |
|---|---|
| Existing product section | <`Pages/we are here./` / none> |
| Proposed section | `<Products/ or existing>` |
| File path it maps to | `<path>` |
| Inside the `stories` glob | <yes / no, needs: …> |
| Monorepo boundary | <package that can import every component / n/a> |

## 4. How the system loads in Storybook

- `preview.*` imports, in order: <tokens, base, fonts, registrations…>
- Theme activation: <global / decorator / class> · default theme: <…>
- Existing decorators and globals: <…>
- Existing product CSS and how it's scoped: <none / … / unscoped (finding)>

## 5. Component vocabulary

| Role | Local name | Props that matter | Slots / children | Required wrapper | Evidence |
|---|---|---|---|---|---|
| Page shell | | | | | `[verified]` |
| Header | | | | | |
| Footer | | | | | |
| Grid / grid item | | | | | |
| Card | | | | | |
| Heading | | | | | |
| Prose | | | | | |
| Button | | | | | |
| Form field | | | | | |
| Table | | | | | |
| Navigation | | | | | |
| Media | | | | | |

<n> of <n> `[verified]`. Unmapped: <list>.

## 6. Notes

<Anything that will bite: a light-DOM stylesheet, a registration that must
run before render, a rule from CLAUDE.md.>
