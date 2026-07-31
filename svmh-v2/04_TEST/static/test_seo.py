"""SEO plumbing: canonical origin, JSON-LD validity, sitemap truthfulness.

Added after a review found three different origins in use across four pages,
including a `svmh.example` placeholder that had reached the structured data.
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conftest import BUILD, PAGES, Result, read  # noqa: E402

ORIGIN = "https://www.svind.co.in"
# The form endpoint is a different host on purpose.
ALLOWED_HOSTS = {ORIGIN, "https://forms.svind.co.in"}
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"


def run() -> int:
    r = Result("seo")

    for page in PAGES:
        html = read(page)

        canon = re.search(r'<link rel="canonical" href="([^"]+)"', html)
        r.check(bool(canon), f"{page}: declares a canonical URL")
        if canon:
            r.check(canon.group(1).startswith(ORIGIN),
                    f"{page}: canonical uses the one canonical origin",
                    f"got {canon.group(1)}")

        # Any absolute svind/example host anywhere in the page -- including
        # inside structured data -- must be one of the two allowed.
        hosts = {m for m in re.findall(r"https?://[a-z0-9.-]+", html)}
        offenders = sorted(h for h in hosts
                           if h not in ALLOWED_HOSTS
                           and ("svind" in h or "svmh" in h or "example" in h))
        r.check(not offenders, f"{page}: no stray or placeholder host",
                f"{offenders}")

        # Structured data must parse. A broken block is invisible until a
        # search engine silently drops it.
        blocks = re.findall(
            r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
        r.check(bool(blocks), f"{page}: has structured data")
        for i, b in enumerate(blocks):
            try:
                json.loads(b)
                ok, why = True, ""
            except json.JSONDecodeError as exc:
                ok, why = False, str(exc)
            r.check(ok, f"{page}: JSON-LD block {i} parses", why)

        title = re.search(r"<title>(.*?)</title>", html, re.S)
        desc = re.search(r'<meta name="description" content="([^"]*)"', html)
        r.check(bool(title) and 15 <= len(title.group(1)) <= 75,
                f"{page}: title length is sane",
                f"{len(title.group(1)) if title else 0} chars")
        r.check(bool(desc) and 50 <= len(desc.group(1)) <= 320,
                f"{page}: description length is sane",
                f"{len(desc.group(1)) if desc else 0} chars")

    # --- sitemap ------------------------------------------------------------
    path = os.path.join(BUILD, "sitemap.xml")
    r.check(os.path.isfile(path), "sitemap.xml exists")
    if os.path.isfile(path):
        try:
            root = ET.parse(path).getroot()
            locs = [e.text for e in root.iter(f"{SITEMAP_NS}loc")]
            ok, why = True, ""
        except ET.ParseError as exc:
            locs, ok, why = [], False, str(exc)
        r.check(ok, "sitemap.xml is valid XML", why)

        built = set()
        for base, dirs, files in os.walk(BUILD):
            dirs[:] = [d for d in dirs if not d.startswith((".", "assets"))]
            for f in files:
                if f.endswith(".html"):
                    rel = os.path.relpath(os.path.join(base, f), BUILD)
                    route = "/" + rel.replace(os.sep, "/")
                    route = route[: -len("index.html")] if route.endswith(
                        "/index.html") else route[: -len(".html")]
                    built.add(ORIGIN + (route or "/"))

        # A sitemap must not advertise a page that does not exist, and must not
        # omit one that does.
        r.check(set(locs) <= built | {ORIGIN + "/"},
                "sitemap lists only pages that exist",
                f"phantom: {sorted(set(locs) - built - {ORIGIN + '/'})}")
        r.check(built <= set(locs),
                "sitemap lists every built page",
                f"missing: {sorted(built - set(locs))}")
        r.check(all(loc.startswith(ORIGIN) for loc in locs),
                "every sitemap URL uses the canonical origin")

    return r.report()


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
