---
check: 2
name: References
question: Do semantic tokens reference primitives, or do they hardcode values?
---

# Check 2 — References

The whole point of the ladder is that a value is defined once and referenced
everywhere else. Tier 1 holds raw values. Tier 2 aliases tier 1. Tier 3
aliases tier 2 (or tier 1; both are allowed, 2.3). A raw value above tier 1
is a decision that will not follow the theme when the theme changes, and it
is the single most common way a tiered system quietly stops being one.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Every tier 2 and tier 3 value | Repo: the source JSON, not the build output (built CSS may be resolved to literals, which hides the references) | Pasted JSON · a Figma variables read with alias structure (`VARIABLE_ALIAS` entries) |
| Reference syntax | Style Dictionary `{color.brand.500}` dot paths, DTCG `{color.brand.500}`, CSS `var(--…)` in source | Interview |
| Broken references | Build log, or resolve them yourself | Interview: "does the build warn?" |

## Procedure

1. **Read the source, not the build.** The course's own build resolves
   references to literals in the shipped CSS (the mapping is invisible in
   `tokens.css`). Judge references from the JSON or from Figma's alias
   structure.
2. **Walk tier 2.** Every value should be a reference. List the exceptions
   with file and token name. Some are legitimate and should be recorded as
   such: a unitless line-height ratio, a `transparent`, a composed shadow
   string. A hex color in tier 2 is never legitimate.
3. **Walk tier 3.** Same rule. Note which tier each reference points at.
   Tier 3 pointing at tier 1 is allowed; tier 3 pointing at tier 1 *when an
   equivalent tier 2 token exists* is a smell, because that component won't
   follow a tier 2 remap.
4. **Walk tier 1.** It should contain no references at all. A tier 1 token
   referencing another tier 1 token is a tier 2 token hiding in the wrong
   folder.
5. **Resolve everything.** Follow each reference to its end. Broken
   references (pointing at a name that doesn't exist) are reds. Chains
   longer than tier 3 → tier 2 → tier 1 are worth listing; they're not
   wrong, but each hop is a place to lose track.
6. **On the design side,** read the alias structure if you can (Console
   bridge: `figma_execute` walking `valuesByMode`; native: `get_variable_defs`
   with a layer selected). Tier 2 variables holding literal colors in Figma
   are the same finding as hex in tier 2 JSON.

## Warning lights

- Raw colors, sizes, or font values in tier 2 or tier 3
- Tier 1 tokens that reference other tokens
- Broken references, or a build that doesn't fail on them
- Tier 3 reaching past an existing tier 2 token into tier 1
- Code and Figma disagree about what a tier 2 token points at

## Lights

- **Red:** more than a handful of raw values above tier 1, or any broken
  reference in a published set.
- **Yellow:** a few raw values with a reason (or without one, but few), some
  tier 3 → tier 1 shortcuts past existing tier 2 tokens.
- **Green:** every tier 2 and 3 value resolves through a reference, tier 1
  holds only raw values, the build fails on a broken reference.

## Fixing it

- Raw value in tier 2 → find or mint the tier 1 token it should reference,
  point at it, and check the design side made the same move.
- Broken references → make the build fail on them. Style Dictionary does
  this out of the box; a custom pipeline needs a resolve step.
- Shortcuts → re-point tier 3 at the tier 2 token; if no tier 2 token fits,
  that's a tier 2 gap, not a reason to keep the shortcut.
- Wire this check into CI. It's mechanical and it's the one that drifts
  silently.

## Record

```markdown
### Check 2 — References: <RED|YELLOW|GREEN> (or N/I)
- Tier 2 tokens read: <n> · raw values found: <n> (<list or "none">)
- Tier 3 tokens read: <n> · raw values: <n> · shortcuts past tier 2: <n>
- Tier 1 tokens referencing others: <n>
- Broken references: <n> · Build fails on broken refs: <yes / no / unknown>
- Design side: <alias structure read / not reachable>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- First move: <…>
```
