# Token Architecture Report — <System Name>

_Assessed: <date> · Agent: <agent + model> · Previous assessment: <date or "first assessment">_
_Profile: `ds-token-architecture/PROFILE.md` (checked in <date>)_
_Architecture reference: `reference/SUBATOMIC-ARCHITECTURE.md`_

## The short version

<Three to five plain-language sentences: does a real tier ladder exist, where
it holds, where it breaks, and the single most important thing to do next.
Write it for a teammate who reads nothing else. Lead with counts: "Tier 2 is
solid for color (41 tokens, all aliased) and absent for spacing (0 tokens;
14 components hardcode px)." >

**Lights:** 🟢 <n> green · 🟡 <n> yellow · 🔴 <n> red · <n> not inspected

There is no score. Nine lights on a sheet tell the team where to look; a
number out of a hundred tells them nothing they can act on.

## The sheet

<!-- Agent formatting rules:
     1. PAD every cell so the pipes line up. This is read as plain text in
        terminals as often as it's rendered.
     2. One row per check, in order. No extra columns.
     3. The lights below are EXAMPLES. Replace every one with this run's
        real result. A check you could not gather evidence for gets N/I. -->

|  # | Check                              | Light | One line                                              |
|---:|:-----------------------------------|:-----:|:------------------------------------------------------|
|  1 | The tier ladder                    |  🟢   | Three distinct tiers, directory per tier               |
|  2 | References                         |  🟡   | 6 tier-2 tokens carry raw hex                          |
|  3 | Naming                             |  🟡   | Algorithm holds for color, drifts for typography       |
|  4 | Color semantics                    |  🔴   | No knockout pairs; 3 filled surfaces have no content   |
|  5 | Beyond color                       |  🟡   | Typography composite present, spacing tier 2 absent    |
|  6 | Tier 3 discipline                  |  🟢   | 22 tier-3 tokens across 4 components                   |
|  7 | Themes, core, and modes            |  🟡   | Second theme works; no core collection yet             |
|  8 | Tokenized in theory, hardcoded in practice | 🔴 | 71 raw values in 14 of 20 components read       |
|  9 | Build, publishing, governance      |  N/I  | No build reachable this run                            |

**Key:** 🔴 Red: the architecture is broken or absent here; fix now · 🟡 Yellow: drift or gaps; schedule · 🟢 Green: holds; leave it alone · **N/I**: not inspected (no evidence; never guessed)

## Evidence basis

- Access used this pass: <live / export / interview, per source>
- Findings tagged `[verified]`: <n> · `[reported]`: <n>
- Token counts read: tier 1 <n> · tier 2 <n> · tier 3 <n> · core <n> (from
  <which files>)
- Consumers read: <n> components / <n> product files (or none)
- <If reported-heavy: "Most findings are [reported]. Better evidence access
  (see the work order) will make the next run sharper.">

## Check records

<Append each check's completed record here, in order, using the record block
at the bottom of that check's file.>

## What changed since last time

<Re-assessments only: lights that changed, work-order items closed or still
open, token counts then vs now. Delete for a first assessment.>

## Next

- Work order: `ds-token-architecture/work-orders/<date>-work-order.md`
  <!-- If that file doesn't exist yet, you haven't finished the run. A
       prioritized table pasted into this report is not the work order. -->
- Re-check by: <date, or "after the next theme ships">
- Checks worth wiring into CI now: <2 (references) and 8 (hardcoded values)
  are the usual candidates>
