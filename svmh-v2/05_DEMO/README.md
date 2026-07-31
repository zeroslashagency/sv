# 05_DEMO — not the application

Everything in this folder is a **draft or exploration**. None of it ships, none
of it is served, and nothing in `03_BUILD` may link to it.

The application is `03_BUILD/`. If you are looking for the real site, that is
the only folder that matters.

## Why this folder exists

Drafts kept turning up inside `.agents/artifacts/`, mixed in with agent working
notes, where they read like production pages. They use an older design system,
they reference images that were never produced, and two of them are named
`index.html`. That is exactly the mix that gets the wrong file opened, measured,
or copied forward. Quarantining them makes the distinction structural instead of
something you have to remember.

## What is in here

### `pre-dna-agent-drafts/`

Three pages produced by the `page-builder-alpha` agent before the design
direction changed to the DNA system in `01_DESIGN/07_DNA_RM_TEREX.md`.

| File | Was meant to become | Why it is not the app |
|---|---|---|
| `index.html` | Homepage | Pre-DNA: `.hero`, `.trust-strip`, `.stat`, `.band band--*`. No `.dna-*` markup at all |
| `eot-cranes-index.html` | EOT category page | Same vocabulary; category pages are still unbuilt |
| `gantry-cranes-index.html` | Gantry category page | Same |

Between them the three drafts reference **seven** images that do not exist and
never did: `hero-double-girder-eot-crane.jpg`, `double-girder-eot-crane.jpg`,
`goliath-gantry-crane.jpg`, `ladle-crane-foundry.jpg`,
`single-girder-eot-crane.jpg`, `single-leg-gantry.jpg` and
`semi-gantry-crane.jpg`. Their `alt` text states
capacities and spans ("50 T on a 24 m span", "40 T on an 18 m span") that no
photograph in the corpus can support, which is why the copy was not carried
across either. Opening them in a browser shows a broken layout with four missing
images. That is expected.

## Still useful for one thing

The **copy** in the two category drafts is the only written material that exists
for `/eot-cranes` and `/gantry-cranes`. When those pages get built, read the
prose here, verify each claim against `../../research/`, then write fresh markup
in the DNA grammar. Do not copy the HTML.

## Rules

1. Nothing here is served. `04_TEST` deliberately does not scan this folder.
2. No page in `03_BUILD` links here.
3. A draft that gets promoted is **rewritten** in `03_BUILD`, not moved.
4. When a draft's replacement ships, delete the draft. This folder should shrink.
