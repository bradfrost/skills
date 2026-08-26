---
station: 6
name: Visual design
quality: Refined (quality 6 of 10)
question: As rendered, does the product look designed — a cohesive design language with real hierarchy, balance, and brand distinctness — or does it merely look assembled from correct parts?
---

# Station 6 — Visual design

**Quality: Refined.** This station judges the whole visual result, on two levels. The **craft** level: consistent spacing rhythm, true alignment, deliberate type scale — users don't consciously notice good spacing, but they absolutely feel bad spacing. And the **design-language** level: brand expression, distinctness, balance, contrast, art direction — whether the assembled product feels *designed* or merely *assembled*. A design system guarantees consistent parts; it does not guarantee a designed whole. A product can use every component correctly and still read as an undifferentiated spray of stacked text and cards — technically clean, visually anonymous, no point of view. Something that feels refined and intentional scores higher than something that feels disjointed, incomplete, or generic, even when both are "correct."

This is the most subjective station in the set — so hold findings to the same evidence bar as everywhere else: name the screen, describe *what* reads as disjointed (competing focal points, three different section treatments, no dominant hierarchy on the page, cards used as the answer to every layout question), and cite the shared lens (NN/g "aesthetic and minimalist design") rather than asserting taste. If intake captured a stated design ideal — brand guidelines, reference products, north-star mockups (`GARAGE.md` → "Intent & ideal") — score against *that* ambition; the gap between shipped and stated ideal is the finding.

It's distinct from adoption (are the right parts used?) and clarity (do the words work?): this is whether the assembled result looks finished *and* looks like *something*.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Spacing rhythm | Rendered pages: consistent, token-scale spacing between/within blocks | Screenshots · interview |
| Alignment | Rendered: edges and baselines line up; grid honored | Screenshots (overlay a grid) · interview |
| Visual hierarchy | Rendered: type scale, weight, and emphasis guide the eye | Screenshots · interview |
| Cross-page consistency | Same patterns rendered the same way across pages | Side-by-side screenshots · interview |
| Design language & brand | Rendered pages vs. stated brand/design ideal: distinctness, personality, art direction | Brand guidelines · reference products · interview |
| Composition | Page-level layout variety and balance — or template monotony | Full-page screenshots · interview |
| Optical details | Icon sizing/alignment, border/radius consistency, image crops | Zoomed screenshots · interview |
| Theme/dark-mode | If supported: both themes rendered and checked | Screenshots per theme |

## Inspection procedure

**Part A — craft mechanics**

1. **Scan for spacing rhythm.** Is vertical and horizontal spacing on a consistent scale (ideally the system's spacing tokens), or arbitrary and uneven? Cramped here, floaty there is the tell.
2. **Check alignment.** Overlay a mental (or literal) grid: do element edges, text baselines, and columns actually line up? Look for the half-pixel-off, the one card that's indented, the label that doesn't share a baseline with its field.
3. **Check cross-page consistency.** The same construct (a card, a section header, a toolbar) should render identically across pages. Divergence signals one-off overrides — cross-link to Station 1.
4. **Inspect optical details:** icons sized and aligned to their text, consistent border widths and radii, images cropped/positioned deliberately, consistent shadow/elevation. If the product themes (light/dark, brand variants), check both — polish often survives one theme and breaks in the other.

**Part B — design language**

5. **Read the hierarchy.** Squint at each core page — does emphasis (size, weight, color, spacing) guide the eye to what matters, or is everything shouting/flat? Is there a clear dominant element per page, or does every block carry the same visual weight?
6. **Assess distinctness.** Cover the logo: could this be any product built with the same component library, or does it have an identifiable visual voice — color use, type character, imagery, motion, layout personality? Generic-but-tidy is a real finding, not a pass.
7. **Assess composition.** Is there page-level art direction — varied, intentional layouts matched to content — or does every page fall back to the same stack of section-heading + cards? Template monotony is the "spray of stacked text and cards" tell.
8. **Compare against the stated ideal.** If brand guidelines, reference products, or north-star designs exist (intake), put shipped screens side-by-side with them. Name the specific gaps — this converts the most subjective checks into evidence.

## Warning lights

- Inconsistent, off-scale spacing; cramped or floaty regions; misalignment
- Flat or confused hierarchy — no dominant element, everything the same weight
- The same construct rendered differently on different pages
- Every page the same template: heading, stack of cards, repeat — no compositional intent
- No identifiable visual voice — the product could be any other built on the same system
- Shipped screens visibly short of the team's own stated brand/design ideal
- Misaligned/mis-sized icons, inconsistent radii/borders, squished images; polish that breaks in one theme

## Scoring anchors

- **Red (0–3):** Visibly unfinished — pervasive misalignment, arbitrary spacing, inconsistent rendering of the same patterns. Reads as a prototype.
- **Yellow (4–7):** Mechanically tidy but visually anonymous or uneven — spacing and alignment mostly hold, yet the product reads as assembled-not-designed: template monotony, flat hierarchy, no brand distinctness, or a clear gap from the stated design ideal. *(Most component-correct products land here — clean parts, no whole.)*
- **Green (8–10):** The team can honestly say: *"The product reads as deliberately designed — consistent craft under zoom and across themes, clear hierarchy on every page, compositional variety matched to content, and a distinct visual voice that matches our stated brand ambition."*

## Turning off the light

- Craft-level issues usually trace to app CSS overriding the system — fixing Station 1's drift fixes these for free (that's the leverage; sequence Station 1 first). An agent can diff rendered spacing against the token scale.
- Design-language issues are *not* mechanical fixes — they're a design investment. The work-order item is honest framing: "establish/apply a design language" (art direction, layout patterns beyond the card stack, brand expression), owned by a designer, not an agent.
- Cross-page inconsistency of a construct is the signal to extract it into a shared component/recipe.
- If no stated design ideal exists, that's the first move: the team can't converge on "refined" without naming what refined looks like for them.

## Station record

```markdown
### Station 6 — Visual design: <RED|YELLOW|GREEN> (<n>/10)
- Pages reviewed: <n> · Craft (spacing/alignment/consistency): <summary> · Design language (hierarchy/distinctness/composition): <summary> · Ideal compared: <stated ideal or "none provided"> · Themes checked: <list>
- Evidence level: <live / screenshot / interview, per check>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
