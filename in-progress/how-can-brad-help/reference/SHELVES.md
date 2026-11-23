# The shelves

Everything this skill recommends comes from public JSON files that anyone
can open in a browser. `scripts/find.py` downloads them with a plain request
(no query string, nothing about you) and does all the matching on your
machine.

## On the shelves now

| Shelf | File | What's on it | Links go to |
|---|---|---|---|
| Course lessons | [`learn.bradfrost.com/lessons.json`](https://learn.bradfrost.com/lessons.json) | Every lesson in AI and Design Systems, Subatomic: The Complete Guide To Design Tokens, and the Atomic Design Certification Course, with a summary, tags, presenters, and whether it's free | `https://learn.bradfrost.com/lessons/<id>` |
| Blog posts | [`learn.bradfrost.com/assets/help-index.json`](https://learn.bradfrost.com/assets/help-index.json) (`blog`) | Brad's posts about design systems, design tokens, atomic design, CSS, front-end development, process, and AI | bradfrost.com |
| Community links | the same file (`community`) | Articles, tools, and talks people have shared in the AI and Design Systems course community, also published at [aianddesign.systems](https://aianddesign.systems) | the original source |
| FAQ | the same file (`faqs`) | Common questions about the courses, access, and certificates | learn.bradfrost.com/faq/ |
| Free resources | the same file (`resources`) | Free things to read, watch, and use | the resource itself |

A lesson needs a summary to be recommended; a title alone isn't enough to
say it fits.

## Coming to the shelves

These will show up here as they're published as data:

- **Wake Up Excited!** episodes, the podcast where I talk to exuberant
  people about living a creative and fulfilling life.
- More blog posts, including the advice posts about creativity, career,
  and a sustainable working life.
- Community links for Subatomic and the Atomic Design Certification Course.

## Adding a shelf

A shelf is one public JSON file. To add one:

1. Publish it where a plain GET can reach it.
2. Add its URL to `SHELVES` in `scripts/find.py`, and a reader that turns
   each entry into `title`, `url`, `summary`, and `tags`.
3. Add a row to the table above, so the list here stays the truth about
   what the skill reads.
