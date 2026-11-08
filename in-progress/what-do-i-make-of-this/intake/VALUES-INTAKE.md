# Values intake

A read can only hold up a mirror to someone it knows something about. This
intake is how the skill learns what it needs, without reaching into anything
the person didn't hand over. Follow [`DATA-HYGIENE.md`](../reference/DATA-HYGIENE.md)
throughout.

## 1. Ask for a source

Ask once, in these words:

> Before I read this, I need to know a little about you, so the read is about *you* and not some generic person. You can point me at a file where you've written down what you value, paste it in, or answer 4 short questions. Which do you want?

- **A file:** read exactly the file they named, nothing else. If it can't be
  read, say so and offer the other two options. Never go looking for one.
- **Pasted text:** use it as given.
- **The questions:** ask them below.

If they already handed you a file or text in the same message as the thing
to read, skip this step and use it.

## 2. The four questions

Ask one at a time. Each one can be skipped, and a skipped question is fine;
the read just marks more claims `[inferred]`.

> (1 of 4) What do you care about most, in your own words? A few values or principles is plenty.

> (2 of 4) Which of those tend to pull against each other for you? (For example, family against ambition, or generosity against your own time.)

> (3 of 4) What's on your plate right now? The work and life stuff that's actually taking your attention this month.

> (4 of 4) Is there anything you've said publicly, or decided in the past, that this read should know about?

Quote their answers back exactly when you cite them. Never tidy their words
into something that sounds better.

## 3. Offer to save, once

Only after the questions (never after a file they already own), ask:

> Want me to save these answers as a values file you can point me at next time? If so, tell me where. A personal notes app or a private folder outside any work or code directory is a good spot. (Saying no is totally fine; I'll just ask again next time.)

If they say yes, follow [`DATA-HYGIENE.md`](../reference/DATA-HYGIENE.md):
warn in one line if the path is in a work directory, a git repository, or a
synced company drive, then write a plain markdown file with their answers
under the four questions as headings. If they say no, write nothing.

## 4. What the source becomes

Whatever the source, it is the **only** thing a claim about the person can
be `[documented]` against for this run:

- From a file: cite the file name and the line or heading.
- From pasted text or the questions: cite "you said" and quote it.

Everything else about them (their public record, their tendencies, what
"people like them" think) is `[inferred]`, every time.
