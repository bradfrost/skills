---
station: 4
name: Shared language
quality: Sound (quality 2 of 5)
question: Is language consistent and coherent within and across system assets — tokens, props, layers, code, component APIs, docs?
---

# Station 4 — Shared language

**Quality: Sound.** Naming inconsistency is the single most common issue in real-world design systems. Consistent language isn't a nice-to-have — it's the glue, the *contract* that ties design, code, and docs together, and it's what lets both humans and AI agents internalize the system and wield it correctly. This station checks consistency **within** each asset and — more importantly — **across** them.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Token names | Token files + design variables side by side | Pasted exports of both |
| Component APIs | Repo: props/values across all components (types/interfaces are gold) | Pasted API tables · docs |
| Design-side names | Live bridge: component/variant/property/layer names | Screenshots · pasted lists |
| Docs vocabulary | Docs: what things are *called* on the page | Pasted pages |
| Naming standards | Documented conventions, API guidelines, token naming algorithm | Interview: "is the scheme written down?" |

## Inspection procedure

1. **Cross-component API sweep (the classic):** collect prop names and values across components and hunt for the same concept under different names — `size="large"` here, `size="lg"` there; `variant` vs `appearance` vs `kind`; `onClose` vs `onDismiss`. This tedious pattern-matching is exactly what AI is great at — sweep everything, not a sample.
2. **Token naming algorithm:** is there one coherent scheme, or competing patterns (`typography-body-large` vs `large-body-text`)? Are tokens named by **role** (`color.action.primary`) or raw value (`blue-500`) at the semantic tier? Old and new schemes coexisting with no migration?
3. **Cross-asset agreement (the money check):** pick 5 components and trace each across design ↔ code ↔ docs. Does `Button/Primary` in design match `<Button variant="primary">` in code and "Primary button" in docs? Do design variant properties match code props? Do design token/variable names match code token names?
4. **Within-asset hygiene:** layer and property naming patterns in design; function/variable/file naming in code; docs calling the same thing the same name on every page.
5. **Check for guardrails:** documented naming conventions? A naming validator or lint rule? Anything catching drift at PR time, or is consistency running on vibes?

## Warning lights

- Different prop names for the same concept across components
- Token names with no coherent scheme
- `size` vs `scale` vs `sz` for the same idea
- Naming drift — old and new schemes coexisting with no migration
- No naming validator or drift detection
- Tokens named by raw value (`blue-500`) instead of role (`color.action.primary`)

## Scoring anchors

- **Red (0–3):** No discernible scheme; the same concept goes by different names asset to asset; docs disagree with both design and code.
- **Yellow (4–7):** A scheme exists and is mostly followed, but drift is accumulating and nothing enforces it; design and code agree *usually*.
- **Green (8–10):** One documented naming algorithm; APIs consistent across components; the same name traces cleanly through design, code, and docs; a validator catches drift before merge.

## Turning off the light

- Have AI produce a **consistency report** across every category where naming matters — component APIs, tokens, layers, docs — in one sweep.
- This is the one station where fixing **across all assets in one go** is possible (and often preferable) — align design, code, and docs to the same target vocabulary in a single coordinated pass, with per-asset QA after. This genuinely wasn't practical before LLMs.
- **Careful — bull in a china shop:** renaming props, values, and tokens breaks production consumers. Version it, generate codemods, communicate the migration. Hard-earned naming conventions shouldn't be upended casually.
- Write the naming algorithm down and add a validator so the language stays aligned after the cleanup.
- Related deep tools: Design System Ops `naming-audit`, `codemod-generator`.

## Station record

```markdown
### Station 4 — Shared language: <RED|YELLOW|GREEN> (<n>/10)
- Swept: <APIs, tokens, assets traced>
- Evidence level: <live / export / screenshot / interview, per asset>
- Findings:
  - [verified|reported] <inconsistency + examples, within-asset or cross-asset>
- Not inspected: <…>
- Deviations noted: <…>
- First move: <…>
```
