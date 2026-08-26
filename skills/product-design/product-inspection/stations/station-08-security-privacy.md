---
station: 8
name: Security & privacy
quality: Secure (quality 8 of 10)
question: As shipped, does the product protect its users' sessions and data — auth, permissions, exposure, transport, dependencies — or does it trust the client, leak internals, and hope?
---

# Station 8 — Security & privacy

**Quality: Secure.** Users hand a product their sessions, their data, and their trust; this station checks whether the shipped product deserves it. Not a penetration test — a *health inspection*: are the well-known doors locked? Sessions that expire and log out cleanly, permissions enforced on the server (not just hidden in the UI), APIs that return only what the page needs, errors that don't narrate the stack, dependencies without known holes, and no more tracking or data collection than the product can justify. Most product security failures aren't exotic — they're the basics skipped under deadline. This inspection is for the product's own team, on their own product; anything deeper (real pentesting, adversarial testing of third-party services) is out of scope and needs explicit authorization.

## Evidence to gather

| What to look at | Best source | Fallbacks |
|---|---|---|
| Auth & session behavior | Live instance: log in/out, expire a session mid-action, check cookie flags (`HttpOnly`, `Secure`, `SameSite`) | Repo auth code · interview |
| Authorization enforcement | Live: request another user's/role's resource directly (own test data only) — does the server refuse? | Repo route guards · interview |
| Data exposure | API responses on core routes: over-returning fields? Stack traces or internal paths in error bodies? Secrets in the client bundle/env? | Repo grep for keys · interview |
| Transport & headers | Response headers on real routes: HTTPS, HSTS, content-security policy, mixed content | Deploy config · interview |
| Input handling (security lens) | Live: does user input render unescaped anywhere (stored XSS)? Do queries concatenate input? | Repo review · interview |
| Dependency vulnerabilities | `npm audit` / the ecosystem's equivalent, on the lockfile | CI audit output · interview |
| Privacy & tracking | Network panel: third-party requests, trackers, PII in URLs or analytics events; data collection vs. stated need | Privacy policy · interview |

## Inspection procedure

1. **Walk the auth lifecycle** (if the product has auth). Log in, log out, let a session expire mid-action: does expiry land as a graceful re-auth prompt or a crash/silent failure? Check session cookie flags on the real response.
2. **Probe authorization server-side, on your own test data.** Take a resource ID you own, request it as a different/unprivileged user (or logged out). UI hiding is not enforcement — the server must refuse. Internal tools skip this at their peril; "everyone here is trusted" lasts until the URL leaves the building.
3. **Read what the API actually returns.** On the core routes, diff the response against what the page renders — flag over-returned fields (emails, tokens, other users' data). Trigger an error and read the body: production must not return stack traces, absolute paths, or query fragments.
4. **Sweep for exposed secrets.** Grep the client bundle and repo for API keys, tokens, credentials; check that `.env` files are gitignored and that server-only secrets never reach the browser.
5. **Check transport and headers** on real responses: HTTPS everywhere (no mixed content), and the basic protective headers present for the product's risk level.
6. **Test input handling with a security lens.** Enter script-looking strings (`<img onerror=…>`-style, on your own instance) into fields that later render: escaped or executed? Check how queries are built — parameterized or concatenated?
7. **Run the dependency audit.** `npm audit` (or the ecosystem's equivalent — an exemplar, not a requirement; name the tool). Triage: known-critical vulns in production dependencies are findings; unreachable dev-dep noise is context.
8. **Review privacy posture.** What third parties get pinged on page load? Is PII in URLs, logs, or analytics events? Is data collection proportionate to what the product does — and disclosed where the audience expects it?

## Warning lights

- Session cookies without `HttpOnly`/`Secure`/`SameSite`; sessions that never expire or expire into a crash
- Authorization enforced only in the UI — direct requests succeed for the wrong user
- API responses returning far more than the page needs; other users' data reachable by ID
- Stack traces, absolute paths, or internals in error responses; secrets in the client bundle or repo
- Mixed content; missing basic protective headers on a public product
- User input rendered unescaped; queries built by string concatenation
- Known-critical vulnerabilities in production dependencies, unaddressed
- Trackers or PII flows the product can't justify or never discloses

## Scoring anchors

- **Red (0–3):** A locked-door basic is open — authorization bypassable, secrets exposed, unescaped input rendering, critical known vulns shipped, or PII leaking to third parties. The light is ON regardless of product size.
- **Yellow (4–7):** Fundamentals mostly hold but with real gaps — a missing cookie flag, over-returning APIs, dev-grade error bodies reachable in production, an unaudited dependency tree, undisclosed tracking.
- **Green (8–10):** The team can honestly say: *"Sessions and permissions are enforced server-side, APIs return only what's needed, errors and bundles leak nothing, dependencies are audited on a cadence, and we collect no more data than the product needs — and can say why."*

## Turning off the light

- Sanitizing error responses and adding cookie flags are afternoon-sized fixes with outsized payoff — do them first.
- Wire the dependency audit (`npm audit` or equivalent) into CI so the tree can't silently rot.
- Server-side authorization checks belong at the route/handler layer — an agent can inventory unguarded routes; a human decides the permission model.
- Scale the frame honestly (ground rule 8): an internal tool behind a VPN doesn't need a flagship's header set — but authorization, secret handling, and error sanitization are non-negotiable at every size.
- If auth/session primitives come from a platform or the design system's app shell, cross-file gaps upstream — same dual-filing pattern as every other station.

## Station record

```markdown
### Station 8 — Security & privacy: <RED|YELLOW|GREEN> (<n>/10)
- Checked: <auth/session · authorization · exposure · transport · input · deps · privacy> · Audit tool: <tool + version> · Worst finding: <what>
- Evidence level: <live / code / interview, per check>
- Findings:
  - [verified|reported] <finding + evidence>
- Not inspected: <what and why — e.g. "no auth in this product; auth checks N/A">
- Deviations noted: <intentional departures>
- First move: <single highest-leverage fix>
```
