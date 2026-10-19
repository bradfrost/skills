# What this skill can and can't do

Read this before promising anybody a result. Every limit here is real, and
each one has an honest thing to say instead.

---

## It can

- Read a story as a spec: every region, every component, every comment
  about what was dropped, and the git history of the redesign.
- Work out what it takes to carry a story into a product, region by
  region, with an estimate, before changing anything.
- Find every piece of the design system a story needs that the product
  can't install yet.
- Sort a fixture's content into copy that should ship and content that was
  only ever a placeholder, and ask about the rest.
- Translate a story's markup and styles into the product's own templating
  language and stylesheet conventions.
- Wire the new markup to the product's data, scripts, forms, and links, and
  find every behavior the story left behind.
- Prove the product matches the story, in a browser, and that nothing from
  Storybook leaked into the build.
- Record which version of each story shipped, so later changes can be
  carried over one catch-up at a time.

## It can't

- **Release the design system.** When the story needs unreleased system
  work, it asks what to do and waits on the answer. Publishing a release is
  somebody else's job, in somebody else's repo.
- **Merge or deploy.** It opens a pull request and stops. Shipping to
  production is a person's call, every time.
- **Decide content on its own.** It proposes a default for every field and
  asks about everything it can't prove. Images and media are always asked.
- **Invent behavior.** A trigger the story implies and nobody specified
  gets the smallest honest version, proposed and approved, never a guess
  built in full.
- **Test against live systems.** It never submits a real signup, a real
  payment, or a real email. No test mode means it tests up to the network
  request and says so.
- **See behind a login on its own.** It never handles credentials. The
  user signs in themselves when a page needs it.
- **Verify a render without a browser.** No browser means the report says
  "not rendered", and the pull request says it too.
- **Overwrite production edits.** A catch-up that finds a field changed on
  both sides asks. The live fix might be the right one.

---

## Where it degrades, and what to say

| Situation | What still works | What to say |
|---|---|---|
| The story didn't come from `product-to-storybook` | Everything; phase 1 maps stories to templates by hand | "There's no inventory linking stories to templates, so I matched them myself. Check the pairs." |
| Story source unavailable, only a running Storybook | Rendered-DOM reading, no git history | "I can see what the story renders, not how it got there. Content provenance is mostly `unknown`, so expect more questions." |
| Unreleased system dependencies | Everything, behind the release gate answer | "Blocked on the design system release: <components>." |
| No browser | Build, leak search, links, source review | "Not rendered. Nobody has confirmed these pages display." |
| No test mode for forms | Everything up to the network request | "Forms checked up to the request. Nobody has submitted one." |
| Product has no data source for repeating content | Content hardcoded in the template, with a proposal | "These regions repeat. I left them in the template; moving them to data is a separate decision." |
| Product carries its own process rules | Those rules, first | "Following this repo's own rules; where they differ from this skill, the repo wins." |
