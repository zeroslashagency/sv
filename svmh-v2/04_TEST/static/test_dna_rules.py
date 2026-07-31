"""The 01_DESIGN/07_DNA_RM_TEREX.md rules, expressed as assertions.

The design doc is the authority; this file is its enforcement. If a rule here
disagrees with the doc, the doc wins and this file is the bug.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conftest import PAGES, Result, main_of, read  # noqa: E402

# The DNA surface palette from 07_DNA_RM_TEREX.md §2.
DNA_COLORS = {
    "#EFEFEF", "#E7E7E7", "#FFFFFF", "#1E3A6B", "#162C52", "#1A1D21",
    "#8A8F96", "#DEDEDE", "#5A6067", "#B2B5C6",
}
# Permitted outside the surface palette: darker ink steps used for inverted
# text surfaces, and the three semantic status colours the form needs. These are
# not decorative choices, so they are not part of the accent budget.
UTILITY_COLORS = {
    "#202429", "#2A2F35",          # ink steps
    "#2F6F4E", "#8A6A1F", "#9E3535",  # safe / warn / alert
}
# Retired names that may survive only as a remap onto a DNA value, never as a
# live colour of their own.
RETIRED = ["copper", "concrete"]


def run() -> int:
    r = Result("dna rules")

    for page in PAGES:
        html = read(page)
        body = main_of(html)

        # S1 — knockout wordmarks are decorative, so they must be hidden from
        # assistive tech. Giant white-on-grey type fails contrast by design and
        # is only permitted because it is not content.
        knockouts = re.findall(r"<\w+[^>]*class=\"[^\"]*dna-knockout[^\"]*\"[^>]*>", html)
        r.check(bool(knockouts), f"{page}: has at least one S1 knockout")
        bad = [k for k in knockouts if 'aria-hidden="true"' not in k]
        r.check(not bad, f"{page}: every knockout is aria-hidden",
                f"{len(bad)} exposed to screen readers")

        # S3 — the label/counter frame. Counters must be sequential against a
        # single consistent total, or the "slide N of M" story breaks.
        counters = re.findall(
            r"<b>(\d+)</b><span class=\"dna-frame__rule\"></span>(\d+)", html)
        totals = {t for _, t in counters}
        nums = [int(n) for n, _ in counters]
        r.check(bool(counters), f"{page}: has S3 counters")
        r.check(len(totals) <= 1, f"{page}: one counter total",
                f"totals seen: {sorted(totals)}")
        r.check(nums == sorted(nums), f"{page}: counters ascend", f"{nums}")
        r.check(nums == list(range(1, len(nums) + 1)),
                f"{page}: counters have no gaps",
                f"{nums} -- expected 1..{len(nums)}")
        if totals:
            r.check(int(totals.pop()) == len(nums),
                    f"{page}: counter total equals the number of framed bands",
                    f"{len(nums)} framed bands")

        # Accent budget — at most one inverted navy band per page, and never two
        # adjacent inverted surfaces.
        r.check(body.count("dna-band--navy") <= 1,
                f"{page}: at most one inverted navy band",
                f"found {body.count('dna-band--navy')}")
        fills = re.findall(r'class="dna-band([^"]*)"', body)
        adjacent = [(a, b) for a, b in zip(fills, fills[1:])
                    if "--navy" in a and "--navy" in b]
        r.check(not adjacent, f"{page}: no two adjacent navy bands")

        # S4 — the last panel in a three-up row is the filled one, and only one
        # panel per row is inverted.
        for row in re.findall(r"<ol[^>]*dna-panels.*?</ol>", body, re.S):
            panels = re.findall(r'<li class="dna-panel([^"]*)"', row)
            navy = [i for i, p in enumerate(panels) if "--navy" in p]
            r.check(len(navy) <= 1, f"{page}: one navy panel per row",
                    f"navy at {navy} of {len(panels)}")
            if navy:
                r.check(navy[0] == len(panels) - 1,
                        f"{page}: the navy panel is the last one",
                        f"navy at index {navy[0]} of {len(panels) - 1}")

        # §7 rejects — no boxed hero photo behind text, no legacy shells.
        for legacy in ('class="hero"', "trust-strip", 'class="band band--'):
            r.check(legacy not in body, f"{page}: no legacy {legacy} in main")

        # Surfaces carry no ornament of their own.
        r.check("style=\"border" not in body,
                f"{page}: no inline border in main")
        r.check("border-radius" not in body,
                f"{page}: no inline radius in main")

    # --- CSS-level rules ---------------------------------------------------
    dna = read("assets/css/dna.css")
    tokens = read("assets/css/tokens.css")

    for word in RETIRED:
        # A retired name is acceptable only when its value points at a DNA
        # token, an rgba() built from navy, or transparent. A raw warm hex on
        # one of these lines means the old system is still alive.
        # Strip comments first: the file's own header explains what was retired,
        # and prose about the retirement is not a live declaration.
        code = re.sub(r"/\*.*?\*/", "", tokens, flags=re.S)
        live = []
        for ln in code.splitlines():
            stripped = ln.strip()
            if word not in stripped.lower() or not stripped.startswith("--"):
                continue
            if ":" not in stripped:
                continue
            value = stripped.split(":", 1)[1]
            remapped = ("var(--color-navy" in value or "var(--color-canvas" in value
                        or "transparent" in value
                        or re.search(r"rgba\(\s*30,\s*58,\s*107", value)
                        or (re.search(r"#[0-9A-Fa-f]{6}", value)
                            and re.search(r"#[0-9A-Fa-f]{6}", value).group(0).upper()
                            in DNA_COLORS))
            if not remapped:
                live.append(stripped)
        r.check(not live, f"tokens.css: '{word}' survives only as a remap",
                f"live: {live[:3]}")

    hexes = {h.upper() for h in re.findall(r"#[0-9A-Fa-f]{6}", tokens)}
    off = hexes - DNA_COLORS - UTILITY_COLORS
    r.check(not off, "tokens.css uses only the DNA palette plus known utilities",
            f"unexpected {sorted(off)}")

    radii = re.findall(r"--radius-[a-z]+:\s*([^;]+);", tokens)
    r.check(all("0px" in v for v in radii), "every radius token is 0px", f"{radii}")

    shadows = re.findall(r"--elevation-[a-z]+:\s*([^;]+);", tokens)
    r.check(all(v.strip() == "none" for v in shadows),
            "no elevation shadows", f"{shadows}")

    # The only permitted 1px marks: the S3 counter rule, form field underlines,
    # and the dotted table leader. Everything else uses fill changes.
    rule_uses = len(re.findall(r"var\(--color-rule\)", dna))
    r.check(rule_uses <= 6, "the 1px rule token stays rare",
            f"used {rule_uses} times in dna.css")

    return r.report()


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
