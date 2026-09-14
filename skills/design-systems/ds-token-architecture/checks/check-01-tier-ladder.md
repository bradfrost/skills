---
check: 1
name: The tier ladder
question: Is there an actual tier ladder, or is everything one flat pile?
---

# Check 1 — The tier ladder

The architecture is three tiers: definitions, usage, components (2.3). This
check asks whether those tiers exist as *distinct things* in the system,
whatever they're called. Everything downstream (references, naming, theming)
assumes the answer is yes, so this check runs first and the others read its
record.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Folder or file structure of the token source | Repo: `tokens/` tree, one directory per tier or per theme | Pasted file list · pasted JSON with a top-level key per tier |
| Figma collections | Bridge: list collections and their modes | Screenshot of the variables panel · interview |
| Build config | Style Dictionary config or equivalent: how it tells tiers apart | Interview: "how does the build know tier 2 from tier 1?" |
| Token counts per tier | Count them from the source | Interview (tag `[reported]`) |

## Procedure

1. **Find the tiers.** Look for the three buckets by any name (see the
   vocabulary translation in `PROFILE.md`). In code they're usually
   directories (`tier-1-definitions/`, `primitives/`, `core/`) or top-level
   JSON keys. In Figma they're usually collections, one per tier (4.08,
   4.10, 4.12). Record where each tier lives and how many tokens it holds.
2. **Check that the buckets are real, not decorative.** A `semantic/` folder
   that contains raw hex values is a tier 1 folder with a nicer name. A
   quick tell: sample ten tokens per bucket and note whether each holds a
   raw value or a reference. Check 2 goes deep on this; here you're
   confirming the tiers mean what their names say.
3. **Check how the build tells them apart.** The course keys the tier
   identifier off the directory path (4.15). Whatever the mechanism, there
   should be one, and it should be structural (path, collection, file), not a
   naming convention someone has to remember.
4. **Check for a core bucket.** With more than one theme, the universal
   decisions (neutrals, utility colors, the type scale, the grid) should live
   once, in core, not in every theme (4.76). With one theme, note whether the
   split exists yet; it's not a finding until theme two.
5. **Count the pile.** Total tokens, per tier. Ratios are informative: a
   system with 40 tier 1, 300 tier 2, and 900 tier 3 tokens has its weight in
   the wrong place (check 6 takes that up).

## Warning lights

- No tiers: one flat list of names mapped to values
- Two tiers where the "semantic" tier holds raw values (a renamed tier 1)
- Tiers exist in code but not in Figma, or the reverse, or the two sides
  slice the tiers differently
- The build has no structural way to tell tiers apart
- Multiple themes and no core, so neutrals and utility colors are duplicated
  per theme

## Lights

- **Red:** no ladder. Flat pile, or tiers that are names only.
- **Yellow:** a ladder exists but one rung is soft: a tier is missing on one
  side, core is missing with several themes, or the build relies on a
  convention instead of structure.
- **Green:** three distinct tiers on both sides, keyed structurally, with
  core split out where there's more than one theme.

## Fixing it

- Flat pile → start with the MVP move (2.2): pull raw values into tier 1,
  give the ones in use jobs in tier 2, wire one component. Establish mode
  (`establish/ESTABLISH.md`) is this at full scale.
- Soft rung → put the missing tier where the other side already has it, and
  key the build off the path (4.15) so the identifier can't drift.
- Duplicated universals → create `core/` and move neutrals, utility colors,
  the type scale, spacing, animation, and z-index into it (4.76 through
  4.79).

## Record

```markdown
### Check 1 — The tier ladder: <RED|YELLOW|GREEN> (or N/I)
- Tiers found: tier 1 <where, n tokens> · tier 2 <where, n> · tier 3 <where, n> · core <where, n or "none">
- Design side: <collections found, or not reachable>
- Build keys tiers by: <path / collection / convention / nothing>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- First move: <the one fix that unblocks the most>
```
