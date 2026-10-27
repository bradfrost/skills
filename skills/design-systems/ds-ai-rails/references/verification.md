# Verify the workflow

Choose a small representative page or flow in an authorized sandbox. Agree
on scope and time/usage budget, reusing authorization already given. Include
a common component, a meaningful interaction, an existing composition when
appropriate, and an intentionally uncovered requirement. A pilot is useful
when it can show both a successful path and how a gap is handled.

## Evidence to collect

| Question | Exercise | Limit to report |
|---|---|---|
| Is this the real implementation? | Trace rendered regions to actual package/local-library exports and resolved versions. Check imports are used and look for local imitations, copied implementations, and unauthorized overrides. | An import or visual resemblance alone is insufficient. Report what the available inspection could not detect. |
| Are APIs and tokens real? | Check names, properties, slots, events, variants, and token references against the matching source. | A correct declaration may still conceal a behavior defect. |
| Does it work? | Render and exercise required states, keyboard/focus behavior, responsive layouts, links/forms, and applicable accessibility/performance checks. | Static checks do not prove runtime behavior; automated accessibility checks do not establish complete conformance. |
| Does it follow system guidance? | Compare composition, content, and interaction decisions with the working policy and intended use. | Model review is supporting evidence, not an independent guarantee. |
| Does it serve the user? | Review the actual task, usability, content, and design quality with a human. | System compliance does not establish good design. If review has not happened, say so. |
| Does a gap follow its route? | Present the uncovered requirement; observe lookup, classification, proposed destination, and behavior under the current policy. | A draft is not filed or accepted; a provisional agreement is not settled policy. |
| Do the controls work? | Run a known-valid case and relevant deliberate violations; inspect the actual merge/release controls where accessible. | Local detection is not release enforcement. Never merge broken work to test a gate. |

For each control, report **advisory** (instructions only), **detecting**
(observed violation caught), **blocking** (observed mechanism prevents the
specified action), or **unverified**. Name the surface and path covered,
including known bypasses. A passing CI job does not establish that the
branch requires it.

## Check the checking machinery

Use fixtures in a temporary or approved test location; do not contaminate
production output. Choose the cases relevant to this environment:

- A legal nested composition and optional property usage should pass.
- A fabricated property or token should fail its API check.
- A prohibited local imitation should be caught by a provenance/policy
  check, or remain an explicit detection gap.
- A nonexistent component should yield honest absence.
- An empty, stale, wrong-version, or sample-data source should not count as
  healthy system access.
- Loss of a required source should invoke only a permitted adequate fallback
  or pause affected implementation.
- A scoped exception should apply only inside its scope and review period.
- A new pattern with no primitive gap should follow its allowed composition
  path instead of forcing an unnecessary core-component proposal.

If valid use fails, investigate metadata or validator behavior. Do not
distort a legal product implementation or loosen checks just to get green.
Keep failure evidence and route the defect. Correcting a faulty check is
appropriate when supported by the authoritative API and a regression case.

## Repetition and comparison

For an initial repeatability sample, propose three fresh sessions per
claimed AI environment, within the agreed budget. Use the same brief and
record model/tool versions, policy revision, system version, output,
interventions, failures, and elapsed work where measurable. Three is a
starting sample, not a statistical guarantee or a requirement to spend more
than the user authorized.

If only one run or one surface is available, report exactly that. Do not
simulate independent sessions by rereading the same answer. A before/after
comparison can help, but changing models, prompts, and tool access together
does not isolate one guardrail's effect. Record those differences.

Where supported and safe, a controlled theme or dependency change can add
evidence that the product remains connected to the system. Recheck relevant
fixtures after meaningful system, model, tool, policy, or integration
changes. Keep successful fixtures as regression cases and remove redundant
guidance when observed results support it.

## Stop at a useful boundary

Use a bounded repair budget appropriate to the exercise; two repair attempts
is a reasonable proposal for a small pilot. Continue only while the work is
authorized and producing new evidence. On repeated failure, retain the
reproduction, route the defect, and finish the useful independent checks.

Without runtime access, render and behavior remain unverified. Without
release-control access, release enforcement remains unverified. Without a
team decision, the affected policy remains unresolved. These limits belong
in the result, not behind a green overall label.
