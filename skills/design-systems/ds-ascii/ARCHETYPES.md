# The archetypes

Fourteen shapes this skill knows how to draw.

ASCII doesn't need to know your 164 components. It needs to know which of
these fourteen shapes each region of the page is, and what your system calls
that shape. Archetypes are stable across design systems. Component names
never are. Every system has a card; no two agree on what its zones are
called.

Binding an archetype means answering its questions in your profile. An
archetype with no binding still renders, it just renders honestly (see
**Unmapped archetypes** at the end).

---

## 1. `page-shell`

The outer frame that holds everything. Most systems have no component for
this, and that's fine. It's the `╔═╗ … ╚═╝` border and nothing else.

**Binding questions:** Does your system have a page wrapper? If not, leave
it unbound. It costs nothing.

## 2. `site-header`

The global bar across the top: brand, navigation, and usually one utility
action.

```
╔═ [1] <site-header> ════════════════════════════════╗
║ BRANDMARK    Work  Writing  About    [ Sign in ]   ║
```

**Zones:** brand, navigation, utility actions.

**Binding questions:** What is the header component called? What holds the
brand mark? What is the navigation component, and does it have its own item
component? Is there a separate utility nav?

## 3. `hero`

The page banner. Owns the page's single h1, spans the full width, and often
carries a media element beside or behind the copy.

```
╠═ [2] <hero> ═══════════════════════════════════════╣
║            · eyebrow or dim date caption ·         ║
║           O  U  T  E  R   B  A  N  K  S            ║
║           ═════════════════════════════            ║
║          One line of supporting body copy.         ║
║     ▛▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▜   ┌────────────────┐     ║
║     ▌ GET THE DETAILS ▸ ▐   │  Packing list  │     ║
║     ▙▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▟   └────────────────┘     ║
```

**Zones:** eyebrow, h1, body, actions, media.

**Binding questions:** What is the hero or banner component called? Does it
take a background image, a side image, or neither? Which prop sets the
media's side? Is there a height or size prop, and what are its values?

If a system has no hero (many component libraries don't), it is usually
composed from a section plus a heading. Record that composition in the
profile rather than inventing a hero component.

## 4. `section`

A content region with a heading and a body. The workhorse of any marketing
or docs page.

```
╠═ [3] <section> ════════════════════════════════════╣
║                The Trip at a Glance                ║
║                ────────────────────                ║
║          Supporting description in body type.      ║
```

**Zones:** heading, description, body.

**Binding questions:** What is the section component called? Does it have a
dedicated heading slot, or does the heading just go inside it? Is there a
separate width-capping container that belongs inside it?

## 5. `grid`

Equal columns. Almost always wraps cards.

**Binding questions:** What is the grid component called? How are columns
specified (a `variant="3up"` string, a `columns={3}` number, a CSS class)?
Does each cell need its own wrapper component, and what is it called?

The cell wrapper matters more than it looks. Several systems refuse to lay
out anything that isn't their own grid-item child, so a render that skips it
is describing markup that would not work.

## 6. `card`

Three stacked zones: media, body, actions.

```
┏━━━━━━━━━━━━┓
┃▒▒▒▒▒▒▒▒▒▒▒▒┃   media zone: shaded band, media only
┃░░░░/^^\░░░░┃
┃▒▒▒▒▒▒▒▒▒▒▒▒┃
┣━━━━━━━━━━━━┫
┃ The House  ┃   body zone: h3, copy, »accent«
┃ 6BR sound- ┃
┃ »sleeps 11«┃
┣━━━━━━━━━━━━┫
┃ [ Floors ] ┃   action zone: buttons only
┗━━━━━━━━━━━━┛
```

Any zone can be absent. A text-only card is just the body zone.

**Binding questions:** What is the card component called? What are its three
zones called in your system (slots, props, sub-components)? **Can the media
zone hold a heading, or is it media only?** Are there card variants
(elevated, outlined, filled) and which is the default?

That third question is the one that catches people. Several systems forbid
a heading in the media zone because it paints as an image band and drops out
of the document outline. If your system forbids it, record that as an
anti-pattern in the profile and the render will respect it.

## 7. `button`

Three visual ranks. See the grammar for the exact patterns.

**Binding questions:** What is the button component called? What are the
primary, secondary, and tertiary variants called? Does it become a link when
given an href, or is there a separate link component? Is there a button
group component for pairs?

If your system has five ranks, bind the three with the most visual weight
and list the rest in the legend. ASCII gives you about three distinguishable
weights.

## 8. `field`

A single form input: text, textarea, select, radio, checkbox, toggle.

**Binding questions:** For each of the six kinds, what is the component
called? Do grouped inputs (radios, checkboxes) need a group wrapper, and
what is it called? Is there a separate help-text or error-message component?

It's normal to bind some kinds and not others. Bind what exists.

## 9. `form`

A field paired with a submit action. The newsletter signup, the search box.

**Binding questions:** Does your system ship a single-field form, a search
form, or a newsletter signup as their own components? If not, this
archetype is composed from a field plus a button, and the profile should say
so.

## 10. `table`

Rows and columns of structured data.

```
┌──────────┬───────────────────┬─────────────┐
│ DATE     │ VENUE             │             │
├──────────┼───────────────────┼─────────────┤
│ Oct 31   │ The Crypt, Philly │ [ Tix ]     │
└──────────┴───────────────────┴─────────────┘
```

**Binding questions:** What is the table component called? Are there
separate components for header, body, row, header cell, and data cell? Is
there a responsive wrapper for horizontal overflow?

## 11. `list`

Repeating vertical items. Link lists, feeds, event listings.

**Binding questions:** What is the list component called, and its item
component? Are there purpose-built list recipes (a link list, an icon link
list, a timeline) worth binding separately?

## 12. `media`

An image, a video embed, or a figure. Drawn as a shaded band with a small
ASCII sketch, never as a heading.

```
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒░░░░░▛▀▀▀▀▀▜░░░░░▒
▒░░░░░▌  ▸  ▐░░░░░▒
▒░░░░░▙▄▄▄▄▄▟░░░░░▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
```

**Binding questions:** What is the image component called? Is there a
separate figure component with a caption, or a video embed wrapper? Is alt
text a prop or an attribute on a slotted `<img>`?

Keep alt text visible in the render where you can. An empty media box with
its alt text showing is a better wireframe than a grey rectangle, because it
puts the accessibility decision on the page where someone will argue with
it.

## 13. `overlay`

A modal or a drawer. Shade the backdrop, float a heavy box on top.

```
║░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░║
║░░░░░┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓░░░░░░░░░░░░░░║
║░░░░░┃ Modal Title            [ × ]  ┃░░░░░░░░░░░░░░║
║░░░░░┃ Body…        ▐ Confirm ▸ ▌    ┃░░░░░░░░░░░░░░║
║░░░░░┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛░░░░░░░░░░░░░░║
```

A drawer is the same box, flush to one wall.

**Binding questions:** What are the modal and drawer components called? Do
they have header and footer regions?

## 14. `footer`

The global bar across the bottom: brand, links, legal.

**Binding questions:** What is the footer component called? What holds the
link list?

---

## Variants worth noting, not archetypes

A **stat tile** is a card with a label, a display-size value, and a meta
line. Bind it as a card variant rather than its own archetype.

A **promo block** is a section with centered content and one primary action.
Same treatment.

---

## Unmapped archetypes

When a page needs a shape your system has no component for, **do not invent
a name.** Draw the shape with the generic border weight and mark it in the
ANATOMY legend:

```
[4] <unmapped: hero>
    · no hero component found in this system
    · composed here from section + heading + button
```

This happens constantly and it is not a failure. Most component libraries
ship buttons, fields, and cards while shipping nothing for page layout. A
render that says so is telling you something true about your system, and it
is a much better artifact than one that quietly makes up a component name
your developers will search for and never find.
