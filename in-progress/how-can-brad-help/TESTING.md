# Try how-can-brad-help (and tell us how it went!)

Thanks so much for testing this! `how-can-brad-help` is still a draft, which
means the regular installer (`npx skills add bradfrost/skills`) doesn't pick
it up yet. You'll install it by hand instead. It takes about five minutes.

You need an AI agent that runs skills (Claude Code or Codex), Git, and
Python 3. The skill's script uses only Python's standard library, so there's
nothing else to install.

## 1. Install it

Download the draft and copy the skill folder into your agent's skills
folder:

```bash
git clone --branch how-can-brad-help https://github.com/bradfrost/skills.git brad-frost-skills-draft
mkdir -p ~/.claude/skills
cp -R brad-frost-skills-draft/in-progress/how-can-brad-help ~/.claude/skills/
```

For Codex (and other agents that read `~/.agents/skills/`), swap
`~/.claude/skills` for `~/.agents/skills` in both lines.

Keep the folder name as-is, because the folder name becomes the command.

## 2. Check that the script can reach the catalogs

```bash
python3 ~/.claude/skills/how-can-brad-help/scripts/find.py "design tokens" --limit 2
```

You should see a few lessons, blog posts, and community links as JSON. If
you see a shelf listed under `unavailable`, that shelf couldn't be
downloaded; please tell us which one!

## 3. Use it like you normally would

Start a new session in your agent and say something like:

```
/how-can-brad-help
```

or just "how can Brad help with this?" Then describe what you're working on,
in your own words. A paragraph about yourself works great. If you'd like a
starting point, pretend to be one of these people:

- someone looking for their next job who wants to get better at design systems;
- a team lead whose design system team is stuck on adoption;
- someone working toward their Atomic Design certification;
- a designer whose company just told everyone to "use AI".

## 4. Tell us how it went

Open an issue on this repo, or add a comment to
[#51](https://github.com/bradfrost/skills/issues/51). These are the things
we most want to know:

- Which agent you used (Claude Code, Codex, something else).
- Who you were (yourself, or one of the people above).
- Did it explain the privacy promise BEFORE it read anything?
- Would you actually click on at least three of the lessons it picked?
- Did anything it recommended not belong?
- Did every link work? Did it ever invent a lesson, post, or link?
- What did you wish it had told you?

Please don't paste anything private into the issue. The shape of your
situation is plenty (we don't need the details!).

## For the team: try it against your own copy of learn

If you're changing what learn.bradfrost.com publishes, you can point the
script at your local build instead of the live site. Build learn, then:

```bash
mkdir -p /tmp/shelves
cp path/to/learn/_site/lessons.json /tmp/shelves/lessons.json
cp path/to/learn/_site/assets/help-index.json /tmp/shelves/help-index.json
python3 scripts/find.py "design tokens" --from /tmp/shelves
```

That's the best way to check that a change to learn doesn't break the skill.
