---
station: 2
name: Best practices
quality: Sound (quality 2 of 10)
question: Does the product do the standard technical things right — responsive across devices, deliberate interaction states, graceful failure, and clean web-platform hygiene?
---

# Station 2 — Best practices

**Quality: Sound.** This is the catch-all for table-stakes technical correctness — the things a competent product just *does*, the way [Lighthouse's **Best Practices** category](https://developer.chrome.com/docs/lighthouse/best-practices/) bundles console errors, image sizing, viewport, and deprecated-API checks into one "are the fundamentals in order?" score. It's the product-side rhyme of `ds-inspection`'s **Best practices** station: do the assets embody industry and format best practices? None of these dimensions is a headline on its own — but skip enough of them and the product feels broken in a dozen small ways. Three sub-areas, each scored, rolled into one light.

Deliberately *not* here: accessibility (Station 3), performance (Station 7), and deep security (Station 8) each earn their own station. Best practices catches what's left — the general hygiene those specialized stations don't own.

## 2a · Responsive & cross-device

Designs are drawn at a comfortable desktop width; users show up on phones, tablets, split-screen windows, zoomed-in browsers, and touchscreens.

- **Breakpoints:** walk the core flows at ~360px (phone), ~768px (tablet), and desktop. Layout reflows sensibly at each — not just shrinks or clips.
- **Horizontal overflow:** the classic break. Any element forcing sideways scroll at narrow widths is a flag — find the offender (fixed widths, unwrapped tables, oversized media).
- **Touch ergonomics:** tap targets comfortably thumb-sized (~44px), adequately spaced, and — critically — **no action available only on hover** that a touch user can't trigger.
- **Zoom / reflow to 200%:** text reflows to a single readable column, nothing clipped or lost. (Also a WCAG requirement — cross-links to Station 3.)
- Establish the target range from real usage: pull the audience's actual device/viewport mix from analytics if reachable; otherwise ask. Score against *their* range.

## 2b · Interaction states & resilience

The happy path is the easy 20%. Real products live in the other states, and real conditions are hostile.

- **The four states, per async surface:** **loading** (a deliberate skeleton/spinner, not a blank flash), **empty** (a designed first-use state that orients, not a bare region that reads as broken), **error** (caught and actionable, not silent/raw/hung), **success** (confirmation; control disabled mid-submit to prevent double-submit).
- **Under stress:** bad/empty/oversized/malformed input into forms — validated with clear guidance, or does it break? Network offline mid-flow — does it detect, tell the user, **preserve entered data**, and allow retry, or hang and lose the form? Boundary data (zero items, hundreds, very long strings) — overflow, layout breakage, performance cliffs?
- **Failure surfacing:** errors reach the *user* as actionable messages — not only the console, and never a raw stack trace or leaked internal.

## 2c · Web-platform hygiene

The Lighthouse-style fundamentals a healthy page just gets right.

- **No console errors** on load or during core flows (uncaught exceptions, failed requests, framework warnings).
- **Valid, semantic markup:** a doctype, a declared charset, no `div`-soup where semantic elements belong, no duplicate IDs.
- **Images sized right:** correct aspect ratios (no squished/stretched), not a 3000px file served into a 300px slot.
- **No deprecated or broken APIs;** no libraries with known issues used for core behavior (deep dependency-vuln audit lives in Station 8).
- **Transport basics:** HTTPS with no mixed content (the deeper header/CSP review is Station 8).

## Warning lights

- Horizontal scroll at common phone widths; fixed-width elements, unwrapped tables, hover-only affordances
- Content clipped or lost at 200% zoom; tap targets too small/tight
- Blank screens or layout jumps standing in for loading; empty states that read as errors
- Silent failures, raw stack traces to users, work lost on a dropped request, double-submittable actions
- Console errors on core routes; missing charset/doctype; squished or oversized images; deprecated APIs

## Scoring anchors

- **Red (0–3):** Fundamentals broken — core flows unusable on common devices, only the happy path exists, failures are destructive or silent, console throwing errors.
- **Yellow (4–7):** Works, with rough edges across the sub-areas — a hover-only control, a table that overflows, a missing empty state, an unvalidated input, some console noise.
- **Green (8–10):** The team can honestly say: *"Core flows work across the devices our users bring, every surface handles loading/empty/error/success, bad input and dropped requests fail gracefully, and the page is free of console errors and platform-hygiene misses."*

## Turning off the light

- Overflow offenders are usually a short list of fixed-width elements and unwrapped tables — an agent can find every one; wrapping/reflowing is mechanical. Replace hover-only affordances with tap-and-focus equivalents (doubles as an a11y fix).
- Build the state inventory as a grid (surface × loading/empty/error/success) — the holes are the punch list. Empty and error states are often the highest-value, lowest-effort wins.
- Client-side validation with inline guidance, and preserving form state across failures, are small and disproportionately trust-building.
- Console errors and image-sizing misses are mechanical; wire them into the same CI check as the a11y/performance gates (Station 9).
- If reflow or state patterns trace to the design system's own components, file upstream — but most of this is composition, which is the product's to fix.

## Station record

```markdown
### Station 2 — Best practices: <RED|YELLOW|GREEN> (<n>/10)
- Responsive: <widths checked, overflow?> · States: <loading/empty/error/success hit-rate> · Hygiene: <console/markup/images/APIs>
- Evidence level: <live / screenshot / code / interview, per check>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
