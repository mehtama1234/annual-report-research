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
| UNP-T1 | AnnualReports.com Union Pacific company page | 2026-08-08 | Aggregator page | Confirms Industrial Goods / Railroads classification and shows AnnualReports still lagging at `2024` for the hosted annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/industrial-goods/railroads/union-pacific-corporation/company-page-annualreports.html) |
| UNP-T2 | SEC submissions JSON for Union Pacific | 2026-08-08 | SEC index JSON | Confirms CIK, filing chronology, and the authoritative annual and trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/sec-submissions.json) |
| UNP-T3 | Union Pacific 2025 Form 10-K | 2026-02-06 | SEC filing HTML | Filed annual package for the year ended `2025-12-31`, covering revenue, operating ratio, capital investment, service metrics, and risk disclosures | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2025-10k.html) |
| UNP-T4 | Q4 2025 8-K | 2026-01-27 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2025-q4-8k.html) |
| UNP-T5 | Q4 2025 earnings release exhibit | 2026-01-27 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics, operating ratio, outlook, and merger-cost disclosure | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2025-q4-earnings-release-sec-ex99.html) |
| UNP-T6 | Q4 2025 official IR earnings release page | 2026-01-27 | Company IR page | Official presentation of Q4 2025 and full-year 2025 results on the Union Pacific website | `[Disclosed]` | [2025-q4-earnings-release-ir.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/industrial-goods/railroads/union-pacific-corporation/2025-q4-earnings-release-ir.html) |
| UNP-T7 | Q1 2026 8-K | 2026-04-23 | SEC filing HTML | Wrapper filing for first-quarter 2026 earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2026-q1-8k.html) |
| UNP-T8 | Q1 2026 earnings release exhibit | 2026-04-23 | SEC exhibit HTML | Exact Q1 2026 metrics, guidance reaffirmation, and service/productivity language | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2026-q1-earnings-release-sec-ex99.html) |
| UNP-T9 | Q1 2026 official IR earnings release page | 2026-04-23 | Company IR page | Official presentation of first-quarter 2026 results on the Union Pacific website | `[Disclosed]` | [2026-q1-earnings-release-ir.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/industrial-goods/railroads/union-pacific-corporation/2026-q1-earnings-release-ir.html) |
| UNP-T10 | Q1 2026 Form 10-Q | 2026-04-23 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31`, including volume, mix, and merger-process context | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2026-q1-10q.html) |
| UNP-T11 | Q2 2026 8-K | 2026-07-23 | SEC filing HTML | Wrapper filing for second-quarter 2026 earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2026-q2-8k.html) |
| UNP-T12 | Q2 2026 earnings release exhibit | 2026-07-23 | SEC exhibit HTML | Exact Q2 2026 metrics, improved EPS outlook, and capital-plan reaffirmation | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2026-q2-earnings-release-sec-ex99.html) |
| UNP-T13 | Q2 2026 official IR earnings release page | 2026-07-23 | Company IR page | Official presentation of second-quarter 2026 results on the Union Pacific website | `[Disclosed]` | [2026-q2-earnings-release-ir.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/industrial-goods/railroads/union-pacific-corporation/2026-q2-earnings-release-ir.html) |
| UNP-T14 | Q2 2026 Form 10-Q | 2026-07-23 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30`, including volume, pricing, mix, and merger-process context | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/railroads/union-pacific-corporation/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for classification and folder taxonomy, but as of `2026-08-08` it still lags at `2024` for the hosted annual package.
- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- This pass captured the annual evidence through the filed `2025` Form `10-K`; a separate official 2025 annual-report PDF was not directly surfaced during source capture.
- The Union Pacific evidence chain is fully covered with SEC annual and quarterly filings, `8-K` wrappers, filed earnings-release exhibits, and official company IR earnings-release pages.

## Missing evidence

- No official transcript artifact was collected for Q4 2025, Q1 2026, or Q2 2026.
