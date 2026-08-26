---
station: 3
name: Accessibility
quality: Accessible (quality 3 of 10)
question: On the real running DOM — keyboard, focus, ARIA, contrast, semantics — does the product hold up where actual users are, not just where the design system promised it would?
---

# Station 3 — Accessibility

**Quality: Accessible.** A design system can ship perfectly accessible components and a product can still be unusable — because accessibility lives in *composition* and *content*: reading order, focus management across route changes, form labels wired to the right inputs, live-region announcements, contrast against the actual backgrounds in play. This station checks the product as a screen-reader and keyboard user meet it, not as the component library intends. If a paired `ds-inspection` graded the system's a11y green, that's the floor — this asks whether the product kept it.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Automated ruleset pass | Live instance + axe/Lighthouse/pa11y against real routes | CI a11y job output · pasted report |
| Keyboard operability | Live instance: tab through each core flow, no mouse | Screen recording · interview |
| Focus management | Live instance: focus visible? trapped in modals? restored on close/route change? | Screenshots of focus states · interview |
| Semantics & landmarks | Rendered DOM: headings order, landmark regions, list/table semantics | View-source · interview |
| Form accessibility | Rendered DOM: label↔input association, error text tied via aria-describedby | Repo form markup · interview |
| Contrast in context | Computed colors on real elements (text on its actual background) | Screenshots + contrast check |

## Inspection procedure

1. **Run an automated pass on real routes.** Reference tools: axe-core, [Lighthouse CLI](https://github.com/GoogleChrome/lighthouse), or pa11y — whichever is available (or equivalent; name the tool + version in the finding). Run against 3–5 representative pages, not just the homepage. Automated tools catch ~30–40% of issues — treat a clean pass as necessary, not sufficient.
2. **Keyboard-only walk of each core flow.** Unplug the mouse. Can you reach and operate every control? Is focus always visible? Any keyboard traps? Does tab order match visual/reading order?
3. **Focus management across state changes.** Open/close modals and menus — is focus moved in and restored out? On client-side route change, does focus land somewhere sensible (not lost to `<body>`)?
4. **Screen-reader spot check** of one core flow (VoiceOver/NVDA): are controls announced with name+role+state? Do dynamic updates (toasts, validation, async results) announce via live regions?
5. **Semantics audit** on rendered DOM: exactly one logical heading outline, proper landmarks (`main`/`nav`/`header`), lists and tables using real list/table markup — not `div` soup styled to look right.
6. **Forms:** every input has a programmatic label; errors are associated (`aria-describedby`) and announced, not just colored red.
7. **Contrast in context:** check text against the background it actually renders on (theme + any imagery), not the token's nominal pairing.

## Warning lights

- Automated violations on core routes (missing alt, unlabeled controls, low contrast)
- Anything reachable by mouse but not keyboard; invisible focus; keyboard traps
- Focus lost on route change or not restored after closing overlays
- Heading levels skipped or multiple `h1`s; `div`/`span` where semantic elements belong
- Inputs without associated labels; errors conveyed by color alone
- Dynamic content (toasts, async results, validation) that never reaches a screen reader

## Scoring anchors

- **Red (0–3):** Core flows unusable by keyboard or screen reader; systemic automated violations; forms unlabeled.
- **Yellow (4–7):** Broadly operable but real gaps — focus not managed on route/overlay changes, some contrast/label misses, dynamic updates silent to AT.
- **Green (8–10):** The team can honestly say: *"Every core flow is fully keyboard- and screen-reader-operable on the shipped product, focus is managed, forms and dynamic updates are announced, and automated checks are clean on real routes."*

## Turning off the light

- Wire an automated a11y check (axe/Lighthouse/pa11y) into CI against real rendered routes — the cheapest guardrail, and it stops regressions cold.
- Focus management and route-change focus are the highest-leverage manual fixes; they're small code changes with outsized impact.
- If issues trace to the components themselves (not composition), that's a **design-system finding** — file it upstream; it should show in the DS's accessibility station.
- Hand an agent the automated report to draft fixes, but keep the keyboard/SR walk human — the judgment calls (is focus order sensible? is this announcement useful?) don't automate.

## Station record

```markdown
### Station 3 — Accessibility: <RED|YELLOW|GREEN> (<n>/10)
- Automated: <tool> on <n> routes → <n> violations · Keyboard walk: <flows covered> · SR spot check: <flow>
- Evidence level: <live / recording / interview, per check>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
