# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CZR-T1 | AnnualReports.com Caesars verification note | 2026-08-09 | Aggregator verification note | Confirms sector / industry labeling and shows the AnnualReports coverage mismatch that should not anchor the packet | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/resorts-casinos/caesars-entertainment-corporation/annualreports-verification.md) |
| CZR-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/caesars-entertainment-corporation/official-ir-verification.md) |
| CZR-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001590895.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/caesars-entertainment-corporation/submissions-cik0001590895.json) |
| CZR-T4 | 2025 Form `10-K` | 2026-02-17 filed / 2026-08-09 collected | SEC filing HTML | Annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/caesars-entertainment-corporation/2025-10k.html) |
| CZR-T5 | 2025 Q4 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves fourth-quarter and full-year `2025` operating narrative and metrics | `[Disclosed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/caesars-entertainment-corporation/2025-q4-press-release.html) |
| CZR-T6 | 2025 Q4 earnings `8-K` | 2026-02-17 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/caesars-entertainment-corporation/2025-q4-8k.html) |
| CZR-T7 | 2026 Q1 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves first-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/caesars-entertainment-corporation/2026-q1-press-release.html) |
| CZR-T8 | 2026 Q1 earnings `8-K` | 2026-04-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/caesars-entertainment-corporation/2026-q1-8k.html) |
| CZR-T9 | 2026 Q1 Form `10-Q` | 2026-04-28 filed / 2026-08-09 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/caesars-entertainment-corporation/2026-q1-10q.html) |
| CZR-T10 | 2026 Q2 press release exhibit | 2026-08-09 collected | Company press release HTML via SEC exhibit | Preserves second-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/resorts-casinos/caesars-entertainment-corporation/2026-q2-press-release.html) |
| CZR-T11 | 2026 Q2 earnings `8-K` | 2026-07-28 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/caesars-entertainment-corporation/2026-q2-8k.html) |
| CZR-T12 | 2026 Q2 Form `10-Q` | 2026-07-28 filed / 2026-08-09 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/resorts-casinos/caesars-entertainment-corporation/2026-q2-10q.html) |

## Reconciliation notes

- Caesars now has the core SEC filing chain on disk for the fiscal `2025` annual filing and the last three quarters in scope.
- The local packet does not yet include the official annual report PDF even though the current live Caesars IR page exposes a real `195` page PDF object, because machine-local shell clients still fail after connect against that object from this environment.
- That gap does not materially weaken the annual evidence chain because the local SEC `10-K` is already on disk and contains the loyalty, digital-wallet, and segment disclosures needed for the current packet.
- AnnualReports.com is useful for discovery and classification, but its current Caesars click-through path is not reliable enough to anchor the annual artifact for this packet.

## Missing evidence

- No standalone transcript artifacts for the `Q4 2025`, `Q1 2026`, or `Q2 2026` earnings calls are saved locally.
- No local copy of the official IR annual report PDF is saved yet, even though the live IR URL has been verified.
