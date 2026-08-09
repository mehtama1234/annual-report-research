# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| IVZ-T1 | AnnualReports.com Invesco verification note | 2026-08-09 | Aggregator verification note | Records company metadata and confirms AnnualReports lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/financial/asset-management/invesco-ltd/annualreports-verification.md) |
| IVZ-T2 | Invesco IR source-links note | 2026-08-09 | Official-source link ledger | Preserves the verified official annual-report and earnings-release source pages | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/asset-management/invesco-ltd/ir-source-links.md) |
| IVZ-T3 | Invesco 2025 annual report PDF | 2026-08-09 collected | Annual report PDF | Official annual-report artifact for fiscal `2025` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/asset-management/invesco-ltd/2025-annual-report.pdf) |
| IVZ-T4 | Invesco 2025 Form 10-K | 2026-02-24 filed / 2026-08-09 collected | SEC filing HTML | Filed annual report for fiscal `2025` | `[Filed]` | [2026-02-24-10-k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/invesco-ltd/2026-02-24-10-k.html) |
| IVZ-T5 | Invesco Q4 2025 earnings release | 2026-01-27 filed / 2026-08-09 collected | SEC Exhibit `99.1` HTML | Most direct local late-`2025` earnings-release artifact | `[Filed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/asset-management/invesco-ltd/2025-q4-earnings-release.html) |
| IVZ-T6 | Invesco Q4 2025 earnings 8-K | 2026-01-27 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for the late-`2025` earnings release | `[Filed]` | [2026-01-27-8-k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/invesco-ltd/2026-01-27-8-k.html) |
| IVZ-T7 | Invesco Q1 2026 earnings release | 2026-04-28 filed / 2026-08-09 collected | SEC Exhibit `99.1` HTML | Most direct local quarterly release artifact for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/asset-management/invesco-ltd/2026-q1-earnings-release.html) |
| IVZ-T8 | Invesco Q1 2026 earnings 8-K | 2026-04-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for the Q1 `2026` earnings release | `[Filed]` | [2026-04-28-8-k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/invesco-ltd/2026-04-28-8-k.html) |
| IVZ-T9 | Invesco Q1 2026 Form 10-Q | 2026-05-05 filed / 2026-08-09 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-05-05-10-q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/invesco-ltd/2026-05-05-10-q.html) |
| IVZ-T10 | Invesco Q2 2026 earnings release | 2026-07-28 filed / 2026-08-09 collected | SEC Exhibit `99.1` HTML | Most direct local quarterly release artifact for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/asset-management/invesco-ltd/2026-q2-earnings-release.html) |
| IVZ-T11 | Invesco Q2 2026 earnings 8-K | 2026-07-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for the Q2 `2026` earnings release | `[Filed]` | [2026-07-28-8-k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/invesco-ltd/2026-07-28-8-k.html) |
| IVZ-T12 | Invesco Q2 2026 Form 10-Q | 2026-08-04 filed / 2026-08-09 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-08-04-10-q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/asset-management/invesco-ltd/2026-08-04-10-q.html) |

## Reconciliation notes

- Invesco now has a clean annual-plus-quarterly evidence chain on disk for the `2025` annual package and the last three reported quarters as of `2026-08-09`.
- The saved quarterly release artifacts are SEC-hosted Exhibit `99.1` HTML files rather than official IR PDFs because those were the most reliable fetch path in this shell pass.
- AnnualReports metadata was verified, but AnnualReports itself still lagged at `2024` even though the official company site already exposed the `2025` annual report.

## Missing evidence

- A direct saved AnnualReports HTML artifact.
- Local transcript artifacts for the `Q4 2025`, `Q1 2026`, and `Q2 2026` earnings calls.
- Local investor-presentation PDFs for the in-scope quarterly events.
