---
station: 3
name: Accessibility
quality: Sound (quality 2 of 5)
question: Do design system assets embody accessibility best practices and deliver inclusive experiences?
---

# Station 3 — Accessibility

**Quality: Sound.** Technically this belongs under best practices — it gets its own station because it's that important. An accessible design system foundation gives every downstream team accessible smart defaults, and it's one of the strongest ways to position the system in an age of AI-generated UI: *our components are tested, verified, and put through the wringer.* Baked-in accessibility doesn't automatically make accessible products (composition and page-level work still matter, and that's the product teams' job too) — but it's the leg up everything else stands on.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Component markup & behavior | Repo: read interactive components (focus, ARIA, keyboard handlers) | Pasted source · rendered HTML |
| Contrast | Token/variable values across themes — compute ratios | Pasted palette · screenshots |
| Automated checks | CI config: axe-core/Lighthouse/pa11y steps; test files | Interview: "what runs on every PR?" |
| A11y documentation | Docs: per-component a11y notes + org-level guidance | Interview |
| Real-world signal | Support tickets, user feedback, audit/legal history | Interview |

## Inspection procedure

1. **Read 3–5 interactive components for the fundamentals:** semantic elements (`<button>` for buttons); keyboard operability (focus visible, tab order, Escape/arrow patterns where expected); ARIA only where semantics don't cover it — and *correct* (wrong ARIA is worse than none); focus management for overlays/state changes; touch-target sizes.
2. **Compute contrast from the tokens.** Body text 4.5:1, large text and non-text 3:1 — across *every theme/mode*, not just the default. Dark mode is where contrast quietly dies.
3. **Check the testing wiring:** automated a11y checks (axe-core or similar) in CI on every change? Keyboard-navigation assertions in component tests? A screen-reader test plan anywhere?
4. **Check the docs:** per-component a11y notes (keyboard interactions, screen-reader behavior, dos/don'ts)? Org-level accessibility guidance? Is "accessible" part of the definition of done?
5. **Read the culture** (interview): is a11y in the workflow, or "we'll get to it"? Any legal exposure or user complaints? Does the team communicate to product teams that the system is a leg up, not a hall pass?

## Warning lights

- No automated a11y checks (e.g. axe-core) in CI
- No keyboard navigation tests
- Theme colors never validated for contrast
- Few or no per-component a11y notes
- No screen reader test plan

## Scoring anchors

- **Red (0–3):** Fundamental violations in shipped components (unreachable by keyboard, failing contrast, wrong semantics) and no testing safety net.
- **Yellow (4–7):** Components mostly sound, but verification is thin — no CI checks, contrast unvalidated across themes, a11y docs sparse. Sound today, no guarantee tomorrow.
- **Green (8–10):** Sampled components pass fundamentals; contrast validated across all themes; automated checks run on every change; keyboard/screen-reader coverage exists; a11y is documented per-component and in the definition of done.

## Turning off the light

- **Wire automated a11y scanning into CI first** — it's the highest-leverage single move; every future component gets checked forever.
- Feed contrast failures to AI to **retune the token system** so themes pass WCAG at the token level — fixing it in the tokens fixes it everywhere.
- Use AI to **draft per-component a11y guidance** (keyboard maps, ARIA rationale, screen-reader behavior) — then verify by hand.
- Automated checks are only part of the game: tab through it, run VoiceOver, put a human on it. AI can draft the manual test plan too.
- Related deep tools: Design System Ops `accessibility-per-component`; axe-core, Lighthouse, Playwright a11y assertions (see Station 5 for the self-healing-loop pattern).

## Station record

```markdown
### Station 3 — Accessibility: <RED|YELLOW|GREEN> (<n>/10)
- Sampled: <components, themes checked>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <finding + evidence, WCAG criterion where applicable>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
