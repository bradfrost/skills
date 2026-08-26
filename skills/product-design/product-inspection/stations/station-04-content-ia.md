---
station: 4
name: Content & information architecture
quality: Clear (quality 4 of 10)
question: Can people understand the words, find what they need, and know where they are — or do labels, navigation, and structure get in the way?
---

# Station 4 — Content & information architecture

**Quality: Clear.** The most beautiful, fast, accessible product still fails if users can't understand the labels or find the thing they came for. This station inspects the product as a reader and wayfinder: is the language plain and consistent, is navigation learnable, is content structured so it's scannable, and does the product always answer "where am I and where can I go?" It's the layer design systems rarely cover — components are correct, but the *words and structure* are the product team's. (NN/g lens: "match between the system and the real world," "consistency and standards," "recognition rather than recall" — cite these by name on judgment findings.)

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Navigation & IA | Live instance: walk the nav, map the structure | Sitemap · screenshots · interview |
| Labels & terminology | Rendered UI: button/link/menu/field labels, consistency | Screenshots · interview |
| Microcopy | Empty states, errors, help text, confirmations, tooltips | Screenshots · interview |
| Wayfinding | Breadcrumbs, active-state, page titles, back behavior | Live walk · screenshots |
| Content structure | Headings, scannability, chunking on dense pages | Rendered DOM · screenshots |
| Reading level & tone | The actual copy vs. audience | Interview: "who reads this?" |

## Inspection procedure

1. **Map the IA.** Walk the navigation and sketch the structure. Is it shallow enough to learn, grouped sensibly, labeled in the users' language (not internal jargon or system nouns)?
2. **Audit labels for clarity and consistency.** Do the same concepts use the same words everywhere? Are actions verbs the user understands ("Publish," not "Commit entity")? Any label that needs a tooltip to decode is a finding.
3. **Read the microcopy** in the seams — empty states, error messages, confirmations, help text. Is it human, specific, and actionable, or generic/blaming/absent? ("Something went wrong" tells the user nothing.)
4. **Check wayfinding:** does every page have a meaningful title, an active nav indication, breadcrumbs where depth warrants, and sane back behavior? Can a user always tell where they are?
5. **Assess content structure** on the densest pages: real heading hierarchy, chunked and scannable, not a wall of text or an undifferentiated grid.
6. **Gauge reading level and tone** against the audience — plain for a broad audience, precise for an expert one; consistent voice throughout.

## Warning lights

- Navigation labeled in internal/system jargon; structure too deep or miscategorized
- The same concept called different things in different places
- Generic or blaming error copy; empty states with no guidance
- No page titles, active-state, or breadcrumbs — users can't tell where they are
- Dense pages with no heading structure or scannable chunking
- Tone or reading level mismatched to the audience

## Scoring anchors

- **Red (0–3):** Users routinely can't find or understand things — jargon labels, broken wayfinding, absent or unhelpful microcopy.
- **Yellow (4–7):** Broadly clear with rough spots — an inconsistent term, a generic error, a page that's hard to scan, a nav grouping that misleads.
- **Green (8–10):** The team can honestly say: *"Labels are plain and consistent, navigation is learnable, microcopy is helpful, and users always know where they are and where they can go."*

## Turning off the light

- A terminology pass (one concept → one word) is cheap and disproportionately improves perceived quality; an agent can inventory inconsistencies.
- Rewrite the generic errors and empty states first — highest-friction, lowest-effort.
- If the product has search/analytics, mine failed searches and drop-off pages for where IA is failing real users.

## Station record

```markdown
### Station 4 — Content & information architecture: <RED|YELLOW|GREEN> (<n>/10)
- IA depth/shape: <summary> · Label consistency: <findings> · Microcopy quality: <summary>
- Evidence level: <live / screenshot / interview, per check>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
