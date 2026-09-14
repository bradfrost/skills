# Token intake: what are we looking at?

Before any check runs, build `ds-token-architecture/PROFILE.md`: what the
token set is, where it lives, what consumes it, and what evidence you can
actually reach. Every check reads this file first. A good intake is what
makes findings specific ("`--ds-theme-color-content-subtle` resolves to the
same hex as `content-brand`") instead of generic ("naming could be clearer").

**Agent:** work through this conversationally, a few questions at a time.
Wherever you have live access (repo, pasted JSON, a design-tool bridge),
*discover* the answer and confirm it instead of asking. The opener in
SKILL.md promised five minutes; keep that promise. Then write `PROFILE.md`
from the template at the bottom and read it back.

## 0. Which mode?

Ask first, because the two modes read different evidence. Put it to the
user in these words:

> What design token work would you like to do? Select a mode:
>
> - **Assess an existing token system** - Analyze your design token system
>   (in code and/or Figma) against the three-tier architecture
> - **Establish a design token system** - Create a structured design token
>   architecture from nonexistent or incomplete token values in a codebase
>   and/or Figma file

**Assess** is the common case, and it's the one a course learner is in when
they paste their JSON and ask "is this right?" **Establish** runs
`establish/ESTABLISH.md` instead of the checks; the checks come back at the
end, to grade what you built.

If the answer is "we have some tokens but they're a mess," that's assess.
Assess finds out how much of a mess, and its work order may well say "start
over with establish for these categories."

## 1. The system

One question, in these words:

> What context is important to know about your design token system?
> Describe the products the system needs to serve, a brief history, who
> owns it, and what are your goals for the system?

What you're listening for in the answer, and why each one matters
downstream:

- **Products served** (how many components, products, teams): sets the
  scoring frame and scopes check 8
- **History**: "built deliberately" and "accreted" predict very different
  check 1 results
- **Owner**: fills the work order's owner line; "nobody" is a check 9
  finding on its own
- **Goals**: a second theme, dark mode, a rebrand, or "someone said we have
  4,000 tokens" each move a different check to the top of the work order

Don't follow up for anything they skipped unless a check needs it; the
checks will surface it.

## 2. The token sources

One question, in these words:

> Where does your design token system live? Provide links to code repos,
> Figma files, docs, consuming products, and other relevant sources if they
> exist.

Then go read what they gave you. For each source, record *what exists* and
*where it lives*:

- **Code:** repo path or pasted files. Format: Style Dictionary JSON, DTCG
  JSON, Tokens Studio export, raw CSS custom properties, SCSS variables, a
  Tailwind config, a JS theme object. Build pipeline, if any, and what it
  outputs (CSS, SCSS, JS, iOS, Android).
- **Design:** Figma variables (how many collections, how many modes), Figma
  styles, or nothing. If both sides exist, ask one follow-up: which is the
  source of truth when they disagree?
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

**Probe the design side every run.** If they named a Figma file in section
2 (or you found Figma-shaped tools), ask, in these words:

> If Figma is to be inspected, please make sure Figma Console MCP
> (recommended, since it reads whole variable collections) or the native
> Figma MCP (reads one selected layer at a time) is connected.
>
> - I have a Figma bridge connected
> - I don't have one / skip this (the Figma side will be assessed from what
>   you tell me)

"Connected" is a claim until you test it. Look at your own tools for
anything Figma-shaped and make one call that returns real variables from
their actual file. `reference/FIGMA-ACCESS.md` says what each bridge can
and can't see and how each one quietly fails. Record which bridge you used.

If everything lands on `interview`, say so: the assessment will run, every
finding will be `[reported]`, and the first item on the work order will be
getting the agent real evidence.

## 4. The vocabulary translation

The architecture has its own words (`definitions` / `usage` / `components`,
`theme`, `knockout`). The system under review will have its own. This is
not a question for the user: fill the table yourself from the files you
just read, then read it back in one line ("I'm reading `primitives/` as
tier 1, `semantic/` as tier 2, and `on-*` as your knockout pairs; shout if
that's wrong"). Only ask about a row you genuinely can't fill.

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

## 5. Anything else

One question, in these words:

> Anything else worth sharing (additional considerations, known pain
> points, etc) before the inspection begins?

Sort whatever comes back into the profile's buckets:

- **Known symptoms**: "I never know which token to use," "dark mode broke
  three components," "we have eleven grays." Each one points a check at
  something.
- **Probable greens**: anything they're proud of. Worth verifying and
  celebrating.
- **Intentional deviations**: a two-tier system by design, tier 1 published
  on purpose for a stated reason. Record these so the checks note them
  instead of flagging them.

"Nothing" is a fine answer. Move on.

## 6. Scope & frame

No question. Nobody should have to memorize nine checks to answer one, so:

- **Run all nine by default.** Narrow only if the user asked for a specific
  check by name, or a re-run is scoped to the checks that changed.
- **Infer the frame** from section 1's answer (solo maintainer / small team
  / platform org) and state it in one line before the checks start, so
  they can correct it. A yellow for a two-person system is not a yellow for
  a platform team.
- **Out of scope** is whatever they said in section 5, or nothing.

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
