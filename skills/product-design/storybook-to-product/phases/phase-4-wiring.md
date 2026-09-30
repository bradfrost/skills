# Phase 4: Wiring

Connect the new front of the front end to everything behind it: the data,
the forms, the scripts, the links out to other systems. This is the work
Storybook never had to do, and it's where a screen that looked finished
turns out not to be.

**Output:** every row in the behavior inventory resolved, every link and
form pointed somewhere real, and the link record from `reference/LINKS.md`
written.

---

## 1. Data

Every region that repeats or reads content now reads it from where the
product keeps it, per `CONTENT.md`:

- **Loops read the product's data source,** with the fixture's shape as the
  guide. When the story's fixture shape and the product's data shape
  disagree (the story wants `quote`, the data file has `text`), change the
  template to fit the data, not the data to fit the fixture, unless
  `CONTENT.md` moved that content on purpose.
- **A field the story renders and the product's data doesn't have** is a
  finding: either the data source grows a field (and somebody fills it in
  for every entry, not just the ones in the fixture), or the region goes
  without it. Ask; don't invent values to fill the gap.
- **Empty and long states.** The fixture showed one shape. Real data has
  entries with no image, a 90-character name, zero items. Render each loop
  with the product's actual full data set, not a sample.

## 2. Behaviors

Work the behavior inventory from phase 1, row by row:

- **Restore:** point the existing script at the new markup. Prefer putting
  the hooks back on the markup (phase 3 should have) over rewriting the
  script's selectors, so the script's own history stays readable.
- **Rebuild:** use the system component's own API first. A modal that has
  an open property and a close event doesn't need the old hand-rolled
  toggle script; a scroller that scrolls natively doesn't need a cycler.
  Read the component's catalog entry for the version the product now pins.
  Delete the old script once nothing calls it.
- **New:** a behavior nobody has decided on yet. Propose the smallest
  version that makes the trigger honest (a play button opens the video), and
  ask before building anything bigger.
- **Retire:** delete the script and its script tag. Search for its hooks
  one more time.

**Every trigger needs a target, and every target needs a trigger.** A modal
with no button that opens it is dead markup; a button that opens nothing is
a broken promise. Walk both directions.

Keep interaction accessible while you're in there: a trigger is a
`<button>` (or the system's button), the thing it opens is labeled, focus
moves in and comes back, and the Escape key closes it. When a system
component handles this, let it.

## 3. Forms and backends

For each form the story renders:

- **It posts where the product's form posts,** with the field names the
  backend expects. A story's form is usually static markup with field names
  somebody guessed; the serverless function or the email service provider
  decides what they're really called.
- **Its success and error states exist,** and they're wired. A story often
  shows the success state as its own permutation; in production something
  has to switch to it.
- **Never submit to a live list or a live payment flow while testing.** Use
  the product's local or test mode (a local functions server, a test
  audience, a sandbox key). If the product has none, test up to the network
  request and stop there, and say so in the report.

## 4. Links

Every `href` in the new markup goes somewhere real:

- **In-page anchors** match an `id` that actually exists on the page (a
  redesign that renames sections breaks the nav's `#about` quietly).
- **Links out** (checkout, sign in, course platform, social profiles) come
  from the product, never from the fixture. A fixture link is invented
  until proven otherwise.
- **Links the story dropped** (a nav item that was cut) are gone from every
  page, not just the redesigned one.
- **A retired page gets a redirect**, a permanent one, to wherever its job
  went now (`/order` → `/#order`), so old links, emails, and bookmarks
  still land.

**Third-party embeds can refuse the production domain.** An embed that
talks to its host by `postMessage` usually checks the host's origin. Read
the embed's own allowlist: the course site's generative backdrop accepted
messages from `localhost` and `*.bradfrost.com`, so it worked in Storybook
and on localhost, and silently dropped every message on
`aianddesign.systems` and on deploy previews. File it where the embed
lives.

## 5. The page around the page

Storybook renders a body. The product renders a document. Check the parts
nobody designs in Storybook:

- `<title>`, meta description, canonical URL, and social card images still
  match the page's new content.
- Analytics and tag scripts still load, and any event they tracked on a
  retired or renamed element is moved or retired with it.
- The skip link targets something that still exists.
- Fonts, favicons, and preloads the new UI needs are in the head.

## 6. Write the links

Write `storybook-to-product/links.json` and the file headers per
`reference/LINKS.md`, on the same branch as the work, so the record merges
with it. Then check the loops that already exist (usage reporting,
release propagation) and note what you found for the report.

Close the phase in one line:

> Wired: 9 behaviors (4 restored, 2 rebuilt on `ed-modal`'s own API, 1 new,
> 2 retired), 1 form on the local functions server (not submitted live), 23
> links checked, 2 anchors renamed. Links written for 3 stories. Proof
> next.
