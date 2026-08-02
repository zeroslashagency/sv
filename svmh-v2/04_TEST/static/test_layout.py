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

    # -- 3. The inset must scale with the viewport, not pin to a fixed px ----
    # A fixed cap here was the second half of the same defect. Removing the
    # shell's max-width made the *fill* full-bleed, but the content stayed on
    # a 1240px measure, so ~280px per side sat empty at 1800px: an edge-to-edge
    # band wrapped around a narrow floating column. The inset has to grow with
    # the viewport for the layout to actually adapt.
    m = re.search(r"--band-inset:\s*([^;]+);", tokens, re.S)
    r.check(m is not None, "--band-inset is defined in tokens.css")
    if m is not None:
        value = " ".join(m.group(1).split())
        r.check("vw" in value,
                "--band-inset scales with the viewport",
                "Without a vw term the content column cannot follow the "
                f"full-bleed fill as the screen widens. Found: {value!r}")
        r.check("var(--max-content)" not in value,
                "--band-inset does not pin content to the fixed --max-content",
                "That is what left dead space either side on a wide screen; "
                f"line length is capped in ch on the text itself. Found: {value!r}")
        r.check(value.startswith("clamp("),
                "--band-inset uses clamp() for a floor and a ceiling",
                f"Found: {value!r}")
        floor = re.match(r"clamp\(\s*(\d+)px", value)
        r.check(floor is not None and int(floor.group(1)) <= 24,
                "--band-inset floors at a small mobile pad (<= 24px)",
                "A large floor wastes horizontal space on a phone, where "
                f"every pixel of measure counts. Found: {value!r}")
        r.check("var(--max-shoulder)" in value,
                "--band-inset ceilings at --max-shoulder",
                f"Found: {value!r}")

    shoulder = re.search(r"--max-shoulder:\s*(\d+)px", tokens)
    r.check(shoulder is not None, "--max-shoulder is defined")
    if shoulder is not None:
        px = int(shoulder.group(1))
        r.check(px <= 260,
                "--max-shoulder stays under 260px",
                "Above that the ultrawide gutter starts reading as the dead "
                f"frame this fix removed. Found: {px}px")

    # --band-pad-x is retired but kept as an alias. If it ever stops
    # resolving to --band-inset, every rule still naming it silently
    # misaligns against the bands.
    pad_x = re.search(r"--band-pad-x:\s*([^;]+);", tokens)
    if pad_x is not None:
        r.check("var(--band-inset)" in " ".join(pad_x.group(1).split()),
                "--band-pad-x aliases --band-inset (retired, kept safe)",
                f"Found: {pad_x.group(1).strip()!r}")

    # -- 4. Edge-anchored children must stay viewport-relative --------------
    # The S3 frame carries the band's label and counter, so it has to track
    # --band-inset exactly: if it keeps using --band-pad-x while the band pads
    # with --band-inset, the label drifts out of the content column on a wide
    # screen -- visible misalignment, not a crash.
    for selector, prop in ((".dna-frame", "inset-inline"),):
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

    # The stage knockout is decorative (aria-hidden) and deliberately does NOT
    # sit on the content column -- it is indented so the product cut-out
    # crosses it, per 07_DNA_RM_TEREX.md S1. So it is not held to --band-inset.
    # What it must not do is use a fixed pixel offset: a design edit captured
    # at 1440px proposed `left: 432px`, which measured 1075px against a 1024px
    # band and 914px against a 768px band -- the glyph run left the band. The
    # requirement is that the offset scales with the viewport.
    ko = rule_body(dna, ".dna-knockout--stage")
    r.check(ko is not None, ".dna-knockout--stage rule exists")
    if ko is not None:
        decl = re.search(r"inset-inline-start:\s*([^;]+);", ko)
        r.check(decl is not None, ".dna-knockout--stage sets inset-inline-start")
        if decl is not None:
            val = " ".join(decl.group(1).split())
            r.check(("vw" in val) or ("var(--band-inset)" in val),
                    ".dna-knockout--stage offset scales with the viewport",
                    "A fixed px offset pushes the glyph run past the band edge "
                    f"on narrow screens. Found: {val!r}")
            r.check(re.fullmatch(r"-?[\d.]+px", val) is None,
                    ".dna-knockout--stage is not pinned to a fixed px offset",
                    f"Found: {val!r}")

        # will-change was present in the captured edit only because the element
        # was mid-drag. Nothing animates top/left at runtime, so a permanent
        # hint would hold a compositor layer for decorative text on every page.
        r.check("will-change" not in ko,
                ".dna-knockout--stage carries no will-change",
                "Drag artifact from a visual edit; it pins a compositor layer "
                f"for no runtime benefit. Found: {ko.strip()!r}")

    # The stage band must stay content-sized. The same captured edit reported
    # `height: 905.215px` on the band; that was the measured height of one
    # viewport, not an intent. A fixed height clips content on narrow screens
    # and strands whitespace on tall ones, so the band keeps its min-height.
    stage = rule_body(dna, ".dna-band--stage")
    r.check(stage is not None, ".dna-band--stage rule exists")
    if stage is not None:
        r.check(re.search(r"(?<!min-)(?<!max-)height:", stage) is None,
                ".dna-band--stage sets no fixed height (stays content-sized)",
                f"Found: {stage.strip()!r}")
        r.check("min-height" in stage,
                ".dna-band--stage keeps a fluid min-height")

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

    # .container wraps the nav rail, the footer and the mobile overlay. It has
    # to share the bands' inset or the wordmark and footer columns sit on a
    # different vertical line than the content below them -- the misalignment
    # is subtle on a laptop and obvious on a wide monitor.
    container = rule_body(base, ".container")
    r.check(container is not None, ".container rule exists")
    if container is not None:
        r.check("var(--band-inset)" in container,
                ".container shares --band-inset with the bands",
                f"Found: {container.strip()!r}")
        r.check("max-width" not in container,
                ".container does not cap itself below the band width",
                "A fixed cap here leaves the nav narrower than the bands "
                f"once the viewport passes it. Found: {container.strip()!r}")
    for selector in (".nav", ".footer"):
        body = rule_body(components, selector)
        if body is None:
            r.check(False, f"{selector} rule exists")
            continue
        r.check("max-width" not in body,
                f"{selector} paints full width, capping only its .container",
                f"Found: {body.strip()!r}")

    # ------------------------------------------------------------------
    # 7. The header CTA must actually disappear below 1024px.
    #
    # `.nav__cta { display: none }` sits at the top of components.css and
    # `.btn { display: inline-flex }` roughly 500 lines below it. Both are
    # single-class selectors, so they tie on specificity and source order
    # decides -- .btn wins. Three of the four built pages write
    # `class="btn nav__cta"`, so the mobile hide silently did nothing: at 390px
    # the CTA stayed in the header, wrapped onto two lines and crowded the
    # burger, duplicating the quote action already in .mobile-bar and the
    # overlay foot. Scoping both halves of the pair to `.nav .nav__cta` raises
    # them above .btn. These checks fail if either half loses that scope.
    # ------------------------------------------------------------------
    raw = css("components.css")

    r.check(re.search(r"(?<![\w.-])\.nav\s+\.nav__cta\s*\{\s*display:\s*none", raw)
            is not None,
            ".nav__cta hide rule is scoped .nav .nav__cta so it outranks .btn",
            "A bare `.nav__cta { display: none }` ties with `.btn { display: "
            "inline-flex }` and loses on source order, leaving the CTA visible "
            "on phones.")

    # The show rule must carry the same scope, otherwise the pair is asymmetric
    # and the desktop CTA loses its copper cell to .btn's own background.
    #
    # components.css has several `min-width: 1024px` blocks, so this walks
    # braces to find the one that actually mentions the CTA rather than
    # regex-matching the first block and reading the nav menu by accident.
    def media_blocks(text: str, query: str) -> list[str]:
        """Bodies of every @media block whose condition contains `query`."""
        out = []
        for m in re.finditer(r"@media([^{]*)\{", text):
            if query not in m.group(1):
                continue
            depth, i = 1, m.end()
            while i < len(text) and depth:
                if text[i] == "{":
                    depth += 1
                elif text[i] == "}":
                    depth -= 1
                i += 1
            out.append(text[m.end():i - 1])
        return out

    desktop = [b for b in media_blocks(raw, "1024px") if ".nav__cta" in b]
    r.check(len(desktop) == 1,
            "exactly one 1024px block reveals the nav CTA",
            f"Found {len(desktop)}. Two blocks styling it invites drift.")
    for block in desktop:
        r.check(re.search(r"(?<![\w.-])\.nav\s+\.nav__cta\s*\{", block) is not None,
                "the 1024px reveal is scoped to match the hide rule",
                "Hide and show must share a scope or they can be won by "
                "different rules at different widths.")
        r.check("display: flex" in block,
                "the 1024px block restores the CTA to display: flex")

    # Every page has to agree on the class, or the CTA behaves differently
    # page to page for reasons invisible in the CSS.
    import glob
    pages = sorted(glob.glob(os.path.join(BUILD, "**", "*.html"), recursive=True))
    r.check(len(pages) >= 4, "built pages found for nav CTA audit",
            f"Found {len(pages)}")
    for path in pages:
        rel = os.path.relpath(path, BUILD)
        with open(path, encoding="utf-8") as fh:
            html = fh.read()
        if "nav__cta" not in html:
            continue
        # The CTA is a 44px-min-height tap target only because of .btn
        # (WCAG 2.5.8). double-girder.html shipped without it.
        r.check(re.search(r'class="btn nav__cta"', html) is not None,
                f"{rel}: nav CTA keeps the btn class for its 44px tap target",
                "Without `btn` the link loses min-height: 44px.")

    return r.report()


if __name__ == "__main__":
    raise SystemExit(1 if run() else 0)
