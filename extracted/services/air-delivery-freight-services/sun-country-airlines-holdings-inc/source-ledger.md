# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| SNCY-T1 | AnnualReports.com Sun Country verification note | 2026-08-09 | Aggregator verification note | Confirms sector / industry labeling and documents that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/annualreports-verification.md) |
| SNCY-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Preserves the official IR URL chain and documents the merger-era quarter gap plus current retrieval issues | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/official-ir-verification.md) |
| SNCY-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence through the `2025` annual and `2026` merger window | `[Filed]` | [submissions-cik0001743907.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/submissions-cik0001743907.json) |
| SNCY-T4 | 2025 Form `10-K` | 2026-02-12 filed / 2026-08-09 collected | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/2025-10k.html) |
| SNCY-T5 | 2025 Form `10-K/A` | 2026-04-30 filed / 2026-08-09 collected | SEC filing HTML | Amended annual filing preserved alongside the base annual filing | `[Filed]` | [2025-10k-a.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/2025-10k-a.html) |
| SNCY-T6 | 2025 Q4 earnings `8-K` | 2026-02-05 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/2025-q4-8k.html) |
| SNCY-T7 | 2025 Q3 Form `10-Q` | 2025-10-30 filed / 2026-08-09 collected | SEC filing HTML | Filed third-quarter report showing the mid-`2025` capacity shift toward cargo | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/2025-q3-10q.html) |
| SNCY-T8 | 2025 Q3 earnings `8-K` | 2025-10-29 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/2025-q3-8k.html) |
| SNCY-T9 | 2026 Q1 Form `10-Q` | 2026-05-01 filed / 2026-08-09 collected | SEC filing HTML | Latest filed quarter in scope, including merger status and cargo-growth details | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/sun-country-airlines-holdings-inc/2026-q1-10q.html) |

## Reconciliation notes

- Sun Country does not currently present as a full airline IR packet in the same way Delta, United, or Southwest do in this archive.
- The strongest evidence chain is the saved AnnualReports page plus the SEC annual and quarter filings.
- The official IR URLs are preserved in the verification note because the live site exposed the relevant pages through discovery, but repeated direct shell retrieval of those HTML pages was unreliable in this environment.
- As of `2026-08-09`, the latest verified quarter in the public chain was `Q1 2026`; after that point, the disclosure stream was dominated by Allegiant merger materials rather than a normal next earnings cycle.

## Missing evidence

- No standalone `2025` annual-report PDF artifact is saved locally.
- No standalone `Q4 2025`, `Q1 2026`, or `Q3 2025` transcript files are saved locally.
- No clean local HTML snapshots of the live Sun Country IR release pages are saved because direct retrieval repeatedly stalled in this environment.
