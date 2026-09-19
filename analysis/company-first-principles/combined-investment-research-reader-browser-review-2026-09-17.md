# Combined investment research reader browser review — 2026-09-17

## Result

The repository reader was served locally with:

`python3 scripts/reader-server.py 8765`

The Chromium suite then completed with exit code `0`:

`node scripts/check-reader-browser.mjs`

## Covered routes

- Desktop and mobile catalog layouts
- Article and comparison routes
- Legacy `site/viewer.html?file=` handoff
- Private-capital, energy, power-demand, healthcare, and payer comparison
  handoffs
- External-only filing boundaries and source-link accessibility
- Company dossiers including Cigna, UnitedHealth, TJX, and other representative
  company pages
- Search results, empty state, trend archive return, editorial labels, and
  framework-index mobile layout
- Research-method and current-review handoffs

## Browser assertions

- No horizontal overflow at tested desktop or mobile widths
- Article metadata, evidence-language, definitions, coverage, and reading-path
  controls loaded
- Cross-links resolved to the intended company and comparison artifacts
- Legacy viewer query routing passed
- Search restore and empty-state behavior passed
- Trend and framework-index navigation passed

## Boundary

This confirms reader rendering, navigation, and language controls. It does not
upgrade the underlying evidence grades or convert qualified diagnostics into
normalized owner cash.

