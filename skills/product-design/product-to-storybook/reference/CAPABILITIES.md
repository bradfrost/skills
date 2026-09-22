# What this skill can and can't do

Read this before promising anybody a result. Every limit here is real, and
each one has an honest thing to say instead.

---

## It can

- Find a product's core page templates from its source, or infer them from
  a live site (less accurately, and it says so).
- Rebuild those templates as Storybook stories inside any Storybook it can
  read, in that Storybook's own conventions.
- Render the regions the product builds from your system with your
  *local* system, so a local change shows its ripple across every product.
- Flag every region that isn't from the system, in the markup and in a
  ledger, with a screenshot and the nearest system component.
- Keep a product's own CSS from touching anything but that product's
  stories, and prove it.
- Report how far a product has drifted from its Storybook copy since the
  last capture.

## It can't

- **Convert anything.** A region that isn't from the system stays that
  way, flagged. Converting it is `vibe-killer`'s job, afterward, if you
  want it.
- **Author production components.** Question 4 option B sets up files. It
  does not build a props API, register anything in the system's package,
  or write docs. A person decides what becomes a real component.
- **Prototype.** Every screen it builds already exists. "This product
  doesn't exist yet" is a different skill with different placeholders.
- **See behind a login on its own.** It never handles credentials. The
  user signs in themselves, or the fixtures are built from the data's
  shape.
- **Put a real person's data in a fixture.** By design, and it stops the
  run if it finds it did.
- **Tell you the stories match the product.** They run on a newer system
  than the product pins, so they *shouldn't* match exactly. The report
  labels each difference; it doesn't score them.
- **Verify a render without a browser.** Source that reads correctly is
  not a rendered story. No browser means the report says "not rendered"
  and means it.
- **Keep the stories current by itself.** The refresh mode reports drift
  and asks. It never overwrites, because the Storybook copy may be ahead
  of the product on purpose.
- **Fix version drift.** A prop the product uses that the local system
  dropped is a ledger entry, not a patch.

---

## Where it degrades, and what to say

| Situation | What still works | What to say |
|---|---|---|
| Live URL, no repo | Inferred inventory, rendered-DOM capture, full relocation | "Templates are inferred from rendered pages. Check the grouping before I build." |
| Repo, no reachable URL | Full inventory from source, fixtures from the data shape | "Content is from the repo's own data, not a live capture." |
| Behind a login | Fixtures from shape, or user-driven capture | "I'll never touch credentials or real user data. Sign in yourself, or I build from shape." |
| No browser | Stories written, no proof | "Not rendered. Nobody has confirmed these stories display." |
| Live product unreachable under a browser (wedged local server, throttling) | Everything except the live captures | "Live side by side not captured; expected differences described from source." |
| Host validator rejects product classes | Everything | "N naming findings, all the product's own classes. Expected; see the ledger." |
| No `@scope` support in the target browser | Selector prefixing under the product wrapper | "Product CSS is prefixed instead of scoped. Less airtight; the scope check still runs." |
| No sibling profiles | Storybook intake from scratch | Nothing special; it takes ten minutes longer. |
| Host has no product section | `Products/` created | "New section. Confirm the file path lands inside the `stories` glob." |
| Version drift everywhere | Stories render on local API, ledger fills up | "The product is N versions behind. Most differences below are version drift, labeled." |
