# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| SBUX-T1 | AnnualReports.com Starbucks verification note | 2026-08-09 | Aggregator verification note | Confirms AnnualReports still labeled `2024` as most recent on `2026-08-09` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/restaurants/starbucks-corporation/annualreports-verification.md) |
| SBUX-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window and documents Cloudflare blocking on shell fetches | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/restaurants/starbucks-corporation/official-ir-verification.md) |
| SBUX-T3 | Official fiscal 2025 annual report PDF | 2025-11-14 filed / 2026-08-09 collected | Official IR PDF | Direct annual report artifact exposed by the Starbucks SEC filing detail page inside the IR stack | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/restaurants/starbucks-corporation/2025-annual-report.pdf) |
| SBUX-T4 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, SIC, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000829224.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/restaurants/starbucks-corporation/submissions-cik0000829224.json) |
| SBUX-T5 | Fiscal 2025 Form `10-K` | 2025-11-14 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2025-09-28` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/restaurants/starbucks-corporation/2025-10k.html) |
| SBUX-T6 | Fiscal Q1 2026 earnings `8-K` | 2026-01-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter fiscal `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/restaurants/starbucks-corporation/2026-q1-8k.html) |
| SBUX-T7 | Fiscal Q2 2026 earnings `8-K` | 2026-04-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for second-quarter fiscal `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/restaurants/starbucks-corporation/2026-q2-8k.html) |
| SBUX-T8 | Fiscal Q3 2026 earnings `8-K` | 2026-07-29 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter fiscal `2026` results | `[Filed]` | [2026-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/restaurants/starbucks-corporation/2026-q3-8k.html) |
| SBUX-T9 | Fiscal Q1 2026 Form `10-Q` | 2026-01-28 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/restaurants/starbucks-corporation/2026-q1-10q.html) |
| SBUX-T10 | Fiscal Q2 2026 Form `10-Q` | 2026-04-28 filed / 2026-08-09 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/restaurants/starbucks-corporation/2026-q2-10q.html) |
| SBUX-T11 | Fiscal Q3 2026 Form `10-Q` | 2026-07-29 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/restaurants/starbucks-corporation/2026-q3-10q.html) |

## Reconciliation notes

- Starbucks now has the core SEC chain on disk for the fiscal `2025` annual filing and the last three fiscal quarters in scope.
- The official IR URL chain is verified, and the direct annual report PDF exposed by that chain is now saved locally.
- The Starbucks IR host still served Cloudflare challenge HTML to direct shell fetches on `2026-08-09`, so the raw IR landing pages themselves were not retained as HTML artifacts.
- The current packet therefore has a cleaner annual artifact stack than before: official annual report PDF plus the SEC filings, while still relying on the verification note to preserve the live IR navigation chain.

## Missing evidence

- Local copies of the official Starbucks quarter earnings-release pages or PDF attachments from the investor-relations host.
- Any transcript or webcast transcript artifacts for the `Q3 2026`, `Q2 2026`, and `Q1 2026` earnings calls.
