# Discover the actual environment

Inspect before interviewing. Reuse existing project and system profiles,
but refresh the facts needed for this run. Record one source map rather
than copying catalogs into instructions.

## Evidence to collect

| Area | Establish | Useful proof |
|---|---|---|
| Scope and purpose | System, product, target user task, exploration/prototype/production, changed areas, and intentional exclusions. | Brief, project rules, and the user's decisions. |
| AI surfaces | Editors, CLI/chat/cloud agents, models, skills, plugins, hooks, delegated agents, and settings that participate. | Accessible configuration plus observed tools and behavior. Mark inaccessible surfaces as reported or not inspected. |
| Applicable instructions | Global, organization, project, and directory guidance; conflicting generic UI instructions; who receives which rules. | Actual instruction files and their documented scope. Do not assume all agents share precedence or discover package instructions automatically. |
| Access | Sanctioned providers, data access, read/write boundaries, required roles, and missing capabilities. | Current permissions and tool responses; redact secrets. Use approved environments, not personal-account workarounds. |
| Runtime | Actual component/token dependencies, resolved versions, imports, styles, assets, registration, adapters, and build/runtime integration. | Source and lockfiles, package exports, and a rendered example when accessible. |
| Foundation health | Whether the pilot's chosen ingredients work in their required states. | Existing inspection evidence plus relevant behavior, accessibility, and token checks. Do not demand a perfect system first. |
| Knowledge | APIs, tokens, intents, do/don't guidance, states, accessibility, deprecated paths, and representative examples. | Maintained sources matching the runtime version. |
| Composition | Patterns/pages discoverable from intent, permitted assembly, content and layout guidance, and ownership. | A mapping of requested regions and behavior to real ingredients and patterns. |
| Checks and release | Structural, behavioral, accessibility, visual, performance, and human-review requirements applicable to this task. | Executable checks, their coverage, actual merge/release controls, and known bypasses. |
| Feedback | Where defects, discrepancies, proposed additions, and exceptions go. | Maintained contribution process, owners, tracker, and resolution/adoption evidence where available. |

Tag each finding with evidence location, date, version or revision, scope,
and verified/reported/unknown status. Keep “missing” separate from “not
inspected.” Prioritize consequential gaps and achievable improvements;
do not average them into a reassuring readiness percentage.

## Map authority per concern

Code establishes implemented APIs; design references and narrative guidance
can explain intent that code alone does not. Determine the authoritative
source and owner for tokens, implementation, behavior, composition, content,
and governance. Record where other representations derive from or link to
those sources. A consolidated reference website need not own every source.

Where maintained design and code representations exist, inspect identifiers
and relevant state, layout, token, and interaction mappings. Source conflicts
need an owner and a decision. Do not silently declare that one tool always
wins. An intentionally absent design library is not a defect; a design-only
library is not proof of a working component implementation.

## Probe access, including absence

Use the system's available MCP, CLI, API, repository, versioned exports, or
documentation. A general design-system knowledge service cannot establish
this organization's real API. A configured endpoint or reachable URL proves
less than a successful, relevant catalog lookup.

For the actual consuming environment:

1. Establish tool discovery, connection, authentication, and correct system
   identity through real reads. Never paste credentials into the report.
2. Look up a known component's API and intent and resolve a known token.
   Sample additional distinct assets or concerns to detect empty/sample
   catalogs and responses that repeat irrelevant content.
3. Compare returned versions with the consumed runtime. Newer documentation
   needs matching-version evidence or a separately authorized upgrade.
4. Query a deliberately nonexistent asset. Record whether absence is honest
   or the source fabricates or silently substitutes a result.
5. Probe composition and validation capabilities separately if available.
   Do not assume every MCP provides them.

Record content coverage, freshness, degraded/fallback responses, and limits
independently of transport health. Repository access can be sufficient
without MCP. Remote access may be useful for designers outside the checkout;
local access may fit the sanctioned developer environment. Choose based on
the actual consumers and maintenance burden.

## Retrieve the decisions behind the UI

Try a user-need query such as “help someone recover from a failed payment,”
not only “find Alert.” Inspect purpose, appropriate and inappropriate use,
related patterns, prerequisites, required/optional regions, slot meanings,
ordering, content, responsive behavior, and accessibility interactions.

For example, a component named Alert may carry urgent announcement behavior
that is wrong for a decorative notice. Verify the usage guidance before
confirming the mapping. A page template may be useful or too restrictive;
the need and working policy decide.

Reuse existing contract formats. Schemas, narrative guidance, and executable
examples have different jobs. They need to agree on overlapping facts, not
duplicate everything. Retrieve relevant context on demand instead of
loading the entire ecosystem into every prompt.
