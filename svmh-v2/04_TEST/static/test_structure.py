"""Document structure: headings, landmarks, stylesheet load order, page inventory.

These are the checks that fail loudly if a page is rebuilt from the wrong
template or a stylesheet gets inserted in the wrong place.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conftest import PAGES, Result, load_fixture, main_of, read  # noqa: E402

CSS_ORDER = ["tokens.css", "base.css", "components.css", "dna.css"]


def run() -> int:
    r = Result("structure")
    expected = load_fixture("pages.json")

    for page in PAGES:
        html = read(page)
        body = main_of(html)
        exp = expected.get(page, {})

        r.check(html.count("<h1") == 1, f"{page}: exactly one h1",
                f"found {html.count('<h1')}")
        r.check(bool(body), f"{page}: has a <main>")
        r.check('id="main"' in html, f"{page}: main is the skip-link target")
        r.check('class="page"' in html, f"{page}: main carries the .page shell")

        # Stylesheets must load tokens -> base -> components -> dna, because
        # dna.css intentionally overrides the earlier layers.
        found = [c for c in CSS_ORDER if f"css/{c}" in html]
        idx = [html.find(f"css/{c}") for c in found]
        r.check(found == CSS_ORDER, f"{page}: all four stylesheets linked",
                f"found {found}")
        r.check(idx == sorted(idx), f"{page}: stylesheet order is tokens->dna",
                f"positions {idx}")

        # One <header>, one <footer>, one nav landmark set: the furniture was
        # meant to be preserved byte-for-byte across the re-skin.
        r.check(html.count("<header") == 1, f"{page}: single header")
        r.check(html.count("<footer") == 1, f"{page}: single footer")
        r.check('class="skip-link"' in html, f"{page}: skip link present")

        # Heading order: no level skipped inside main.
        levels = [int(m) for m in re.findall(r"<h([1-6])\b", body)]
        jumps = [(a, b) for a, b in zip(levels, levels[1:]) if b - a > 1]
        r.check(not jumps, f"{page}: no heading level skipped in main",
                f"jumps {jumps}")

        if exp:
            r.check(html.count("<h1") == exp["h1_count"],
                    f"{page}: h1 count matches fixture")
            r.check(body.count("dna-band--navy") == exp["navy_bands"],
                    f"{page}: navy band count matches fixture")
            bands = len(re.findall(r'class="dna-band', body))
            r.check(bands == exp["bands"],
                    f"{page}: band count matches fixture "
                    f"(expected {exp['bands']})",
                    f"found {bands}")

            # Fields captured in the fixture but previously never compared. An
            # unasserted fixture field reads as coverage without being any.
            r.check(html.count("dna-panel--navy") == exp["navy_panels"],
                    f"{page}: navy panel count matches fixture")
            r.check(body.count("dna-frame__label") == exp["frames"],
                    f"{page}: S3 frame count matches fixture "
                    f"(expected {exp['frames']})",
                    f"found {body.count('dna-frame__label')}")
            counters = re.findall(
                r"<b>(\d+)</b><span class=\"dna-frame__rule\"></span>(\d+)", html)
            r.check([int(n) for n, _ in counters] == exp["counter_steps"],
                    f"{page}: counter sequence matches fixture")
            r.check((counters[0][1] if counters else None) == exp["counter_total"],
                    f"{page}: counter total matches fixture")
            current = re.search(r"<title>(.*?)</title>", html, re.S)
            r.check(bool(current) and current.group(1).strip() == exp["title"],
                    f"{page}: title unchanged from fixture",
                    f"got {current.group(1).strip() if current else None!r}")

    return r.report()


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
