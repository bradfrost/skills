#!/usr/bin/env python3
"""Padding helper for ds-ascii renders.

Guarantees exact widths by construction, so a render can't wrap. Import it,
build your page, and call check() before you ship.

Every character used here is single-width: box-drawing, block elements,
and the few punctuation marks the grammar allows. Never put emoji inside a
frame; check() will not catch them, but your right wall will move.
"""

CLIPPED = []


class Frame:
    """A fixed-width page frame. width is the INNER width (52 by default)."""

    def __init__(self, width=52):
        self.w = width
        self.rows = []

    # ---- primitives -------------------------------------------------------
    def clip(self, s, w):
        if len(s) > w:
            CLIPPED.append((s, w))
        return s[:w]

    def center(self, s, w):
        s = self.clip(s, w)
        pad = w - len(s)
        return " " * (pad // 2) + s + " " * (pad - pad // 2)

    def left(self, s, w, indent=1):
        s = self.clip(s, w - indent)
        return " " * indent + s + " " * (w - indent - len(s))

    # ---- shell ------------------------------------------------------------
    def open(self, tag):
        """Top border carrying the first region's tag."""
        self.rows.append(self._tagbar(tag, "╔", "╗"))

    def region(self, tag):
        """Divider carrying a new region's tag."""
        self.rows.append(self._tagbar(tag, "╠", "╣"))

    def close(self):
        self.rows.append("╚" + "═" * self.w + "╝")

    def _tagbar(self, tag, l, r):
        label = f"═ [{tag[0]}] {tag[1]} "
        return l + label + "═" * (self.w - len(label)) + r

    # ---- content ----------------------------------------------------------
    def row(self, s="", align="left"):
        inner = self.center(s, self.w) if align == "center" else self.left(s, self.w)
        self.rows.append("║" + inner + "║")

    def blank(self):
        self.row("")

    def heading(self, text, level=2):
        """h1 gets ═══, h2 gets ───, h3 gets no rule."""
        self.row(text, "center")
        if level == 1:
            self.row("═" * len(text), "center")
        elif level == 2:
            self.row("─" * len(text), "center")

    # ---- checks -----------------------------------------------------------
    def render(self):
        return "\n".join(self.rows)

    def check(self):
        widths = sorted(set(len(r) for r in self.rows))
        ok = widths == [self.w + 2] and not CLIPPED
        report = [
            f"rows: {len(self.rows)}",
            f"widths: {widths} (expected [{self.w + 2}])",
            f"clipped: {CLIPPED if CLIPPED else 'none'}",
            f"RESULT: {'PASS' if ok else 'FAIL'}",
        ]
        return ok, "\n".join(report)


# ---- buttons --------------------------------------------------------------
def button_primary(label):
    inner = f" {label} "
    w = len(inner)
    return ["▛" + "▀" * w + "▜", "▌" + inner + "▐", "▙" + "▄" * w + "▟"]


def button_primary_compact(label):
    return f"▐ {label} ▸ ▌"


def button_secondary(label):
    inner = f"  {label}  "
    return ["┌" + "─" * len(inner) + "┐", "│" + inner + "│", "└" + "─" * len(inner) + "┘"]


# ---- cards ----------------------------------------------------------------
def card(frame, title_lines, body_lines=(), action=None, media=None, cw=14):
    """Three-zone card. Any zone may be omitted. Returns a list of lines."""
    inner = cw - 2
    L = ["┏" + "━" * inner + "┓"]
    if media:
        L.append("┃" + "▒" * inner + "┃")
        L.append("┃" + frame.center(media, inner).replace(" ", "░") + "┃")
        L.append("┃" + "▒" * inner + "┃")
        L.append("┣" + "━" * inner + "┫")
    for t in title_lines:
        L.append("┃" + frame.center(t, inner) + "┃")
    if body_lines:
        L.append("┃" + " " * inner + "┃")
    for b in body_lines:
        L.append("┃" + frame.left(b, inner) + "┃")
    if action:
        L.append("┣" + "━" * inner + "┫")
        L.append("┃" + frame.center(action, inner) + "┃")
    L.append("┗" + "━" * inner + "┛")
    return L


def card_row(frame, cards, gutter=2, align="center"):
    """Lay cards side by side. Pad them to equal height first for a clean row."""
    h = max(len(c) for c in cards)
    for i in range(h):
        segs = [c[i] if i < len(c) else " " * len(c[0]) for c in cards]
        frame.row((" " * gutter).join(segs), align)


def two_col(frame, lcol, rcol, lw, rw, gap=2, lead=2):
    h = max(len(lcol), len(rcol))
    for i in range(h):
        ls = lcol[i] if i < len(lcol) else ""
        rs = rcol[i] if i < len(rcol) else ""
        frame.row(" " * (lead - 1) + frame.clip(ls, lw).ljust(lw) + " " * gap + frame.clip(rs, rw).ljust(rw))


if __name__ == "__main__":
    f = Frame(52)
    f.open(("1", "<site-header>"))
    f.row("BRANDMARK    Work  Writing  About    [ Sign in ]")
    f.region(("2", "<hero>"))
    f.blank()
    f.heading("H E L L O", level=1)
    f.blank()
    f.close()
    print(f.render())
    print()
    print(f.check()[1])
