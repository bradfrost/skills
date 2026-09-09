---
name: ds-ascii
description: Render UI wireframes as labeled ASCII art where every region maps to a real component in YOUR design system. Use when someone asks for an ASCII prototype, a text wireframe, a monospace mockup, or wants to sketch a page layout inside a chat, PR, issue, or Slack thread without opening a design tool. Triggers include "make me an ASCII prototype of…", "wireframe this as text", "sketch a homepage for…", "mock this up in ASCII", "show me this page as ASCII". Builds a one-time profile of the design system's component vocabulary, then renders against it. Typography hierarchy is drawn, not described.
---

# ASCII prototyping with your design system

Turn a plain-language brief into a monospace wireframe where every region is
a labeled component from your own design system, and the type hierarchy is
visible rather than described.

It's a real spec you can read anywhere text goes: a chat, a PR description,
a code comment, a Slack thread. No rendering pipeline, no context switch,
and because the constraint is a monospace grid, it forces the ruthless
boxes-and-arrows thinking that good wireframing wants anyway.

The part that makes it more than doodling is that **every region maps to a
component that actually exists in your system**, with its real name. That
turns a picture into something a designer or a developer can build from.

## The three layers

1. **`GRAMMAR.md` — how to draw.** The frame, the border weights, the
   shading ramp, the type ramp, the button ranks. Universal, and it never
   names a component.
2. **`ARCHETYPES.md` — what to draw.** Fourteen shapes: page shell, header,
   hero, section, grid, card, button, field, form, table, list, media,
   overlay, footer. Also universal.
3. **`ds-ascii/PROFILE.md` — what your team calls it.** The binding table
   from archetype to real component name, built once by
   `intake/PROFILE-INTAKE.md` and kept in the user's project.

Archetypes are stable across design systems. Component names never are. That
split is the whole design: every system has a card, and no two agree on what
its zones are called.

## Modes

### Mode 1 — Render (the common case)

1. **Find the profile.** Read `ds-ascii/PROFILE.md` if it exists and confirm
   it's current ("this profile was verified on <date>, still good?"). If
   there's no profile, run `intake/PROFILE-INTAKE.md` first. It takes a
   couple of minutes and everything after it is faster.
2. **Read the brief for page type.** Homepage, listing, form, dashboard,
   auth? That sets the skeleton.
3. **Pick the fidelity level.** Default to **wireframe**. Go
   **illustrated** when the brief has a strong visual hook, and drop a dense
   region to **sketch** rather than clipping its copy.
4. **Compose top to bottom**, mapping each region to an archetype and each
   archetype to its binding.
5. **Build it with the padding helper** in `tools/build_example.py` so
   widths are exact by construction. Hand-counting is where renders break.
6. **Write the ANATOMY legend** underneath, with the real component names,
   and a `DEVIATIONS` note if you had to bend the grammar.

### Mode 2 — Build or refresh a profile

Run `intake/PROFILE-INTAKE.md`. Also the right move when a render produced a
name someone couldn't find, or when the system shipped a major version.

### Mode 3 — Re-render against a different profile

Same brief, different profile. Useful for comparing what two systems make
easy, and it's how the proof gate in `examples/` works.

## The rules that keep a render honest

1. **Never invent a component name.** If an archetype has no binding in the
   profile, draw the generic shape and mark it `<unmapped: hero>` in the
   legend. Most component libraries ship nothing for page layout, so this
   comes up constantly and it is not a failure. A render that says so is
   telling you something true about your system.
2. **Carry the evidence tags through.** A binding read from a manifest is
   `[verified]`; one a human told you is `[reported]`. If a render leans on
   `[reported]` bindings, say so under the legend.
3. **Never exceed the frame width.** One long line wraps and every box below
   it shatters. The helper checks this; run it.
4. **No emoji inside a framed region.** They're double-width and shift the
   right wall. Emoji belong in the prose around the frame.
5. **Declare your deviations.** When a real page forced you to bend the
   grammar, write it down underneath. A declared deviation is a judgment
   call the reader can check; an undeclared one is a broken rule.
6. **Say what the output is not.** It's a wireframe spec, not generated
   code. Nobody should paste it into a build expecting markup.

## Anti-patterns

- Flat text at one weight. If the hierarchy isn't visible, the render failed.
- Unlabeled ASCII art. That's decoration, not a prototype.
- Tagging nested parts on the diagram. Tag the container; the legend carries
  the parts.
- Rendering primary and secondary buttons at the same weight. Rank has to
  show.
- Headings in a card's media zone, when the profile's anti-patterns forbid
  it.
- Three columns of real sentences in a 52-column frame. That leaves about 11
  usable characters per line. Drop to two columns or drop the fidelity.

## Files in this kit

- `GRAMMAR.md` — the universal rendering grammar
- `ARCHETYPES.md` — the fourteen shapes and their binding questions
- `intake/PROFILE-INTAKE.md` — the evidence chain that builds a profile
- `profiles/PROFILE-FORMAT.md` — the profile file format
- `profiles/material-web.md`, `profiles/eddie.md` — two real, verified
  profiles, deliberately opposite
- `reference/CAPABILITIES.md` — what this skill can and cannot do
- `reference/FIGMA-ACCESS.md` — reaching a design library, and what each
  bridge actually sees
- `examples/` — the same brief rendered against both profiles
- `tools/build_example.py` — the padding helper

## State (in the user's project)

```
ds-ascii/
└── PROFILE.md          ← the binding table, built once
```

If you can write files, keep the profile there. If you can't, produce it as
a message the user can save and paste back next time.
