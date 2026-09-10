# System intake

Build the profile once, convert against it forever. This is the interview
that teaches the skill your design system: how to load it, what it contains,
what it calls things, and what it refuses to do.

Output: `vibe-killer/SYSTEM.md`, built from `templates/system.md`.

Budget five to fifteen minutes depending on how reachable the system is.
Every minute here saves you a wrong component name later, and a wrong
component name is the failure that renders as an empty page with no error.

---

## Before you ask a single question

**Look for a profile that already exists.** These are cheap wins:

- `vibe-killer/SYSTEM.md` — already done, just confirm it's current
- `ds-ascii/PROFILE.md` — the sibling skill's binding table. Read it and
  carry the bindings across with their evidence tags intact. It covers the
  archetype-to-name half and none of the runtime half, so you still need
  sections 1 and 5 below.
- `ds-adoption-plan/GARAGE.md` — carries a tested catalog access map. If
  it's there, you already know which rung of the evidence chain works.
- The project's own `CLAUDE.md`, `AGENTS.md`, or contributing guide. Teams
  that use a design system tend to write down the rules, and those rules
  outrank anything you'd infer.

Say what you found before you start asking. Nobody enjoys answering a
question the repo already answered.

---

## 1. Reach the catalog, and prove it

**This is the most important step in the intake.** Do not take an answer on
faith. Make one real call, read one real file, and record what worked.

Ask: *"How can I read your design system's actual component list? An MCP
server, a components manifest, the repo itself, a docs site, a Storybook?"*

Then walk the chain from `SKILL.md` and **stop at the first rung that
answers**:

1. The system's MCP server or CLI
2. A machine-readable export (`custom-elements.json`, Storybook's
   `index.json`, a token JSON)
3. The repo on disk
4. The docs site
5. The design library (naming and coverage only, never code APIs)
6. Interview the human

**Prove it.** Look up one component you know exists and read back its real
props and slots. If that works, record the rung and move on. If it doesn't,
you've learned something important before you wasted an hour: say so, drop
to the next rung, and note in the profile that everything below is
`[reported]`.

Record: which rung worked, the exact command or URL, and today's date.

---

## 2. The runtime (how a page loads the system)

**This is the part nobody writes down, and it's the part the standalone
deliverable lives or dies on.** A perfect list of component names is useless
if the converted page can't load them.

Ask, or find out yourself:

- **Package names and current version.** What's on npm, and what version is
  live right now? Don't guess from a docs site; published docs commonly
  trail the shipped version by months.
- **CDN URLs, if there are any.** unpkg, jsDelivr, or the team's own host.
  Get the exact paths for tokens CSS, component JS, and anything else
  required. Pin a version or use the floating tag deliberately, and know
  which you chose. A floating tag means the demo you rehearsed on Monday is
  not guaranteed to be the demo you give on Thursday.
- **Load order.** Tokens almost always have to come before components, and
  before any base or reset layer that consumes them.
- **Fonts.** How does a page get the system's typefaces? A stylesheet that
  ships with the theme, a self-hosted file, a loader script? This one is a
  reliable trap: a system's tokens usually just *name* a family, so a page
  that loads tokens without fonts renders in a fallback serif and nothing
  errors.
- **Theme activation.** A class on `<html>`? A `data-theme` attribute? A
  provider component? What's the default theme, and what else is available?
- **A base or reset layer.** Many systems ship one. Find out whether it's
  required, and whether it makes layout assumptions the page has to respect.
- **Any light-DOM stylesheets.** Some components style content outside their
  own shadow root and ship that CSS as a separate file. These are easy to
  miss and the page looks broken without them.

**Then test it.** Write the smallest possible page that loads the runtime and
renders one component. If you can open it, you're done. If you can't render
anything in this environment, write the boot block down anyway and mark it
`[untested]` in the profile, loudly.

---

## 3. The vocabulary

You don't need the whole catalog. You need enough to convert a page, which
is roughly the fifteen to twenty-five things a page is made of.

Work through this list and record the real name, the real props, and the
real slots for each. Mark anything the system doesn't have as `unmapped`,
because absence is a genuine finding.

**Page-level:** page shell, header, main, footer, section or band, layout
container, grid, grid item, stack or spacing container

**Content:** heading, prose or rich-text passage, text link, list, image or
media, icon

**Components:** button, button group, card and its zones, badge or tag,
hero or page header, form field types, alert or notice, table, tabs,
accordion, modal or dialog, navigation

For each one, capture:

- the **exact tag or import name**, in the system's own casing
- the **real props**, especially the variant axes, and their allowed values
- the **real slots or children**, exactly as declared
- any **required wrapper**, which is the number one cause of a conversion
  rendering wrong. Grids that need an item wrapper around each child are
  extremely common and completely invisible until the layout collapses.
- an **evidence tag**

**Read the guidance too, not just the API.** A catalog that says "don't use
alert for non-urgent messages, use a notice band" has just saved you the
most common wrong mapping there is. Copy those don'ts into the profile.

---

## 4. Tokens

- **The custom property prefix.** `--ds-`, `--ed-theme-`, `--spectrum-`,
  whatever it is. This is what phase 4 greps for.
- **The tiers**, if the system has them. Most mature systems separate
  primitives from semantic tokens, and consumers are meant to use the
  semantic tier only.
- **The families you'll actually need**: background, foreground or content,
  border, spacing, radius, shadow, type scale.
- **What's off-limits.** If primitives are private, say so here, because
  "use tokens" and "use the right tier of tokens" are different rules and
  only one of them survives review.

---

## 5. The rules

Every system has opinions. Write them down, because these are what make a
conversion feel like it belongs to this team rather than to a generic
"design system" idea.

- **Naming convention** for classes, if consumers write any at all
- **Anti-patterns** the system explicitly forbids
- **The spacing doctrine.** Who owns the space between two things: the
  parent, the child, a utility? Getting this backwards produces a page that
  validates and still looks wrong.
- **Accessibility baseline.** Which level, and what's automatic versus what
  the consumer has to supply.
- **Canonical compositions.** Does the system publish reference examples for
  a page shell, a card grid, a section with a heading? **Copy these
  verbatim into the profile.** They're worth more than any prose, because a
  canonical composition is the system telling you exactly how its parts fit
  together.
- **Page templates.** Some systems ship whole-page starting points. If yours
  does, list them, because starting from a template beats composing from
  primitives every time.

---

## 6. Validation

Ask: *"Is there a way to check that a page is using the system correctly?"*

A validator tool, a linter rule set, a CI check, a codemod. Record the exact
command. Phase 4 will run it. If there isn't one, record that honestly; the
receipt will lean on the deterministic greps instead, and it'll say so.

---

## 7. Write the profile

Fill in `templates/system.md` and save it to `vibe-killer/SYSTEM.md`.

Then read it back to the user in about five lines: which rung of the chain
answered, how many components you captured, how many are `[verified]`,
whether the runtime is tested, and what's unmapped. Ask them to correct
anything that looks wrong. They'll spot a bad name instantly and it costs
nothing to fix now.

---

## Keeping it honest

Re-run this intake when:

- the system ships a major version
- a conversion produces a name nobody can find
- the runtime URLs stop working, or the version they resolve to has moved
- `verified_on` is more than a couple of months old

A stale profile is worse than no profile, because it's confident. The
hand-written component reference this skill's approach grew out of was 26%
wrong against its own live catalog after six weeks, and every error in it
was invisible until something rendered empty.
