# Keep AI on the rails of your design system

Status: approved by Brad and implemented in the repository, October 22, 2026, with the reuse-policy clarification below. The [skill](../../skills/design-systems/ds-ai-rails/SKILL.md) contains the working instructions. This specification does not establish runtime enforcement; see the [validation record](ds-ai-rails-validation.md) for what was checked.

Help teams configure and verify an AI workflow that builds with their actual design system. Give them a clear picture of what works today, the next useful improvements, and evidence that generated UI follows the rules they set for themselves.

The skill should help someone answer: **“Can I trust this setup to use our system, and what happens when our system doesn't cover something?”**

This should put the central thesis of the AI & Design Systems course into practice: marry AI's generative capabilities with the organization's hard-earned foundations, strengthen the connections between design, code, documentation, and people, and feed product experience back into those foundations. The [research basis](ds-ai-rails-research.md) connects the requirements below to the course, community discussions, and jam sessions.

## The promise

October 25 refinement: use the State of AI in Design Systems study as a
selective evidence library for evaluating mechanisms and proposing changes.
The [techniques reference](../../skills/design-systems/ds-ai-rails/references/techniques.md)
maps its categories to local evidence, fit, ownership, and acceptance
exercises. Technique counts do not establish readiness; neither the study's
MCP nor every category is required. A conversational dry run can review the
user-facing exchange without claiming an environment assessment.

Your team has invested in components, tokens, accessibility, documentation, and ways of working. AI should put that investment to work! This skill connects those pieces to the environment where AI builds websites, then checks whether the connection holds up in practice.

It is important to say that a skill cannot guarantee an agent will always follow instructions. Confidence comes from authoritative information, explicit policies, working checks, and repeatable evidence. Report exactly which rules are advisory, which are mechanically enforced, and where enforcement ends.

There are two directions to this work. A sound, accessible system helps AI make better products. Building real products exposes missing context, broken components, and unmet needs that can improve the system. The skill needs to establish both connections. A growing pile of rules, an impressive demo, or a green compliance check is not the outcome. A team should be able to build useful work, explain what it trusts, and know where the next problem goes.

## Who this helps

- A design system team enabling AI across several products and tools.
- A product team trying to make its coding agent reliably use the shared system.
- A designer exploring in a sandbox with limited access to product code.

Start with one design system, one consuming project or sandbox, and one AI environment. Expand once that path works. The organization can have multiple component libraries, frameworks, brands, or levels of ownership; the skill records those differences instead of forcing one architecture on everyone.

## What this skill owns

The skill assesses the connection between a design system and an AI development workflow, prepares or applies scoped setup changes when requested, and verifies the result with a representative build exercise.

| Related skill | Boundary |
|---|---|
| `ds-inspection` | Assesses the health of the system itself. Reuse current evidence where available; route underlying system problems there without requiring a full inspection first. |
| `ds-adoption-plan` | Plans an existing product's migration onto a system. |
| `vibe-killer` | Converts an existing page onto real system components. |
| `product-to-storybook` / `storybook-to-product` | Move design work between a component workshop and a product. This skill establishes the rules and checks those workflows should follow. |

Version one focuses on AI-assisted website development. Runtime generative UI, agent-operated websites, and automated organization-wide monitoring are separate extensions. The discussions of A2UI and WebMCP inform future possibilities; neither is a prerequisite for this skill.

Preserve room for those extensions by describing capabilities and responsibilities rather than baking a particular framework, editor, vendor, or contract schema into the skill. Component and page contracts are useful evidence when an organization has them. The course and jams include work in progress on these ideas; the skill must not present one experimental schema as a settled industry standard.

## Three ways to use it

**Assess.** Inspect the available environment, identify gaps, and produce a prioritized setup plan. This is the default when someone asks whether their setup is ready. Assessment does not change settings or build product features.

**Set up.** Use the assessment to prepare or apply the changes the user requested. Preserve existing instructions and tooling. Show concrete diffs, describe their scope, and distinguish files prepared from settings activated. Organization-wide configuration, credentials, protected-branch settings, and external writes require the appropriate authority.

**Verify.** Exercise an existing setup or recheck it after changes. Compare evidence against the previous run where available. A configuration change is not verified merely because the file exists.

Each mode can finish usefully on its own. An inaccessible tool limits the claims and dependent work; it does not prevent an honest assessment of everything else.

## Discover first, interview second

Read the accessible project, existing design system profiles, instructions, manifests, documentation, and tool inventory before asking the user to describe them. Resolve only the gaps that change the plan:

1. Which system, product, user need, and AI environment are in scope?
2. Where are the authoritative code, tokens, usage guidance, and design references?
3. What does the team require AI to reuse, and where may it create something new?
4. Who owns shared components, product patterns, and exceptions? Where does each kind of request go?
5. What can this user inspect or change, and what would make a useful pilot?

Use the team's own terms: recipes, patterns, compositions, modules, templates, or something else. Do not require separate packages for each layer. A pattern can live in a product repository if that is the team's established home for it.

### Establish the starting point and intended destination

Record whether this is a new product, ongoing development, a legacy migration, or a rebrand. Define the areas being changed and the existing problems outside that scope. Adopting the skill must not silently turn a page change into a whole-product migration.

Also establish what the work is for:

| Work | Agreement to establish |
|---|---|
| Open exploration | Where experimentation is allowed, what may diverge, and how the result is labeled. An off-system experiment is never reported as verified system reuse. |
| A prototype using the system | Which real ingredients and behaviors must be present, which integrations are mocked, and who evaluates the experience. |
| Production work | Applicable system policy, real integration requirements, release controls, accountable reviewers, and the path to adoption. |

These are purposes, independent of the skill's assess/setup/verify modes. Moving a prototype toward production requires an explicit review of its provenance, unresolved gaps, integrations, and quality evidence. Looking finished does not establish readiness to ship.

For a designer without product-code access, a sanctioned sandbox using the real package can be a useful starting point. For a team with only a design library, the immediate outcome is an implementation and access plan. Do not fabricate a component library and call it integration with the existing system.

## Inspect the whole path

For each finding, record the evidence location, relevant version or revision, observation date, scope, and whether it was directly verified, reported by the user, or remains unknown. Redact secrets from settings and tool results.

| Area | What to establish | Evidence that matters |
|---|---|---|
| AI environment | Which editor, CLI, browser tool, cloud agent, skills, plugins, and delegated agents participate? | Actual accessible configuration and tools; distinguish inspected surfaces from reported ones. |
| Organizational access | Which tools, providers, accounts, data access, and operations are permitted? Who can activate missing capabilities? | Approved environments, read/write boundaries, access restrictions, and setup responsibilities. Never route around company restrictions with personal accounts or credentials. |
| Instructions | Which global, organization, project, and directory rules apply? Do generic UI skills conflict with the system? | Loaded rules, scope, conflicts, and observed behavior in a fresh session where possible. A file on disk does not prove an agent loaded it. |
| System runtime | Can this project consume the real implementation? | Resolved dependency versions, imports, styles, assets, registration or framework integration, and a rendered example. |
| Foundation health | Are the ingredients selected for this pilot sound enough to use? | Working behavior, supported states, token bindings, accessibility evidence, and known defects. Reuse inspection results without requiring the entire system to be perfect first. |
| System knowledge | Can the agent find real APIs and understand when to use them? | Component APIs, tokens, composition examples, variants, interaction states, accessibility guidance, deprecated APIs, and version alignment. |
| Tool access | Can the active agent retrieve that knowledge? | Successful discovery and lookup through the available MCP, API, repository, manifests, or documentation. |
| Composition | Does the agent reuse suitable existing patterns and build new ones in the right place? | A region-by-region mapping from a representative requirement to existing components and approved composition rules. |
| Validation | What catches wrong APIs, unauthorized styling, inaccessible interactions, or broken renders? | Executed checks with known passing and failing fixtures; document what each check cannot establish. |
| Review and release | What must pass before generated work reaches users? | Existing review policy, required checks, branch/release controls, applicable bypasses, and human review. |
| Feedback | What happens to gaps, exceptions, and useful new compositions? | Real destinations, owners, contribution instructions, and an example tracked through resolution where available. |

Do not collapse this into a readiness percentage. Missing authoritative APIs or a bypassable release check can matter more than several completed checklist items. Give findings a status such as working, partial, missing, not inspected, or not applicable, with the reason.

Keep setup approachable. Explain which application or repository an action belongs in, who can perform it, how success is observed, and the smallest useful next step. A designer, system maintainer, and product engineer may need different instructions for the same capability. Record ongoing hosting, maintenance, and paid-access requirements when known; do not prescribe a new service merely because it appeared in a demo.

### Map authority across the ecosystem

The ecosystem is the source of truth collectively. Within it, establish authority for each concern: implementation API, design intent, tokens, interaction behavior, composition guidance, content, and governance. Record the maintained source, owner, supported version, and how other representations derive from or link to it.

Code can establish which properties are implemented without fully explaining when a component should be used. A Figma description can express design intent without proving runtime behavior. A documentation site can bring sources together without becoming the editorial home for everything. If two sources disagree, surface the conflict and route it to the owner; do not silently declare that code or Figma always wins.

Keep facts close to their maintained assets where practical. Prefer generated API reference and stable links over copied property tables in several instruction files. Link narrative guidance to technical contracts; they need to agree where they overlap, but they do not need to contain identical information. Where the organization maintains design/code mappings, verify identifiers and representative state, token, layout, and interaction parity. An intentionally absent design library is not a defect.

The skill contains procedure. The environment profile points to organizational policy. The system's maintained sources contain its changing data. A skill should not ship a frozen copy of an organization's component catalog.

### Make intent and composition discoverable

Inspect more than component anatomy. Can an agent find the right pattern for “help someone recover from a failed payment,” without already knowing its catalog name? Useful context includes purpose, when to use or avoid it, related patterns, prerequisites, required and optional regions, content guidance, responsive behavior, accessibility interactions, and a working reference where available.

For a composition, establish which choices are fixed and which remain open: component sequence, slot meaning, layout constraints, allowed variants, content, and behavior. Reuse the organization's current format. Markdown guidance, typed schemas, examples, and executable checks have different jobs; do not require every pattern to acquire a new JSON contract.

Separate ingredient policy from composition freedom. A team can require real components and tokens while allowing flexible layouts. Another can require an approved page template for a regulated flow. Starting with a larger composition is useful when it fits the need; it is not a universal rule that every page must start from a template.

Retrieve relevant context as needed, including organizational decisions and their rationale. Avoid loading the entire design system into every prompt. Missing knowledge and excessive, contradictory knowledge can both hurt the result.

### Probe capabilities, not product names

An MCP configuration entry proves only that somebody configured an endpoint. Test whether the active environment can connect, discover the relevant tools, find a known component, retrieve its real API and usage guidance, and resolve a token. Record any version mismatch with the installed runtime.

Also query a deliberately nonexistent component. The useful result is an honest absence. Check validation or composition tools separately if the server exposes them; do not assume all design system MCPs do.

Probe several distinct known assets or concerns when the catalog supports them. A reachable server returning the same sample button for every request is not healthy system access. Distinguish connection, authentication, tool visibility, correct system identity, content coverage, freshness, and version alignment. Record degraded or fallback responses explicitly.

Choose local files, CLI, MCP, or another access method according to who needs access and where their agents run. A remote endpoint may help people outside the repository; local access may fit an approved developer environment. Test the actual consuming surface. Success in the maintainer's checkout does not establish success for a designer's chat or a cloud agent.

An accessible repository or versioned documentation can provide a legitimate knowledge path without MCP. If only screenshots or a design file are available, record the visual evidence and the missing implementation evidence. Do not claim to have established real code reuse from appearance alone.

If a required source fails during a build, use only a fallback already allowed by the team's policy and adequate for that version. Otherwise stop the affected work and explain what is missing. Never invent APIs to keep moving.

## Let the organization define its reuse policy

Policy strength and enforcement strength are separate. A team may demand exclusive reuse while its current tools provide only advisory instructions. The report must make that mismatch visible.

| Policy | Expected behavior |
|---|---|
| Prefer the system | Discover and use suitable existing assets first. Record custom UI and why it was needed. |
| Require it within defined scope | Require reuse for named concerns, such as buttons, forms, typography, and tokens. State what remains flexible. |
| Use the approved ecosystem exclusively | Use approved implementations and permitted compositions for all in-scope UI. Route uncovered needs before implementation; never silently weaken the policy. |

Default to the organization's existing policy. If it is unsettled, explain that this work may surface decisions the team needs to discuss. A user can choose a scoped, provisional working agreement within their authority so a pilot can proceed; do not present that choice as settled organization-wide policy. Record its scope, permitted actions, unresolved questions, decision owner, and review trigger. Continue assessment and already-covered work while broader decisions remain open.

Help the team put a finer point on what happens when coverage runs out. Reuse posture alone is insufficient: decide which compositions are permitted, where product-specific extensions belong, when a shared addition is appropriate, how a temporary exception is approved, and what must wait. A missing component does not automatically authorize a new framework, styling stack, or bespoke primitive. If no authorized route covers the affected work, prepare concrete alternatives and pause that portion, not the entire effort.

Define “approved ecosystem” explicitly: foundations, core components, supported adapters, product-owned compositions, permitted third-party libraries, and any approved exceptions. Also define allowed semantic HTML, layout glue, application logic, content, and media. Otherwise “only use the design system” can accidentally prohibit ordinary page assembly.

New composition is different from a new primitive. Combining real cards, buttons, and tokens into a product comparison section may already be permitted. Reimplementing the button inside that section is a separate decision. An import somewhere in the file does not establish that the visible UI actually uses it.

## Give uncovered needs a destination

Start by checking whether an existing component, variant, composition, or documented usage solves the problem. Then classify the remaining need with the team. AI proposes a classification; unclear ownership or intent goes to a human.

| Situation | Default routing to adapt to the organization |
|---|---|
| Existing solution was hard to find | Use it; route a discoverability or documentation improvement. |
| An existing component behaves incorrectly | Send a reproducible defect to its owning team. Record any permitted workaround separately. |
| Design and implementation disagree | Establish which source governs the disputed detail. Route library drift to its owner or discuss whether the product intentionally diverged. |
| Existing primitives cover a new product composition | Create it in the approved product or shared-pattern location, under the appropriate team's ownership. |
| A new primitive or variant may serve many products | Propose a core addition through the team's contribution process. The design system owner decides acceptance. |
| A need is specific to one product | Use the approved local extension path. Record boundaries and ownership. |
| A deliberate experiment or exception is justified | Record who authorized it, where it applies, its review date, and what determines removal, renewal, or promotion. |
| The core team cannot meet the product deadline | Propose an owned temporary implementation only if policy permits it, with a linked upstream request and migration/removal plan. |
| An approved capability is unavailable | Stop dependent implementation; record the access or tooling blocker rather than labeling it a component gap. |

These categories adapt the [governance article](https://bradfrost.com/blog/post/design-system-governance-bugs-design-discrepancies-features-and-recipes/). The owner/destination records and exception lifecycle below are proposed requirements for this skill.

Every unresolved need should carry: the user need, evidence, solutions checked, proposed category, affected product, destination, owner or unresolved ownership, current status, and a next decision. Temporary exceptions also need approval evidence, scope, review/expiry criteria, and an exit plan.

A draft request is not a filed issue. A filed issue is not an accepted contribution. An accepted contribution is not a released dependency. A released dependency is not adopted until the consuming product uses it. Track these distinctions so “close the loop” means something concrete.

## Establish a repeatable build workflow

Generate concise instructions for the user's actual environment that point to authoritative sources and define this behavior:

1. Read the applicable project rules and confirm the required system sources are available.
2. Map the requested UI to existing components, tokens, and compositions. Check APIs against the version the project consumes.
3. Route uncovered needs using the agreed policy. Continue independent, covered work where useful.
4. Build with the real dependencies and approved extension points.
5. Run the relevant structural, behavioral, accessibility, and render checks. Fix failures without weakening checks to achieve a pass.
6. Present rendered results, implementation provenance, remaining limitations, and exceptions for review.
7. Use the organization's release process and capture useful feedback in its established destinations.

These are behavior requirements, not a replacement for the organization's software delivery process. Map them into existing stages and terminology. Eddie's packages, BFW's six phases, specific file names, and automated reporting loops are examples, not prerequisites.

Keep a single maintained policy source where practical, with small environment-specific adapters. Include how collaborators and delegated agents receive it. Do not claim an adapter works on a surface until it has been exercised there.

Preserve working deterministic tools. An agent can invoke a token exporter or generator without rewriting its output through a model. Describe determinism at the operation where it exists; it does not make the surrounding agent workflow deterministic. Keep repair attempts bounded, retain failure evidence, and hand unresolved defects to an owner instead of repeatedly adding more instructions.

## Prove the setup with a small pilot

Choose a representative page or flow in an authorized sandbox. Use the same brief before and after setup changes when a baseline is useful. Include a common component, a meaningful interaction, an existing composition if available, and an intentionally uncovered requirement.

The proof should establish:

- **Provenance:** rendered UI resolves to the approved implementation and version. Detect lookalike local components, unused imports, copied source, and unauthorized overrides where the available tooling permits it.
- **API correctness:** names, properties, slots, events, tokens, and variants exist and are used correctly.
- **Behavior:** content renders, interactions work, keyboard access and responsive states are checked, and the team's applicable accessibility requirements are evaluated.
- **Purpose and design quality:** the result supports the intended user task, follows applicable content and interaction guidance, and receives human review for usability, craft, and appropriate expression. System compliance alone cannot establish these qualities.
- **Governance:** the uncovered requirement follows the configured route, including stopping when exclusive-use policy has no approved solution.
- **Enforcement:** a deliberate violation fails the expected check. Verify whether that failure actually blocks the relevant merge or release path.

Use existing deterministic checks wherever possible. Agent review supplements those checks and human judgment; an agent declaring its own work correct is not independent proof. Static checks alone cannot establish interaction quality, accessibility, or visual fidelity.

Keep three judgments visible: mechanically tested behavior, adherence to the organization's system and guidance, and human evaluation of the experience. State which evidence supports each. Do not collapse them into a single model-generated quality score or claim that an automated accessibility scan proves complete conformance.

Verify the validators too. A legal composition should pass, a fabricated property should fail, and a prohibited local imitation should be caught by the appropriate check or remain an explicit detection gap. Test optional properties and nested composition where relevant. If valid system use fails, investigate the validator or metadata rather than distorting the product to appease it.

Record completion quality, human corrections, unresolved exceptions, and elapsed work where measurable. Compare equivalent briefs and environments when assessing a setup change; changing the model and removing tool access at the same time cannot isolate the effect of one guardrail. If the system supports it, a controlled theme or dependency update can provide additional evidence that the product remains connected to the actual system.

As a starting evaluation protocol, run the brief in three fresh sessions per claimed supported AI environment. Record model/tool versions, policy revision, system version, results, interventions, and failures. This is a repeatability sample, not a statistical guarantee. Recheck after meaningful changes to any of those inputs.

The three-session sample is a proposed default, not a course rule. Agree on the pilot's time and usage budget before running it. Improve the smallest demonstrably weak part of the setup, rerun the relevant exercise, and retain useful checks as regression fixtures. Remove redundant guidance when evidence supports doing so; more rules and tools do not automatically mean better results.

No browser or runtime access means the render and behavior proof remains unverified. No access to release controls means merge/release enforcement remains unverified. The skill still produces the useful evidence it has.

## Deliverables

Keep the output small enough that a team will use it. Prefer the team's existing documentation location; otherwise propose a `ds-ai-rails/` folder in the consuming repository or designated shared configuration repository.

1. **Environment profile:** sources, versions, ecosystem boundaries, policy, owners, tool access, and inspected surfaces. Link existing maintained profiles instead of creating competing copies.
2. **Assessment and setup plan:** evidence, the most consequential gaps, and ordered changes. Each change names its destination, dependency, owner or required role, and acceptance check. Start with a useful pilot instead of requiring every capability at once.
3. **Setup changes, when requested:** reviewable instructions, configuration, and appropriate checks for the actual environment. Include activation status and rollback instructions for changed settings.
4. **Verification record:** brief, runtime provenance, check results, rendered evidence where available, negative tests, repeated-run outcomes, and exact limits of the claim.

Use the existing tracker for actionable needs and exceptions; avoid creating a parallel backlog. When filing is unavailable or unauthorized, preserve a clearly marked draft with its intended destination.

## Version-one scope and acceptance

Ship one portable skill with assessment, setup, and verification modes. Keep the entrypoint concise; put detailed discovery guidance, routing, verification scenarios, and artifact templates in supporting files loaded when needed. It must work without Brad's private tools or the rest of this skill collection.

The following are behavioral acceptance scenarios for the future skill, not tests performed for this specification:

| Scenario | Required result |
|---|---|
| Mature system with an MCP | Probe it, use installed-version APIs, and verify actual runtime reuse. |
| Real component library with no MCP | Establish an adequate repository/docs path; identify what MCP could improve without making it a prerequisite. |
| Design library only | Report implementation access as missing; never claim a successful code integration. |
| Conflicting global and project instructions | Explain the conflict and actual applicable scope; prepare a targeted fix without rewriting unrelated preferences. |
| Docs describe a newer component version | Detect the mismatch; use matching evidence or route a dependency change. |
| Agent invents a property or imitates a component | Catch it through API/provenance checks, or explicitly report the detection gap. |
| Product needs a new composition | Reuse real ingredients and follow the configured ownership/location policy. |
| Product needs an absent primitive under exclusive policy | Stop that portion and route the need; do not disguise new custom UI as a recipe. |
| A temporary exception is approved | Enforce its scope and record its review and exit conditions. |
| Checks run but do not block merging | Describe them as detection, not release enforcement. |
| A delegated or cloud agent lacks the main agent's tools | Report the difference and avoid claiming shared readiness. |
| Only chat or exported evidence is available | Produce a scoped assessment and setup drafts; distinguish instructions from activated changes. |
| An initially working setup loses its required source | Follow an explicitly allowed fallback or stop dependent work. |
| An MCP returns sample data or the wrong system | Detect inadequate coverage or identity; do not mark access healthy. |
| The agent knows component names but misses a suitable pattern | Exercise intent-based discovery and improve its guidance or retrieval path. |
| A valid nested composition fails validation | Identify the validator or metadata defect; preserve valid implementation. |
| Design, code, and usage guidance disagree | Resolve authority per concern and route the conflict to its owner. |
| A compliant page fails the intended user task | Report the quality failure independently of system compliance. |
| The company permits only a restricted tool environment | Work within it and name access dependencies; do not recommend bypassing restrictions. |
| An exploratory prototype is proposed for production | Reassess real dependencies, mocked behavior, gaps, quality, and release requirements. |
| A legacy page is the agreed scope | Apply the agreed policy to that scope and record surrounding debt separately. |
| The organization has no shared pattern package | Use its permitted location and ownership rather than creating an Eddie-shaped architecture. |
| The team has not settled its gap policy | Support an authorized, scoped working agreement; preserve unresolved decisions and a review trigger without blanket permission for custom UI. |

Validate the skill against contrasting environments before calling it portable: an MCP-backed system, a source-accessible library without MCP, and a limited-access design-led environment. Test real outcomes, including honest stops, rather than matching the wording of its reports.

## Source basis and design decisions

The [local rails demo](../../../ai-design-systems-resources/_site/demos/keep-ai-on-the-rails/index.html) supplies the progression from prompts and instructions through real dependencies, retrieval, composition, validation, review, release gates, and feedback. Its comparison captures are placeholders. The course's [footer demonstration](https://app.notion.com/p/3ad3c9323e86819f8be0ec7cd93c45fe) does describe an actual comparison: a custom footer versus the real Eddie recipe. It also changes the agent environment and deliberately skips an MCP lookup, so treat it as an illustrative case rather than a controlled reliability measurement.

The expanded research retrieved all 218 entries in the supplied [course transcript database](https://app.notion.com/p/34a3c9323e86802ab3ebc1964320d79c), screened their full text thematically, and close-read selected lessons and passages. Community research covered the available channel history and selected complete discussions. Jam research covered the located recordings and meeting transcripts, with missing and duplicate material recorded in the [research ledger](ds-ai-rails-research.md). Retrieval and screening are not a claim that every sentence or every Slack reply received equal review.

The most direct course anchors are [Principles and Our Approach to AI](https://app.notion.com/p/34a3c9323e8681859a0fc379dd635f38), [Context-Based Design Systems](https://app.notion.com/p/3c23c9323e86813e8260edbe7793ded8), [Keeping Product on the Eddie Rails](https://app.notion.com/p/3ad3c9323e86811bbdc9ed6d0ce78d27), [The Steel Curtain](https://app.notion.com/p/3c73c9323e868154bc3efd05e4c47b29), and [Selling AI & Design Systems](https://app.notion.com/p/3ce3c9323e86811a9793eb32fa53f139). The ledger maps supporting lessons and community evidence to individual requirements.

The [October 22 workshop notes](https://app.notion.com/p/4013c9323e8681a2aea7cf401514c0b8) support incremental setup, organization-defined compliance scope, early testing, low-stakes pilots, and human governance. The discussion of the date-picker change specifically connects checks to runtime behavior and keeping machine-readable knowledge current.

The [October 22 jam-session notes](https://app.notion.com/p/4013c9323e8681fbb08bddc43d032967) inform usage guidance beyond API anatomy, actionable and respectful findings, and workflows for designers who lack product-code access. Meeting summaries and relevant transcript passages were reviewed; vendor claims in those discussions are not treated as verified product capabilities.

The [ecosystem article](https://bradfrost.com/blog/post/the-design-system-ecosystem/) supplies the distinction between foundations, implementations, and optional product-owned compositions. The skill maps those responsibilities onto the organization instead of prescribing Eddie's package layout.

The proposed name, three modes, reuse-policy choices, evidence format, and three-session evaluation sample are recommendations for this skill. They are open to revision as it is tried against real environments. The concrete success condition remains: a team can demonstrate actual system reuse, explain its enforcement limits, and route unsupported needs without the agent inventing a replacement system.
