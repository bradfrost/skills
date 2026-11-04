# Research basis for ds-ai-rails

Research snapshot: October 22, 2026. Supports the [approved specification](ds-ai-rails.md), now implemented as [ds-ai-rails](../../skills/design-systems/ds-ai-rails/SKILL.md). This is a requirements synthesis, not a benchmark of current AI products or evidence of runtime enforcement.

## What the broader research changes

### October 25 addition: State of AI in Design Systems

Brad requested that the skill incorporate Kaelig Deloumeau-Prigent's
[techniques resource](https://state-of-ai-in-design-systems.netlify.app/techniques.md).
The retrieved edition describes 165 techniques in 11 categories, with data
collected July 26–28 and generated September 21, 2026. Its CC BY 4.0
attribution and dated scope are retained in the new
[techniques reference](../../skills/design-systems/ds-ai-rails/references/techniques.md).
The index and selected passages in the validation, prohibition, tool-gating,
exemplar, and scaffolding category files informed this addition. The category
map is adapted into assessment questions; it is not copied as a compliance
checklist or treated as proof of effectiveness.

The [Kaelig AI & Design Systems podcast composition](https://web.descript.com/62505a7e-6d3d-43d0-81e8-559315eac0ed)
was exported read-only and relevant passages reviewed:

- **14:58–18:20:** distinguish official/community availability and unknowns;
  inspect how a capability works instead of recording its presence alone.
- **22:17–24:52 and 33:26–38:59:** fit techniques and peers to the team,
  framework, and actual consumer experience. Not every team needs every tool.
- **1:08:31–1:12:43:** reconcile conflicting foundations before expanding
  AI access, assign ownership, and test effectiveness over time.
- **1:13:07–1:17:57:** combine practical heuristics with external evidence
  and carry actionable findings into the team's maintained workflow.

Two upstream references were also inspected:
[Mantine's custom-component skill](https://raw.githubusercontent.com/mantinedev/skills/HEAD/skills/mantine-custom-components/SKILL.md)
provides a concrete example of an extension that retains system integration;
[Atlassian's context-delivery evaluation](https://www.atlassian.com/blog/how-we-build/atlassians-design-md-is-here-what-we-learned-testing-portable-design-context-in-practice)
motivates comparing outcomes rather than assuming a context format improves
reuse. Neither implementation nor any reported performance figure becomes a
universal requirement. The new reference keeps actual reuse, local policy,
measured effects, and maintenance burden as the basis for recommendations.

Brad chose a conversational copy walkthrough for this iteration's dry run.
It does not validate a live consumer environment. Preliminary read-only
inspection of the resources-site file inventory and status was stopped at
that clarification; no consumer files or settings were changed.

### Original course and community synthesis

The rails demo provides a useful sequence. The course provides the larger purpose: AI should help people put their design system investment to work, connect its parts, and improve those foundations through real product work. The community supplies the situations that make a generic skill difficult: mixed tool access, fragmented documentation, unfamiliar setup, weak pattern discovery, and uncertainty about what “working” actually means.

The resulting skill should establish a usable relationship between an organization's system, its AI environments, and its delivery process. It should leave the organization with a working pilot and evidence when access permits, or a concrete, scoped assessment when it does not. Installing an MCP and writing an instruction file are possible steps in that work.

## Coverage and limits

| Source | Coverage in this pass | Limit |
|---|---|---|
| [Course transcript database](https://app.notion.com/p/34a3c9323e86802ab3ebc1964320d79c) | Enumerated and retrieved all 218 entries; each returned nonempty transcript content. Full text was screened for themes, with selected lessons and passages read closely. | This covers the supplied database snapshot, not a reconciliation against every published video. Not every sentence received equal close reading. |
| [#ai-and-design-systems](https://bradfrost.slack.com/archives/C09TMK7DS7J) | Retrieved eight pages containing 760 channel-history records, from November 13, 2025 through October 22, 2026. Screened for relevant discussions; opened 19 selected discussions, including their 62 replies. | Does not include every reply in the channel, linked attachments, private DMs, or every external article. Community reports are observations, not independently reproduced tests. |
| Jam recordings in Descript | Retrieved 15 substantial transcript exports, plus one short clip excluded from substantive evidence. Located projects by search and by enumerating the jam folder. | Several April projects contain overlapping material and inconsistent titles. Fifteen exports do not mean fifteen distinct sessions. See the recording ledger below. |
| Jam meeting notes | Reviewed October 22 notes and transcript passages; consulted August 13 and September 24 notes/transcripts alongside recordings, plus March 26 notes. | No transcript was located for the March 12 session or September 10 feedback session. Their Slack references establish that the sessions occurred, not their complete content. |
| October 22 workshop | Notes and relevant transcript passages reviewed. | A particular workshop's advice must be adapted to the receiving organization. |
| Rails demo and two blog posts | Demo text, ecosystem article, and governance article reviewed. | The demo's comparison images are placeholders. The course has a separate real footer demonstration. |

The [course index](ds-ai-rails-course-index.csv) preserves all 218 titles, source URLs, transcript lengths, and the database's existing course-link status. It contains no transcript bodies. Chapter counts are 7, 43, 38, 69, 53, 5, 2, and 1 for Chapters 0 through 7 respectively. The database marks 184 entries “matched,” two “needs review,” three “no match,” and leaves 29 unset. Those flags concern course linking; they are not evidence that a transcript is absent.

The screening covered purpose, foundation health, access and context, reuse and composition, validation, governance, and organizational adoption. It included both successful demonstrations and failures. Selected passages in the source map below carry the requirements; keyword matches alone do not establish a conclusion. Repeated lessons or recordings are not independent corroboration.

Private student names, emails, transcript bodies, and attachments are not copied into these artifacts. Discussion links preserve traceability for people who already have access. Historical statements about a product's features or pricing are not turned into current product recommendations.

## Requirements traced to evidence

| Requirement | Source evidence | Consequence for this skill |
|---|---|---|
| Preserve human agency and the value of existing foundations. | [Principles and Our Approach to AI](https://app.notion.com/p/34a3c9323e8681859a0fc379dd635f38); [AI as Mortar](https://app.notion.com/p/34a3c9323e86815c945dc194dfa90afd). | Begin with the team's goal and choices. Establish connections across design, code, documentation, and people. Keep human responsibility for what ships. |
| Treat foundation health and product outcomes as connected. | [Testing & Validation](https://app.notion.com/p/39d3c9323e86818f91d4cc878eb65a63); [danger-button dead property](https://app.notion.com/p/39d3c9323e86816c9c58f1d2c0f65c59); [Selling AI & Design Systems](https://app.notion.com/p/3ce3c9323e86811a9793eb32fa53f139). | Inspect the pilot's ingredients. An API declaration does not prove behavior. Route underlying defects upstream instead of hiding them with more prompting. |
| Map authority by concern across the ecosystem. | [August 13 jam](https://app.notion.com/p/3bb3c9323e8681e8bccbfc266ad6822d); [documentation ownership discussion](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1785944215419489); [Brad's ecosystem clarification](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1776189686867229). | Establish the editorial home, owner, and derived representations for each concern. A unified reference can bring distributed sources together without moving everything into one tool. |
| Separate procedure, changing system data, and access mechanisms. | [October 6 access architecture discussion](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1791284656461069); [agent-access recap](https://app.notion.com/p/39d3c9323e86818ab702ea406b469f5c). | The skill teaches a workflow; it points to versioned system knowledge. Choose files, CLI, MCP, or other access according to the consuming environment. Hosted access can serve people outside the maintainer's checkout. |
| Test usable access, including honest failure. | [Enabled MCP without available tools](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1783612952377529); [sample-data fallback incident and resolution](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1786081069690329). | Connection, tool visibility, catalog identity, coverage, and freshness are distinct checks. A successful tool response can still be inadequate. The incident was reported fixed; retain the failure scenario, not a claim that the service remains broken. |
| Retrieve intent and composition guidance. | [Pattern-contract discussion](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1786359761282749); [experience-level context discussion](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1782909496545519); [October 8 jam](https://web.descript.com/a3aa946b-c364-46fd-abbd-958575fba5e6). | Test discovery from a user problem. Cover required/optional regions, sequence, content, behavior, and degrees of freedom. Pages and patterns can improve reuse without becoming mandatory packages. |
| Carry semantics and accessibility context. | [Context-Based Design Systems](https://app.notion.com/p/3c23c9323e86813e8260edbe7793ded8); [descriptions and accessibility annotations](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1788017821872259). | Include purpose, do/don't guidance, roles, keyboard behavior, focus, state announcements, and interactions where applicable. A property list is only part of the contract. |
| Avoid duplicating knowledge into instruction files. | [Docs and contracts discussion](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1788020132334009); [knowledge graph synchronization lesson](https://app.notion.com/p/39d3c9323e8681cbb940ea10f92c0e75). | Keep narrative guidance linked to technical infrastructure and generate reference from maintained sources where possible. Keep overlapping facts consistent without making every representation identical. |
| Distinguish exploration, system prototypes, and production. | [Prototyping without the system](https://app.notion.com/p/3c33c9323e868157ba16c47b77f12fad); [Prototyping with the system](https://app.notion.com/p/3c43c9323e8681aa9c32d603f8f67150); [Chapter 4 homework](https://app.notion.com/p/3c73c9323e8681d08089e0231f8e7948). | Ask what the work is for. Label mock behavior and permitted deviations. Define promotion criteria before treating an exploratory artifact as production work. |
| Verify real reuse and meaningful quality separately. | [Footer comparison](https://app.notion.com/p/3ad3c9323e86819f8be0ec7cd93c45fe); [Steel Curtain](https://app.notion.com/p/3c73c9323e868154bc3efd05e4c47b29); October 8 jam's three kinds of evaluation. | Check runtime provenance and behavior, assess system adherence, and retain human judgment of usability and craft. The footer uses real ingredients while still needing visual refinement. |
| Test the checking machinery. | [False-positive slot validation and inaccurate metadata](https://app.notion.com/p/39d3c9323e868107bd4cfc4d9438bb20); [deterministic and agentic testing](https://app.notion.com/p/39d3c9323e8681b8904dc16ec4fe5a2d). | Include both known-valid and known-invalid fixtures. Correct the validator when it rejects legal use. Do not equate green checks with good coverage. |
| Preserve deterministic operations and measure repeatability honestly. | [Token-export consistency discussion](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1781867573969459); [How do you know it's working?](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1791900590323079). | Distinguish fixed-code transformations from model decisions. Record repeated outcomes and corrections. Do not use “feels better” as the only evidence. |
| Fit organizational access and people's working environments. | [Selling AI & Design Systems](https://app.notion.com/p/3ce3c9323e86811a9793eb32fa53f139); [enterprise API-key restriction](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1785447848915409); [prototype tool and setup discussion](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1776774522751709); May 7 jam. | Work within approved environments. Separate required capabilities from particular vendors. Make setup steps understandable and identify who can perform them. |
| Route unmet needs and preserve the feedback path. | [Keeping Product on the Eddie Rails](https://app.notion.com/p/3ad3c9323e86811bbdc9ed6d0ce78d27); [pattern exploration with gap analysis](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1769656600575459); [governance article](https://bradfrost.com/blog/post/design-system-governance-bugs-design-discrepancies-features-and-recipes/). | Route discoverability, bugs, discrepancies, features, compositions, and exceptions separately. Track draft, filed, accepted, released, and adopted states. Product experiments can expose useful system needs without automatically approving additions. |
| Keep the setup proportionate and adaptable. | [October 22 workshop](https://app.notion.com/p/4013c9323e8681a2aea7cf401514c0b8); October 8 jam's discussion of simpler guidance and organizational decisions. | Start with a representative pilot. Improve demonstrated weaknesses. Do not require a large agent architecture, a new MCP server, a bespoke contract system, or every possible check. |

## Tensions the spec must preserve

**Actual reuse and creative freedom are separate decisions.** A team can insist on its real components while leaving composition flexible. A template may improve consistency but be a poor fit for a particular task. The skill should establish the organization's desired boundaries and test the outcome. It should not assume that more prescription always produces better design.

**The ecosystem has several maintained sources.** Some demonstrations start from design; others start from code and mirror into design. The [September 24 jam](https://app.notion.com/p/3e53c9323e86813c93f6fa25c4e61542) shows the latter and discusses layout translation difficulties. Neither example establishes that all organizations should adopt the same direction. Authority needs to be clear for the decision in dispute.

**Structured contracts are promising, with unsettled implementations.** The July 16 and October 8 jams explore contracts, cross-platform representations, and pages as data. The October discussion explicitly describes unsolved problems. Version one should consume existing contracts and identify missing semantics; it should not require an experimental standard or attempt universal design-to-code transpilation.

**A demonstration is evidence with a scope.** The footer lesson changes both the agent environment and access to context. It demonstrates the difference between custom output and actual system reuse, but cannot quantify how much improvement one specific intervention caused. The spec's proposed repeatability exercise is new evaluation design, not a result already established by the course.

**More capable models do not eliminate organizational decisions.** The October 8 discussion questions elaborate agent infrastructure while reinforcing the importance of local do/don't guidance. The spec should favor clear intent, retrievable facts, and useful checks, then add orchestration only where it earns its maintenance cost.

**The full course is wider than version one.** Chapter 5's generative UI and hyperpersonalization lessons argue for reusable, accessible, well-defined ingredients. They inform the capability model and future extensions. Runtime generation and native rendering need separate pilots and validation; they are not verified by a website-development exercise. Chapter 6 supports sanctioned pilots and organizational adoption. Chapter 7's evolving outlook supports revisiting the setup as tools change.

## Recording ledger

These are retrieved source artifacts, not a deduplicated count of meetings. Selected relevant passages were reviewed across the exports. The primary edited composition was used where there were multiple compositions; this does not cover every word removed from the original recording.

| Recording | Treatment |
|---|---|
| [Course Jam Session #1](https://web.descript.com/ac83f067-4a03-406c-b20b-2d9ca0ff5da8) | Full transcript export retrieved; context, quality, and connected assets. |
| [Jam Session #3](https://web.descript.com/c4c017c1-76e1-4f59-98b6-c9a532eb0ef4) | Full export retrieved; metadata and design intent. March 26 notes provide additional context. |
| [Jam Session #4](https://web.descript.com/26f11378-45e9-4afe-8481-18db41f1077f) | Full export retrieved. Substantial overlap with the next two exports; not treated as independent evidence. |
| [Jam Session, 4-9-2026](https://web.descript.com/5ba8986c-9d39-4d77-89dd-3d3ab1ad9dca) | Full export retrieved; overlaps #4's system-tool and workflow discussion. |
| [Jam Session #5, titled April 7th](https://web.descript.com/826cd878-c2ad-4239-990c-6631bc83c314) | Full export retrieved; overlapping material and uncertain title/date mapping. No session date inferred from the title alone. |
| [May 7](https://web.descript.com/7c3c654f-973e-4f3a-8280-6bc7e8e492e7) | Full export retrieved; DESIGN.md, actual systems, and preparing foundations under restricted access. |
| [May 21](https://web.descript.com/aa1aa91b-36fc-4172-8de8-e00d80d56635) | Full export retrieved; localization, asset synchronization, guidance, and collaboration. |
| [June 18](https://web.descript.com/bebbb103-1bf5-449a-94fc-8d6f527bbe3d) | Full export retrieved; actual package availability and compositions. |
| [July 2 project](https://web.descript.com/214fd90e-4f97-40a3-986d-62bb3b58b45e) | Full export retrieved. Composition is named “June 3”; preserve that discrepancy rather than infer a date. |
| [July 16](https://web.descript.com/2cffed5a-dd3a-48ca-b553-3371234e297a) | Edited transcript retrieved; contracts and design/code consistency. |
| [July 30](https://web.descript.com/3ef135f6-bf7f-47e1-9e33-0ed3a22ee14a) | Full export retrieved; reusable governance rules, checks after generation, and human interpretation of failures. |
| [August 13](https://web.descript.com/f14f7fe9-aa05-46cb-8374-f52d096b25f6) | Full export plus Notion notes retrieved; distributed authorship and unified discovery. |
| [August 27](https://web.descript.com/bfe1e7ac-491e-4914-a995-0c90cd1f5671) | Full export retrieved; AI-use limits and personalized accessibility. Personal limits are not imported as universal design-system policy. |
| [September 24](https://web.descript.com/e3de8db0-f2fd-43e3-9568-372bc6aed15a) | Edited export plus Notion notes retrieved; code-to-design workflow, parity, and evaluation. |
| [October 8](https://web.descript.com/a3aa946b-c364-46fd-abbd-958575fba5e6) | Edited export retrieved; contracts, pages, proportional tooling, and three kinds of evaluation. |
| [October 22](https://app.notion.com/p/4013c9323e8681fbb08bddc43d032967) | Notion notes and transcript passages reviewed; actionable inspection, usage intent, and designer access. |
| [March 12 announcement](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1773687929838569) | Recording link located in Slack; full transcript not located in the searched sources. |
| [September 10 discussion](https://bradfrost.slack.com/archives/C09TMK7DS7J/p1789068321757959) | Slack replies describe a course-feedback session and link its FigJam. Full transcript and FigJam feedback were not reviewed. |

The 51-second “AI-Driven Design System Jam Session” project is a short clip, not a full session. Unrelated conference recordings and the January meet-and-greet were not treated as course jam evidence. No private transcript corpus was copied into the repository.

## Proposed decisions, distinct from the source material

The name `ds-ai-rails`, assess/setup/verify modes, three reuse-policy choices, artifact formats, exception record, and three-fresh-session pilot are proposed design decisions. They are informed by the sources but are not quotations or settled course doctrine.

The skill needs evaluation in contrasting real environments before it can claim verified portability. Its first useful release should assess, configure, and verify one path from a real system to a real website, while giving every uncovered need an honest destination. The approved specification has now been turned into a skill and supporting reference files; implementation validation is recorded separately from this research. This research pass did not install tooling, alter external settings, publish community material, or establish that its acceptance scenarios had passed.
