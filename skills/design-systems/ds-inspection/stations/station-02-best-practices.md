---
station: 2
name: Best practices
quality: Sound (quality 2 of 5)
question: Do design system assets embody industry, organization, and format best practices?
---

# Station 2 — Best practices

**Quality: Sound.** Existence isn't enough — is what's in the system actually good? Three lenses: industry best practices, *your organization's* standards (brand, UX, front-end conventions), and format-specific craft — a Figma library should follow Figma best practices, a web-component library should follow web-component best practices, docs should follow docs best practices. Judge against the house conventions recorded in GARAGE.md, not a generic bar.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Design library craft | Live bridge: inspect component structure, auto-layout, layer names, properties | Screenshots of layers/properties panels · interview |
| Code craft | Repo: read 3–5 representative components end to end | Pasted component source |
| Docs craft | Docs site: read 2–3 component pages + one guideline page | Pasted pages · screenshots |
| House conventions | Org standards docs, lint configs, contribution guide | Interview: "what are your own rules?" |

## Inspection procedure

1. **Design library (sample 3–5 components):** auto-layout everywhere it belongs, or absolute positioning? Real component properties/variants, or near-duplicate components? Layer names meaningful, or `Frame 22`? Values bound to variables/styles, or hardcoded? Instances attached, or detached copies? File hierarchy sane — library, product, and draft files separated?
2. **Code library (read 3–5 components):** semantic markup or div soup? Modern, fluid layout or brittle fixed dimensions? Magic numbers, or tokens? Logical properties (so RTL and vertical writing modes don't break)? Component APIs right-sized — or overstuffed props and rigid, brittle JavaScript? Token architecture referenced properly (semantic tier, not raw primitives)?
3. **Docs (read 2–3 pages):** clear description, anatomy, do/don't, live examples — or walls of text? Written for all disciplines, or skewed to one? Cross-linking between components and high-level guidelines (a11y, i18n), or orphan pages?
4. **House-standards check:** for each violation, ask whether it breaks *industry* practice, *org* standards, or *format* conventions — and whether it's a documented intentional deviation.

## Warning lights

- Absolute positioning where auto-layout belongs; detached instances
- Meaningless layer names (`Frame 22`)
- Div soup, magic numbers, brittle fixed layouts
- No logical properties, so RTL and vertical writing break
- Docs that are walls of text with no examples
- No file hierarchy — library, product, and draft files all mixed together

## Scoring anchors

- **Red (0–3):** Craft problems are structural: pervasive absolute positioning or detached instances, div soup and magic numbers throughout, docs effectively unusable.
- **Yellow (4–7):** Fundamentals in place but drift is visible — some sloppy layer naming, occasional hardcoded values, docs uneven, conventions exist but aren't enforced.
- **Green (8–10):** Sampled assets consistently follow industry, org, and format best practices; downstream users get those best practices for free just by using the system.

## Turning off the light

- Have AI **scan for un-idiomatic patterns** — non-semantic markup, missing auto-layout, magic numbers — against your house conventions. FigmaLint-style linting surfaces much of the design-side automatically.
- Then feed the audit + your conventions back through AI to **make the improvements**: richer layer names, tokens replacing hardcoded values, semantic markup replacing div soup. Work asset-by-asset (Figma pass, code pass, docs pass) so each lands its format's conventions.
- Write the conventions down as you go — an org-standards doc turns every future audit from opinion into a checklist (and becomes machine-checkable at Station 5, and machine-readable context at Station 9).
- Related deep tools: Design System Ops `component-api-validator`, `token-compliance`, `naming-audit`.

## Station record

```markdown
### Station 2 — Best practices: <RED|YELLOW|GREEN> (<n>/10)
- Sampled: <components/files/pages inspected>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <finding + evidence, tagged industry|org|format>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
