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
| ROL-T1 | AnnualReports.com Rollins company page | 2026-08-10 | Aggregator page | Confirms `Services` / `Personal Services` classification and shows AnnualReports still lagging at `2024` for the hosted annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/personal-services/rollins-inc/company-page-annualreports.html) |
| ROL-T2 | Rollins annual-reports IR page | 2026-08-10 | Official IR HTML | Confirms the company itself now hosts the `2025 Annual Report` | `[Disclosed]` | [annual-reports-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/personal-services/rollins-inc/annual-reports-page.html) |
| ROL-T3 | Rollins quarterly-earnings IR page | 2026-08-10 | Official IR HTML | Confirms the company maintains a dedicated quarterly-earnings archive alongside filed SEC materials | `[Disclosed]` | [quarterly-earnings-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/personal-services/rollins-inc/quarterly-earnings-page.html) |
| ROL-T4 | Rollins 2025 annual report PDF | 2026-08-10 | Annual report PDF | Official annual-report artifact for the year ended `2025-12-31` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/personal-services/rollins-inc/2025-annual-report.pdf) |
| ROL-T5 | SEC submissions JSON for Rollins | 2026-08-10 | SEC index JSON | Confirms CIK, filing chronology, and the authoritative annual and trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/sec-submissions.json) |
| ROL-T6 | Rollins 2025 Form 10-K | 2026-02-12 | SEC filing HTML | Filed annual package covering revenues, cash flow, acquisitions, and operating disclosures for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2025-10k.html) |
| ROL-T7 | Q4 2025 8-K | 2026-02-11 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year 2025 results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2025-q4-8k.html) |
| ROL-T8 | Q4 2025 earnings release exhibit | 2026-02-11 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics, cash flow, and management outlook for `2026` | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2025-q4-earnings-release-sec-ex99.html) |
| ROL-T9 | Q1 2026 8-K | 2026-04-22 | SEC filing HTML | Wrapper filing for first-quarter 2026 results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2026-q1-8k.html) |
| ROL-T10 | Q1 2026 earnings release exhibit | 2026-04-22 | SEC exhibit HTML | Exact Q1 2026 metrics, March exit commentary, and margin-pressure explanation | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2026-q1-earnings-release-sec-ex99.html) |
| ROL-T11 | Q1 2026 Form 10-Q | 2026-04-23 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2026-q1-10q.html) |
| ROL-T12 | Q2 2026 8-K | 2026-07-22 | SEC filing HTML | Wrapper filing for second-quarter 2026 results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2026-q2-8k.html) |
| ROL-T13 | Q2 2026 earnings release exhibit | 2026-07-22 | SEC exhibit HTML | Exact Q2 2026 metrics and commentary on softer consumer-initiated demand and channel mix | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2026-q2-earnings-release-sec-ex99.html) |
| ROL-T14 | Q2 2026 Form 10-Q | 2026-07-23 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/personal-services/rollins-inc/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for classification and folder taxonomy, but as of `2026-08-10` it still lags at `2024` for the hosted annual package.
- The official Rollins investor-relations site now hosts the `2025 Annual Report`, so the annual evidence chain is stronger than an AnnualReports-only capture.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The quarterlies are fully covered with `8-K` wrappers, filed earnings-release exhibits, and filed `10-Q`s.

## Missing evidence

- No official transcript artifact was collected for Q4 2025, Q1 2026, or Q2 2026.
