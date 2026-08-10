# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| ULCC-T1 | AnnualReports Frontier verification note | 2026-08-09 | Aggregator verification note | Confirms current AnnualReports taxonomy and archive lag | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/annualreports-verification.md) |
| ULCC-T2 | Official IR verification note | 2026-08-09 | Official IR verification note | Preserves the official IR URL chain and notes live retrieval instability | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/official-ir-verification.md) |
| ULCC-T3 | SEC submissions index | 2026-08-09 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0001670076.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/submissions-cik0001670076.json) |
| ULCC-T4 | 2025 annual report PDF | 2026-02-18 filed / 2026-08-09 collected | SEC-hosted annual report PDF | Standalone annual-report artifact for the target annual year | `[Filed]` | [2025-annual-report-ars.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2025-annual-report-ars.pdf) |
| ULCC-T5 | 2025 Form `10-K` | 2026-02-18 filed / 2026-08-09 collected | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2025-10k.html) |
| ULCC-T6 | 2025 Q4 earnings `8-K` | 2026-02-11 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2025-q4-8k.html) |
| ULCC-T7 | 2025 Q4 earnings release | 2026-02-11 filed / 2026-08-09 collected | SEC Exhibit `99.1` HTML | Full fourth-quarter and full-year `2025` results text | `[Filed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2025-q4-earnings-release.html) |
| ULCC-T8 | 2026 Q1 `10-Q` | 2026-05-05 filed / 2026-08-09 collected | SEC filing HTML | Latest spring quarter in scope, including TSA reserve and early-return charges | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2026-q1-10q.html) |
| ULCC-T9 | 2026 Q1 earnings `8-K` | 2026-05-05 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2026-q1-8k.html) |
| ULCC-T10 | 2026 Q1 earnings release | 2026-05-05 filed / 2026-08-09 collected | SEC Exhibit `99.1` HTML | Full first-quarter `2026` results text and guidance framing | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2026-q1-earnings-release.html) |
| ULCC-T11 | 2026 Q2 `10-Q` | 2026-07-29 filed / 2026-08-09 collected | SEC filing HTML | Most recent quarter in scope, including full first-half bridge | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2026-q2-10q.html) |
| ULCC-T12 | 2026 Q2 earnings `8-K` | 2026-07-29 filed / 2026-08-09 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2026-q2-8k.html) |
| ULCC-T13 | 2026 Q2 earnings release | 2026-07-29 filed / 2026-08-09 collected | SEC Exhibit `99.1` HTML | Full second-quarter `2026` results text including early-return reconciliation | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/air-delivery-freight-services/frontier-group-holdings-inc/2026-q2-earnings-release.html) |

## Reconciliation notes

- AnnualReports currently places Frontier in `Industrial Goods / Air Delivery & Freight Services`, even though the company is plainly one of the archive's most consumer-facing airline operators.
- The official IR site clearly exposes the current quarter pages, but the reliable local text chain in this environment is the SEC exhibit stack.
- The packet therefore uses the official IR URL verification note plus the locally saved SEC earnings-release exhibits and filings.

## Missing evidence

- No standalone latest-quarter transcript artifact is saved locally.
- No clean local HTML snapshots of the live Frontier IR result pages are saved because direct shell retrieval returned challenge-style pages in this environment.
