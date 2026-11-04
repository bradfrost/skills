# Set up the agreed path

Start from the current assessment, user authorization, and working policy.
Make the smallest useful changes that address observed weaknesses. Preserve
the existing delivery process, instructions, working tools, and unrelated
settings. Use the system's actual names and APIs in generated instructions.

## Prepare concrete changes

For each change, name its target file or setting, scope, rationale, owner
or required role, activation step, verification, and rollback. Distinguish
prepared, applied, activated, and verified states. If permissions or a
connector are missing, produce a usable patch or precise setup instructions
and continue independent work. Never label the change active merely because
its instructions were written.

Common changes, only where the assessment justifies them:

| Observed gap | Useful change |
|---|---|
| The agent follows generic UI guidance | Add a small, scoped adapter pointing to the maintained policy and sources. Explain conflicts using the host's actual instruction rules. |
| Real dependencies do not load | Fix the approved package/import/style/asset integration for the existing stack and prove a component renders. |
| The agent cannot reach system knowledge | Configure an available, approved access path; probe from the consuming surface. Identify external access changes that require another role. |
| It invents APIs or misses patterns | Add version-aware lookup and intent-based discovery steps; improve the maintained source rather than copying its catalog into the skill. |
| A known violation escapes checks | Extend the relevant existing validation with both legal and illegal fixtures. Describe the detection boundary. |
| Checks run but do not gate release | Document or configure the agreed release control within authorization. Verify enforcement separately from a local test result. |
| Gaps disappear into chat | Connect the existing tracker and contribution process, or prepare complete drafts with destinations. |

## Instructions that future agents can actually follow

Maintain one policy source where practical and small adapters for each
surface. Each adapter should identify:

- Where to read the current policy, including provisional scope and review
  triggers, and which sources supply the consumed-version APIs and intent.
- When to perform lookup: before mapping or generating in-scope UI, and
  after meaningful changes to versions or access.
- How to discover suitable compositions and check their permitted freedom.
- How uncovered needs are classified and routed, including the affected-work
  stopping condition when no authorized solution exists.
- Which real commands/tools validate output and what still needs browser or
  human review. Use known commands, not plausible command names.
- What evidence to present and where product learning belongs.

Generate runnable instructions only after resolving their references. Mark
missing destinations and commands as unresolved rather than leaving a
finished-looking adapter with invented tools. You can prepare an inactive
draft from available evidence; identify the references that must be resolved
before activation. A provisional choice belongs
in its agreed pilot/project scope; do not install it as a global default.

Subagents and cloud agents may have different instructions, credentials,
and tools. Arrange the handoff within the available platform, then test it
before claiming the same coverage. A file in a dependency package does not
establish that any agent loaded it.

## Preserve useful deterministic work

Let an agent invoke fixed-code exporters, transformations, and checks.
Avoid replacing them with model interpretation. Record determinism only for
the operation that provides it, not for the entire generation workflow.

Use hooks and CI where supported and appropriate. Do not invent a universal
hook format or promise enforcement on surfaces that only support prose.
Agree on a bounded repair budget for verification; retain evidence and route
unresolved failures rather than weakening checks or growing instructions
indefinitely.

## Close the setup with evidence

Run the relevant exercises in [Verification](verification.md) within the
agreed scope. Show the concrete diffs, activation status, successful checks,
failed checks, and what remains unverified. Explain required maintenance,
hosting, or paid access when known. Preserve a rollback path for changed
settings. Do not merge, publish, deploy, or message people merely because
setup checks passed; use the authorization and process for those actions.
