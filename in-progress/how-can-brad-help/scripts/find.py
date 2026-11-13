#!/usr/bin/env python3
"""Find the lessons, posts, and resources that fit what someone is working on.

What this script does, all of it:

1. Downloads the public shelves listed in SHELVES below with a plain GET.
   No query string, no cookies, no headers about you. Nothing is sent
   anywhere else, and nothing you typed leaves your machine.
2. Scores every item against the search terms you pass on the command line,
   here, locally.
3. Prints the best matches as JSON, grouped by shelf.

A shelf that can't be read (offline, moved, not published yet) is skipped
and named in the output, so the rest still works.

Usage:
    python3 find.py "design tokens" "dark mode" theming --limit 8
    python3 find.py tokens --from ./saved-shelves   # read saved copies instead

Standard library only, so there's nothing to install.
"""

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

LEARN = "https://learn.bradfrost.com"

# Each shelf is one public JSON file. Adding a shelf (Wake Up Excited!
# episodes, more blog posts, another course's community links) means adding
# a line here and a reader below; see reference/SHELVES.md.
SHELVES = {
    "lessons": f"{LEARN}/lessons.json",
    "help-index": f"{LEARN}/assets/help-index.json",
}

STOP = set("a an and are as at be but by can do does for from how i in is it its me my of on or our so that the their them they this to us we what when with you your".split())


def words(text):
    return [w for w in re.findall(r"[a-z0-9][a-z0-9+#.-]*", str(text or "").lower()) if w not in STOP]


def load(name, source_dir):
    if source_dir:
        path = Path(source_dir) / f"{name}.json"
        return json.loads(path.read_text(encoding="utf-8"))
    request = urllib.request.Request(SHELVES[name], headers={"User-Agent": "how-can-brad-help"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def from_lessons(data):
    courses = {c["id"]: c.get("title", c["id"]) for c in data.get("courses", [])}
    for item in data.get("lessons", []):
        summary = str(item.get("summary") or "").strip()
        # Only real lessons with a summary: a title alone isn't enough to
        # say a lesson fits.
        if item.get("kind") != "lesson" or not summary or not item.get("id"):
            continue
        yield {
            "shelf": "lessons",
            "title": item.get("title"),
            "url": f"{LEARN}/lessons/{item['id']}",
            "summary": summary,
            "tags": item.get("tags") or [],
            "course": courses.get(item.get("course"), item.get("course")),
            "chapter": (item.get("chapter") or {}).get("title"),
            "presenters": item.get("presenters") or [],
            "free": item.get("free"),
        }


def from_help_index(data):
    for shelf, key in (("blog", "blog"), ("community", "community")):
        for item in data.get(key) or []:
            if not item.get("url"):
                continue
            yield {
                "shelf": shelf,
                "title": item.get("title"),
                "url": item.get("url"),
                "summary": item.get("summary") or "",
                "tags": item.get("tags") or [],
                "date": item.get("created"),
            }
    for item in data.get("faqs") or []:
        yield {
            "shelf": "faq",
            "title": item.get("title"),
            "url": f"{LEARN}/faq/",
            "summary": item.get("summary") or "",
            "tags": item.get("tags") or [],
        }
    for item in data.get("resources") or []:
        if not item.get("url"):
            continue
        yield {
            "shelf": "free-resources",
            "title": item.get("title"),
            "url": item.get("url"),
            "summary": item.get("description") or "",
            "tags": [],
        }


READERS = {"lessons": from_lessons, "help-index": from_help_index}


def score(item, terms):
    title = " ".join(words(item["title"]))
    tags = " ".join(words(" ".join(map(str, item["tags"]))))
    summary = " ".join(words(item["summary"]))
    total = 0
    for term in terms:
        phrase = " ".join(words(term))
        if not phrase:
            continue
        pattern = r"\b" + re.escape(phrase) + r"\b"
        total += 3 * len(re.findall(pattern, title))
        total += 2 * len(re.findall(pattern, tags))
        total += len(re.findall(pattern, summary))
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("terms", nargs="+", help="words or short phrases describing the situation")
    parser.add_argument("--limit", type=int, default=8, help="matches to keep per shelf (default 8)")
    parser.add_argument("--from", dest="source_dir", help="read saved shelf files (<name>.json) from this folder")
    args = parser.parse_args()

    items, unavailable = [], []
    for name in SHELVES:
        try:
            items.extend(READERS[name](load(name, args.source_dir)))
        except Exception as error:  # a missing shelf shouldn't sink the others
            unavailable.append({"shelf": name, "url": SHELVES[name], "reason": str(error)[:200]})

    results = {}
    for item in items:
        points = score(item, args.terms)
        if points:
            results.setdefault(item["shelf"], []).append({**item, "score": points})
    for shelf in results:
        results[shelf] = sorted(results[shelf], key=lambda i: -i["score"])[: args.limit]

    json.dump({"matches": results, "unavailable": unavailable}, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
