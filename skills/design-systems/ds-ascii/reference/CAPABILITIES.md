# What this skill can and cannot do

The value of an ASCII prototype from this skill is that its labels are real.
That claim is only worth something if it comes with an honest account of
where the labels came from, so here it is.

## What it does

Reads your design system's component vocabulary once, writes it to a
profile, and renders wireframes whose every region carries a real component
name from that profile.

## What it does not do

- **It does not generate code.** The output is a wireframe spec. Nobody
  should paste it into a build expecting markup.
- **It does not validate compositions.** It respects the anti-patterns your
  profile declares, and it knows nothing about the ones it doesn't.
- **It does not keep itself current.** A profile is a reading taken on a
  date. Systems ship. See **Drift** below.
- **It does not read a Figma library on its own.** That needs a bridge, and
  `FIGMA-ACCESS.md` in this folder covers what each one can see.

## How good is a binding, by tier

| Tier | Source | Names | Zones and anatomy | Tag |
|---|---|---|---|---|
| 1 | Design system MCP | **Live** | Often live | `[verified]` |
| 2 | Custom Elements Manifest, Storybook index | **Live** | **Usually absent** | `[verified]` names, `[reported]` anatomy |
| 3 | The repo | Live | Partial, from source | `[verified]` |
| 4 | Docs site | Live | Partial | `[verified]` |
| 5 | Figma library | Live for design names | Design-side only | `[verified]`, but design names may differ from code names |
| 6 | Interview | Human memory | Human memory | `[reported]` |

**Tier 2 is the one to aim for, and it has a specific hole.** A Custom
Elements Manifest reliably carries tag names and very often carries nothing
about slots. Material Web's manifest declares 54 elements and no slots on
any of the ones this skill checked. So the honest pattern is a tier-2 read
for names paired with three interview questions for anatomy, which is what
`intake/PROFILE-INTAKE.md` does.

**Tier 5 has a trap worth naming.** Figma component names and code component
names drift apart in most organizations. A binding read from a design
library tells you what designers call it, which is not always what a
developer will find in the package.

## Unmapped archetypes are a result, not an error

When a page needs a shape your system has no component for, the render marks
it `<unmapped: hero>` and composes it from what exists.

This is common. Most component libraries ship buttons, fields, and cards
while shipping nothing for page layout. The two profiles in this kit are
deliberately chosen to show both ends: Material Web binds seven of fourteen
archetypes, Eddie binds all fourteen. Neither is wrong. They're different
kinds of thing, and a render that shows the difference is doing its job.

## Drift

A profile is true on the day it was written and decays from there.

This skill exists because of a specific instance of that. Its own
hand-written component list, covering a design system its author owns, was
26% wrong against the live catalog after six weeks. Six names out of
twenty-three had moved.

That's the reason `verified_on` is in every profile's frontmatter, and the
reason the intake pushes so hard toward machine-readable sources. A profile
you can re-derive in a minute stays true. A profile you typed by hand does
not.

Re-verify when the system ships a major version, or the moment a render
produces a name someone can't find.
