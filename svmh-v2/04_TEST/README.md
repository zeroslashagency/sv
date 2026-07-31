# 04_TEST — verification suite

Checks that run against `../03_BUILD`. No framework, no dependencies beyond
Python 3 stdlib, matching the "static only, no build step" rule in the root
README.

## Layout

```
04_TEST/
├── README.md              ← you are here
├── run.sh                 ← run everything; exits non-zero on failure
├── conftest.py            ← shared helpers: page list, parsing, asset resolution
├── static/                ← no browser needed, reads the files on disk
│   ├── test_structure.py    one <h1>, css load order, landmark/heading sanity
│   ├── test_assets.py       every src/href resolves; declared w/h match real pixels
│   ├── test_dna_rules.py    the 07_DNA_RM_TEREX.md §8 checklist, as assertions
│   └── test_content.py      no lorem, no invented facts, placeholders intact
├── render/                ← needs a served page + a browser (chrome-devtools MCP)
│   ├── README.md            how to drive these, since they are not self-running
│   └── viewport_matrix.md   the widths to check and what must hold at each
├── fixtures/              ← expected values the static tests compare against
│   ├── pages.json           the page inventory: path, title, counters, band count
│   └── asset_manifest.json  every asset, its category, real pixel dimensions
└── reports/               ← run output lands here, gitignored
```

## Run it

```bash
cd 04_TEST && ./run.sh
```

`run.sh` starts its own server on a free port, runs the static suite, writes
`reports/latest.txt`, and cleans up. It does not need the long-running dev
server from the root README.

## The split, and why

**static/** is the gate. Roughly 60 assertion sites expand to about 430 reported
checks across the four pages. It is fast, deterministic, and catches the class of
bug that actually happened during this build: a page referencing an asset that
does not exist, a cut-out being upscaled past its native width, a heading
colliding with an absolutely-positioned label, copper surviving in a palette
that retired it.

**render/** is the part a script cannot honestly do here. Layout collision,
paint order and "does the knockout actually read as decorative" need a real
browser, driven through the chrome-devtools MCP tools. Those steps are written
down as a procedure rather than pretended to be automated.

**fixtures/** holds the expected state so a test failure says *what changed*,
not just *something is off*. Regenerate with `python3 conftest.py --refresh`
after an intentional change, and read the diff before committing it. Every field
captured in a fixture is asserted against — an unasserted field would read as
coverage without being any.

## Trusting it

The suite is mutation-tested: break something on purpose, confirm the run turns
red, restore it. Verified catches include a renamed asset, a wrong declared
width, a second `<h1>`, a second navy band, a knockout losing `aria-hidden`,
swapped stylesheet order, `lorem` in the copy, a typo'd GST number, a counter
gap, a form losing its honeypot, and a retired colour returning to the tokens.
If you add a check, break the thing it guards and watch it fail before you
believe it.
