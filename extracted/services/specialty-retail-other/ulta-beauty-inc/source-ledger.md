# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| ULTA-T1 | AnnualReports.com Ulta verification note | 2026-08-10 | Aggregator verification note | Confirms `Services / Specialty Retail, Other` taxonomy and that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/specialty-retail-other/ulta-beauty-inc/annualreports-verification.md) |
| ULTA-T2 | AnnualReports.com company page snapshot | 2026-08-10 | Aggregator HTML snapshot | Preserves the live discovery page showing the lagged `2024` package | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/specialty-retail-other/ulta-beauty-inc/company-page.html) |
| ULTA-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the annual-report page, results page, quarter-release URLs, and that `Q2 2026` was still future-dated | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/specialty-retail-other/ulta-beauty-inc/official-ir-verification.md) |
| ULTA-T4 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001403568.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/specialty-retail-other/ulta-beauty-inc/submissions-cik0001403568.json) |
| ULTA-T5 | 2025 annual report PDF | 2026-08-10 collected | Official annual report PDF | Official annual-report artifact preserved locally | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/specialty-retail-other/ulta-beauty-inc/2025-annual-report.pdf) |
| ULTA-T6 | 2025 Form `10-K` | 2026-03-27 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for the fiscal year ended `2026-01-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/specialty-retail-other/ulta-beauty-inc/2025-10k.html) |
| ULTA-T7 | 2025 Q3 earnings release | 2025-12-04 released / 2026-08-10 collected | Official IR release HTML | Official third-quarter `2025` results narrative | `[Disclosed]` | [2025-q3-results-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/specialty-retail-other/ulta-beauty-inc/2025-q3-results-release.html) |
| ULTA-T8 | 2025 Q3 earnings `8-K` | 2025-12-04 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/specialty-retail-other/ulta-beauty-inc/2025-q3-8k.html) |
| ULTA-T9 | 2025 Q3 Form `10-Q` | 2025-12-04 filed / 2026-08-10 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/specialty-retail-other/ulta-beauty-inc/2025-q3-10q.html) |
| ULTA-T10 | 2025 Q4 and full-year results release | 2026-03-12 released / 2026-08-10 collected | Official IR release HTML | Official fourth-quarter and full-year `2025` results narrative | `[Disclosed]` | [2025-q4-results-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/specialty-retail-other/ulta-beauty-inc/2025-q4-results-release.html) |
| ULTA-T11 | 2025 Q4 earnings `8-K` | 2026-03-12 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/specialty-retail-other/ulta-beauty-inc/2025-q4-8k.html) |
| ULTA-T12 | 2026 Q1 earnings release | 2026-06-02 released / 2026-08-10 collected | Official IR release HTML | Official first-quarter `2026` results narrative | `[Disclosed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/specialty-retail-other/ulta-beauty-inc/2026-q1-results-release.html) |
| ULTA-T13 | 2026 Q1 earnings `8-K` | 2026-06-02 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/specialty-retail-other/ulta-beauty-inc/2026-q1-8k.html) |
| ULTA-T14 | 2026 Q1 Form `10-Q` | 2026-06-02 filed / 2026-08-10 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/specialty-retail-other/ulta-beauty-inc/2026-q1-10q.html) |

## Reconciliation notes

- Ulta now has a full evidence chain on disk for the fiscal `2025` annual-report window and the latest three reported quarters in scope as of `2026-08-10`.
- The important timing correction is that `Q2 2026` had not yet been reported on `2026-08-10`; Ulta's live IR pages listed the `Q2 2026` earnings call as an upcoming event for `2026-08-27`.
- The official IR layer is unusually helpful for this packet because it preserves both the beauty-discovery operating narrative and the linked annual and quarterly presentation files in addition to the SEC chain.
