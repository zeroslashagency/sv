"""Layout containment: bands are full-bleed, reading width is capped inside.

This file exists because of a real defect. `.page` (the `<main>` shell) carried
`max-width: var(--max-content)` plus `margin-inline: auto`, so on any viewport
wider than 1240px the auto margins ate the surplus and the bands could never
reach the viewport edge: ~98px of dead gutter per side at 1435px, 340px at
1920px, 660px at 2560px. It read as an unexplained border down both sides of
the site.

That contradicted the design law. 07_DNA_RM_TEREX.md calls bands "full-bleed"
and specifies a "full-bleed color change between bands", and dna.css's own
section header says "1. BAND -- full-bleed gray stage" -- twenty lines below a
comment claiming "the gray never touches the viewport edge on desktop".

The fix moved the cap off the shell and into the bands, via `--band-inset`.
These checks are the guard rails for that arrangement:

  * the shell must not cap or centre itself again,
  * bands must pad with `--band-inset`, not the raw `--band-pad-x`,
  * `--band-inset` must keep the `--max-content` measure,
  * anything absolutely positioned against the band edge must track the
    same inset, or the S3 label drifts away from the content column.

None of this is checkable by rendering here (the suite is stdlib-only and
browserless), so these are assertions about the CSS source. The geometry was
verified separately in headless Chromium at 375/640/1024/1240/1435/1920/2560px:
every band reported 0px left and right gutter, content stayed on a 493px
measure, and no page overflowed horizontally.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from conftest import BUILD, Result  # noqa: E402

CSS_DIR = os.path.join(BUILD, "assets", "css")


def css(name: str) -> str:
    with open(os.path.join(CSS_DIR, name), encoding="utf-8") as fh:
        return fh.read()


def strip_comments(text: str) -> str:
    """Drop /* ... */ so prose about a retired rule never satisfies a check."""
    return re.sub(r"/\*.*?\*/", "", text, flags=re.S)


def rule_body(text: str, selector: str) -> str | None:
    """The declaration block for an exact standalone selector, comments gone.

    The selector must be the whole selector list, so `.page` cannot return the
    body of `.page > * + *` (trailing guard) and `.dna-band` cannot return
    `.dna-band--navy .dna-frame__label` (leading guard). The character before
    the match must end a previous rule or open a block, never continue a
    selector -- that rules out `,`, `>` and bare descendant combinators.
    """
    pattern = re.escape(selector) + r"\s*\{([^}]*)\}"
    for m in re.finditer(pattern, text):
        before = text[: m.start()].rstrip()
        if before and before[-1] not in "}{;":
            continue
        return m.group(1)
    return None


def run() -> int:
    r = Result("layout")

    tokens = strip_comments(css("tokens.css"))
    dna = strip_comments(css("dna.css"))

    # -- 1. The shell must stay full width -----------------------------------
    page = rule_body(dna, ".page")
    r.check(page is not None, ".page rule exists in dna.css")
    if page is None:
        return r.report()

    r.check("max-width" not in page,
            ".page has no max-width (the gutter regression)",
            "A max-width here plus margin-inline:auto is exactly the defect "
            "this file guards: bands stop reaching the viewport edge above "
            f"the cap. Found: {page.strip()!r}")

    r.check("margin-inline" not in page and "margin:" not in page,
            ".page does not centre itself with a margin",
            f"Found: {page.strip()!r}")

    r.check("padding-inline" not in page,
            ".page carries no inline padding (bands own their inset)",
            f"Found: {page.strip()!r}")

    r.check("width: 100%" in page, ".page spans the viewport")

    # -- 2. Bands must be full-bleed and use the inset -----------------------
    band = rule_body(dna, ".dna-band")
    r.check(band is not None, ".dna-band rule exists")
    if band is not None:
        r.check("max-width" not in band,
                ".dna-band has no max-width (it is the full-bleed fill)",
                f"Found: {band.strip()!r}")
        r.check("margin-inline" not in band,
                ".dna-band is not centred by a margin",
                f"Found: {band.strip()!r}")
        r.check("var(--band-inset)" in band,
                ".dna-band pads with --band-inset",
                "Without it the fill is edge to edge but the copy stretches "
                f"to the full viewport on an ultrawide display. Found: {band.strip()!r}")
        r.check("var(--band-pad-x)" not in band,
                ".dna-band does not pad with the raw --band-pad-x",
                "--band-pad-x tops out at 93px, so content would keep "
                f"widening past --max-content. Found: {band.strip()!r}")

    # -- 3. The inset token must preserve the reading measure ----------------
    m = re.search(r"--band-inset:\s*([^;]+);", tokens, re.S)
    r.check(m is not None, "--band-inset is defined in tokens.css")
    if m is not None:
        value = " ".join(m.group(1).split())
        r.check("var(--max-content)" in value,
                "--band-inset caps content at --max-content",
                f"Found: {value!r}")
        r.check("var(--band-pad-x)" in value,
                "--band-inset keeps a minimum edge pad below the cap",
                f"Found: {value!r}")
        r.check(value.startswith("max("),
                "--band-inset uses max() so it never goes negative",
                "Below --max-content the (100% - max)/2 term is negative; "
                f"max() with --band-pad-x is what floors it. Found: {value!r}")

    # -- 4. Edge-anchored children must track the same inset ----------------
    # The S3 frame and the stage knockout are absolutely positioned against
    # the band's inline edge. If they keep using --band-pad-x while the band
    # pads with --band-inset, the label and counter drift out of the content
    # column on a wide screen -- visible misalignment, not a crash.
    for selector, prop in (
        (".dna-frame", "inset-inline"),
        (".dna-knockout--stage", "inset-inline-start"),
    ):
        body = rule_body(dna, selector)
        r.check(body is not None, f"{selector} rule exists")
        if body is None:
            continue
        decl = re.search(re.escape(prop) + r":\s*([^;]+);", body)
        r.check(decl is not None, f"{selector} sets {prop}")
        if decl is not None:
            val = " ".join(decl.group(1).split())
            r.check("var(--band-inset)" in val,
                    f"{selector} anchors to --band-inset",
                    f"Must track the band's own padding or it misaligns "
                    f"with the content column. Found: {val!r}")

    # -- 5. The narrow override must not reintroduce shell padding ----------
    narrow = re.search(r"@media\s*\(max-width:\s*640px\)\s*\{(.*?)\n\}",
                       dna, re.S)
    r.check(narrow is not None, "the 640px narrow block still exists")
    if narrow is not None:
        inner = narrow.group(1)
        page_override = rule_body(inner, ".page")
        r.check(page_override is None or "padding-inline" not in page_override,
                "the 640px block does not re-pad .page",
                "That override only existed to cancel the shell padding the "
                f"fix removed. Found: {(page_override or '').strip()!r}")

    # -- 6. Nav and footer keep their own full-bleed arrangement ------------
    # These sit outside main.page and paint edge to edge with a capped
    # .container inside. That is now the same strategy the bands use; the
    # check records the agreement so a future edit does not split them again.
    base = strip_comments(css("base.css"))
    components = strip_comments(css("components.css"))
    container = rule_body(base, ".container")
    r.check(container is not None and "max-width" in container,
            ".container still caps content (nav + footer measure)")
    for selector in (".nav", ".footer"):
        body = rule_body(components, selector)
        if body is None:
            r.check(False, f"{selector} rule exists")
            continue
        r.check("max-width" not in body,
                f"{selector} paints full width, capping only its .container",
                f"Found: {body.strip()!r}")

    return r.report()


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
