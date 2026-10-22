#!/usr/bin/env python3
"""Link this checkout's public skills into Codex's user skill directory."""

import argparse
from datetime import datetime
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills")
    parser.add_argument("--replace", action="store_true", help="Back up conflicting entries before linking the current skills.")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    sources = sorted(p.parent for p in (root / "skills").rglob("SKILL.md"))
    names = [p.name for p in sources]
    if not sources or len(names) != len(set(names)):
        parser.error("This checkout must contain skills with unique folder names.")
    dest = args.dest.expanduser().absolute()
    conflicts = [dest / p.name for p in sources if (dest / p.name).exists() or (dest / p.name).is_symlink()]
    conflicts = [p for p in conflicts if not (p.is_symlink() and p.resolve() == next(s for s in sources if s.name == p.name))]
    if conflicts and not args.replace:
        parser.error("Existing skills: " + ", ".join(p.name for p in conflicts) + ". Use --replace to back them up first.")
    backup = dest.parent / "skill-backups" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    dest.mkdir(parents=True, exist_ok=True)
    for source in sources:
        target = dest / source.name
        if target in conflicts:
            backup.mkdir(parents=True, exist_ok=True)
            target.rename(backup / target.name)
        if not target.is_symlink():
            target.symlink_to(source, target_is_directory=True)
        if target.resolve() != source or not (target / "SKILL.md").is_file():
            raise RuntimeError(f"Could not verify {target}.")
    print(f"Verified {len(sources)} skill links in {dest}")
    if conflicts:
        print(f"Previous entries are backed up in {backup}")


if __name__ == "__main__":
    main()
