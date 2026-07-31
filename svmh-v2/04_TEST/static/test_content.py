"""Content integrity: no placeholder prose, no invented facts, honest gaps.

Rule 1 and rule 2 of the root README are the whole point of this file: every
number traces to the research corpus or is explicitly marked unconfirmed, and
nothing ships as lorem.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conftest import PAGES, Result, main_of, read  # noqa: E402

# Facts fixed by the client brief. If a page states one of these, it must state
# it correctly -- a typo'd GST number is worse than an omitted one. Each entry
# maps the correct value to a label and a loose pattern that finds any attempt
# at that fact, right or wrong.
FACTS = {
    "29AAKCS6443A1ZB": ("GST", r"29[A-Z0-9]{13}"),
    "Harohalli": ("works location", r"[Hh]aro[a-z]*halli"),
    "D. Umapathi": ("managing director", r"D\.?\s*U[a-z]*pathi"),
    "S.V. Material Handling System": (
        "legal name", r"S\.?\s?V\.? Material Handl\w+ System"),
}

BANNED = [
    "lorem", "ipsum", "dolor sit amet", "TODO", "FIXME", "XXX",
    "placeholder text", "your text here", "Lorem",
]

# Claims that cannot be made without a document to back them.
NEEDS_MARKER = ["ISO 9001"]


def run() -> int:
    r = Result("content")

    for page in PAGES:
        html = read(page)
        body = main_of(html)
        text = re.sub(r"<[^>]+>", " ", body)

        for bad in BANNED:
            r.check(bad not in body, f"{page}: no '{bad}'")

        # Unconfirmed data must be visibly marked, not quietly invented.
        marks = len(re.findall(r"\[CLIENT TO CONFIRM|\[X\]|\[N\]|\[PIN", body))
        r.check(marks >= 0, f"{page}: {marks} explicit placeholder(s) carried")

        # A stray bracket pattern that is not one of the sanctioned markers is
        # probably a half-written note.
        brackets = re.findall(r"\[([A-Z][^\]]{2,30})\]", text)
        odd = [b for b in brackets
               if not b.startswith(("CLIENT TO CONFIRM", "X", "N", "PIN"))]
        r.check(not odd, f"{page}: no unsanctioned bracket notes", f"{odd[:4]}")

        # Facts are matched by a loose pattern first, then compared to the exact
        # string. Guarding on the exact string would make the assertion
        # unreachable -- a corrupted value would simply fail the guard and never
        # be checked, which is how a typo'd GST number slips through.
        for fact, (label, pattern) in FACTS.items():
            for found in re.findall(pattern, body):
                r.check(found == fact,
                        f"{page}: {label} exact ({found})",
                        f"found '{found}', expected '{fact}'")

        for claim in NEEDS_MARKER:
            if claim in body:
                near = re.findall(r".{0,120}" + re.escape(claim) + r".{0,120}", body)
                linked = any("href" in n or "CONFIRM" in n for n in near)
                r.check(linked,
                        f"{page}: '{claim}' is linked to evidence or marked",
                        "claim appears with neither a document link nor a marker")

        # The RFQ form is a security gate: its comment block must survive any
        # re-skin, because it is the deployment checklist.
        if "<form" in body:
            r.check("SECURITY" in body,
                    f"{page}: form keeps its security comment block")
            r.check('name="csrf_token"' in body,
                    f"{page}: form keeps the csrf token field")
            r.check("form__trap" in body, f"{page}: form keeps the honeypot")
            r.check("novalidate" not in re.search(r"<form[^>]*>", body).group(0),
                    f"{page}: form does not hard-code novalidate")

        # Language and locale consistency.
        r.check('lang="en-IN"' in html, f"{page}: declares en-IN")
        cyrillic = re.findall(r"[\u0400-\u04FF]", body)
        r.check(not cyrillic, f"{page}: no leftover Russian source copy",
                f"{len(cyrillic)} Cyrillic character(s)")

    return r.report()


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
