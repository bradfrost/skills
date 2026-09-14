# Reaching the design library

What you can actually see in Figma, per bridge, and what to do when you
can't see anything. No bridge gets to look more capable than it is.

> **This file is duplicated, on purpose.** Identical copies ship inside
> `ds-inspection`, `product-inspection`, `ds-adoption-plan`, `ds-ascii`,
> `vibe-killer`, and `ds-token-architecture`, because skills install as
> standalone folders and any one of them may be the only one you installed.
> `ds-inspection`'s copy is canonical. If you edit one, sync the other five.

Probed against a live account on 2026-09-08, then corrected against a real
system (Forma 36) on 2026-09-10. The capability rows come from each server's
own tool contracts. Re-run the probe below against your own setup rather than
trusting this table blindly.

## The two bridges

**Native Figma MCP** is Figma's own remote server. You sign in once, then
point it at a Figma URL. Nothing to install, no plugin, no local process.
It works a node at a time, which means you hand it a link to a component or
a frame and it hands you back that thing.

**Figma Console MCP** is a local bridge that runs Plugin API code inside
your open Figma Desktop file. That's what makes whole-file work possible,
which is the difference between "read me this button" and "audit all 400
components." It needs Figma Desktop, a bridge plugin, and a free port.

## What each one gets you

Evidence levels are the same ones the stations use: **live** means you read
the real thing and findings can be tagged `[verified]`; **partial** means
you can get there but only one node at a time; **none** means drop down the
chain to exports, screenshots, or the interview, and tag findings
`[reported]`.

| What you want to do | Native Figma MCP | Figma Console MCP |
|---|---|---|
| Read one component or frame (code context, screenshot, metadata) | **Live** (`get_design_context`, `get_screenshot`, `get_metadata`) | **Live** (`figma_get_component_details`, `figma_capture_screenshot`) |
| Inventory the whole library | **Partial** — node at a time, so you're feeding it URLs | **Live** (`figma_search_components`, `figma_get_design_system_summary`) |
| Read variables, styles, and token values | **Partial** — `get_variable_defs` needs a layer selected in Figma Desktop, so a file key plus node id is not enough on its own | **Live** (`figma_get_variables`, `figma_get_token_values`, `figma_get_styles`) |
| Score the library's health in one call | **None** | **Live** (`figma_audit_design_system` scores naming, token architecture, component metadata, accessibility, consistency, and coverage) |
| Check one component's design against its code | **Partial** (`get_code_connect_map`, where Code Connect is set up) | **Live** (`figma_check_design_parity` returns a parity score plus fix items for both sides) |
| Find detached instances and off-library styles | **None** | **Live** (`figma_execute` runs Plugin API code across the file) |
| Read component descriptions and metadata | **Live** (`get_metadata`) | **Live** (`figma_get_component_details`) |
| See what changed since last time | **None** | **Live** (`figma_get_design_changes`) |

Two Console-side gotchas, both verified on 2026-09-10:

- **`figma_get_variables` with `resolveAliases: true` can return empty
  `resolvedValuesByMode`** when it serves from cache. When you need real
  values, go straight to `figma_execute` and walk `valuesByMode` yourself,
  following `VARIABLE_ALIAS` entries to their target. That also hands you the
  alias *structure*, which is usually the more interesting finding.
- **Don't relay `figma_audit_design_system` subscores as findings.** On Forma
  36 it returned Accessibility 49/100, while computing WCAG ratios from the
  same file's variables showed all four semantic colors passing 4.5:1 on
  white and zero of 67 colors failing against both white and black. The
  subscore is measuring something other than contrast. Use the audit to aim
  your attention, then verify the specific claim yourself before it reaches a
  report.

One trap worth knowing: `search_design_system` searches the *operator's own*
subscribed libraries, not the file key you hand it. Point it at someone
else's system and it will cheerfully return your own components with no
error, which is a great way to report findings about the wrong library.
Check the `libraryName` on every result before you believe it.

**Default: native Figma MCP.** It's the one that works with zero setup, and
zero setup is the only kind that survives a room full of people trying it at
once. Reach for Figma Console MCP when the job is genuinely whole-library
(a coverage inventory, a health audit, hunting detached instances), and
treat it as an upgrade rather than a requirement.

## The four states, and what each costs you

**Both connected.** Use the native server for reading specific components
the user points you at, and the Console server for anything that has to
sweep the whole file. Say which one produced which finding.

**Native only.** The common case. You can verify anything the user can hand
you a link to, which covers most of a station's sampled evidence. Whole-file
claims stay `[reported]`, so scope them: *"the 6 components you linked"*,
never *"your library."*

**Console only.** Whole-file work is open to you and node-specific requests
need the file open in Desktop. Fine, and worth saying out loud that findings
reflect the file as it sits on this machine right now, unpublished changes
and all.

**Neither.** The inspection still runs. Ask for exports (a component list, a
variables export, a screenshot of the assets panel), then screenshots, then
the interview questions the station already carries. It's important to know
what this costs: every design-side finding is `[reported]`, and a station
scored entirely from interview answers about the design library cannot be
recorded as a confirmed green. Note the ceiling in the station record, and
make bridge access the station's first move.

**A connected bridge is not reachable content.** You can be signed in, with
a working server and a valid file key, and still land in the "neither" state.
Verified on Forma 36 on 2026-09-10: the native bridge authenticated fine and
returned nothing usable, because the canonical library needed edit access and
the public Community mirrors expose only a cover page. Probe for *content*,
not for a connection.

### The repo often holds design evidence when Figma doesn't

Before you write off the design side, look for **Code Connect definitions in
the codebase** (`*.figma.tsx` for React, plus a `figma.config.json`). They
record the Figma component's variant property names and how each maps to a
code prop, which means a design↔code naming audit is possible from the repo
alone with no Figma access at all.

It's important to say what that evidence is and isn't. It's first-hand about
the *contract* between design and code, and second-hand about Figma itself,
since it reflects what the mapping's author believed when they wrote it. Tag
findings accordingly: the mapping is `[verified]`, the claim about what the
live library contains today is not.

Two things worth checking whenever you find them:

- **Which file key do the mappings bind to?** If the system distributes its
  library as a Figma Community file people duplicate, a mapping published
  against the internal source file cannot resolve against anyone's duplicate,
  because a duplicate is a new file with new node ids.
- **Do sibling components model the same property the same way?** The same
  concept bound as an enum in one component and a boolean in its neighbor is
  a finding you can make without opening Figma.

## Probe before you promise

One real call, every run, every mode. Don't announce access you haven't
tested.

1. Ask: *"Do you have a Figma or other design library for this system, and
   is a Figma MCP or bridge connected so I can read it live?"*
2. Check your own available tools for anything Figma-shaped. People often
   have a bridge running that you won't notice unless you look.
3. Make one call that returns real content from their actual file. A tool
   existing is not the same as a tool working.
4. Record the result in the access map either way.

## When it breaks

**All ports in use / `EADDRINUSE` (Figma Console MCP).** Stale server
instances hold the 9223 to 9232 range. This happens when sessions
accumulate over a few days, and it's the single most common way this bridge
is silently unavailable. Close the other agent sessions or terminal windows
running the server, then restart. `figma_get_status` names the PIDs holding
the ports.

**Console bridge connected but no file.** The Desktop Bridge plugin has to
be running in the open Figma Desktop file. `figma_get_status` reporting
`transport.active: "none"` means the plugin side isn't up.

**Native server returns nothing for a URL.** It needs a node-specific link.
A file URL with no `node-id` isn't enough; ask for a link to the actual
component or frame.

**Server running on a fallback port, plugin not connected (Figma Console
MCP).** `figma_get_status` shows `serverRunning: true` on a port like 9228,
`portFallbackUsed: true`, and no plugin. The bridge plugin scans port 9223
only, so it never finds a server that fell back. Re-import the Desktop Bridge
plugin in Figma (Plugins → Development → Import plugin from manifest) to pick
up multi-port scanning. One-time fix, and it is distinct from the
`EADDRINUSE` case above even though both end with no transport.

**"You don't have edit access to this file" (native).** Reading a file
through the native bridge needs **edit** access, not view. Verified on
2026-09-10. This is the one that will bite workshop attendees: being able to
open a link in the browser says nothing about whether the bridge can read it.
`whoami` reports the account's plans and seats when you need to see what
you're actually working with.

**A Community file returns only a "Cover" page (native only).** Published
Figma Community files expose almost nothing to the *native* bridge until
they're duplicated. If `get_metadata` lists a single page called Cover,
that's what happened.

**The Console bridge is the fix, and it's a better one than duplicating.**
Verified on Forma 36's Tokens Community file on 2026-09-10: native
`get_metadata` saw one Cover page and nothing else, while the Console bridge,
with the same file open in Desktop, read all **149 variables across 4
collections**. The plugin runs inside the app, so it sees what the person
sitting there sees, Community restrictions included. Duplicating also works,
but it hands you a *different file* with different node ids, which quietly
breaks anything Code Connect touches. Prefer the bridge.

This is the clearest case for keeping both bridges around: it isn't only that
Console does whole-file work faster, it's that Console can read files native
cannot open at all.
