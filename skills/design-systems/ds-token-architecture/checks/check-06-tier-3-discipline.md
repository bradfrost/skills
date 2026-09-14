---
check: 6
name: Tier 3 discipline
question: Are component tokens used sparingly and for the sanctioned reasons, or is tier 3 where the system went to sprawl?
---

# Check 6 — Tier 3 discipline

The course's rule: use tier 3 "really sparingly," and "when you find yourself
adding tier three tokens, you should feel bad" (2.3). The cautionary tale is
4,000 tokens minted one per property per variant per component. This check
counts tier 3, checks each token against the sanctioned reasons, and looks
for the tier 3 tokens that are really tier 2 tokens in disguise.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Every tier 3 token, with what it references | Repo or pasted JSON | Figma tier 3 collection |
| Which components consume them | Component source | Interview |
| Tier 2 tokens that could have served | Check 4 and 5's inventories | |

## Procedure

1. **Count.** Tier 3 total, tokens per component, and the ratio of tier 3
   to tier 2. A tier 3 larger than tier 2 is the first finding.
2. **Sort each token into a reason.** The sanctioned ones (2.3, 6.27):
   - Heavily variable component (buttons, with real variants and states)
   - Component category sharing a decision (input border across text
     input, textarea, select)
   - Special case (focus ring, highlighted table row, chart)
   - Mapping that legitimately differs per theme (link color: brand in one
     theme, interactive blue in another)
   Anything that doesn't fit is a candidate for deletion or demotion.
3. **Find the disguised tier 2 tokens.** A `card-color-background` that
   resolves to `color-background-default` in every theme is a tier 2
   reference with an extra name. A `button-padding-x` that equals
   `spacing-16` everywhere is the same. These cost a name and buy nothing.
4. **Find the duplicated disabled.** Disabled states at tier 3 can fall back
   to tier 2 `content-disabled` / `background-disabled` (6.27). Count the
   components that minted their own.
5. **Check what tier 3 references.** Tier 2 by preference; tier 1 is
   allowed (2.3). A tier 3 token pointing at tier 1 *past* an existing tier
   2 token won't follow a remap (check 2 records this too).
6. **Check the sprawl vector.** Is there a per-property-per-variant pattern
   (`button-primary-background-hover`, `button-primary-background-active`,
   `button-secondary-background-hover`, …)? Count the tokens it generates
   and ask which of them differ from what tier 2 would have given.
7. **Check what tier 3 doesn't cover.** Focus ring with colors but no
   offset, a button with colors but a hardcoded padding: a component
   half-tokenized at tier 3 is often worse than one wired straight to tier
   2, because the half that's tokenized creates the impression the whole
   thing is.

## Warning lights

- Tier 3 larger than tier 2
- Tokens with no sanctioned reason
- Tier 3 tokens that resolve to the same tier 2 token in every theme
- Disabled states re-minted per component
- Per-property-per-variant sprawl
- Components half-covered by tier 3 with the rest hardcoded

## Lights

- **Red:** sprawl. Tier 3 dominates, most tokens have no reason, or the
  per-property-per-variant pattern is the norm.
- **Yellow:** tier 3 is bounded but carries disguised tier 2 tokens,
  duplicated disabled states, or a few components half-covered.
- **Green:** a short tier 3, every token with a reason you can name, wired
  to tier 2, with disabled falling back.

## Fixing it

- Demote disguised tier 2 tokens: replace the reference in the component,
  delete the token, note it in the changelog.
- Collapse disabled to tier 2.
- For a sprawling button, keep the variants that differ from the semantic
  defaults and delete the rest; the component can read tier 2 directly for
  the rest.
- An empty tier 3 is a legitimate result. Say so if it's the right answer.

## Record

```markdown
### Check 6 — Tier 3 discipline: <RED|YELLOW|GREEN> (or N/I)
- Tier 3 total: <n> across <n> components · tier 3 : tier 2 ratio <x>
- By reason: variable component <n> · category <n> · special case <n> · per-theme mapping <n> · no reason <n>
- Disguised tier 2: <n> (<examples>) · re-minted disabled: <n>
- References: tier 2 <n> · tier 1 <n> (past existing tier 2: <n>)
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- First move: <…>
```
