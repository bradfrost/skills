---
check: 4
name: Color semantics
question: Do the color tokens cover the jobs a UI actually has, and does every filled surface have a content color that reads on it?
---

# Check 4 — Color semantics

Color is where the architecture is most specific and where systems most
often look tiered while behaving flat. Tier 2 color has three properties
(background, content, border), a fixed set of intentions, and a variant
vocabulary that includes the pairing rule: a filled surface needs a
"knockout" (or `on-`) content color, and the pair has to pass contrast
(2.10, 3.48, 6.20 through 6.26).

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Tier 2 color tokens, all three properties | Repo or pasted JSON | Figma `color/` variables |
| Resolved values per theme | Build output or resolve the references yourself | Figma resolved values by mode |
| Where components get their colors | Component source (a sample of 5 to 10) | Interview |
| Contrast of the pairs | Compute it: WCAG 2.x relative luminance | A contrast tool run by the human (tag `[reported]`) |

## Procedure

1. **Inventory by property.** Group tier 2 color into `background`,
   `content`, and `border` (or the system's words for them). A system with
   only `background` and `text` is missing borders and probably has them
   hardcoded in components. A system with `content` split into `text` and
   `icon` is fine if it needed the split (2.10).
2. **Inventory by intention.** For each property, which intentions exist:
   `default`, `brand`, `accent`, `disabled`, `utility` (error / warning /
   success / info), `dataviz`, `transparent`. Missing `default` means the
   page's own colors are hardcoded. Missing `utility` means every alert
   invents its own red. Missing `disabled` at the intention level means it's
   been re-minted per variant (check 3).
3. **Find every filled surface and its pair.** For each `background-*` that
   is not the page default, find the content token that is meant to sit on
   it. In the architecture's words that's `content-knockout` on
   `background-knockout` and `content-brand-knockout` on `background-brand`
   (6.25); other systems say `on-brand`, `on-accent-3`, `on-surface`. The
   word doesn't matter. The pair does. A filled surface with no pair means
   components are choosing white or black by hand, and one of them is
   wrong.
4. **Compute the contrast of every pair, per theme.** Text pairs need
   4.5:1 (3:1 for large text, only if the system's smallest use of that
   pair is actually large). Non-text pairs (a progress fill on its track, a
   border on its surface) need 3:1. Do the arithmetic on the resolved
   values; don't take the token's name as proof. A token named `on-brand`
   that fails on the brand fill is a stronger finding than one that was
   never named.
5. **Check the states.** `hover`, `active`, `focus` variants where the
   system has interactive surfaces. In a dark theme, note whether hover goes
   the right direction (lighter on dark, darker on light): a dark theme
   built by copying the light theme's values usually gets this backwards.
6. **Check the subtle/strong dial.** `subtle` should recede relative to
   `default`; `strong` should advance (6.26). Resolve the values and
   confirm. `content-subtle` resolving to the same value as `content-brand`
   is a real finding from a real system.
7. **Check what components actually reach for.** Sample components and note
   whether they use tier 2 (good), tier 3 (fine), tier 1 (a finding), or raw
   values (check 8's finding; record it there).

## Warning lights

- Only one or two of the three properties tokenized
- No `default` intention; page colors hardcoded
- Filled surfaces with no paired content token
- Pairs that fail contrast in any theme
- Dark theme hover states moving the wrong direction
- `subtle` louder than `default`, or `strong` indistinguishable from it
- Components reaching into tier 1 for color

## Lights

- **Red:** a property missing, or filled surfaces with no pairs, or pairs
  failing contrast in the default theme.
- **Yellow:** the structure holds but intentions are missing, a few pairs
  fail in a secondary theme, or the dial is inconsistent.
- **Green:** three properties, the core intentions, every filled surface
  paired, every pair passing in every theme, subtle/strong behaving.

## Fixing it

- Missing pairs → mint the content token for each filled surface, name it
  by the surface it sits on (`content-brand-knockout`, or `on-brand`), and
  choose its value by the surface's luminance.
- Failing pairs → move the *foreground* first (it's the one with room to
  move); only ease the background if no foreground lightness passes.
- Write the pairs down as a list and check them in CI. Contrast lives in
  the relationship between two tokens, not in either one, and the list is
  the only way to test the relationship.
- Dark theme direction → treat it as a rule ("hover increases separation
  from the page") rather than a value to copy (8.02).

## Record

```markdown
### Check 4 — Color semantics: <RED|YELLOW|GREEN> (or N/I)
- Properties: background <n> · content <n> · border <n>
- Intentions present: <list> · missing: <list>
- Filled surfaces: <n> · paired: <n> · unpaired: <list>
- Pairs computed: <n> · failing: <n> (<pair, ratio, theme>)
- Subtle/strong dial: <holds / inverted at …>
- Components sampled: <n> · reaching into tier 1: <n>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- First move: <…>
```
