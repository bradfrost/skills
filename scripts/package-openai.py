#!/usr/bin/env python3
"""Build a ChatGPT plugin archive from the public skills in this checkout."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--version", default="1.0.0")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    output = args.output or root / "dist" / "brad-frost-skills.zip"
    if not re.fullmatch(r"\d+\.\d+\.\d+", args.version):
        parser.error("Use a numeric major.minor.patch version.")

    files = {}
    modes = {}
    sources = {}
    quoted = []
    for manifest in sorted((root / "skills").rglob("SKILL.md")):
        source = manifest.parent
        name = source.name
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or name in sources:
            parser.error(f"Skill folder names must be safe and unique: {name!r}")
        text = manifest.read_text()
        match = re.match(r"\A---\n(.*?)\n---(?=\n|$)", text, re.S)
        if not match or not re.search(rf"^name: {re.escape(name)}$", match[1], re.M):
            parser.error(f"Check the YAML name in {manifest.relative_to(root)}.")
        if not re.search(r"^description:\s*\S", match[1], re.M):
            parser.error(f"Add a description to {manifest.relative_to(root)}.")
        sources[name] = source.relative_to(root).as_posix()
        for path in sorted(source.rglob("*")):
            if path.name == ".DS_Store" or "__pycache__" in path.parts:
                continue
            if path.is_symlink():
                parser.error(f"The archive cannot include a symlink: {path}")
            if not path.is_file():
                continue
            data = path.read_bytes()
            if path == manifest:
                # Quote plain descriptions for strict YAML parsers. The body
                # and all source files remain unchanged.
                front = match[1]
                for line in front.splitlines():
                    if line.startswith("description: "):
                        value = line[len("description: "):]
                        if value and value[0] not in "\"'|>":
                            front = front.replace(line, "description: " + json.dumps(value, ensure_ascii=False), 1)
                            quoted.append(name)
                data = ("---\n" + front + "\n---" + text[match.end():]).encode()
            target = f"skills/{name}/{path.relative_to(source).as_posix()}"
            files[target] = data
            modes[target] = path.stat().st_mode & 0o777
    if not sources:
        parser.error("No skills were found in this checkout.")

    plugin = {
        "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        "name": "brad-frost-skills",
        "version": args.version,
        "description": "Brad Frost's public skills for design systems, product design, judgment, and healthy AI limits.",
        "author": {"name": "Brad Frost"},
        "repository": "https://github.com/bradfrost/skills",
    }
    files["plugin.json"] = (json.dumps(plugin, indent=2) + "\n").encode()
    for name in ("LICENSE", "OPENAI.md"):
        files[name] = (root / name).read_bytes()
    receipt = {
        "source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip(),
        "plugin_version": args.version,
        "skills": sources,
        "metadata_quoted": quoted,
        "sha256": {name: hashlib.sha256(data).hexdigest() for name, data in files.items()},
    }
    files["package-receipt.json"] = (json.dumps(receipt, indent=2) + "\n").encode()
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100000 | modes.get(name, 0o644)) << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(output) as archive:
        assert archive.testzip() is None
        assert sum(name.endswith("/SKILL.md") for name in archive.namelist()) == len(sources)
    print(f"Packaged and verified {len(sources)} skills: {output}")


if __name__ == "__main__":
    main()
