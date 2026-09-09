#!/usr/bin/env python3
"""The proof gate.

Renders ONE brief against TWO profiles. If the split between the universal
grammar and the per-team profile is correct, the ASCII structure is identical
and only the labels change.

    python3 build_proof_gate.py material > material-web-homepage.txt
    python3 build_proof_gate.py eddie    > eddie-homepage.txt
    diff material-web-homepage.txt eddie-homepage.txt

Every differing line should be a region tag or a legend entry. If a content
row moves, something system-specific is still stuck in the grammar.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tools"))
from build_example import Frame, card, card_row, button_primary, button_secondary  # noqa: E402

# --- the two profiles, as label sets ---------------------------------------
PROFILES = {
    "material": {
        "name": "Material Web",
        "site-header": "<unmapped: site-header>",
        "hero": "<unmapped: hero>",
        "section": "<unmapped: section> › <unmapped: grid>",
        "form": "<unmapped: form>",
        "footer": "<unmapped: footer>",
        "legend": [
            "[1] <unmapped: site-header> — no component; page chrome is yours",
            "[2] <unmapped: hero> — compose from your own heading +",
            "    <md-filled-button>  [verified]",
            "[3] <unmapped: section> › <unmapped: grid>",
            "    · 3 × <md-outlined-card>  [verified]",
            "    · card zones are a composition, not named slots",
            "[4] <unmapped: form>",
            "    · <md-outlined-text-field> + <md-filled-button>  [verified]",
            "[5] <unmapped: footer> — no component",
            "",
            "Six of this page's nine archetypes have no Material Web",
            "component. The cards, buttons, and fields are real; the page",
            "structure around them is yours to build.",
        ],
    },
    "eddie": {
        "name": "Eddie",
        "site-header": "<ed-r-site-header>",
        "hero": "<ed-hero>",
        "section": "<ed-section> › <ed-grid>",
        "form": "<ed-single-field-form>",
        "footer": "<ed-r-site-footer>",
        "legend": [
            "[1] <ed-r-site-header>  [verified]",
            "    · <ed-logo> · <ed-primary-nav> › <ed-primary-nav-item>",
            "[2] <ed-hero> align=\"center\"  [verified]",
            "    · h1 + <ed-text-passage> + <ed-button-group>",
            "[3] <ed-section> › <ed-grid variant=\"3up\">  [verified]",
            "    · 3 × <ed-grid-item> › <ed-card>",
            "    · header slot → media (media only) · default → body",
            "      · footer slot → actions",
            "[4] <ed-single-field-form>  [verified]",
            "    · <ed-text-field> + <ed-button variant=\"primary\">",
            "[5] <ed-r-site-footer>  [verified]",
            "",
            "All 14 archetypes bind. Eddie ships page-level composition",
            "alongside its primitives.",
        ],
    },
}


def build(p):
    f = Frame(52)

    f.open(("1", p["site-header"]))
    f.row("BRANDMARK    Product  Pricing  Docs   [ Sign in ]")

    f.region(("2", p["hero"]))
    f.blank()
    f.row("· now in public beta ·", "center")
    f.heading("S H I P   F A S T E R", level=1)
    f.row("One place for the work your team keeps losing.", "center")
    f.blank()
    pb = button_primary("START FREE ▸")
    sb = button_secondary("Read the docs")
    for i in range(3):
        f.row(pb[i] + "   " + sb[i], "center")
    f.blank()

    f.region(("3", p["section"]))
    f.blank()
    f.heading("What You Get", level=2)
    f.blank()
    c1 = card(f, ["Capture"], ["Everything", "in one", "inbox.", "»2 sec«"], "[ Tour ]", media="[###]")
    c2 = card(f, ["Organize"], ["Boards that", "match how", "you work.", "»no setup«"], "[ Tour ]", media="/ / /")
    c3 = card(f, ["Ship"], ["Close the", "loop where", "it started.", "»1 click«"], "[ Tour ]", media="(-o-)")
    card_row(f, [c1, c2, c3])
    f.blank()

    f.region(("4", p["form"]))
    f.blank()
    f.heading("Get the monthly note", level=2)
    f.row("What we shipped, what broke, what we learned.", "center")
    f.blank()
    f.row("[ you@email.com________ ]  ▐ Subscribe ▸ ▌", "center")
    f.blank()

    f.region(("5", p["footer"]))
    f.row("BRANDMARK          hello@example.com")
    f.row("Product · Pricing · Docs · Terms · © 2026")
    f.close()
    return f


if __name__ == "__main__":
    key = sys.argv[1] if len(sys.argv) > 1 else "eddie"
    p = PROFILES[key]
    f = build(p)
    print(f"PROOF GATE — one brief, rendered against: {p['name']}")
    print("Brief: a homepage for a product that helps teams ship faster.")
    print("Fidelity: wireframe · Frame: 52 inner")
    print()
    print(f.render())
    print()
    print("ANATOMY")
    for line in p["legend"]:
        print(line)
    ok, report = f.check()
    print()
    print("WIDTH CHECK")
    print(report)
