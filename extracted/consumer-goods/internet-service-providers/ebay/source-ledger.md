# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| EBAY-T1 | AnnualReports.com eBay verification note | 2026-08-10 | Aggregator verification note | Confirms sector / industry labeling and documents that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/consumer-goods/internet-service-providers/ebay/annualreports-verification.md) |
| EBAY-T2 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official annual-report and quarterly-results URL chain for the target window, including the live IR rate-limit note | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/internet-service-providers/ebay/official-ir-verification.md) |
| EBAY-T3 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001065088.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/internet-service-providers/ebay/submissions-cik0001065088.json) |
| EBAY-T4 | 2025 annual report SEC artifact | 2026-04-30 filed / 2026-08-10 collected | SEC PDF | Preserves the annual-report artifact for the year ended `2025-12-31` | `[Filed]` | [2025-annual-report-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/internet-service-providers/ebay/2025-annual-report-ars.pdf) |
| EBAY-T5 | 2025 Form `10-K` | 2026-02-19 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/internet-service-providers/ebay/2025-10k.html) |
| EBAY-T6 | Q4 2025 results page | 2026-02-18 published / 2026-08-10 collected | Official company results HTML | Preserves fourth-quarter and full-year `2025` operating narrative and metrics | `[Disclosed]` | [2025-q4-results.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/internet-service-providers/ebay/2025-q4-results.html) |
| EBAY-T7 | Q4 2025 earnings `8-K` | 2026-02-18 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/internet-service-providers/ebay/2025-q4-8k.html) |
| EBAY-T8 | Q1 2026 results page | 2026-04-29 published / 2026-08-10 collected | Official company results HTML | Preserves first-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q1-results.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/internet-service-providers/ebay/2026-q1-results.html) |
| EBAY-T9 | Q1 2026 earnings `8-K` | 2026-04-29 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/internet-service-providers/ebay/2026-q1-8k.html) |
| EBAY-T10 | Q1 2026 Form `10-Q` | 2026-04-29 filed / 2026-08-10 collected | SEC filing HTML | Filed first-quarter report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/internet-service-providers/ebay/2026-q1-10q.html) |
| EBAY-T11 | Q2 2026 results page | 2026-08-05 published / 2026-08-10 collected | Official company results HTML | Preserves second-quarter `2026` operating narrative and metrics | `[Disclosed]` | [2026-q2-results.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/consumer-goods/internet-service-providers/ebay/2026-q2-results.html) |
| EBAY-T12 | Q2 2026 earnings `8-K` | 2026-08-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/internet-service-providers/ebay/2026-q2-8k.html) |
| EBAY-T13 | Q2 2026 Form `10-Q` | 2026-08-06 filed / 2026-08-10 collected | SEC filing HTML | Filed second-quarter report | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/consumer-goods/internet-service-providers/ebay/2026-q2-10q.html) |

## Reconciliation notes

- eBay now has the full annual-plus-quarter chain on disk for the fiscal `2025` annual package and the last three quarters in scope.
- AnnualReports remained useful for taxonomy discovery, but as of `2026-08-10` it still lagged at `2024`.
- The official live investor-navigation pages rate-limited direct shell requests during this pass, but the saved official company results pages and SEC chain were sufficient to preserve the economic evidence cleanly.
- The packet should be read as a marketplace and recommerce case, not flattened into generic online retail.

## Missing evidence

- No standalone transcript artifacts for `Q4 2025`, `Q1 2026`, or `Q2 2026` are saved locally.
- No direct local HTML snapshot of the official annual-reports page is saved because live shell requests to `investors.ebayinc.com` returned HTTP `429` during collection.
