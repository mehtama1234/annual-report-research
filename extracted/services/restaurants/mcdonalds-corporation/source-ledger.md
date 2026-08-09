# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| MCD-T1 | AnnualReports.com McDonald's verification note | 2026-08-09 | Aggregator verification note | Confirms AnnualReports still labeled `2024` as most recent on `2026-08-09` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/restaurants/mcdonalds-corporation/annualreports-verification.md) |
| MCD-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/restaurants/mcdonalds-corporation/official-ir-verification.md) |
| MCD-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, SIC, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000063908.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/submissions-cik0000063908.json) |
| MCD-T4 | 2025 Form `10-K` | 2026-02-24 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2025-10k.html) |
| MCD-T5 | 2025 Q4 earnings `8-K` | 2026-02-11 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2025-q4-8k.html) |
| MCD-T6 | 2026 Q1 earnings `8-K` | 2026-05-07 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q1-8k.html) |
| MCD-T7 | 2026 Q2 earnings `8-K` | 2026-08-04 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q2-8k.html) |
| MCD-T8 | 2026 Q1 Form `10-Q` | 2026-05-07 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q1-10q.html) |
| MCD-T9 | 2026 Q2 Form `10-Q` | 2026-08-07 filed / 2026-08-09 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/restaurants/mcdonalds-corporation/2026-q2-10q.html) |
| MCD-T10 | 2025 Q4 earnings release PDF via SEC exhibit | 2026-02-11 filed / 2026-08-09 collected | Earnings release PDF | Local fourth-quarter / full-year release artifact | `[Filed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/restaurants/mcdonalds-corporation/2025-q4-earnings-release.pdf) |
| MCD-T11 | 2026 Q1 earnings release PDF via SEC exhibit | 2026-05-07 filed / 2026-08-09 collected | Earnings release PDF | Local first-quarter release artifact | `[Filed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/restaurants/mcdonalds-corporation/2026-q1-earnings-release.pdf) |

## Reconciliation notes

- McDonald's now has the core SEC chain on disk for the `2025` annual filing and the last three quarters in scope.
- The official IR URL chain is verified, but the corporate-hosted annual-report PDF and some IR HTML / PDF assets timed out repeatedly from this shell environment on `2026-08-09`.
- The local quarter-release artifacts currently on disk are strongest for `Q4 2025` and `Q1 2026`, where the matching SEC exhibit PDFs were captured cleanly.

## Missing evidence

- A locally saved copy of the official McDonald's `2025` annual-report PDF.
- A locally saved copy of the official McDonald's `Q2 2026` earnings-release PDF from the corporate host.
- Saved HTML mirrors of the McDonald's financial-information and quarter story pages if the corporate host becomes more cooperative in a later pass.
