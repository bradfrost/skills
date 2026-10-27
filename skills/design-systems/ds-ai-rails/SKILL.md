---
name: ds-ai-rails
description: Assess, set up, and verify how an AI development environment uses an organization's actual design system. Use when someone wants to keep AI on their system's rails, connect system knowledge and tools to coding agents, establish reuse and gap policies, or check whether those guardrails work. Focuses on the workflow and its evidence; ordinary page building or a full system inspection alone does not require this skill.
---

# Keep AI on the rails of the design system

Your team has invested in components, tokens, accessibility, documentation,
and ways of working. Help people put that investment to work! Establish a
usable connection between their design system and the AI tools building
websites, then show what that connection can actually be trusted to do.

Use the public name above consistently. Present the work directly in
second person or neutral language; avoid first-person assistant narration.
Keep the purpose clear: help AI use the sturdy foundations of the actual
design system instead of hallucinating UI.

Work with the organization's ecosystem and vocabulary. Recipes, patterns,
modules, templates, and pages can live in different places under different
owners. No particular framework, MCP, vendor, package layout, or other
skill is required.

Use the [user-facing workflow](references/conversation.md) for the approved
presentation copy. Read the relevant stages as the work progresses. Ask only
unanswered questions, show only applicable branches, and fill every finding
from evidence. The procedural references below govern what to inspect and do.

## Choose the work

Infer the mode from the request and existing context; ask only when the
answer changes what you should do.

| Mode | What you do | Where it ends |
|---|---|---|
| Assess | Inspect the available environment and propose ordered improvements. Default for readiness questions. | Evidence, a practical plan, and unresolved team decisions. No settings or product changes. |
| Set up | Assess enough to make the requested changes, then prepare or apply scoped instructions, configuration, and checks. | Reviewable changes, activation status, and verification within available access. |
| Verify | Exercise an existing setup or recheck it after changes. | Observed results, failures, interventions, and exact limits of the claim. |

Start with one system, one consuming project or sanctioned sandbox, and one
AI environment unless the user specifies a wider scope. Distinguish open
exploration, a prototype using the system, and production work. Record what
may diverge or be mocked and what must be revisited before promotion. A
legacy page change does not authorize migrating the whole product.

## Establish the context

Read accessible project instructions, system profiles, manifests, catalogs,
and tool settings before interviewing the user. Reuse maintained profiles
rather than creating a competing source. Ask only for missing information
that changes the work: the user need, relevant system and environment,
required reuse, permitted extension paths, ownership, and access.

For an assessment or new setup, read [Discovery](references/discovery.md).
For verification, refresh the relevant discovery evidence instead of
repeating a whole assessment. Record sources and versions; an old successful
connection does not prove the current one works.

During assessment, use the [techniques review](references/techniques.md)
to connect observed weaknesses to relevant approaches from the State of AI
in Design Systems study. Select what fits the team; technique counts are
not a readiness score. For a conversational dry run, walk through the
user-facing exchange without implying that an environment was inspected.

Keep these distinctions throughout the run:

- **Knowledge:** which assets and guidance exist, who maintains them, and
  what version the project actually consumes.
- **Policy:** what the organization wants agents to do, including where
  they may compose, extend, or experiment.
- **Enforcement:** what observed mechanisms detect or block a violation
  on each surface. Instructions alone are advisory.
- **Quality:** whether the resulting experience works for its users.
  Compliant imports do not prove good design or working behavior.

## Establish a working policy

Read [Policy and gap routing](references/policy.md) before proposing a
reuse policy or deciding what to do with an uncovered need.

This work often surfaces decisions a team has never made explicitly.
Acknowledge that! Help people make a scoped working choice when they have
the authority, while recording what still needs team discussion. A pilot
agreement is not automatically organization-wide policy.

Keep assessment and covered work moving. When an unresolved decision changes
whether new UI is allowed, present concrete options and pause that portion
until an authorized route exists. A system gap never grants blanket
permission to switch stacks or invent a replacement system.

## Connect and exercise the workflow

For setup work, read [Setup](references/setup.md). Adapt the following
behavior to the existing delivery process, rather than installing a new
process around it:

1. Load the applicable rules and confirm access to authoritative sources.
2. Map the requested experience to real components, tokens, and suitable
   compositions. Verify APIs and usage guidance for the consumed version.
3. Route uncovered needs under the working policy.
4. Build with the actual dependencies and permitted extension points.
5. Run relevant code, behavior, accessibility, and rendered-result checks.
6. Present provenance, results, limitations, and exceptions for review.
7. Follow the existing release process and route product learning upstream.

For a requested pilot or verification, read
[Verification](references/verification.md). Use a small representative task
with a meaningful interaction and an uncovered requirement. Test the checks
as well as the output. Retain human judgment of the experience.

## Keep the claims honest

- Verify real APIs and rendered implementation where possible. A screenshot,
  design file, unused import, or agent's self-report does not prove code reuse.
- Attribute evidence as **verified**, **reported**, or **unknown**, with
  location, version/revision, date, and scope. Give findings a status of
  working, partial, missing, not inspected, or not applicable. Avoid a single
  readiness percentage that hides an important gap.
- Label each control **advisory**, **detecting**, **blocking**, or
  **unverified**. Name the exact path it covers and any known bypasses.
- A blocked capability limits dependent work and its claims. Continue the
  useful independent work; use a fallback only when policy permits it and
  it supplies adequate evidence for the relevant version.
- Preserve existing permissions. A request to assess is not permission to
  change settings. A request to set up can authorize scoped local changes;
  it does not grant credentials, broaden organizational policy, or authorize
  messages, publication, or changes to unrelated projects.
- Separate a prepared change from an activated one, a draft issue from a
  filed one, and a released system fix from its adoption in the product.

## Leave something the team can use

Read [Artifacts](references/artifacts.md) when producing the outputs.
Prefer the team's existing documentation and tracker; otherwise use a
`ds-ai-rails/` directory in the agreed project. In plain chat, provide the
same records as saveable text and state what you could not inspect or run.

Assessment produces a profile and a prioritized plan. Setup adds concrete
diffs, activation/rollback notes, and available verification. Verification
produces a record of what was actually exercised. Include a short decision
list with scoped working choices, unresolved questions, owners, and review
triggers; do not create a parallel backlog when one already exists.

End with what works, what remains unverified or blocked, and the specific
team decisions needed for this work. Explain the most useful next action
without implying that the whole organization must be redesigned first.

This skill establishes an AI-assisted website workflow. Full system health
inspections, product migrations, native rendering, runtime generative UI,
and organization-wide monitoring are separate work. Reuse evidence from
other skills when available; none is a prerequisite for completing this one.
