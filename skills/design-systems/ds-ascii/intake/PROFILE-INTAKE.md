# Profile Intake — teach the skill your design system

Before the first render, build the profile. This step produces
`ds-ascii/PROFILE.md` in the user's project: a binding table from the
fourteen archetypes to their real component names, with an evidence tag on
every row.

It's a one-time step. Every render after it reads the file and takes about a
minute.

**Agent: discover, don't interrogate.** Work down the evidence chain below
and read the vocabulary yourself wherever you can. Ask questions only for
what you genuinely cannot reach. A good intake against a published manifest
takes two minutes and asks maybe three questions. A pure interview takes
fifteen and is the fallback, not the goal.

**Never invent a component name.** If an archetype has no binding, write
`unmapped` in the table. That is a real, useful answer, and it is the whole
reason the evidence tags exist.

## 1. The evidence chain

Try these in order and stop when you have the names. Record which tier you
used in the profile's `source_kind`.

**Tier 1 — a design system MCP or knowledge server.** Check your own
available tools for anything that serves this system's catalog. If one is
connected, make a real call and confirm you're seeing their actual
components. This is the best tier: it's live, and it stays true.

**Tier 2 — a machine-readable catalog.** The one worth hunting for. Look
for:

- `custom-elements.json`, the Custom Elements Manifest, in the package root
  or on unpkg (`https://unpkg.com/<package>/custom-elements.json`)
- Storybook's `index.json` or `stories.json` at the docs site root
- any published `catalog.json` or design system API

Tiers 1 and 2 are the only ones that don't rot. Optimize for reaching them.

**Tier 3 — the repo.** Component directory names and exported symbols. Good
for names, poor for anatomy.

**Tier 4 — the docs site.** Fetch the component index page.

**Tier 5 — the design library.** Published Figma component names. Ask
whether a Figma library exists and probe your own tools for a bridge, the
same way the inspection skills do. `reference/FIGMA-ACCESS.md` covers what
each bridge can actually see and what to do when none is connected.

**Tier 6 — the interview.** Ask the human. See §3.

## 2. What to extract

For each of the fourteen archetypes in `ARCHETYPES.md`, answer its binding
questions. The manifest tiers will hand you names reliably and anatomy
hardly at all, which is normal, so expect to pair a tier-2 read for names
with a few interview questions for zones.

Three questions are worth asking even when ingestion went well, because they
change how the render draws and no manifest carries them:

1. **Can the card's media zone hold a heading, or is it media only?**
2. **Does the grid require its own cell wrapper component?**
3. **Which button variants are your primary, secondary, and tertiary?**

## 3. The interview, when you need it

Keep it short and conversational. Six questions, not a form.

1. What's the design system called, and is there a published component list
   anywhere I can read?
2. Are these web components, React components, or CSS classes? How should a
   component name look when I write it in a label?
3. Name the ten or fifteen components you reach for most.
4. Your card: what are its zones called, and can the media zone hold a
   heading?
5. Your buttons: which variant is the loud one, which is the quiet one?
6. Anything your system refuses that I should know about? (A grid that only
   accepts its own children, a slot that rejects headings.)

Then tell them plainly what just happened: *"Everything in this profile is
tagged `[reported]`, which means it came from you rather than from a catalog
I read. If you can point me at a `custom-elements.json` or a Storybook
index, I'll re-run this and upgrade the tags."*

## 4. Where the file goes

```
ds-ascii/
└── PROFILE.md
```

Write it using the format in `profiles/PROFILE-FORMAT.md`. If you can't
write files, produce the same content as a message the user can save.

Read the binding table back before you use it. A wrong name here becomes a
wrong label on every render.

## 5. Two profiles ship with this skill

`profiles/material-web.md` and `profiles/eddie.md` are real, verified
profiles you can read as worked examples. They're deliberately opposite:
Material Web binds seven of fourteen archetypes, Eddie binds all fourteen.

If the system you're rendering is one of those two, copy the file and you're
done. Otherwise use them as the shape to aim at.
