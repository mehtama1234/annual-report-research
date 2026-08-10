# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| KR-T1 | AnnualReports.com Kroger verification note | 2026-08-09 | Aggregator verification note | Confirms industry discovery and documents that AnnualReports still lags at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/retail-grocery-stores/the-kroger-company/annualreports-verification.md) |
| KR-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/retail-grocery-stores/the-kroger-company/official-ir-verification.md) |
| KR-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000056873.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/retail-grocery-stores/the-kroger-company/submissions-cik0000056873.json) |
| KR-T4 | 2025 annual report PDF | 2026-08-09 collected | Official annual report PDF | Preserves the official Kroger annual report artifact surfaced through the IR filing-details chain | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/retail-grocery-stores/the-kroger-company/2025-annual-report.pdf) |
| KR-T5 | 2025 Form `10-K` | 2026-03-31 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2026-01-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/retail-grocery-stores/the-kroger-company/2025-10k.html) |
| KR-T6 | 2025 Q3 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves third-quarter `2025` operating narrative and metrics | `[Disclosed]` | [2025-q3-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/retail-grocery-stores/the-kroger-company/2025-q3-press-release.html) |
| KR-T7 | 2025 Q3 earnings `8-K` | 2025-12-04 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/retail-grocery-stores/the-kroger-company/2025-q3-8k.html) |
| KR-T8 | 2025 Q3 Form `10-Q` | 2025-12-12 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/retail-grocery-stores/the-kroger-company/2025-q3-10q.html) |
| KR-T9 | 2025 Q4 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves fourth-quarter and full-year `2025` operating narrative and metrics | `[Disclosed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/retail-grocery-stores/the-kroger-company/2025-q4-press-release.html) |
| KR-T10 | 2025 Q4 earnings `8-K` | 2026-03-05 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/retail-grocery-stores/the-kroger-company/2025-q4-8k.html) |
| KR-T11 | 2026 Q1 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves first-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/retail-grocery-stores/the-kroger-company/2026-q1-press-release.html) |
| KR-T12 | 2026 Q1 earnings `8-K` | 2026-06-18 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/retail-grocery-stores/the-kroger-company/2026-q1-8k.html) |
| KR-T13 | 2026 Q1 Form `10-Q` | 2026-06-26 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/retail-grocery-stores/the-kroger-company/2026-q1-10q.html) |

## Reconciliation notes

- Kroger now has the core SEC filing chain on disk for the fiscal `2025` annual filing and the last three quarters in scope.
- Kroger now also has the official `2025` annual report PDF on disk from the IR filing-details chain.
- AnnualReports is still useful for classification discovery, but it lags the annual package and should not anchor the current year.
- The strongest retail-media evidence comes directly from the `10-K` and the `Q1 2026` results release, not from third-party commentary.

## Missing evidence

- No standalone transcript artifacts for the `Q3 2025`, `Q4 2025`, or `Q1 2026` earnings calls are saved locally.
