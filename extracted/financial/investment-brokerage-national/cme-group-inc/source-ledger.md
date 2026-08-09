# Source Ledger

Date baseline: 2026-08-08

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CME-T1 | AnnualReports.com CME verification note | 2026-08-08 | Aggregator verification note | Records company metadata and latest annual-report label from AnnualReports | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/financial/investment-brokerage-national/cme-group-inc/annualreports-verification.md) |
| CME-T2 | CME IR source-links note | 2026-08-08 | Official-source link ledger | Preserves verified official annual and quarterly IR URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/investment-brokerage-national/cme-group-inc/ir-source-links.md) |
| CME-T3 | CME 4Q25 / FY2025 earnings release PDF | 2026-02-04 | Earnings release PDF | Late-2025 quarter and full-year `2025` operating and volume metrics | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/investment-brokerage-national/cme-group-inc/2025-q4-earnings-release.pdf) |
| CME-T4 | CME 2025 Form 10-K | 2026-02-26 filed / 2026-08-08 collected | SEC filing HTML | Filed annual report for `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/investment-brokerage-national/cme-group-inc/2025-10k.html) |
| CME-T5 | CME 4Q25 earnings 8-K | 2026-02-04 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for late-2025 earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/investment-brokerage-national/cme-group-inc/2025-q4-8k.html) |
| CME-T6 | CME 1Q26 Form 10-Q | 2026-04-24 filed / 2026-08-08 collected | SEC filing HTML | Filed prior quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/investment-brokerage-national/cme-group-inc/2026-q1-10q.html) |
| CME-T7 | CME 1Q26 earnings 8-K | 2026-04-22 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for first-quarter release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/investment-brokerage-national/cme-group-inc/2026-q1-8k.html) |
| CME-T8 | CME 2Q26 Form 10-Q | 2026-07-24 filed / 2026-08-08 collected | SEC filing HTML | Filed most recent quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/investment-brokerage-national/cme-group-inc/2026-q2-10q.html) |
| CME-T9 | CME 2Q26 earnings 8-K | 2026-07-22 filed / 2026-08-08 collected | SEC filing HTML | Filing wrapper for most recent quarter release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/financial/investment-brokerage-national/cme-group-inc/2026-q2-8k.html) |
| CME-T10 | CME 2025 annual report PDF | 2026-08-08 collected | Official annual report PDF | Official designed annual-report package saved locally | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/financial/investment-brokerage-national/cme-group-inc/2025-annual-report.pdf) |

## Reconciliation notes

- CME now has a full SEC filing chain on disk for the target annual report and the last three quarters.
- The official `2025` annual report PDF is now saved locally.
- The official `4Q25` earnings release PDF is saved locally.
- Official `1Q26` and `2Q26` quarter-material URLs were verified through CME event pages, but shell fetches to those specific IR endpoints returned incomplete placeholder HTML during this pass.

## Missing evidence

- A direct saved AnnualReports.com HTML artifact if shell access to `annualreports.com` becomes reliable later.
- Local copies of the official `1Q26` and `2Q26` earnings release PDFs and related commentary or introduction files if a later fetch pass succeeds.
- Local transcript artifacts for the in-scope earnings calls.
