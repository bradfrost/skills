---
check: 3
name: Naming
question: Does the naming survive contact with a second theme, a second brand, and a designer who has never seen the code?
---

# Check 3 — Naming

Names are the API. Tier 1 names "can be loose"; tier 2 and 3 "need to be
strictly defined" (3.45). This check tests whether the names follow *an*
algorithm consistently, whether that algorithm matches the architecture's
order (prefix → tier → category → the category's own segments, 3.43 through
3.49), and whether the names would still make sense if the values changed
underneath them.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| The full list of tier 2 and tier 3 names | Repo or pasted JSON | Figma variable names (bridge or screenshot) |
| Tier 1 names | Same | Same |
| Any written naming guide | Docs, README, a FigJam | Interview: "what's the rule?" |
| Figma vs code names for the same token | Both sides | Interview |

## Procedure

1. **Reverse-engineer the algorithm.** Take twenty tier 2 names and write
   down the segment order each one follows. If you get one pattern, the
   system has a convention. If you get three, that's the finding.
2. **Compare to the architecture's order.** Global prefix, then tier
   identifier (tier 2/3 only), then category, then category-specific
   segments. For color: property → intention → variant → state (3.48). For
   typography: intention → size → screen → property (3.51). Deviations are
   fine if consistent; record them in the vocabulary translation.
3. **Test the names against change.** For each of these, pick a token and
   ask whether its name still makes sense:
   - The brand color changes from blue to green. (`color-blue-primary`
     fails; `color-content-brand` survives.)
   - Dark mode arrives. (`color-background-white` fails; `background-default`
     survives.)
   - A second brand arrives. (`acme-red` in tier 2 fails; it belongs in tier
     1.)
   A tier 2 or 3 name that describes a *value* instead of a *job* is the
   red flag here (3.21, 3.27).
4. **Check consistency of the vocabulary.** One word per concept: not
   `text` in one place and `content` in another, not `hover` here and
   `over` there, not `lg` here and `large` there (3.23). Synonym pairs are
   findings (3.38).
5. **Check the tier identifier.** Tier 2 and 3 should carry it in code
   (`theme`, `semantic`, `sys`); tier 1 should not. It's the signal that
   tells a consumer "this is API" versus "this is raw material" (3.45).
6. **Check Figma parity.** Same names, minus the global prefix and tier
   identifier, with slashes for dashes (3.32, 3.45). `default` spelled out on
   both sides, since Figma can't express an unnamed default (3.36). List the
   tokens whose names differ between the two sides beyond those rules.
7. **Check the disabled decision.** The architecture hoists `disabled` to
   the intention level so it isn't re-minted per variant (3.48, 6.23). A
   system with `brand-disabled`, `utility-error-disabled`, and
   `accent-1-disabled` is paying for the same gray many times.

## Warning lights

- No discernible algorithm, or several
- Tier 2 or 3 names that describe values (`blue-500-text`, `white-bg`)
- Synonyms for one concept
- No tier identifier, so consumers can't tell API from raw material
- Figma and code names diverge beyond the documented parity rules
- Abbreviations nobody can expand (`clr-bg-pri-hv`)

## Lights

- **Red:** no consistent algorithm, or tier 2 names that will break on the
  first theme change.
- **Yellow:** an algorithm that mostly holds, with synonyms, a few
  value-named tokens, or a parity gap with Figma.
- **Green:** one algorithm, consistently applied, job-named at tier 2 and 3,
  documented, matched in Figma.

## Fixing it

- Write the algorithm down in one paragraph and a table of allowed words
  per segment. The FigJam exercise in the course (3.40 through 3.42) is
  built for this.
- Rename while there's one consumer (7.19). Every rename after that is a
  major version.
- Value-named tier 2 tokens: rename by job, keep the old name as a
  deprecated alias for one release.
- Wire a lint rule for the segment order and the allowed vocabulary once the
  algorithm is settled.

## Record

```markdown
### Check 3 — Naming: <RED|YELLOW|GREEN> (or N/I)
- Algorithm found: <segment order, or "none" / "three competing">
- Matches architecture order: <yes / with these deviations>
- Value-named tokens at tier 2/3: <n> (<examples>)
- Synonym pairs: <list>
- Tier identifier present: <yes / no>
- Figma parity: <n tokens diverge beyond the parity rules / not reachable>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- First move: <…>
```
