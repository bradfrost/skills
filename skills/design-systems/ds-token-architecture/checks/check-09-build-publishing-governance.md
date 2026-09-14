---
check: 9
name: Build, publishing, and governance
question: Can the token set be built, shipped, versioned, and changed without breaking the people who depend on it?
---

# Check 9 — Build, publishing, and governance

The last check leaves the architecture and looks at the machinery around
it: the build (4.05 through 4.15), what gets published and what gets hidden
(5.06, 5.10, 4.26), versioning (7.15, 7.19), and the workflow for changing a
token once products depend on it (7.26). A perfect ladder nobody can ship or
safely change is a diagram.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Build config | Style Dictionary config, build scripts, package.json | Interview |
| Published artifact | npm package contents, or the `dist/` folder | Interview |
| Figma publishing | Which collections are published; scopes; hidden collections | Bridge · screenshot · interview |
| Version history | Tags, changelog, package versions | Interview |
| Change process | Contribution docs, issue templates, a governance page | Interview: "how does a token get added?" |
| Tests and gates | CI config, scripts named `check:*`, test files | Interview |

## Procedure

1. **Build.** Source is JSON (or DTCG JSON) built into per-platform outputs
   (4.05). Check: the global prefix is a config value, not typed into every
   name (4.14); the tier identifier is added by a transform keyed on the
   path (4.15); outputs exist for every platform that consumes them (CSS at
   minimum; JS, iOS, Android where relevant). Note whether the output
   preserves references or resolves them; both are defensible, but a system
   should know which it does.
2. **What's published.** Is tier 1 published to consumers? The course leans
   no (5.06): consumers with raw palette access build contrast failures and
   bypass the theme. If tier 1 is published, is there a reason, and is it
   documented? In Figma: is tier 1 hidden from publishing (5.10), and are
   variables scoped so a content color can't be applied as a frame fill
   (4.26)?
3. **Design/code alignment at publish time.** The pre-publishing checklist
   (5.07 through 5.13): mapping correct in both places, scopes set, hidden
   collections hidden, contrast checked, build tested, docs present. Ask
   which of these happen and whether any are automated.
4. **Versioning.** Semver with tokens' meaning: additive is minor, rename is
   major, `0.x` while emerging (7.15). Is there a changelog per release
   (7.19)? Are token and component library versions coordinated (7.22)?
5. **Deprecation.** The architecture stops at "rename is a major." Check
   whether the system has a deprecation path anyway: an old name kept as an
   alias with a migration note, a `deprecated` flag in metadata, a sunset
   window. Report what exists; the architecture has no rule here.
6. **Governance workflow.** Is there a named owner (a token czar, 4.84)?
   When a product team needs a token, what happens (7.26)? Is there a
   classification (education / bug / new token / visual discrepancy) or
   does every request become a debate? Are bugs (wrong mapping, drift,
   contrast, inconsistent names) treated as urgent?
7. **Gates.** Which of the earlier checks are automated? References
   resolve (check 2). Raw values in consumers (check 8). Contrast pairs
   (check 4). Theme key parity (check 7). Anything in CI is a green habit;
   anything only a human remembers to do is a yellow waiting to happen.
8. **Docs.** Is there a place a consumer can see every tier 2 token with its
   resolved value per theme, and its job (5.13)? A Storybook token page, a
   docs site, a generated table. Undocumented tokens get reinvented.

## Warning lights

- Prefix or tier identifier typed by hand into names
- Tier 1 published with no reason
- No scopes, tier 1 visible in every Figma fill picker
- No changelog, or versions that don't follow semver
- No owner, no request path
- Nothing automated: every check is a human ritual
- No token docs

## Lights

- **Red:** can't be built reliably, or published with no versioning, or
  changed with no process.
- **Yellow:** builds and ships, but tier 1 is published without a reason,
  versioning is loose, or nothing is automated.
- **Green:** structural build, tier 1 hidden (or published for a stated
  reason), semver and a changelog, an owner and a request path, at least
  two of the earlier checks gated in CI, docs generated from the source.

## Fixing it

- Hand-typed prefix → move it to config; hand-typed tier → a path-keyed
  transform.
- Tier 1 published by accident → add a filter to the build and hide the
  collection in Figma; publish tier 2/3 only.
- No gates → start with references (mechanical) and raw values (a grep),
  then contrast pairs once check 4's list exists.
- No process → name the owner and write the four-way classification down.
  One page is enough.

## Record

```markdown
### Check 9 — Build, publishing, and governance: <RED|YELLOW|GREEN> (or N/I)
- Build: <tool, outputs> · prefix by config: <yes/no> · tier by transform: <yes/no> · refs in output: <preserved / resolved>
- Tier 1 published: <yes (reason) / no> · Figma: hidden <yes/no> · scoped <yes/no>
- Versioning: <semver / loose / none> · changelog: <yes/no>
- Deprecation path: <what exists, or none; no architecture guidance>
- Owner: <name / none> · request path: <documented / ad hoc>
- Gates in CI: <list>
- Docs: <where / none>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <…>
- First move: <…>
```
