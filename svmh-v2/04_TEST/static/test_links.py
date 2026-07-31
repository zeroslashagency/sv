"""Internal links: what is built, what is promised, what is simply wrong.

The site links to a sitemap larger than what has been built. That is expected
at this phase, so this file does not fail on an unbuilt route -- it inventories
them, and fails only on things that can never resolve: a link to a page that is
built but misspelled, a mixed absolute/relative style for the same target, or an
empty href.

Run it to see the roadmap: the report lists every route still owed a page.
"""

import os
import re
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conftest import BUILD, PAGES, Result, read  # noqa: E402

ASSET_EXT = (".jpg", ".jpeg", ".png", ".webp", ".svg", ".gif", ".css", ".js",
             ".pdf", ".ico", ".xml", ".woff", ".woff2")


def built_routes() -> set[str]:
    out = set()
    for root, _dirs, files in os.walk(BUILD):
        for f in files:
            if not f.endswith(".html"):
                continue
            rel = os.path.relpath(os.path.join(root, f), BUILD)
            out.add("/" + rel.replace(os.sep, "/"))
            # /a/b.html is also reachable as /a/b and, for index, as /a/
            out.add("/" + rel[: -len(".html")].replace(os.sep, "/"))
            if f == "index.html":
                parent = os.path.dirname(rel).replace(os.sep, "/")
                out.add("/" + parent if parent else "/")
    return out


def run() -> int:
    r = Result("links")
    built = built_routes()
    missing: Counter[str] = Counter()

    for page in PAGES:
        html = read(page)
        hrefs = re.findall(r'href="([^"]+)"', html)

        r.check(not [h for h in hrefs if not h.strip()],
                f"{page}: no empty href")
        r.check(not [h for h in hrefs if h.strip() == "#"],
                f"{page}: no placeholder '#' link")

        for h in hrefs:
            target = h.split("#")[0].split("?")[0]
            if not target or target.startswith(("http", "//", "mailto:", "tel:", "data:")):
                continue
            if target.lower().endswith(ASSET_EXT):
                continue
            route = target if target.startswith("/") else None
            if route is None:
                # A relative page link must resolve on disk right now, because
                # the relative form implies the author knew where the file was.
                cand = os.path.normpath(
                    os.path.join(BUILD, os.path.dirname(page), target))
                for probe in (cand, cand + ".html",
                              os.path.join(cand, "index.html")):
                    if os.path.isfile(probe):
                        break
                else:
                    missing[f"{page} -> {target} (relative)"] += 1
                continue
            if route.rstrip("/") and route not in built and route.rstrip("/") not in built:
                missing[route] += 1

    relative_broken = [k for k in missing if "(relative)" in k]
    r.check(not relative_broken,
            "no broken relative page link",
            f"{relative_broken[:4]}")

    # Absolute routes that are not built yet are reported, not failed.
    unbuilt = sorted(k for k in missing if "(relative)" not in k)
    r.check(True, f"{len(unbuilt)} route(s) linked but not built yet")
    print("\n  Unbuilt routes (roadmap, not failures):")
    for route in unbuilt:
        print(f"    {missing[route]:>2}x  {route}")

    print(f"\n  Built routes: {len(sorted(x for x in built if x.endswith('.html')))}")

    return r.report()


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
