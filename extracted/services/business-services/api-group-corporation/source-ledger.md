# Source Ledger

Date baseline: 2026-08-10

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
| APG-T1 | AnnualReports.com APi Group company page | 2026-08-10 | Aggregator page | Confirms `Services` / `Business Services` classification and shows AnnualReports already hosting the `2025` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/business-services/api-group-corporation/company-page-annualreports.html) |
| APG-T2 | AnnualReports-hosted 2025 annual report PDF | 2026-08-10 | Annual report PDF | Captures the hosted annual-report artifact linked from AnnualReports for the `2025` cycle | `[Reported]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/business-services/api-group-corporation/2025-annual-report.pdf) |
| APG-T3 | SEC-filed 2025 annual report PDF / ARS | 2026-04-03 | Annual report PDF / ARS | Official annual-report artifact for the year ended `2025-12-31` | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/business-services/api-group-corporation/2025-annual-report-sec-ars.pdf) |
| APG-T4 | SEC submissions JSON for APi Group | 2026-08-10 | SEC index JSON | Confirms CIK, ticker, exchange, filing chronology, and the authoritative annual and trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/sec-submissions.json) |
| APG-T5 | APi Group 2025 Form 10-K | 2026-02-25 | SEC filing HTML | Filed annual package covering segment structure, recurring service model, acquisitions, leverage, and business-scale disclosures | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2025-10k.html) |
| APG-T6 | Q4 2025 8-K | 2026-02-25 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2025-q4-8k.html) |
| APG-T7 | Q4 2025 earnings release exhibit | 2026-02-25 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics, free-cash-flow, leverage, and `2026` guidance | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2025-q4-earnings-release-sec-ex99.html) |
| APG-T8 | Q1 2026 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter 2026 results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2026-q1-8k.html) |
| APG-T9 | Q1 2026 earnings release exhibit | 2026-04-30 | SEC exhibit HTML | Exact Q1 2026 metrics, raised full-year guidance, and acquisition commentary covering CertaSite, Wtech, and Onyx | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2026-q1-earnings-release-sec-ex99.html) |
| APG-T10 | Q1 2026 Form 10-Q | 2026-04-30 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2026-q1-10q.html) |
| APG-T11 | Q2 2026 8-K | 2026-07-30 | SEC filing HTML | Wrapper filing for second-quarter 2026 results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2026-q2-8k.html) |
| APG-T12 | Q2 2026 earnings release exhibit | 2026-07-30 | SEC exhibit HTML | Exact Q2 2026 metrics, raised full-year guidance, and backlog / recurring-revenue commentary | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2026-q2-earnings-release-sec-ex99.html) |
| APG-T13 | Q2 2026 Form 10-Q | 2026-07-30 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/business-services/api-group-corporation/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for classification and a directly hosted `2025` annual-report PDF; unlike several names in the archive, it is not lagging for APi as of `2026-08-10`.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- APi provides both an AnnualReports-hosted annual-report PDF and an SEC-filed `ARS` annual-report PDF, which makes the annual evidence chain stronger than a `10-K`-only capture.
- The quarterlies are fully covered with `8-K` wrappers, filed earnings-release exhibits, and filed `10-Q`s.

## Missing evidence

- No official transcript artifact was collected for Q4 2025, Q1 2026, or Q2 2026.
