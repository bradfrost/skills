---
station: 7
name: Performance
quality: Fast (quality 7 of 10)
question: On a real connection and device, does the product load and respond fast enough that users don't feel it — or is it heavy, janky, and slow where it counts?
---

# Station 7 — Performance

**Quality: Fast.** Performance is a feature users feel before any other. This station measures the product as delivered — not the dev build on localhost with a warm cache, but payload weight, load milestones, and interaction latency approximating what a real user on a mid-tier device and ordinary network gets. The goal isn't a vanity score; it's whether the core flows feel immediate.

**Reference tool:** [Lighthouse CLI](https://github.com/GoogleChrome/lighthouse) (`npx lighthouse <url> --preset=perf`) is this station's reference instrument — it's open, scriptable, CI-friendly, and produces comparable numbers across inspections. WebPageTest, the browser's own performance panel, or any equivalent counts just as well — the tool is an exemplar, not a requirement. Whatever you use, name the tool, version, and throttling conditions in the findings so the measurement can be re-run.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Load milestones | Lighthouse CLI / WebPageTest on a production-like build, throttled | Pasted Lighthouse report · interview |
| Payload weight | Network panel: JS/CSS/image/font bytes on core routes | Build output / bundle report · interview |
| Interaction latency | Live instance: input responsiveness, long tasks, jank | Performance-panel trace · interview |
| Bundle composition | Repo/build: bundle analyzer — what's big and why | `package.json` deps · interview |
| Images & fonts | Rendered: formats, sizing, lazy-loading, font loading strategy | Network panel · interview |
| Caching / delivery | Response headers, CDN, compression on real responses | Interview |

## Inspection procedure

1. **Measure a production-like build, throttled.** Localhost dev numbers lie (no minification, unbundled modules, no network latency). Run Lighthouse (or equivalent) against a built/preview build or deployed URL with network+CPU throttling. Capture the core-web-vitals-style milestones (first paint, largest content, interaction readiness) and total transfer weight per core route. **If only a dev build is reachable, score what you can `[verify]` (bundle composition, delivery config, code-level signals), mark the load-milestone checks `[reported]`/N-in-part, and put "run a production build" on the work order** — don't score dev numbers as if they were shipped numbers.
2. **Weigh the payload.** Break down bytes by type. Oversized JS is the usual culprit; flag routes shipping far more than they render.
3. **Analyze the bundle.** Run the analyzer: large dependencies, duplicate libs, un-code-split routes, moment/lodash-style heavyweights, an entire icon set imported for three icons.
4. **Feel the interactions.** Type in inputs, open menus, scroll long lists. Watch for jank, long tasks blocking the main thread, layout thrash. Trace the worst offender.
5. **Images and fonts:** modern formats, correctly sized (not 3000px served into a 300px slot), lazy-loaded below the fold; fonts using `font-display` and not blocking render.
6. **Delivery:** compression on, sensible cache headers, a CDN if the audience is distributed.

## Warning lights

- Slow load milestones on throttled/real conditions; heavy per-route transfer weight
- Large or duplicated dependencies; no code-splitting; whole libraries imported for a fraction
- Input lag, jank, long main-thread tasks, layout thrash on core interactions
- Full-size images served into small slots; no lazy-loading; render-blocking fonts
- No compression, poor caching, no CDN for a distributed audience

## Scoring anchors

- **Red (0–3):** Core routes slow to load or interact on real conditions; bloated bundle; visible jank. Users feel the weight.
- **Yellow (4–7):** Acceptable but improvable — a heavy dependency, a missing code-split, unoptimized images, some interaction lag.
- **Green (8–10):** The team can honestly say: *"Core flows load and respond fast on a mid-tier device and ordinary network — measured on a production-like build, not just localhost."*

## Turning off the light

- Bundle analysis usually surfaces one or two big wins (code-split a route, drop/replace a heavyweight dep, tree-shake an icon import) — high leverage, an agent can do most of it.
- Image optimization and lazy-loading are mechanical and often the biggest byte savings.
- Wire [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci) (or an equivalent performance budget) so regressions get caught at PR time.

## Station record

```markdown
### Station 7 — Performance: <RED|YELLOW|GREEN> (<n>/10)
- Conditions: <tool + version, build type, throttling> · Milestones: <load metrics> · Weight: <bytes/route> · Worst interaction: <trace>
- Evidence level: <live / report / build / interview, per check>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why>
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
