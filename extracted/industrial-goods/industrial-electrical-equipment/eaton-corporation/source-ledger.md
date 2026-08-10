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
| ETN-T1 | AnnualReports.com Eaton company page | 2026-08-08 | Aggregator page | Confirms Industrial Goods / Industrial Electrical Equipment classification and shows AnnualReports still lagging at `2024` for the hosted annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/industrial-goods/industrial-electrical-equipment/eaton-corporation/company-page-annualreports.html) |
| ETN-T2 | SEC submissions JSON for Eaton | 2026-08-08 | SEC index JSON | Confirms CIK, fiscal year-end, and the authoritative annual and trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/sec-submissions.json) |
| ETN-T3 | Eaton 2025 annual report | 2026-03-13 | Annual report PDF | Core annual narrative covering electrification, data centers, AI infrastructure, acquisitions, and capacity investment | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/industrial-goods/industrial-electrical-equipment/eaton-corporation/2025-annual-report-sec-ars.pdf) |
| ETN-T4 | Eaton 2025 Form 10-K | 2026-02-26 | SEC filing HTML | Standalone annual filing for the year ended `2025-12-31`, including segment structure, backlog framing, and risk disclosures | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2025-10k.html) |
| ETN-T5 | Q4 2025 8-K | 2026-02-03 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 earnings results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2025-q4-8k.html) |
| ETN-T6 | Q4 2025 earnings release exhibit | 2026-02-26 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics, 2026 initial guidance, and order/backlog acceleration language | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2025-q4-earnings-release-sec-ex99.html) |
| ETN-T7 | Q1 2026 8-K | 2026-05-05 | SEC filing HTML | Wrapper filing for first-quarter 2026 earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2026-q1-8k.html) |
| ETN-T8 | Q1 2026 earnings release exhibit | 2026-05-05 | SEC exhibit HTML | Exact Q1 2026 metrics, raised organic-growth guidance, and large acquisition-close detail | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2026-q1-earnings-release-sec-ex99.html) |
| ETN-T9 | Q1 2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31`, including total backlog near `$22.8 billion` and acquisition accounting detail | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2026-q1-10q.html) |
| ETN-T10 | Q2 2026 8-K | 2026-07-31 | SEC filing HTML | Wrapper filing for second-quarter 2026 earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2026-q2-8k.html) |
| ETN-T11 | Q2 2026 earnings release exhibit | 2026-07-31 | SEC exhibit HTML | Exact Q2 2026 metrics, raised organic-growth and adjusted-EPS guidance, and Mobility separation announcement | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2026-q2-earnings-release-sec-ex99.html) |
| ETN-T12 | Q2 2026 Form 10-Q | 2026-07-31 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30`, including total backlog near `$24.1 billion` and acquisition-accounting updates | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/industrial-goods/industrial-electrical-equipment/eaton-corporation/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for classification and folder taxonomy, but as of `2026-08-08` it still lags at `2024` for the hosted annual package.
- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The Eaton evidence chain is fully covered with SEC annual-report materials, `8-K` wrappers, filed earnings-release exhibits, and `10-Q` filings.
- No official latest-quarter earnings-call transcript was collected during this pass even though the releases reference a webcast.

## Missing evidence

- No official transcript artifact was collected for Q4 2025, Q1 2026, or Q2 2026.
