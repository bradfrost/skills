# Reuse policy and uncovered needs

Help the team decide how its system should be used when AI is doing the
assembly. This may expose questions they have not settled yet. That is a
useful outcome, provided people can see what is decided, what is provisional,
and what still needs discussion.

## Separate reuse posture from the gap policy

Start with existing rules. These choices describe reuse posture, not a
complete governance model:

| Posture | Meaning |
|---|---|
| Prefer the system | Discover and use suitable existing assets first. Custom UI still needs a reason and a permitted route. |
| Require reuse within a defined scope | Require named concerns such as controls, typography, tokens, or particular flows. Explicitly name the remaining freedom. |
| Use the approved ecosystem exclusively | All in-scope UI uses approved implementations and permitted compositions. An uncovered need needs an approved solution or exception before it is implemented. |

Define the approved ecosystem: foundations, core components, supported
adapters, product-owned compositions, permitted third-party assets, and
approved exceptions. Clarify ordinary semantic HTML, layout glue,
application logic, content, and media. Otherwise “only use the system” can
accidentally prohibit assembling a page at all.

Decide composition freedom separately. Using real inputs and buttons in a
new filter bar may be allowed while inventing a new input is not. Some
flows may require a page template; others may allow flexible layouts. A
recipe is not a loophole for hiding replacement primitives inside a wrapper.

React, Tailwind, or any other technology may already belong to the approved
system. Their names alone do not make them valid or invalid. What matters
is the organization's actual implementation and permitted boundaries;
missing coverage is not authorization to introduce a different stack.

## When the team has not decided

Do not force a final organization-wide decision to complete an assessment.
Offer a concrete working agreement for the current scope, using existing
rules and the user's authority. Identify choices that need a system owner,
product owner, or other decision-maker without inventing who those people
are. Preserve permissions already granted in the conversation; do not ask
for the same decision again.

If no policy exists, a useful starting proposal is: reuse verified assets,
compose them within documented extension points, and route new primitives,
overrides, and external dependencies for a decision. This is a proposal,
not an automatically adopted restriction or grant. During assessment you
may use it as an explicitly labeled assumption. Before dependent setup or
implementation, establish an authorized working choice. Covered work and
independent assessment can continue while that choice is pending.

Use these statuses:

- **Settled:** supported by an existing organizational decision; cite it.
- **Provisional:** an authorized choice for a named pilot, product, or
  period, with a review trigger. It does not silently expand to other work.
- **Proposed:** a recommendation awaiting a decision; it grants no permission.
- **Unresolved:** no agreed route yet; state which work it affects.

Keep the conversation concrete. Ask only the questions the evidence cannot
answer, for example:

> For this pilot, are new sections composed from existing components and
> tokens allowed, while new primitives wait for the system owner? That lets
> covered work continue while your team settles its extension policy.

> When a product-specific need cannot be composed from the system, should
> it live locally under a named owner, enter a shared contribution process,
> or wait? A temporary exception can have its own scope and removal plan.

Recommend a route based on the need and the organization's evidence. Do not
reduce the choice to “stop everything” or “build anything.” The user should
finish with a short decision brief they can discuss with the team: the real
example, viable options and tradeoffs, the current working choice, its
limits, the decision owner or missing ownership, and when to revisit it.

## Route the actual need

Check the installed-version catalog, usage guidance, related components,
and existing compositions first. A retrieval failure is not proof of a
missing component. Then propose the appropriate route:

| Finding | Route and boundary |
|---|---|
| An existing solution was hard to find | Use it and route a documentation or discovery improvement. |
| An existing component is broken | Give its owner a reproduction. A workaround needs a separate permitted scope. |
| Design, code, and guidance disagree | Establish authority for the disputed concern; route drift or an intentional product difference to its owner. |
| A new composition uses existing ingredients | Put it in the agreed product or shared-pattern location with ownership. Do not create a new package merely to call it a recipe. |
| A new primitive or variant may serve several products | Prepare a core contribution proposal. The owning team decides acceptance and release. |
| The need belongs to one product | Use an approved local extension route with boundaries, tests, and maintenance ownership; otherwise propose that route. |
| A sanctioned external library fits | Record its approval, integration boundary, token/accessibility expectations, and owner. Do not silently install it because it is familiar. |
| An experiment or deadline requires a temporary exception | Record authorization, scope, review date or trigger, exit conditions, and any upstream dependency. |
| A required capability or source is unavailable | Record the access/tooling blocker. Use an allowed adequate fallback or pause dependent work. |
| No route is authorized | Present concrete alternatives and pause the affected portion. Keep independent covered work moving. |

Check the existing tracker before preparing a new request. For every
unresolved need, preserve the user need, evidence, solutions checked,
category, affected scope, proposed destination, owner or unresolved
ownership, status, and next decision. Do not send messages or file requests
without authorization; a complete draft is still useful.

Temporary implementations also need the approval evidence, limits,
review/expiry conditions, and removal, migration, or renewal plan. An
expired exception returns to a decision; it does not renew itself. Repeated
use can justify a shared contribution proposal, but does not promote it
automatically. A filed request is not accepted, accepted is not released,
and released is not adopted until the consuming product uses it.

These distinctions draw on the [design system ecosystem](https://bradfrost.com/blog/post/the-design-system-ecosystem/)
and [governance categories](https://bradfrost.com/blog/post/design-system-governance-bugs-design-discrepancies-features-and-recipes/).
Use the receiving organization's terminology and process.
