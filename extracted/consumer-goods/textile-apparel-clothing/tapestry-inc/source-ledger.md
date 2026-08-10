# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| TPR-T1 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Confirms `Consumer Goods / Textile - Apparel Clothing` taxonomy and documents the live annual-report lag | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/consumer-goods/textile-apparel-clothing/tapestry-inc/annualreports-verification.md) |
| TPR-T2 | AnnualReports.com company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves company identity, exchange, ticker, geography, and lagging annual-report status | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/consumer-goods/textile-apparel-clothing/tapestry-inc/company-page.html) |
| TPR-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official annual and quarterly routes plus the collection constraints in this environment | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/textile-apparel-clothing/tapestry-inc/official-ir-verification.md) |
| TPR-T4 | Investor overview page snapshot | 2026-08-10 collected | Official IR HTML snapshot | Preserves the current company description, FY25 metrics, and Amplify Growth Strategy framing | `[Disclosed]` | [investor-overview.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/textile-apparel-clothing/tapestry-inc/investor-overview.html) |
| TPR-T5 | Quarterly results page snapshot | 2026-08-10 collected | Official IR HTML snapshot | Confirms the active quarter chain and the exact Q1 through Q3 2026 artifact links | `[Disclosed]` | [quarterly-results.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/textile-apparel-clothing/tapestry-inc/quarterly-results.html) |
| TPR-T6 | Events and presentations page snapshot | 2026-08-10 collected | Official IR HTML snapshot | Confirms the investor-presentation chain and the 2025 Investor Day strategy deck route | `[Disclosed]` | [events-presentations.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/textile-apparel-clothing/tapestry-inc/events-presentations.html) |
| TPR-T7 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, filing dates, accession numbers, and the correct annual-plus-trailing-quarter sequence | `[Filed]` | [submissions-cik0001116132.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/textile-apparel-clothing/tapestry-inc/submissions-cik0001116132.json) |

## Reconciliation notes

- Tapestry now has a stable local taxonomy and IR-page evidence chain for the `2025` annual-report window and the last three reported quarters in scope as of `2026-08-10`.
- The correct quarter window is `Q3 2026`, `Q2 2026`, and `Q1 2026` because the scheduled `Q4 2026` earnings call is set for `August 13, 2026`, which is still in the future as of the current date baseline.
- AnnualReports.com was useful for taxonomy, but not current enough for the `2025` annual package because it still exposed `2024` as the latest annual entry on `2026-08-10`.
- The official IR pages explicitly show the current house-of-brands framing, the FY25 metric stack, the Amplify strategy pillars, and the live quarter-results routing.
- The local SEC submissions JSON confirms the exact filing chain in scope:
  - `2025-08-14` `10-K`
  - `2025-11-06` `10-Q`
  - `2026-02-05` `10-Q`
  - `2026-05-07` `10-Q`
- Direct downloads of official Tapestry PDFs and SEC filing HTML pages were not stable in this shell environment and produced zero-byte files, so those failed artifacts were removed rather than left in the archive.

## Missing evidence

- No standalone annual-report PDF is saved locally yet.
- No standalone local filing HTML pages are saved yet for the annual or trailing-quarter chain.
- No standalone latest-quarter verbatim earnings-call transcript artifact is saved locally yet.
