# Design System AI Rails: validation record

Date: October 22, 2026. Scope: the standalone [ds-ai-rails skill](../../skills/design-systems/ds-ai-rails/SKILL.md), its repository documentation, and its inclusion in the distributable skill collection.

The skill is implemented and packaged. Structural checks and three offline behavior scenarios passed. It's important to say that these exercises do not establish reliable behavior against a live design system or enforcement in a particular AI environment.

## Structural and packaging checks

- The skill-creator validator accepted the skill's frontmatter and naming.
- Every relative reference resolves inside the skill folder. No private workspace path, bf-brain dependency, unfinished scaffold, or trailing whitespace was found in its files.
- The existing OpenAI packager verified all 16 skills in the collection, including all seven files belonging to ds-ai-rails. Research documents are excluded from the archive.
- The existing Codex installer discovered all 16 skills using a temporary destination. This did not install the skill into anyone's active AI configuration.
- `git diff --check` passed.

Commands used from the repository root:

```sh
python3 /Users/brad/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/design-systems/ds-ai-rails
python3 scripts/package-openai.py --output dist/brad-frost-skills-1.0.1.zip --version 1.0.1
python3 scripts/install-codex.py --dest /tmp/ds-ai-rails-build/discovery
git diff --check
```

The validator location belongs to the author's environment. It is not a dependency shipped with the skill. The archive version identifies this local build; it does not mean a release was published.

## Independent behavior exercises

One separate agent read the skill and handled three supplied fictional scenarios. It received the evidence and requested deliverables, without a prescribed answer. It wrote five artifacts in temporary fixture directories. The main agent inspected every artifact against the evidence and authorization boundaries.

| Scenario and supplied evidence | Observed response | Result |
|---|---|---|
| Harbor: an enabled MCP returns the same unrelated sample component for two real component names and one invented name. Matching local documentation exists, but composition permission, a date-range route, host precedence, and browser/release access are incomplete. Assessment only is authorized. | Rejected the earlier green connection claim, distinguished discoverable tools from useful system knowledge, used local evidence only within its coverage, and identified the specific unresolved routes. Did not change settings or build UI. | Passed the offline reasoning check. |
| Fern: a deliberate local-only system has matching v0.8 library guidance, no MCP or design library, and a saved v0.7 checker rejection of a legal nested composition with an omitted optional property. Only prepared instructions and a verification plan are requested. | Accepted local sources as a valid approach, preserved legal API usage, routed the checker discrepancy, and produced explicitly inactive instructions with missing references identified. Did not invent commands, activate settings, or claim release enforcement. | Passed the offline reasoning check. |
| Birch: the product lead has already approved a scoped filter-bar composition until November 5, while an accessible calendar needs a new primitive and has no approved owner or route. Suggestions include unrestricted React/Tailwind or freezing everything. | Applied the existing approval without reconfirmation, preserved its scope and review date, held only the calendar implementation, and offered bounded contribution, extension, integration, or deferral routes. Did not turn the pilot choice into organization-wide policy. | Passed the offline reasoning check. |

The exercises produced a Harbor assessment; Fern proposed instructions, setup record, and verification plan; and a Birch decision record. All were offline documents. No system packages, live services, product UI, or release settings were changed.

One wording ambiguity surfaced: setup guidance allowed preparation while requiring resolved references for runnable instructions. The setup reference now explicitly permits an inactive draft that lists what must be resolved before activation. This clarification was reviewed directly; the behavioral scenarios were not rerun after that wording change.

## What remains unverified

### October 25 update

Added an attributed techniques reference and linked it from the assessment
workflow. Updated artifact guidance to connect recommendations to evidence,
local fit, maintenance, and acceptance exercises. Structural validation,
standalone reference resolution, packaging, and whitespace checks passed
again. The refreshed archive contains eight ds-ai-rails files and all 16
skills. The earlier three behavioral scenarios were not rerun for this
addition. The requested dry run is now a conversational copy walkthrough,
which cannot establish live runtime behavior or enforcement.

These were three scenarios in one evaluator session, not three independent fresh-session runs. Live MCP access, package integration, rendered provenance, interaction and accessibility behavior, validator execution, CI enforcement, cross-host instruction loading, and repeatability remain unverified. No claim about those capabilities follows from packaging or offline reasoning success.

The skill directs its users to gather that evidence in their own authorized environment. Their working policy, scoped exceptions, and actual controls determine what they can trust.
