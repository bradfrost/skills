# Token intake: what are we looking at?

Before any check runs, build `ds-token-architecture/PROFILE.md`: what the
token set is, where it lives, what consumes it, and what evidence you can
actually reach. Every check reads this file first. A good intake is what
makes findings specific ("`--ds-theme-color-content-subtle` resolves to the
same hex as `content-brand`") instead of generic ("naming could be clearer").

**Agent:** work through this conversationally, a few questions at a time.
Wherever you have live access (repo, pasted JSON, a design-tool bridge),
*discover* the answer and confirm it instead of asking. Aim for ten minutes.
Then write `PROFILE.md` from the template at the bottom and read it back.

## 0. Which mode?

Ask first, because the two modes read different evidence:

- **Assess.** A token set exists (in code, in Figma, or both) and the
  question is how well it holds up against the architecture. This is the
  common case, and it's the one a course learner is in when they paste their
  JSON and ask "is this right?"
- **Establish.** No token set exists yet, or what exists is a pile of
  hardcoded values in a production codebase, and the question is how to get
  from there to a tier ladder. Run `establish/ESTABLISH.md` instead of the
  checks. The checks come back at the end, to grade what you built.

If the answer is "we have some tokens but they're a mess," that's assess.
Assess finds out how much of a mess, and its work order may well say "start
over with establish for these categories."

## 1. The system

- Design system or product name, and who consumes the tokens (how many
  components, how many products, how many teams)
- How old is the token set? Was it built deliberately, or did it accrete?
- Who owns it? Is there a token czar, a team, or nobody?
- Why now? (A second theme is coming. Dark mode is coming. A rebrand. An
  audit. "Someone said we have 4,000 tokens.")

## 2. The token sources

Capture *what exists* and *where it lives*, for both sides:

- **Code:** repo path or pasted files. Format: Style Dictionary JSON, DTCG
  JSON, Tokens Studio export, raw CSS custom properties, SCSS variables, a
  Tailwind config, a JS theme object. Build pipeline, if any, and what it
  outputs (CSS, SCSS, JS, iOS, Android).
- **Design:** Figma variables (how many collections, how many modes), Figma
  styles, or nothing. Which is the source of truth when they disagree?
- **Consumers:** the component library and at least one product, so
  check 8 can look for hardcoded values where tokens should be.
- **Docs:** a token page, a Storybook, a README, or nothing.

A course learner in plain chat will often have exactly one thing: a pasted
`tokens.json`. That's enough to run checks 1 through 7. Say plainly that
checks 8 and 9 will be `[reported]` or not inspected until you can see
consumers and a build.

## 3. Evidence access map

Test, don't assume. Read one real file. Make one real bridge call. Record
what worked.

| Source | Access level to record |
|---|---|
| Token source (code) | `live` (repo readable) / `export` (pasted files) / `interview` |
| Token source (design) | `live` (a bridge is connected and returned this file's variables; name the bridge) / `export` (a variables export or a plugin JSON) / `screenshot` / `interview` |
| Consumers | `live` / `export` / `interview` |
| Build & docs | `live` / `export` / `interview` |

**Probe the design side every run.** Ask: *"Do you have Figma variables for
these tokens, and is a Figma MCP or bridge connected so I can read them?"*
Then look at your own tools for anything Figma-shaped and make one call that
returns real variables from their actual file. `reference/FIGMA-ACCESS.md`
says what each bridge can and can't see. The native bridge needs a layer
selected to read variable definitions; the Console bridge reads whole
collections. Record which one you used.

If everything lands on `interview`, say so: the assessment will run, every
finding will be `[reported]`, and the first item on the work order will be
getting the agent real evidence.

## 4. The vocabulary translation

The architecture has its own words (`definitions` / `usage` / `components`,
`theme`, `knockout`). The system under review will have its own. Before the
checks run, write down the mapping so findings speak the team's language:

| Architecture says | This system says | Evidence |
|---|---|---|
| Tier 1 / definitions | e.g. `primitives`, `core`, `base` | |
| Tier 2 / usage | e.g. `semantic`, `alias`, `sys` | |
| Tier 3 / components | e.g. `comp`, per-component files | |
| Knockout | e.g. `on-*`, `inverse`, `contrast` | |
| Content | e.g. `text`, `fg`, `foreground` | |

A system that has these concepts under other names passes the structural
checks. A system where a row is empty because the concept doesn't exist is
where the findings will be.

## 5. Known symptoms

Ask like a mechanic: what's it doing, and when did it start?

- Where does the team already suspect the ladder is broken?
- What do consumers complain about? ("I never know which token to use."
  "Dark mode broke three components." "We have eleven grays.")
- Anything the team is proud of? (Probable greens, worth verifying.)
- Intentional deviations from the architecture the checks should respect
  (a two-tier system by design, tier 1 published on purpose for a reason)

## 6. Scope & frame

- All nine checks, or a subset?
- Frame for the findings: solo maintainer / small team / platform org. A
  yellow for a two-person system is not a yellow for a platform team.
- Out of scope this pass?

---

## PROFILE.md template

```markdown
# PROFILE.md — <System Name>
_Checked in: <date> · Mode: assess | establish · Re-confirm at next run_

## The system
- Serves: <components, products, teams>
- Age & origin: <deliberate build / accreted / migrated from X>
- Owner: <person, team, or nobody>
- Why now: <the prompt for this run>

## Token sources
- Code: <format, path or "pasted", build tool, outputs>
- Design: <Figma variables: n collections, n modes / styles only / none>
- Source of truth when they disagree: <code / design / undecided>
- Consumers reachable: <component library path, product path, or none>
- Docs: <where, or none>

## Evidence access map
| Source | Access | Verified how |
|---|---|---|
| Token source (code) | live / export / interview | <e.g. "read tokens/tier-2-usage/color.json"> |
| Token source (design) | live / export / screenshot / interview | <bridge name and what it returned, or why not> |
| Consumers | live / export / interview | <…> |
| Build & docs | live / export / interview | <…> |

## Vocabulary translation
| Architecture says | This system says | Evidence |
|---|---|---|
| Tier 1 / definitions | <…> | <…> |
| Tier 2 / usage | <…> | <…> |
| Tier 3 / components | <…> | <…> |
| Knockout | <…> | <…> |
| Content | <…> | <…> |

## Known symptoms
- <…>

## Probable greens
- <…>

## Intentional deviations
- <…>

## Scope & frame
- Checks this pass: <all / subset> · Frame: <solo / small team / platform org>
- Out of scope: <…>
```
