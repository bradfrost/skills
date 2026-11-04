#!/usr/bin/env python3
"""Check the public skills' lesson pointers against the current course catalog."""

import argparse
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import re
import sys
from urllib.error import HTTPError
from urllib.request import HTTPRedirectHandler, Request, build_opener, urlopen


ROOT = Path(__file__).resolve().parents[1]
CATALOG_URL = "https://learn.bradfrost.com/lessons.json"
LESSON_URL = "https://learn.bradfrost.com/lessons/"
LINK = re.compile(r"\[([^\]]+)\]\(https://learn\.bradfrost\.com/lessons/([0-9]+)\)")
GUIDANCE = re.compile(
    r"<!-- course-lesson-guidance:start -->.*?<!-- course-lesson-guidance:end -->",
    re.DOTALL,
)


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def check_redirect(item):
    lesson_id, destination = item
    url = LESSON_URL + lesson_id
    try:
        # Read only the redirect response; don't enter a student's session.
        with build_opener(NoRedirect).open(Request(url), timeout=20) as response:
            return f"{url}: expected 302, got {response.status}"
    except HTTPError as error:
        status, location = error.code, error.headers.get("Location")
        error.close()
        if status == 302 and location == destination:
            return None
        return f"{url}: expected 302 to {destination}; got {status} to {location}"
    except Exception as error:
        return f"{url}: redirect check unavailable ({error})"


def check(catalog, root=ROOT):
    errors = []
    if catalog.get("schema_version") != 1 or not isinstance(catalog.get("lessons"), list):
        return ["Unsupported catalog: expected schema_version 1 and a lessons array."], {}, 0
    lessons = {}
    for lesson in catalog["lessons"]:
        lesson_id = lesson.get("id")
        if not isinstance(lesson_id, str) or not lesson_id.isdigit() or lesson_id in lessons:
            errors.append(f"Invalid or duplicate catalog lesson ID: {lesson_id}")
        lessons[lesson_id] = lesson
    courses = {course["id"]: course["title"] for course in catalog["courses"]}
    canonical = root / "skills/design-systems/ds-inspection/reference/COURSE-LESSONS.md"
    block = GUIDANCE.search(canonical.read_text())
    if block is None:
        return ["Canonical lesson guidance block is missing."], {}, 0
    destinations = {}
    references = 0
    for family in ("design-systems", "product-design"):
        for entry in sorted((root / "skills" / family).glob("*/SKILL.md")):
            refs = list(entry.parent.glob("reference*/COURSE-LESSONS.md"))
            if len(refs) != 1:
                errors.append(f"{entry.parent.name}: expected one standalone lesson reference.")
                continue
            ref = refs[0]
            references += 1
            content = ref.read_text()
            relative = ref.relative_to(entry.parent).as_posix()
            if f"]({relative})" not in entry.read_text():
                errors.append(f"{entry}: lesson reference isn't linked from SKILL.md.")
            guidance = GUIDANCE.search(content)
            if guidance is None or guidance.group() != block.group():
                errors.append(f"{ref}: shared guidance differs from the canonical copy.")
            links = LINK.findall(content)
            if not links:
                errors.append(f"{ref}: no lesson pointers.")
            # Catch malformed URLs that the valid-link matcher would otherwise skip.
            if content.count(LESSON_URL) != len(links) + 1:
                errors.append(f"{ref}: unexpected or malformed lesson permalink.")
            for title, lesson_id in links:
                lesson = lessons.get(lesson_id)
                if lesson is None:
                    errors.append(f"{ref}: lesson {lesson_id} is absent from the catalog.")
                    continue
                if lesson.get("title") != title:
                    errors.append(f"{ref}: lesson {lesson_id} title changed: {lesson.get('title')}")
                if lesson.get("kind") != "lesson" or not str(lesson.get("summary") or "").strip():
                    errors.append(f"{ref}: {lesson_id} has no usable lesson summary.")
                if lesson.get("course") not in courses:
                    errors.append(f"{ref}: {lesson_id} has an unknown course.")
                if not isinstance(lesson.get("free"), bool):
                    errors.append(f"{ref}: {lesson_id} has unverified access.")
                destination = lesson.get("url")
                if not isinstance(destination, str) or not destination.startswith("https://"):
                    errors.append(f"{ref}: {lesson_id} has no HTTPS destination.")
                else:
                    destinations[lesson_id] = destination
    # Check lesson links outside the tables too, including README examples.
    for file in [root / "README.md", *(root / "skills").rglob("*.md")]:
        for title, lesson_id in LINK.findall(file.read_text()):
            if lesson_id not in lessons:
                errors.append(f"{file}: unknown lesson {lesson_id}.")
    return errors, destinations, references


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, help="Use a saved catalog for an offline check.")
    parser.add_argument("--check-redirects", action="store_true", help="Verify every unique permalink against its catalog destination.")
    args = parser.parse_args()
    try:
        if args.catalog:
            catalog = json.loads(args.catalog.read_text())
        else:
            with urlopen(CATALOG_URL, timeout=30) as response:
                catalog = json.load(response)
        errors, destinations, references = check(catalog)
        if args.check_redirects and not errors:
            with ThreadPoolExecutor(max_workers=4) as pool:
                errors.extend(error for error in pool.map(check_redirect, sorted(destinations.items())) if error)
    except Exception as error:
        print(f"Course-link check could not complete: {error}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    source = str(args.catalog) if args.catalog else CATALOG_URL
    print(f"PASS: {references} skills, {len(destinations)} unique lessons; catalog generated {catalog.get('generated_at', 'unknown')}.")
    print(f"Catalog source: {source}")
    print("Permalink redirects verified." if args.check_redirects else "Redirects not checked; use --check-redirects to verify destinations.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
