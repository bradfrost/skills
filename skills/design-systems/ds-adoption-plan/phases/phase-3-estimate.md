---
phase: 3
name: Estimate
question: What does each mapping cost — and what's the basis for that number?
output: effort column + basis notes folded into ds-adoption-plan/MAPPING.md
---

# Phase 3 — Estimate

Price the parts list. Every mapping row gets an effort grade **with its basis stated** — never vibes. The grades feed phase 4's wave ordering, and they're what makes the plan an *estimate* instead of a wish.

## The scale

**S / M / L** (+ XS for deletes), the same scale the kit's work orders use:

- **XS** — delete or one-line change
- **S** — ≤ half a day: one template or partial, a `[verified]` direct target, no behavior
- **M** — a day-ish: several templates, a composition with slot contracts to get right, or a partial with many consumers
- **L** — multi-day: touches stored content at scale, carries behavior migration, or requires a build-time transform

Hard time quotes are optional; if the team wants them, attach a range to each grade in GARAGE.md's frame and keep the grades primary.

**Rows carry two grades: code and design.** Most adoption rows need work on both sides, and the two rarely cost the same. Re-attaching a detached instance is XS in the design file and nothing at all in code; a stored-content transform is L in code and nothing at all in design. Grade them separately (`M / S`), use `—` where a side has no work, and roll them up separately. A single blended grade hides which discipline is actually on the hook, which is how design work ends up unscheduled and unstaffed.

## The basis: four factors, stated per row

1. **Instances** — how many times the pattern appears (teardown counts).
2. **Templates touched** — a partial powering 8 routes is one edit with wide blast radius (cheap); a pattern baked into 700 stored posts is a transform project (expensive). This factor dominates.
3. **API distance** — Swap with matching props < Compose with slot contracts < composition plus behavior delta. A `[reported]` (unverified) target adds distance: budget verification time.
4. **Behavioral risk** — states, focus management, dynamic content, anything with JS. Visual-only patterns are cheap; behavioral ones aren't.
5. **Design distance** (the design grade's dominant factor) — re-attaching an instance to its library component is XS. Rebuilding a local component on library parts is S. Designing something that doesn't exist yet, because the row is a system gap or a recipe candidate, is M or L and it blocks the code work behind it. A row whose design target is "no counterpart" is always at least M, because somebody has to design the thing before anybody can build it.

Grade honestly against the dominant factor: a trivial component swap inside 700 markdown files is **L** no matter how simple the target. A gnarly-looking composition confined to one partial is **M** at most.

## Blocked rows

System-gap and upstream-blocked rows get an effort grade for the *local* work once unblocked, plus the blocking issue link. Their timing belongs to phase 4's gap-blocked wave — don't average them into the executable waves.

## Sanity checks before finishing

- Do the S rows outnumber the Ls? Usually they should — if everything graded L, the mapping may be missing intermediate compositions (or the teardown missed leverage like shared partials).
- Does any L hide a scriptable transform? Bulk stored-content work is L as hand-editing but often M as a build-time transform + verification script. Prefer the transform and say so in the basis.
- Is anything graded on an unverified target? Flag it — verification is the first task of its wave.

## Output

Fold into `MAPPING.md`: an **Effort** column per row carrying both grades (code / design), basis noted where it isn't obvious, and a one-line roll-up per group ("Styled patterns: 9 rows — 5 S, 2 M, 2 blocked; design side: 4 rows, 3 XS and 1 M").
