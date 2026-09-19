# Combined investment research reader browser review

Review date: `2026-09-15`

The Chromium review suite was run against the local reader server with
`node scripts/check-reader-browser.mjs` and exited with code `0`.

## Runtime checks exercised

- Desktop and mobile homepage layout with no horizontal overflow.
- Article, comparison, legacy viewer, trend, and company-framework routes.
- Source-status language, evidence-depth labels, confidence legend, financial
  definitions, and open-question reading paths.
- Integrated investment-research section, including the synthesis, three
  pilots, completion audit, deliverable audit, reviewer guide, force atlas,
  Target Q2 call memo, and Apollo fee-rollforward boundary.
- Search restoration, article-type filtering, complete-coverage filtering,
  empty-search recovery, comparison-lane filtering, and anchor handoffs.
- Mobile framework-index layout and trend-archive return links.

## What the browser review proves

The reader can render and navigate the current evidence architecture and
expose depth and confidence labels at runtime. It does not prove the
underlying investment claims, normalize owner cash, or replace the primary
filing and ledger verifiers.

## Reproduction

From the repository root:

```text
python3 scripts/reader-server.py
node scripts/check-reader-browser.mjs
```

The complementary route and structure checks are
`python3 scripts/verify-reader-routes.py` and
`python3 scripts/check-internal-links.py`.
