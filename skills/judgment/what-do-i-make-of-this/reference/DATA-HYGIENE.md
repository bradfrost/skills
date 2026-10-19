# Data hygiene

Reflections about your job, your team, your values, or your life are
personal. They shouldn't sit in plaintext on a work laptop, in a shared
repo, or anywhere an agent (or your employer's tooling) can read them later.

## The rules

- **Nothing is written by default.** A skill in this family keeps what you
  tell it in the conversation and nowhere else unless you ask it to save
  something.
- **Ask before writing, every time.** When a skill produces something
  personal (a values file, a note, a read), it asks whether you want it saved
  at all, and where.
- **Point at private places.** When you do want something saved, suggest
  places you control: a personal notes app, an encrypted note, a file on a
  personal machine, or a private folder outside any work directory or code
  repository.
- **Warn about the risky ones.** If the path you pick is inside a work
  directory, a git repository, a synced company drive, or a folder the agent
  reads by default, say so in one line before writing, and let you choose.
- **Never commit it.** Never add personal reflections to a git repository,
  a pull request, an issue, or a shared document.
- **Read only what you point at.** A skill in this family reads a personal
  file only when you name it in that session. It never goes looking for one.

---

This file ships identically in every skill in the judgment family. If you
change it, change every copy in the same commit.
