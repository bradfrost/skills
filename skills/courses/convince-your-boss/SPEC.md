# Spec: `convince-your-boss`

_Status: draft for Brad's review. Nothing here ships until the open decisions
at the bottom are made and the interview copy is edited line by line._

## The point

Someone wants to take one of our courses, and they want their employer to
pay for it. That's a real, recurring situation (it's why "convince your
boss" letters have been a conference tradition for 20 years), and right now
the best we offer is "email courses@ and we'll send an invoice."

This skill turns that moment into a short, honest business case the learner
sends to their own manager. Not our pitch with their name on it. THEIR case,
in their voice, about their team's actual problems, with real numbers and
one request their manager can say yes to.

The thing that actually persuades a manager isn't a feature list. It's the
learner saying "here's what I'll bring back to the team in 30 days." So the
skill spends most of its effort getting that commitment out of the learner
and onto the page, and comparatively little on describing the course.

## Who it's for

- A designer or developer who already wants the course and needs budget
  approval, a PO, or an invoice route.
- A design system lead who wants seats for a team (3+ gets the automatic
  team discount, which changes the math).
- Someone who *thinks* they want the course. The skill includes a fit check
  and will say "not yet" when that's the honest answer.

Who it is NOT for: us. The skill never speaks as Brad, Ian, or TJ. It never
signs anything. It hands the learner a draft and gets out of the way.

## Principles (binding on the agent)

1. **Their case, not our ad.** Facts about the course come from the facts
   sheet or the live course page. Opinions about whether it's worth it come
   from the learner. The agent quotes the learner's own words back to them.
2. **No invented outcomes. No fake urgency.** Never "your team will ship 40%
   faster." Never "this won't last long!" A dated, real price change can be
   stated with its date; if the agent can't verify it live, it says "confirm
   on the course page before sending."
3. **Honest fit check, and it can end the session.** If the team has no
   design system and no plan for one, or the learner already knows the
   material, or there is genuinely no budget path, the skill says so plainly
   and stops. Telling someone "this course isn't for you yet" is a feature.
   We don't dunk on beginners and we don't upsell people who don't need it.
4. **Manager lane: serious and clear.** Money is involved, so the tone is
   calm, specific, and short. No hype, no CAPS, no exclamation points in the
   draft itself. (The skill can be warm in conversation with the learner.)
5. **Nothing sends.** The output is a draft. The learner reads it, edits it,
   and sends it themselves.
6. **One question per message**, numbered, same as the limits interview.
   This is a conversation, not a form.

## How it runs

```
/convince-your-boss
```

**Step 0: Which course?** If the learner names one, take it. If not, one
question ("what's the problem you're trying to solve?") is usually enough
to route: tokens → Subatomic; AI workflow / inspecting or adopting a design
system → AI & Design Systems; teaching the methodology to a team →
Atomic Design. When two fit, name both and let them choose.

**Step 1: The interview (5 questions, ~5 minutes).** Draft copy lives in
`SKILL.md`; it needs Brad's line-by-line edit before it's real.

1. Who decides, and what do they care about? (Their manager's role and what
   that person is measured on: shipping speed, consistency, headcount,
   accessibility, "leadership wants AI and nobody knows where to start.")
2. What's the pain right now, specifically? If the project already carries
   `ds-inspection/`, `product-inspection/`, or `ds-token-architecture/`
   reports, the agent reads the reds and yellows and offers them as
   evidence. This is where the skills collection and the courses connect:
   an inspection found the problem, the course teaches the fix.
3. What will you bring back? The commitment: a lunch-and-learn, a token
   migration plan, running the inspection and presenting the work order,
   a pilot on one product. Dated.
4. Money, seats, time. How many people, what budget path exists (L&D
   stipend, team budget, an unused conference budget), whether they need an
   invoice or PO, and hours per week they can honestly give it.
5. Format and register. Email, Slack message, or a one-page doc; how formal
   their manager is.

**Step 2: Facts.** Load `reference/COURSES.md`. If the agent has web access,
fetch the live course page and prefer its price and dates over the sheet.
If it can't, use the sheet and add a "confirm the price on the course page
today" line to the before-you-send checklist. The sheet carries a
`last_verified` date and the draft says it.

**Step 3: Fit check, said out loud.** One of three: recommend this course;
recommend a different one of ours (with the reason); or "not yet" (with the
reason and what would change it). No fourth option, no hedging.

**Step 4: Write the case** from `templates/business-case.md`. Roughly 250
words for email, under 120 for Slack, one page for the doc:

- What I'm asking for (one sentence, first line)
- Why now (their pain, with evidence if they have it)
- What it costs (price × seats, team discount if 3+, hours per week)
- What we get back (the dated commitment from question 3)
- How to pay (card, or invoice/PO via courses@bradfrost.com)
- One line on risk ("if it's not useful, I'll say so and we stop")

**Step 5: Hand it back and stop.** The draft, a four-line before-you-send
checklist, and a definitive close. No dangling offers; this repo's whole
mental-health section is about that.

## Files

```
skills/courses/convince-your-boss/
├── SPEC.md                      ← this document (delete before ship, or keep as design record)
├── SKILL.md                     ← the agent procedure and the interview script
├── reference/COURSES.md         ← the facts sheet, every line tagged with its source
└── templates/business-case.md   ← the output shell (email / Slack / one-pager variants)
```

No setup step. `setup-brad-frost-skills` gets one line in its "needs no
setup" list, and the README gets a row in a new **Courses** table.

## Where it plugs into the rest of the collection

The skills strategy names two blockers in front of *promoting* the
collection: the Thinkific paywall experience for non-enrolled visitors, and
the per-finding deep-link map from skill output to course lessons. This
skill leans on the second one directly. Question 2 wants to say "your
inspection flagged station 3 and station 9; Chapter 3 covers both." Until
that map exists as a real table we own, the agent can only point at
chapters, not lessons. The facts sheet carries a coarse version (station →
chapter) to start; the fine version should live in one place and be read
by `ds-inspection`, `ds-token-architecture`, and this skill.

## What this skill must never do

- Speak as Brad, Ian, or TJ, or sign anything.
- Invent a number: a price, a discount, a percentage improvement, a date.
- Print internal discount figures. PPP, student, and job-hunter discounts
  exist and the draft can say "discounts are available, email courses@";
  the amounts are courses@'s to quote, not the skill's.
- Send anything, anywhere.
- Keep going after the fit check says "not yet."
- Add a trailing "want me to also draft a follow-up?"

## Open decisions for Brad

1. **Name and folder.** `/convince-your-boss` is memorable and it's what you
   said. Your own naming rule is category-first (`course-business-case`
   would sort with future course skills). Recommendation: keep
   `convince-your-boss`, because the command IS the pitch, and put it under
   `skills/courses/`.
2. **The interview copy.** Draft in `SKILL.md`. Every quoted line is yours
   to edit before it's real; the README quotes it verbatim afterward.
3. **The facts.** `reference/COURSES.md` marks each line as public FAQ,
   from your records (confirm), or unknown (you fill in). The AI & Design
   Systems price change on 2026-09-30 is the one time-sensitive fact.
   Atomic Design Certification pricing and the Mega Bundle are blank.
4. **Live fetch or sheet only?** Live fetch keeps prices honest without a
   commit every time a number changes, but needs web access and a stable
   page to read. Recommendation: both, live preferred, sheet as fallback,
   and the draft names which one it used.
5. **The station → chapter map.** Coarse version in the sheet now; the real
   one is the deep-link blocker from the skills strategy. Decide where it
   lives.
6. **Scope creep to watch.** "Convince your team" and "convince yourself"
   are adjacent. The fit check covers the second. The first is a different
   skill, if ever.
7. **The close.** The limits kit closes with a signed note from you. This
   one shouldn't (it isn't your letter), but a one-line scripted close is
   still worth writing so it ends the same way every time.

## Proposed README copy (not applied)

New table under **Available skills**:

```markdown
**Courses**

| Skill | What it does |
|---|---|
| [`convince-your-boss`](skills/courses/convince-your-boss/SKILL.md) | Builds an honest business case, in your words, for your employer to pay for one of our courses |
```

New section, placed after "Kill the vibes":

> ## Convince your boss
>
> You want to take one of the courses, and you'd like work to pay for it.
> **[`convince-your-boss`](skills/courses/convince-your-boss/SKILL.md)**
> asks you five questions about your team, your manager, and what you'll
> bring back, then writes a short business case in your voice with real
> numbers and one clear request. It's important to say this is YOUR case,
> not our sales pitch with your name on it; the skill never speaks as us,
> never invents an outcome, and will tell you plainly if a course isn't the
> right fit yet.

Both blocks are proposals. They get written for real only after the
interview copy is final, so the README can quote it exactly.
