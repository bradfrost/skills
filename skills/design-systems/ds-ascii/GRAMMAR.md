# The rendering grammar

How to draw. Not what to draw.

Everything in this file is true no matter whose design system you're
rendering. It describes the frame, the weights, the type ramp, and the
button ranks. It never names a component, because component names belong to
your system and live in your profile.

Follow it and every prototype reads as one system: the boxes mean the same
thing every time.

---

## 1. The frame and the width rule

Everything lives inside a fixed-width frame.

**Default inner width: 52 columns** (54 with walls). That number is tuned so
a render never wraps in a chat pane, a Slack message, or a PR body, which
are the places these things actually get pasted.

Your profile can set a different width with `frame_width`. A team whose
prototypes live in READMEs or terminals might use 80. Whatever the number,
it's a hard ceiling for that render.

> **The single most common failure is a line that exceeds the frame and
> wraps.** One long line shatters every box below it. Count every row before
> you ship, and put labels *inside* the frame rather than hanging them off
> the right margin.

**Emoji are banned inside any framed region.** Most emoji render
double-width in a monospace grid, so a single one silently shifts the right
wall by a column and the box breaks. Use ASCII sketches and the shading ramp
instead. Emoji are fine in the prose around the frame, never inside it.

The same caution applies to any character you aren't certain is
single-width. The characters used in this grammar are safe: box-drawing,
block elements, `·`, `»«`, `→`, `▸`, and `…`.

## 2. Labels: tag the container, list the anatomy below

Only **top-level containers** get a label, embedded in their own top border
with a bracketed key. Nested parts are not tagged on the diagram. They're
described in a keyed `ANATOMY` legend underneath.

Full-bleed region, where the tag rides the divider:

```
╠═ [3] Section › Grid ═══════════════════════════════╣
```

Contained box, where the tag rides the box's own top edge:

```
┏━ [3] Card ━━━━━━━━━┓
```

Then, below the whole diagram:

```
ANATOMY
[3] Section (align center) › Grid (3 columns)
    · h2 "The Trip at a Glance"
    · 3 × Grid Item › Card, each:
        · media zone → shaded band
        · body zone → h3 + copy + »accent«
        · action zone → one button
```

The legend is what makes this a spec rather than art. It's the layer that
connects a picture to real components, so it carries the exact names from
your profile.

## 3. The contrast kit

Thin single lines read as weak. Use weight and shading deliberately.

**Shading ramp**, all single-width: ` ` `░` `▒` `▓` `█`

Use it for media fields, background washes, emphasis fills, and the bodies
of primary buttons.

**Border weights.** Heavier means higher in the hierarchy.

| Weight | Characters | Use |
|--------|-----------|-----|
| double | `╔═╗ ║ ╚═╝` | the page shell and full-bleed regions |
| heavy  | `┏━┓ ┃ ┗━┛` | cards and emphasis containers |
| light  | `┌─┐ │ └─┘` | secondary boxes, outline buttons, form fields |
| tee    | `┣━┫` / `╠═╣` | zone dividers in a box, region dividers in the shell |

## 4. Typography: show the hierarchy

Encode the type scale visually. Never write everything at one weight.

| Level | ASCII encoding |
|---|---|
| h1, display | `S P A C E D  C A P S` + `═══════` rule |
| h2, section title | `Title Case` + `───────` rule |
| h3, card or subsection title | `Title Case`, no rule |
| body | plain sentence case |
| caption, meta, eyebrow | `· dim lowercase ·` |
| accent value (price, stat, link) | `»value«` |

Wider and heavier underline means higher heading level. A reader should feel
the descent from h1 to body without consulting a legend.

**When the column is too narrow for spaced caps**, fall back to plain CAPS
and keep the `═══` rule. The rule is what carries the level. Say you did it
in the deviations note (see §8).

## 5. Buttons: real weight, clear ranks

The contrast between ranks is the whole point. A primary should look like
pressed metal next to a secondary.

**Primary**, filled and three rows:

```
▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜
▌ GET THE DETAILS ▸ ▐
▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟
```

**Primary compact**, one row, for cards and tight rows: `▐ Add ▸ ▌`

**Secondary**, a light outline pill:

```
┌────────────────┐
│  Packing list  │
└────────────────┘
```

or one row: `[ Packing list ]`

**Tertiary or link:** `See roster →`

The `▸` chevron marks the primary action. A button group is buttons sharing
a row, with the filled primary beside the outline secondary.

If your system has more than three button ranks, bind the three that carry
the most visual weight and note the rest in the ANATOMY legend. ASCII has
about three distinguishable weights before the differences stop reading.

## 6. Form fields

```
Text      Label  [____________________]
Textarea  Label  ┌────────────────────┐
                 └────────────────────┘
Select    Label  [ Option           ▾]
Radio            (•) Chosen  ( ) Other
Checkbox         [x] On   [ ] Off
Toggle           [ ON ●━]  /  [━● OFF ]
Single field     [__________________]  ▐ Submit ▸ ▌
```

## 7. The fidelity dial

- **Sketch.** Boxes and keyed labels, no shading, no copy. For structure
  conversations.
- **Wireframe.** The default. Full grammar: shading, weighted borders, real
  copy, ANATOMY legend.
- **Illustrated.** Adds ASCII scenes in the media zones. The fun mode, and
  the right one when the brief has a strong visual hook.

Drop a dense region down a level rather than clipping its copy. Three
columns inside a 52-column frame leaves about 11 usable characters per line,
which is not enough for real sentences. Either go to two columns or render
that region at sketch fidelity and put the copy in the legend.

## 8. Build it with a padding helper, and declare your deviations

Aligning by hand is where width bugs come from. For anything past a quick
sketch, build the render with the padding helper in `tools/build_example.py`
so every row is exact by construction rather than by counting.

Before you ship a render, check two things: every line is the same length,
and no emoji sit inside the frame. The helper prints both.

When you had to bend the grammar to fit a real page, say so underneath the
render in a short `DEVIATIONS` note. A declared deviation is a judgment call
the reader can check. An undeclared one is just a broken rule.
