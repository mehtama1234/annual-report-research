# Source Ledger

Date baseline: 2026-08-08

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BEN-T1 | AnnualReports.com Franklin verification note | 2026-08-08 | Aggregator verification note | Records company metadata and confirms AnnualReports lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/asset-management/franklin-resources-inc/annualreports-verification.md) |
| BEN-T2 | Franklin IR source-links note | 2026-08-08 | Official-source link ledger | Preserves the verified official annual-report, earnings-release, and conference-call URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/franklin-resources-inc/ir-source-links.md) |
| BEN-T3 | Franklin 2025 annual report PDF | 2026-08-08 collected | Annual report PDF | Official annual-report artifact for fiscal `2025` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/franklin-resources-inc/2025-annual-report.pdf) |
| BEN-T4 | Franklin 2025 Form 10-K | 2025-11-10 filed / 2026-08-08 collected | SEC filing HTML | Filed annual report for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/franklin-resources-inc/2025-10k.html) |
| BEN-T5 | Franklin Q1 2026 earnings release | 2026-01-30 filed / 2026-08-08 collected | SEC Exhibit `99.1` HTML | Most direct local quarterly release artifact for the quarter ended `2025-12-31` | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/franklin-resources-inc/2026-q1-earnings-release.html) |
| BEN-T6 | Franklin Q1 2026 Form 10-Q | 2026-01-30 filed / 2026-08-08 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2025-12-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/franklin-resources-inc/2026-q1-10q.html) |
| BEN-T7 | Franklin Q1 2026 earnings 8-K | 2026-01-30 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for the Q1 `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/franklin-resources-inc/2026-q1-8k.html) |
| BEN-T8 | Franklin Q2 2026 earnings release | 2026-04-28 filed / 2026-08-08 collected | SEC Exhibit `99.1` HTML | Most direct local quarterly release artifact for the quarter ended `2026-03-31` | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/franklin-resources-inc/2026-q2-earnings-release.html) |
| BEN-T9 | Franklin Q2 2026 Form 10-Q | 2026-04-28 filed / 2026-08-08 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/franklin-resources-inc/2026-q2-10q.html) |
| BEN-T10 | Franklin Q2 2026 earnings 8-K | 2026-04-28 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for the Q2 `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/franklin-resources-inc/2026-q2-8k.html) |
| BEN-T11 | Franklin Q3 2026 earnings release | 2026-07-31 filed / 2026-08-08 collected | SEC Exhibit `99.1` HTML | Most direct local quarterly release artifact for the quarter ended `2026-06-30` | `[Filed]` | [2026-q3-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/franklin-resources-inc/2026-q3-earnings-release.html) |
| BEN-T12 | Franklin Q3 2026 Form 10-Q | 2026-07-31 filed / 2026-08-08 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/franklin-resources-inc/2026-q3-10q.html) |
| BEN-T13 | Franklin Q3 2026 earnings 8-K | 2026-07-31 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for the Q3 `2026` earnings release | `[Filed]` | [2026-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/franklin-resources-inc/2026-q3-8k.html) |

## Reconciliation notes

- Franklin now has a complete local annual-plus-quarterly filing chain for the target annual package and the last three reported quarters as of `2026-08-08`.
- The saved quarterly release artifacts are SEC-hosted Exhibit `99.1` HTML files rather than the official IR PDFs because SEC-hosted versions were easier to fetch reliably in this shell pass.
- AnnualReports metadata was verified, but AnnualReports itself still lagged at `2024` even though the official company site already exposed the `2025` annual report.

## Missing evidence

- A direct saved AnnualReports HTML artifact.
- Local transcript artifacts for the `Q1 2026`, `Q2 2026`, and `Q3 2026` earnings calls.
- Local investor-presentation PDFs for the in-scope quarterly events.
- A local saved late-`2025` preliminary fourth-quarter earnings-release artifact if a later pass wants a tighter annual-season bridge.
