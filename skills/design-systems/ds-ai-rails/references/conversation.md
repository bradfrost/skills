# Keep AI on the rails of the design system

Use this approved wording for the user-facing conversation. Read the relevant
stages before presenting them. Preserve the quoted copy, filling placeholders
from actual evidence and adapting the scope sentence to the requested mode.
Skip questions already answered by context and carry existing authorization
forward. Present only the relevant branches; do not recite the whole sheet.

The procedural references govern discovery, policy, setup, and verification.
This conversation does not establish facts by itself. In a copy-only dry run,
label examples as hypothetical and do not claim inspection or execution.
Assessment ends with its findings; setup and verification require the relevant
request or authorization.

**Reading key:** Quoted passages are user-facing copy. Bracketed fields are filled from actual evidence. Italic notes explain when a passage appears and are not shown to participants. Only relevant branches appear in a real run. Questions already answered by available context are skipped.

**Path:** Start → establish the context → inspect the setup → agree on reuse and gap handling → present findings and improvements → finish the assessment, or continue into authorized setup and verification → hand over results and team decisions.

## 1. Opening

> Your design system provides sturdy foundations for building websites. This skill helps keep AI on those rails: using your real components, tokens, patterns, and guidance instead of hallucinating UI.
>
> Assess the current AI setup, strengthen its connections to the design system, and establish clear guidance for needs the system doesn't yet cover.
>
> What design system are you using, and where are you using AI to build? Share a project folder, documentation link, or a short description.

*When the project and system are already known, replace the final question with the identified context and continue inspecting accessible sources.*

## 2. Establish the purpose and scope

*Ask only for missing information that changes the work. Present these questions as needed, rather than as a questionnaire dumped into the opening.*

> What would you like to accomplish?
>
> - **Assess the setup:** Understand what works, what's missing, and what to improve.
> - **Set up the connections and rules:** Prepare or apply changes that help AI use your system.
> - **Check an existing setup:** Test whether the current approach works and where it falls short.

> What kind of work should this support: open exploration, a prototype built with the system, or production work?

> What's one representative page or task to focus on? For example, an account-settings form, a search page, or a checkout step.

*Summarize the scope once it is established. Default to assessment when the request is about readiness. Do not ask the user to select a mode they already requested.*

> This assessment covers **[system]**, **[project or sandbox]**, and **[AI environment]**, with **[user task]** as the example. The focus is **[exploration/prototype/production]**.
>
> The result will identify what can be trusted today, the most useful improvements, and decisions that need your team's attention.

## 3. Inspect the actual setup

*Inspect before asking the user to supply facts that are already accessible. Describe the scope briefly, then surface meaningful findings as they emerge.*

> The setup review covers:
>
> - Which instructions, skills, tools, settings, and agents influence the work.
> - How AI finds the system's real components, tokens, patterns, and usage guidance.
> - Whether that information matches the version the project uses.
> - How the actual system code becomes part of the website.
> - Which checks catch mistakes, and what still depends on human review.
> - Where uncovered needs, defects, and proposed changes go.

*If access is incomplete:*

> **[Source or capability] isn't accessible in this environment.** That leaves **[specific question]** unverified. The available **[sources]** still support **[remaining assessment work]**.
>
> To check the missing part, provide **[specific non-sensitive reference or approved access path]**, or have **[required role]** verify **[specific fact]**. Don't share credentials in the conversation.

*If there is no MCP, but another adequate source exists:*

> **[Repository/documentation/CLI] provides access to the system.** An MCP isn't required for this setup. What matters is whether AI can retrieve accurate, relevant information and use the real implementation.

*If an MCP is connected but inadequate:*

> **The connection works, but the returned information isn't sufficient yet.** [Describe the wrong system, stale version, incomplete coverage, repeated sample response, or fabricated result.] This affects **[dependent work]**. The next step is **[repair or permitted alternative]**.

*If instructions or sources conflict:*

> **[Source A] and [source B] disagree about [specific concern].** [Explain the practical consequence.] Resolving this needs **[evidence or owner decision]**. The affected work is **[scope]**; **[independent work]** can continue.

## 4. Show the evidence

*Generate this table from inspected facts, with source links. Do not fill it with assumed successes.*

> **Here's what the current setup supports.**
>
> | Area | Finding | Evidence | Status |
> |---|---|---|---|
> | AI instructions and settings | [Finding] | [Source and scope] | [Status] |
> | Component and token access | [Finding] | [Lookup result and version] | [Status] |
> | Patterns and usage guidance | [Finding] | [Source or task-based lookup] | [Status] |
> | Actual implementation | [Finding] | [Dependency, code, or rendered evidence] | [Status] |
> | Validation and review | [Finding] | [Observed check or documented requirement] | [Status] |
> | Gaps and contribution routes | [Finding] | [Policy or unresolved decision] | [Status] |
>
> **Working** means the relevant capability was demonstrated within the stated scope. **Partial** means some of it works. **Missing** means its absence was established. **Not inspected** means there isn't enough evidence yet. **Not applicable** means it isn't needed for this scope.
>
> Each finding distinguishes what was verified, what was reported by a source, and what remains unknown.

## 5. Decide how the system should be used

*Honor existing rules first. Present choices only where policy is missing or the user requests a change.*

> **How strictly should AI use the design system for this work?**
>
> - **Prefer the system.** Use suitable existing assets first. Custom UI still needs a reason and an agreed place to live.
> - **Require the system for specific parts.** Name the requirements, such as all controls and design tokens, and where composition or layout can vary.
> - **Use the approved ecosystem exclusively.** Build all in-scope UI from approved implementations and permitted compositions. Uncovered needs require an agreed solution or exception.
>
> These choices describe reuse. The next decision is what happens when something is missing.

> **What counts as the approved ecosystem here?** [Summarize known foundations, components, shared patterns, product-owned compositions, and approved external tools.] Are new compositions allowed? Are any page templates or flows required?
>
> Ordinary page structure, application logic, content, and media also need room in the agreement. Using real inputs and buttons in a new filter bar can be allowed while creating a replacement input is not.

*When the team has not settled the policy:*

> **This may surface decisions your team needs to discuss. That's a useful outcome!** A working choice for this project can keep things moving while the broader policy takes shape.
>
> A starting proposal is to reuse verified components and tokens, compose them within agreed boundaries, and route new components, overrides, or dependencies for a decision.
>
> For **[current scope]**, is that an appropriate working agreement? Who can decide the remaining questions, and when should the agreement be revisited?

*Ask for an actual decision only when dependent changes need authorization. During assessment, this can remain a clearly labeled assumption. Existing approval is carried forward without reconfirmation.*

## 6. Handle needs the system doesn't cover

*First check the real catalog, relevant usage guidance, and existing compositions. A failed lookup does not establish that a component is missing. Show only the applicable route and viable alternatives.*

> **[User need] needs a decision.** The available evidence shows **[finding]**, after checking **[sources and existing options]**.
>
> The recommended route is **[route]**, because **[reason]**. It affects **[scope]** and belongs with **[owner or ownership gap]**.

| What the review finds | User-facing route |
|---|---|
| The solution exists but was hard to discover | “Use **[existing solution]**. The discovery or documentation problem belongs in **[destination]**.” |
| An existing component is broken | “Record the reproduction for **[component owner]**. Any temporary workaround needs a defined scope and review point.” |
| Design, code, and guidance disagree | “Resolve **[specific discrepancy]** with **[owner]** before relying on the disputed behavior.” |
| Existing components can form a new composition | “Compose **[ingredients]** in **[agreed location]**, under **[owner]**. This does not require inventing a new primitive.” |
| A new component or variant could serve several products | “Prepare a shared contribution proposal. The owning team decides whether to accept and release it.” |
| The need is specific to one product | “Use **[approved local extension route]**, with its token, accessibility, testing, and maintenance requirements.” |
| An approved external library fits | “Integrate **[approved library]** within **[boundary]** and verify its fit with the system.” |
| A temporary exception is justified | “Record the exception's approval, scope, owner, review date, and removal or migration plan.” |
| No route is approved yet | “Hold **[affected portion]** for a decision. Continue **[independent covered work]**.” |

*If a missing feature prompts an unrestricted fallback:*

> A gap in the system doesn't give AI permission to invent the rest of the interface or switch to another stack. The available choices are **[appropriate contribution, composition, extension, approved integration, exception, or scope adjustment]**.
>
> Calling something a recipe or pattern doesn't change its requirements. The ingredients and ownership still need to fit the agreement.

*React, Tailwind, and other technologies may already belong to the organization's approved ecosystem. The actual policy determines their role.*

## 7. Leave a clear decision record

> **Working agreement for [scope]**
>
> - **Required reuse:** [Components, tokens, patterns, and guidance.]
> - **Permitted freedom:** [Composition, layout, content, and extension boundaries.]
> - **Uncovered needs:** [Routes, owners, and destinations.]
> - **Status:** [Settled / provisional / proposed / unresolved.]
> - **Work that can proceed:** [Scope.]
> - **Work awaiting a decision:** [Scope and decision needed.]
> - **Review point:** [Date, prototype review, production promotion, or other trigger.]
>
> **Team discussion still needed:** [Concrete question, viable options, relevant tradeoffs, and decision owner or ownership gap.]

*A provisional agreement applies only to its approved scope. Temporary exceptions include an exit plan and do not renew automatically. Draft contribution requests remain drafts until actually filed.*

## 8. Recommend improvements that fit

> **The most useful next improvement is [change].** It addresses **[observed failure]** and can be checked by **[acceptance exercise]**.
>
> Relevant approaches from Kaelig Deloumeau-Prigent's [State of AI in Design Systems](https://state-of-ai-in-design-systems.netlify.app/techniques.md) inform these recommendations. The fit with your team and evidence from your own setup determine which approaches are useful.
>
> | Improvement | Why it matters here | Owner and effort | Evidence it helped |
> |---|---|---|---|
> | [Smallest useful change] | [Observed problem and relevant technique/source] | [Owner, prerequisites, maintenance] | [Acceptance exercise] |
> | [Next dependent improvement, if needed] | [Local reason] | [Owner and dependencies] | [Acceptance exercise] |

*Select from validation, prohibitions with useful alternatives, curated context, tool lookup, tokens, examples, metadata, instructions, scaffolding, design–code mapping, and other relevant mechanisms. Do not require every technique or count them into a maturity score. Fix inaccurate sources before distributing them more widely.*

*Assessment-only work can end here using the assessment ending in section 12. If setup was already requested, continue within that authorization. Otherwise, a concrete setup choice can follow the assessment:*

> The proposed changes are **[specific changes]** in **[files or settings]**. They apply to **[scope]**, require **[role/access]**, and can be reversed by **[rollback]**.
>
> Should these changes be prepared for review or applied within this scope?

## 9. Set up the agreed changes

*Present actual changes and their state. Do not imply that writing an instruction file activates it in every agent.*

> **Setup changes**
>
> | Change | Location and scope | State | Verification |
> |---|---|---|---|
> | [Change] | [File or setting] | [Prepared / applied / active / verified] | [Result or remaining check] |
>
> **Activation still needed:** [Specific steps, if any.]
>
> **Rollback:** [How to undo the scoped changes.]

*If settings or references cannot be resolved:*

> **The change is prepared but isn't active.** Activation requires **[specific missing references, permissions, or setup]**. The draft identifies those requirements; it does not assume that the connection works.

## 10. Try a representative task

*Use a small task within the available authorization and budget. A workshop participant can stop at a useful assessment if implementation or runtime access is unavailable.*

> **Try the setup on [representative task].** The exercise includes real system components, a meaningful interaction, and a requirement that tests how an uncovered need gets handled.
>
> Success means:
>
> - The result uses the actual system implementation.
> - Component APIs and token references are real and appropriate.
> - Required interactions, responsive behavior, and accessibility checks work.
> - The uncovered need follows the agreed route.
> - A person can review whether the result is useful and well designed.
>
> The exercise is limited to **[sandbox, time/usage budget, and repair attempts]**.

*If an execution boundary has not been established, ask only for that missing decision before building. If it has, proceed.*

> The checks also need testing. A known-valid example should pass, while a fabricated API or token should be rejected. A check that rejects legal use needs fixing; valid UI shouldn't be distorted to satisfy a faulty validator.

*If a repeated failure exhausts the agreed budget:*

> **[Check] still fails after [attempts].** The reproduction and results are recorded in **[location]**. The next action belongs to **[owner/role]**. **[Independent checks or work]** can continue.

*If a rendered test isn't possible:*

> **The available checks cover [scope].** Rendering, interaction, and accessibility behavior remain unverified because **[specific access limit]**. The report includes the exact checks to run in an environment that supports them.

## 11. Show what the result can be trusted to do

> **Verification results for [task and environment]**
>
> | Question | Result | Evidence and limits |
> |---|---|---|
> | Does it use the actual system? | [Result] | [Used exports, resolved versions, rendered evidence] |
> | Are APIs and tokens valid? | [Result] | [Checks and results] |
> | Does the experience work? | [Result] | [Interaction, responsive, accessibility evidence] |
> | Does it follow the working agreement? | [Result] | [Composition and gap handling] |
> | Do the checks catch mistakes without rejecting valid use? | [Result] | [Valid and invalid cases] |
> | Has a person reviewed the experience? | [Result] | [Review or explicitly pending] |
>
> **What the guardrails actually do:**
>
> - **Advisory:** Instructions guide AI, but do not mechanically prevent a mistake.
> - **Detecting:** A check caught the tested mistake.
> - **Blocking:** An observed control prevented the specified action on the named path.
> - **Unverified:** The control's behavior hasn't been demonstrated.
>
> [Name each relevant control, its classification, scope, and known bypasses.]

> These results cover **[number of runs, environment, system version, and date]**. They do not establish the same behavior in every model, tool, or future session. Passing automated checks also does not establish that the design is good.

*When repeatability is part of the request, propose a bounded set of fresh runs, such as three per claimed environment. Reuse the same brief and record differences, interventions, failures, and measured time or usage. Do not silently start more runs or invent a before/after improvement.*

## 12. Finish with a usable handoff

### Assessment ending

> **The assessment is complete for [scope].**
>
> **What works:** [Verified capabilities.]
>
> **What needs attention:** [Consequential gaps and unknowns.]
>
> **Recommended next step:** [One concrete improvement and how to check it.]
>
> **Team decisions:** [Unresolved questions, current working choices, and owners.]
>
> **Saved record:** [Report link.]

### Setup or verification ending

> **[Scope] now has [verified result].**
>
> **Changed:** [Applied changes and their activation state.]
>
> **Verified:** [Actual reuse and successful checks.]
>
> **Failed or unverified:** [Results and remaining limits.]
>
> **Uncovered needs:** [Agreed routes, exceptions, owners, and review points.]
>
> **Next required action:** [Concrete action needed to finish this scope, or “None for this scope.”]
>
> **Saved record:** [Profile, working agreement, changes, results, and relevant tracker links.]

*Use the team's existing records where possible. Proposed issues are not described as filed. A system fix is not described as adopted until the product uses it. Publication and deployment follow the user's authorization and the existing process.*
