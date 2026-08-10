# Source Ledger

Date baseline: 2026-08-08

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` SEC filing or exhibit
- `[Reported]` credible press or transcript provider
- `[Estimated]` derived or analyst estimate
- `[Speculative]` weak or unverified
- `[verify]` found but not yet confirmed directly

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CHRW-T1 | AnnualReports.com C.H. Robinson company page | 2026-08-08 | Aggregator page | Confirms `Services` / `Air Delivery & Freight Services` classification and shows AnnualReports already hosting the `2025` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/air-delivery-freight-services/ch-robinson-worldwide-inc/company-page-annualreports.html) |
| CHRW-T2 | AnnualReports-hosted 2025 annual report PDF | 2026-08-08 | Annual report PDF | Captures the hosted annual-report artifact linked from AnnualReports for the 2025 cycle | `[Reported]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2025-annual-report.pdf) |
| CHRW-T3 | SEC submissions JSON for C.H. Robinson | 2026-08-08 | SEC index JSON | Confirms CIK, ticker, exchange, filing chronology, and the authoritative annual and trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/sec-submissions.json) |
| CHRW-T4 | C.H. Robinson 2025 Form 10-K | 2026-02-13 | SEC filing HTML | Filed annual package for the year ended `2025-12-31`, covering segment structure, network scale, revenues, earnings, and risk disclosures | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2025-10k.html) |
| CHRW-T5 | Q4 2025 8-K | 2026-01-28 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2025-q4-8k.html) |
| CHRW-T6 | Q4 2025 earnings release exhibit | 2026-01-28 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics, market-share commentary, freight-market framing, and cash-flow guidance | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2025-q4-earnings-release-sec-ex99.html) |
| CHRW-T7 | Q1 2026 8-K | 2026-04-29 | SEC filing HTML | Wrapper filing for first-quarter 2026 earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2026-q1-8k.html) |
| CHRW-T8 | Q1 2026 earnings release exhibit | 2026-04-29 | SEC exhibit HTML | Exact Q1 2026 metrics, Cass comparison, Lean AI framing, and margin context | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2026-q1-earnings-release-sec-ex99.html) |
| CHRW-T9 | Q1 2026 Form 10-Q | 2026-05-01 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31`, including revenue, gross-profit, and segment detail | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2026-q1-10q.html) |
| CHRW-T10 | Q2 2026 8-K | 2026-07-29 | SEC filing HTML | Wrapper filing for second-quarter 2026 earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2026-q2-8k.html) |
| CHRW-T11 | Q2 2026 earnings release exhibit | 2026-07-29 | SEC exhibit HTML | Exact Q2 2026 metrics, margin-target commentary, productivity claims, and working-capital/cash-flow pressure | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2026-q2-earnings-release-sec-ex99.html) |
| CHRW-T12 | Q2 2026 Form 10-Q | 2026-07-31 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30`, including segment-level revenues, profits, and updated balance-sheet context | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/air-delivery-freight-services/ch-robinson-worldwide-inc/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here both for classification and for the hosted `2025` annual-report PDF; unlike several other names in the archive, it is not lagging for CHRW as of `2026-08-08`.
- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The CHRW evidence chain is covered through the AnnualReports company page and annual-report PDF, the filed `2025` Form `10-K`, the filed quarterly `10-Q`s, and the filed earnings-release exhibits.

## Missing evidence

- No official transcript artifact was collected for Q4 2025, Q1 2026, or Q2 2026.
