# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| MGM-T1 | AnnualReports.com MGM verification note | 2026-08-09 | Aggregator verification note | Confirms sector / industry labeling and documents that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/resorts-casinos/mgm-resorts-international/annualreports-verification.md) |
| MGM-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/mgm-resorts-international/official-ir-verification.md) |
| MGM-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000789570.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/mgm-resorts-international/submissions-cik0000789570.json) |
| MGM-T4 | 2025 annual report PDF | 2026-08-09 collected | Official IR PDF | Preserves the official annual-report artifact exposed by MGM IR | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/mgm-resorts-international/2025-annual-report.pdf) |
| MGM-T5 | 2025 Form `10-K` | 2026-02-11 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/mgm-resorts-international/2025-10k.html) |
| MGM-T6 | 2025 annual report SEC artifact | 2026-03-27 filed / 2026-08-09 collected | SEC PDF | Preserves the annual-report artifact filed through the SEC annual-report delivery path | `[Filed]` | [2025-annual-report-ars.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/mgm-resorts-international/2025-annual-report-ars.pdf) |
| MGM-T7 | 2025 Q4 results release page | 2026-08-09 collected | Official IR HTML | Preserves fourth-quarter and full-year `2025` operating narrative and segment metrics | `[Disclosed]` | [2025-q4-results-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/mgm-resorts-international/2025-q4-results-release.html) |
| MGM-T8 | 2025 Q4 earnings `8-K` | 2026-02-05 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/mgm-resorts-international/2025-q4-8k.html) |
| MGM-T9 | 2026 Q1 results release page | 2026-08-09 collected | Official IR HTML | Preserves first-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/mgm-resorts-international/2026-q1-results-release.html) |
| MGM-T10 | 2026 Q1 earnings `8-K` | 2026-04-29 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/mgm-resorts-international/2026-q1-8k.html) |
| MGM-T11 | 2026 Q1 Form `10-Q` | 2026-04-29 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/mgm-resorts-international/2026-q1-10q.html) |
| MGM-T12 | 2026 Q2 results release page | 2026-08-09 collected | Official IR HTML | Preserves second-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q2-results-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/mgm-resorts-international/2026-q2-results-release.html) |
| MGM-T13 | 2026 Q2 earnings `8-K` | 2026-07-29 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/mgm-resorts-international/2026-q2-8k.html) |
| MGM-T14 | 2026 Q2 Form `10-Q` | 2026-07-29 filed / 2026-08-09 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/mgm-resorts-international/2026-q2-10q.html) |

## Reconciliation notes

- MGM now has the full annual-plus-quarter chain on disk for the fiscal `2025` annual package and the last three quarters in scope.
- AnnualReports.com remains useful for discovery and classification, but as of `2026-08-09` it still lagged at `2024` while the official MGM IR stack was current at `2025`.
- The IR stack is strong enough that the packet can preserve both the official annual report PDF and the company results pages, not only the SEC filing wrappers.
- The quarter chain shows a useful structural distinction between `MGM Digital` and the unconsolidated `BetMGM North America Venture`; the packet should not flatten those into one business.

## Missing evidence

- No standalone transcript artifacts for the `Q4 2025`, `Q1 2026`, or `Q2 2026` earnings calls are saved locally.
- No local `Q2 2026` IR-hosted filing PDF is saved; the annual and Q1 IR filing PDFs are preserved, while the SEC `10-Q` HTML remains the main filed artifact for the latest quarter.
