# Reaching the design library

What you can actually see in Figma, per bridge, and what to do when you
can't see anything. No bridge gets to look more capable than it is.

> **This file is duplicated, on purpose.** Identical copies ship inside
> `ds-inspection`, `product-inspection`, and `ds-adoption-plan`, because
> skills install as standalone folders and any one of them may be the only
> one you installed. `ds-inspection`'s copy is canonical. If you edit one,
> sync the other two.

Probed against a live account on 2026-09-08. The capability rows come from
each server's own tool contracts. Re-run the probe below against your own
setup rather than trusting this table blindly.

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
| Read variables, styles, and token values | **Live** (`get_variable_defs`) | **Live** (`figma_get_variables`, `figma_get_token_values`, `figma_get_styles`) |
| Score the library's health in one call | **None** | **Live** (`figma_audit_design_system` scores naming, token architecture, component metadata, accessibility, consistency, and coverage) |
| Check one component's design against its code | **Partial** (`get_code_connect_map`, where Code Connect is set up) | **Live** (`figma_check_design_parity` returns a parity score plus fix items for both sides) |
| Find detached instances and off-library styles | **None** | **Live** (`figma_execute` runs Plugin API code across the file) |
| Read component descriptions and metadata | **Live** (`get_metadata`) | **Live** (`figma_get_component_details`) |
| See what changed since last time | **None** | **Live** (`figma_get_design_changes`) |

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

**Permission and seat limits are not settled here.** Figma seats vary
(Full, Collab, View) and this doc does not claim which capabilities each
one unlocks, because that hasn't been verified. If a call fails on
permissions, `whoami` on the native server reports the account's plans and
seats, which is the fastest way to see what you're actually working with.
Say what failed rather than guessing at why.
