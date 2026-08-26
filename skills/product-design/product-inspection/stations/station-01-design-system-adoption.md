---
station: 1
name: Design system adoption
quality: Adopted (quality 1 of 10)
question: Is the product actually consuming the design system — correctly, as shipped — or has it drifted into one-off CSS, hardcoded values, and detached components?
---

# Station 1 — Design system adoption

**Quality: Adopted.** A design system is only worth what products actually consume — *adoption* is the word the design-system community uses for exactly this, and it's what this station measures: the gap between the system as published and the product as shipped. Low or drifting adoption erodes consistency, doubles maintenance, and quietly reintroduces every bug the system was meant to solve. This is the natural bridge to a paired `ds-inspection` run: that one grades the system (including its own adoption/coverage view from the system side); this one grades whether this product adopted it.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Component usage as rendered | Running instance: inspect the live DOM for the system's component markers (custom-element tags, BEM class prefixes) vs. bespoke markup | Screenshots · interview |
| Token adherence | Computed styles on real elements — are colors/spacing/type coming from the system's CSS custom properties, or hardcoded? | Repo grep for raw hex/px · pasted CSS |
| Dependency & version | Codebase: is the system imported as a versioned package, and how far behind latest? | `package.json` paste · interview |
| One-off styles | Repo: app-level CSS that should not exist (custom component classes, raw font/color/spacing) | Interview |
| Detached / forked components | Diff a sample of rendered components against the system's canonical version | Interview |

## Inspection procedure

1. **Load the running product** and inspect a sample of core screens. For 5–8 visible components, check the DOM: is each the system's real component (its tag / class prefix), or hand-rolled markup imitating it?
2. **Check token adherence on real elements.** Read computed styles: are color, spacing, typography, radii resolved from the system's custom properties, or hardcoded values? Spot the hardcoded ones.
3. **Check the dependency.** Is the system consumed as a published, versioned artifact — and how far behind latest is it? (If a paired `ds-inspection` ran, cross-reference its adoption/version findings.)
4. **Hunt app-level CSS that shouldn't exist.** Custom component classes, raw font/color/spacing declarations in the product's own stylesheets are drift by definition.
5. **Sample for detached components** — pieces that started as the system's and were forked locally, now drifting from canon.

## Warning lights

- Bespoke markup where a system component exists
- Hardcoded colors/spacing/type where tokens should resolve
- System pinned well behind latest, or vendored/copy-pasted instead of installed
- App-level custom component CSS
- Forked/detached components drifting from the canonical version

## Scoring anchors

- **Red (0–3):** The product mostly reimplements the system — bespoke components, hardcoded values throughout, or the system barely imported.
- **Yellow (4–7):** Real adoption with meaningful drift — a chunk of one-off CSS, some hardcoded values, a version well behind, a few detached components.
- **Green (8–10):** The team can honestly say: *"What renders is the system — components consumed as published, styling resolved from tokens, near-zero app-level component CSS, version current."*

## Turning off the light

- Run the companion **`/ds-adoption-plan`** skill — it turns exactly this station's findings into a full restoration estimate: teardown, verified pattern → component mappings, effort grades, and a phased build schedule.
- Feed the list of hardcoded values and bespoke components to an agent for a **drift report with proposed replacements** — most are mechanical swaps to the real component/token.
- Where the product needed something the system lacks, that's not product drift — it's a **system gap**; file it against the design system (and it should surface in that system's `ds-inspection` coverage station).
- Bump the system to latest and re-run; a lot of drift is just staleness.

## Station record

```markdown
### Station 1 — Design system adoption: <RED|YELLOW|GREEN> (<n>/10)
- Sampled: <n> components / <n> screens · System version: <in product> vs <latest>
- Evidence level: <live / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
