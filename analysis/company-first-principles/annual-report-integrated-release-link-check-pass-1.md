# Annual Report Integrated Release Link Check Pass 1

## Purpose

This pass records a live release-time link check for the current article:

`/cluster/annual-report-integrated-final-publication-draft-pass-1.md`

The structured companion table is:

`analysis/company-first-principles/data/annual-report-integrated-release-link-check-pass-1.csv`

## Link Check Verdict

`release-link-check-passed-clean`

The article currently has `58` unique public URLs.

The link check result was:

- `58` URLs opened with HTTP `200`
- `0` URLs need retry or replacement

That is strong enough to keep the article in release-candidate state.

It is not the same as external publication.

## Link Refresh Items

The prior check had three issue anchors:

1. MasTec investor 10-Q page: automated read timed out.
2. Cigna investor SEC filings page: returned HTTP `403`.
3. Broadcom static file: automated read timed out.

Those were replaced with direct SEC URLs where practical.

The replacement links opened successfully in the current check.

Before external publication, links should still be checked again because web availability can change.

## Strong Link Areas

The strongest live-link coverage is:

- SEC archive URLs
- Florida PSC regulatory URLs
- direct annual-report/10-K/10-Q filing URLs

The check found all tested SEC archive and PSC/regulatory links opening successfully.

## Current Release State

The article remains:

- internally reader-ready
- section-anchor cited across all `15` themes plus the proof rule
- sentence-metric risk audited
- release-candidate formatted
- link-checked with all `58` unique URLs opening in this pass

It is still not:

- externally published
- named-cash proof
- investment advice

## Safe Claim

`The integrated annual-report article has passed a release-time link check with 58 of 58 unique URLs opening successfully after replacing the prior MasTec, Cigna, and Broadcom issue anchors. This preserves release-candidate status but does not make the article externally published or named-cash proof.`

## Decision Marker

`annual-report-integrated-release-link-check-ready-clean`
