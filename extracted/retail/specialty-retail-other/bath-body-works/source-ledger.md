# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BBWI-T1 | AnnualReports.com Bath & Body Works verification note | 2026-08-09 | Aggregator verification note | Confirms current annual-package availability and the source-taxonomy label | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/retail/specialty-retail-other/bath-body-works/annualreports-verification.md) |
| BBWI-T2 | AnnualReports.com company page snapshot | 2026-08-09 | Aggregator HTML snapshot | Preserves the live discovery page showing `2025 Annual Report and Form 10K` | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/retail/specialty-retail-other/bath-body-works/company-page.html) |
| BBWI-T3 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms annual-report, quarterly-results, event, and release URL coverage for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/retail/specialty-retail-other/bath-body-works/official-ir-verification.md) |
| BBWI-T4 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000701985.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/specialty-retail-other/bath-body-works/submissions-cik0000701985.json) |
| BBWI-T5 | 2025 annual report PDF | 2026-08-09 collected | SEC annual report PDF | Official annual-report-to-security-holders artifact preserved locally | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/retail/specialty-retail-other/bath-body-works/2025-annual-report.pdf) |
| BBWI-T6 | 2025 Form `10-K` | 2026-03-12 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the fiscal year ended `2026-01-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/specialty-retail-other/bath-body-works/2025-10k.html) |
| BBWI-T7 | 2025 Q3 earnings `8-K` | 2025-11-20 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/specialty-retail-other/bath-body-works/2025-q3-8k.html) |
| BBWI-T8 | 2025 Q3 Form `10-Q` | 2025-11-20 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/specialty-retail-other/bath-body-works/2025-q3-10q.html) |
| BBWI-T9 | 2025 Q4 earnings `8-K` | 2026-03-04 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/specialty-retail-other/bath-body-works/2025-q4-8k.html) |
| BBWI-T10 | 2026 Q1 earnings `8-K` | 2026-05-27 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/specialty-retail-other/bath-body-works/2026-q1-8k.html) |
| BBWI-T11 | 2026 Q1 Form `10-Q` | 2026-05-27 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/retail/specialty-retail-other/bath-body-works/2026-q1-10q.html) |

## Reconciliation notes

- Bath & Body Works now has a full evidence chain on disk for the `2025` annual-report window and the last three reported quarters in scope as of `2026-08-09`.
- The official IR pages are current and verifiable, but direct scripted quarter-release HTML capture repeatedly timed out or dropped on transport errors in this environment.
- The archive therefore relies on the SEC-hosted quarter release chain for durable local preservation and keeps the official IR URLs as verified reference points.
