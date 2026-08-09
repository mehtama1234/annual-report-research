# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| AMZN-T1 | AnnualReports.com Amazon verification note | 2026-08-09 | Aggregator verification note | Confirms sector / industry labeling and that the `2025` annual package is live on AnnualReports | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/retail/specialty-retail-other/amazoncom-inc/annualreports-verification.md) |
| AMZN-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/retail/specialty-retail-other/amazoncom-inc/official-ir-verification.md) |
| AMZN-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001018724.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/retail/specialty-retail-other/amazoncom-inc/submissions-cik0001018724.json) |
| AMZN-T4 | 2025 annual report PDF | 2026-08-09 collected | Official annual report PDF via SEC | Official annual report artifact on disk | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/retail/specialty-retail-other/amazoncom-inc/2025-annual-report.pdf) |
| AMZN-T5 | 2025 Form `10-K` | 2026-02-06 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/retail/specialty-retail-other/amazoncom-inc/2025-10k.html) |
| AMZN-T6 | 2025 Q4 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves fourth-quarter and full-year `2025` operating narrative and metrics | `[Disclosed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/retail/specialty-retail-other/amazoncom-inc/2025-q4-press-release.html) |
| AMZN-T7 | 2025 Q4 earnings `8-K` | 2026-02-05 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/retail/specialty-retail-other/amazoncom-inc/2025-q4-8k.html) |
| AMZN-T8 | 2026 Q1 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves first-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/retail/specialty-retail-other/amazoncom-inc/2026-q1-press-release.html) |
| AMZN-T9 | 2026 Q1 earnings `8-K` | 2026-04-29 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/retail/specialty-retail-other/amazoncom-inc/2026-q1-8k.html) |
| AMZN-T10 | 2026 Q1 Form `10-Q` | 2026-04-30 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/retail/specialty-retail-other/amazoncom-inc/2026-q1-10q.html) |
| AMZN-T11 | 2026 Q2 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves second-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/retail/specialty-retail-other/amazoncom-inc/2026-q2-press-release.html) |
| AMZN-T12 | 2026 Q2 earnings `8-K` | 2026-07-30 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/retail/specialty-retail-other/amazoncom-inc/2026-q2-8k.html) |
| AMZN-T13 | 2026 Q2 Form `10-Q` | 2026-07-31 filed / 2026-08-09 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/retail/specialty-retail-other/amazoncom-inc/2026-q2-10q.html) |

## Reconciliation notes

- Amazon now has the official annual report PDF on disk plus the core SEC filing chain for the fiscal `2025` annual filing and the last three quarters in scope.
- The live Amazon investor-relations site was current and queryable, but scripted collection began hitting rate limits, so the packet preserves quarter release text through the matching SEC-hosted Exhibit `99.1` files.
- This is still a strong evidence chain because the company-issued release text, annual filing, annual report PDF, and quarter reports are all local.

## Missing evidence

- No standalone transcript artifacts for the `Q4 2025`, `Q1 2026`, or `Q2 2026` earnings calls are saved locally.
- No separate local copies of Amazon's IR HTML pages or event-webcast assets are included in this first packet.
