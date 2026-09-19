# Combined investment research reader browser review

Review date: `2026-09-17` (rerun)

The Chromium review suite was run against the local reader server with
`node scripts/check-reader-browser.mjs` and exited with code `0`. All
functional DOM assertions reached and passed the final framework-layout check,
including the seven-document investment-research handoff. Chromium's
screenshot capture channel timed out for each diagnostic image; screenshots
are auxiliary diagnostics, while the functional layout and navigation
assertions passed and the process exited cleanly.

The 2026-09-17 rerun passed the current integrated review path with no
functional reader regression. Screenshot capture again timed out, so this is
functional-navigation evidence rather than a visual screenshot archive.

## Runtime checks exercised

- Desktop and mobile homepage layout with no horizontal overflow.
- Article, comparison, legacy viewer, trend, and company-framework routes.
- Source-status language, evidence-depth labels, confidence legend, financial
  definitions, and open-question reading paths.
- Integrated investment-research section, including the synthesis, three
  pilots, completion audit, deliverable audit, reviewer guide, force atlas,
  Target Q2 call memo, Apollo fee-rollforward boundary, and the pooled,
  within-company, and lagged Q-10 retail diagnostics.
- Latest review-document handoffs for the thesis-breaker register, retail
  interim lease/tax boundary, Concord public-document acquisition boundary,
  Wheaton Q-03 return-input schema, Apollo Q-07 common-owner input schema, the
  Athene corporate-structure presentation boundary, and the retail CA-06
  owner-cash input schema.
- Reader evidence-depth assertion synchronized to the current `225` checked
  evidence gates reported by the pilot verifier.
- ARI buyer-side AUM outflow boundary handoff and dynamic-link assertion.
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
