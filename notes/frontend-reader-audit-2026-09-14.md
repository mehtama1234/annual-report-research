# Reader presentation audit — 2026-09-14

Scope: the local research reader at `http://localhost:8765/` and the mobile
company-framework index.

Capture run: `CHROME_BIN=/home/mehtama1/.cache/ms-playwright/chromium-1140/chrome-linux/chrome node scripts/check-reader-browser.mjs`

## Packet Inputs Used

- the local reader at `site/reader.html`, `site/reader.js`, and `site/reader.css`;
- the running reader API and its current article catalog; and
- the browser capture and interaction checks in `scripts/check-reader-browser.mjs`.

Accepted screenshots from the current run:

- `/tmp/research-reader-browser-5wsxP0/desktop.png`
- `/tmp/research-reader-browser-5wsxP0/mobile.png`
- `/tmp/research-reader-browser-5wsxP0/article.png`
- `/tmp/research-reader-browser-5wsxP0/comparison.png`
- `/tmp/research-reader-browser-5wsxP0/framework-index.png`

## Flow findings

1. **Landing page — healthy.** The opening statement explains the purpose in
   ordinary language. Three evidence-backed findings now appear before the
   theme directory, so a reader encounters a conclusion before choosing a
   sector route. The cards retain the company, period, fact, meaning, and
   unresolved question.

2. **Company article — healthy.** The article begins with an “In brief”
   explanation before the format, read time, date, source trail, and coverage
   metadata. This gives a reader the argument before asking them to interpret
   the accounting detail.

3. **Comparison article — healthy.** The comparison title and opening claim
   are visible before the evidence status. The page identifies the reporting
   period, the links present in that dossier, the questions addressed, and the
   underlying company studies. The reader deliberately calls these “links in
   this dossier” so the count is not mistaken for the complete packet-level
   source inventory.

4. **Framework index on mobile — healthy.** The index explains what the pages
   contain, distinguishes the two worked examples from the packet-backed pages,
   and remains readable at 390px without horizontal overflow.

5. **Article reading order — healthy after the latest pass.** Company,
   explanation, and comparison pages now add a short “How to use this
   study/comparison” block after the title, plain-language summary, and
   evidence metadata. It gives the reader three explicit actions: read the
   claim, check how the business and cash work, and read the open tests. The
   comparison version additionally tells the reader to identify what differs
   between the companies. The block is inside the article flow and stacks
   cleanly on mobile.

6. **Publication front door — healthy after the latest pass.** The opening
   screen now offers two distinct next steps: “Read three findings” for a
   conclusion-first visit and “Browse the full library” for a search-first
   visit. Both routes are visible alongside the archive counts, so a new
   reader does not have to infer where the editorial material begins.

7. **Energy lane handoff — healthy after the latest pass.** The homepage now
   exposes the broader “Power demand: recovery, control points and execution”
   comparison in the Energy and infrastructure lane. It links NextEra, ONEOK,
   Vertiv, Equinix, MasTec, Sterling, Comfort Systems, and EMCOR to the same
   power-demand synthesis, while the separate Exelon/AEP card remains available
   for the narrower regulated-recovery question.

## Accessibility and interaction checks

- The browser check passed desktop and mobile widths with no horizontal
  overflow.
- The reader check passed article navigation, search restore, empty search
  state, complete-coverage filtering, external-only source boundaries, and
  framework-index mobile layout.
- The latest capture set is `/tmp/research-reader-browser-5wsxP0/`; the
  desktop, mobile, article, comparison, and framework-index captures were
  inspected after the reading-order and energy-lane changes.
- The browser harness also checks the private-capital and regulated-wires
  comparison anchors, including the latter’s numeric heading ID.
- It also checks the power-demand synthesis bridge for its heading, eight
  company rows, eight dossier links, and explicit non-ranking language after
  the table is wrapped for mobile scrolling.
- Skip navigation, visible keyboard focus styles, labeled search, semantic
  headings, and expandable contents/glossary sections are present in the
  rendered surface.

## Limits

This is a rendered-surface audit. It does not establish full screen-reader
quality, color-contrast compliance under every browser setting, performance
under slow networks, or the factual quality of each underlying research claim.
Those require separate automated and manual checks.

## Skeptical Reader Test

A skeptical reader should be able to reach a concrete finding, open the
underlying company or comparison page, see the reporting period and evidence
route, and distinguish an open question from a settled conclusion. The audit
does not treat a passing layout check as proof that the research claim itself
is correct.

## Maintenance checks

Re-run the repository control surface with:

```text
bash scripts/verify-insight-system.sh
```
