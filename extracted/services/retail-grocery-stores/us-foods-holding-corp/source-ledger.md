# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| USFD-T1 | AnnualReports company page | 2026-08-10 | Aggregator page | Confirms Food Wholesale taxonomy and AnnualReports lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/retail-grocery-stores/us-foods-holding-corp/company-page.html) |
| USFD-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Normalizes the taxonomy and lag observation into repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/retail-grocery-stores/us-foods-holding-corp/annualreports-verification.md) |
| USFD-T3 | US Foods IR source-links note | 2026-08-10 | Official-source link ledger | Preserves the attempted IR path and documents host-resolution failure in this shell environment | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/us-foods-holding-corp/ir-source-links.md) |
| USFD-T4 | US Foods SEC source-links note | 2026-08-10 | SEC filing URL ledger | Preserves the exact annual and quarter filing URLs used for the packet | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/sec-source-links.md) |
| USFD-T5 | US Foods 2025 annual report PDF | 2026-04-02 filed / 2026-08-10 collected | SEC ARS PDF | Official annual report artifact for fiscal `2025` | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2025-annual-report.pdf) |
| USFD-T6 | US Foods 2025 Form 10-K | 2026-02-12 filed / 2026-08-10 collected | SEC filing HTML | Filed annual report for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2025-10k.html) |
| USFD-T7 | US Foods Q4 2025 earnings-release exhibit | 2026-02-12 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for late-`2025` results | `[Filed]` | [2025-q4-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2025-q4-results-release.html) |
| USFD-T8 | US Foods Q4 2025 earnings 8-K | 2026-02-12 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the late-`2025` release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2025-q4-8k.html) |
| USFD-T9 | US Foods Q1 2026 earnings-release exhibit | 2026-05-07 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for the quarter ended `2026-03-28` | `[Filed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2026-q1-results-release.html) |
| USFD-T10 | US Foods Q1 2026 earnings 8-K | 2026-05-07 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q1 `2026` release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2026-q1-8k.html) |
| USFD-T11 | US Foods Q1 2026 Form 10-Q | 2026-05-07 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-28` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2026-q1-10q.html) |
| USFD-T12 | US Foods Q2 2026 earnings-release exhibit | 2026-08-06 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for the quarter ended `2026-06-27` | `[Filed]` | [2026-q2-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2026-q2-results-release.html) |
| USFD-T13 | US Foods Q2 2026 earnings 8-K | 2026-08-06 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q2 `2026` release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2026-q2-8k.html) |
| USFD-T14 | US Foods Q2 2026 Form 10-Q | 2026-08-06 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-27` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/2026-q2-10q.html) |
| USFD-T15 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Verifies filing dates, accession numbers, CIK, and recent quarter sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/us-foods-holding-corp/sec-submissions.json) |

## Reconciliation notes

- US Foods now has a coherent annual-plus-quarter filing chain for the required `2025` annual package and the last three reported quarters as of `2026-08-10`.
- AnnualReports still lagged at `2024`, so the `2025` annual package is intentionally anchored to the SEC `ARS` and `10-K` chain.
- The official US Foods IR host did not resolve in this shell environment, but that does not weaken the quarter evidence because the filed `99.1` exhibits and `10-Q`s are saved locally.

## Missing evidence

- No local earnings-call transcript artifacts are saved.
- No mirrored official IR HTML pages are saved because the host failed DNS resolution in this shell environment.
