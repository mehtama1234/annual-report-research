# Frontend reader audit — 2026-09-15

This audit covers the local research reader at `http://localhost:8765/`.
Screenshots were captured from the current rendered application after the
theme-directory orientation change. They are stored beside this note.

## Packet Inputs Used

- the rendered local reader at `http://localhost:8765/`;
- the current `site/reader.html`, `site/reader.js`, and `site/reader.css`;
- screenshots captured during this audit run; and
- the browser, scenario-register, cross-framework, and insight-system checks
  listed below.

## Flow and evidence

1. **Home page, desktop** — healthy. The opening statement, three worked
   findings, reading path, method, research status, concepts, themes,
   comparisons and watchlist form a readable editorial sequence. The new
   “Choose a theme, then a company” heading makes the theme directory's role
   clear before the reader reaches Theme 01.
   Screenshot: `01-home-full.png`.

2. **Home page, mobile** — healthy. The navigation wraps without horizontal
   overflow, the headline remains readable, and the first action links remain
   visible without requiring a menu interaction.
   Screenshot: `02-home-mobile.png`.

3. **Company article, mobile** — healthy. The page leads with the title and
   plain-language “In brief” section, then shows format, date, evidence source,
   coverage, reading order, and the article. The table wrapper and glossary are
   available for technical material.
   Screenshot: `03-article-mobile.png`.

4. **Comparison article, mobile** — healthy. The comparison is presented as a
   question, retains the same evidence and reading-order treatment, and links
   back to the company studies.
   Screenshot: `04-comparison-mobile.png`.

## Findings

- The homepage now has a dedicated integrated-investment-research review path
  that routes readers from the current synthesis and detailed goal through the
  Wheaton–Antamina, retail affordability, and Apollo–Athene pilots, then to the
  source/theme handoffs, completion audit, and next-evidence queue. The browser
  suite checks the section heading, six review cards, and the core pilot/audit
  links in the rendered page.

- The strongest editorial choice is the repeated causal order: what the
  business does, how activity becomes cash, what can distort the result, what
  the valuation requires, and what to check next.
- The three homepage findings now represent the newest cross-sector work:
  WESCO's backlog-to-cash gap, State Street's client-assets boundary, and
  Brookdale's operator burden. Each card preserves the period, exact fact,
  interpretation, and unresolved filing question.
- The visible language is mostly everyday wording. Technical terms that remain
  necessary are defined in the article glossary rather than assumed.
- The home page distinguishes a deep company study from the broader framework
  index, which prevents the roster pages from being presented as equally deep.
- A reader-facing language pass replaces early research shorthand such as
  “denominator,” “qualified,” and “framework index” with plain descriptions;
  the technical terms remain available inside the articles and glossary.
- Software, data, and recurring workflows now have a first-class homepage
  theme and research-status lane, linking Adobe, ServiceNow, Snowflake, and
  Cloudflare to the existing first-principles explanations.
- The comparison directory now has a “Software and workflow control” lane for
  the ServiceNow, Cloudflare, and Snowflake comparison, with a URL-persisted
  filter covered by the browser suite.
- The article shell now makes the editorial separation explicit: first read
  the claim, then see how the business works, then check reported profit
  against cash and obligations, and finally read what a future filing could
  confirm or weaken. This is visible before the source article begins.
- The catalog coverage rules now recognize high-level lane summaries as
  overviews rather than leaving them with an empty status. All 427 articles
  in the reader catalog now have at least one honest coverage label; the
  four-lane overview is marked as explaining the business and its open edges,
  without being presented as a cash or valuation study.
- The reader server now keeps the catalog warm for five minutes. The first
  catalog build still parses the research files, but repeated homepage loads
  return the same 427-entry catalog in a fraction of a second; adding research
  remains possible through the explicit `/api/catalog?refresh=1` query or a
  server restart. The server now performs that first build before accepting
  browser requests, and the browser check allows the archive's cold build to
  finish before asserting the rendered home page.
- Large library result sets now render titles and metadata first, while opening
  excerpts appear when a search narrows the list or when the result set is
  small. This keeps the full library available without asking the browser to
  construct hundreds of long excerpts at once.
- The full Chromium reader suite now passes after the cache and result-list
  changes, including long comparison navigation, source-boundary pages,
  comparison filters, search restoration, empty search results, and the
  framework-index mobile layout.
- The curated comparison section now also links directly to all 138 comparison
  essays and to the company/cohort writing map, so the selected themes do not
  hide the rest of the cohort research.
- The cohort writing-map link uses the reader route rather than exposing raw
  Markdown, so it keeps the same source, navigation, glossary, and reading
  order as the other research pages.
- The archive now exposes a dedicated architecture-versus-system-delivery
  comparison for Broadcom, Cisco, and Dell. It keeps design-layer cash,
  installed-network recurring cash, and financing-supported system-delivery
  cash separate instead of grouping all three under “AI demand.”
- Security control is now a first-class software/workflow cohort in the reader,
  linking the dedicated CrowdStrike, Palo Alto Networks, Zscaler, and F5
  forensic comparison to all four company studies.
- The homepage theme directory now surfaces the newer Intel, Broadcom, Cisco,
  Dell, CrowdStrike, Palo Alto Networks, Zscaler, and F5 company studies
  directly, so the latest cohort work is discoverable without filename search.
- The three opening findings now lead with the latest substantive work: Dell's
  financing-supported AI backlog, the security-control cohort's recurring-cash
  test, and Intel's manufacturing capital burden.
- The AI comparison directory now exposes the Intel-versus-KLA contrast: owning
  a manufacturing bottleneck versus selling process-control tools into many
  fabs. This gives the Intel homepage finding an immediate comparative path.
- The consumer theme now surfaces the payment-conversion cohort—Affirm, Uber,
  DoorDash, Booking, and Wayfair—with its direct marketplace-burden comparison.
- The banking and markets theme now surfaces private-capital and custody/
  clearing comparisons alongside its company studies, so customer money,
  collateral, insurance obligations, and shareholder cash are discoverable as
  separate questions.
- The infrastructure theme now surfaces industrial distribution and backlog-
  to-cash cohorts, including Fastenal, Grainger, Ferguson, Core & Main,
  EMCOR, Quanta, and MasTec.
- That same theme now makes regulated wires, large-load demand, and power-
  demand execution explicit, with Exelon, AEP, NextEra, and ONEOK linked to
  the relevant comparisons.
- The consumer theme now exposes the routine-beverage comparison, linking
  Coca-Cola, PepsiCo, Monster Beverage, and Brown-Forman to the brand,
  bottler, price/mix, channel-burden, and owner-cash analysis.
- A direct route-integrity audit now confirms all 24 surfaced article paths and
  all 60 company slugs in the theme directory resolve to local files.
- That audit is now reproducible as `python3 scripts/verify-reader-routes.py`.
- The KLA dossier and the newest AI/security dossiers now keep primary sources
  and local evidence records in a single, readable source sequence rather than
  repeating an empty “Sources” section.
- A spot check of the concise software dossiers (Adobe and Cloudflare) confirms
  that short length reflects compact coverage, not a missing framework: each
  still states the operating chain, cash bridge, earnings-quality tests, Alden
  liquidity risks, Damodaran valuation assumptions, incentives, falsifiers, and
  next-filing questions.
- Industrial distribution is now a first-class industrial-capacity cohort,
  linking Fastenal, Grainger, Ferguson, Core & Main, and WESCO to the existing
  procurement-density and balance-sheet-velocity research.
- Search, article-type filters, coverage filters, comparison-lane filters,
  empty results, and URL restoration passed in the live browser run.
- The library count is now announced as a polite status update, and an empty
  search result provides a focused “Clear search and filters” recovery action
  instead of leaving the reader at a dead end.
- Reader load failures now expose a clear retry action, and the homepage keeps
  technical valuation language out of the first reading path where plain
  wording is sufficient.

## Accessibility risks and limits

- Visible focus treatment is present for links, buttons, inputs and summaries;
  keyboard order and screen-reader announcements were not fully tested with an
  assistive technology.
- Tables are given a labelled scroll region, but a full audit of table headers,
  contrast ratios, reduced motion, and screen-reader reading order still needs
  dedicated automated and assistive-technology checks.
- The screenshots establish layout and visible copy, not the accuracy of every
  underlying financial conclusion or source link.

## Verification

The current browser run passed desktop and mobile layout, article and
comparison rendering, comparison anchors, source-boundary language, search
restore and empty state, and the framework-index mobile layout. The full
research gates also pass: scenario register, cross-framework page coverage,
and the insight-system verifier.

Maintenance command: `bash scripts/verify-insight-system.sh`.

## Skeptical Reader Test

- Can a first-time reader tell where to begin, what a theme contains, and how
  to move from a comparison to a company study?
- Does the page distinguish reported evidence, interpretation, unresolved
  questions, and source availability?
- Can a mobile reader use the navigation, article contents, search, filters,
  and source links without horizontal scrolling?
