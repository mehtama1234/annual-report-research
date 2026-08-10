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
| ABM-T1 | AnnualReports.com ABM company page | 2026-08-10 | Aggregator page | Confirms `Industrial Goods` / `Business Services` classification, headquarters, employee scale, and the hosted `2025` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/business-services/abm-industries-inc/company-page-annualreports.html) |
| ABM-T2 | SEC submissions JSON for ABM | 2026-08-10 | SEC index JSON | Confirms CIK, ticker, exchange, October fiscal year-end, and the authoritative annual plus trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/sec-submissions.json) |
| ABM-T3 | ABM 2025 annual report to shareholders / ARS | 2026-02-13 | Annual report PDF | Core annual narrative package for the year ended `2025-10-31` | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/business-services/abm-industries-inc/2025-annual-report-sec-ars.pdf) |
| ABM-T4 | ABM 2025 Form 10-K | 2025-12-19 | SEC filing HTML | Filed annual package covering business mix, segment structure, technical-solutions positioning, and risk disclosures | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2025-10k.html) |
| ABM-T5 | FY2025 Q4 8-K | 2025-12-17 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year fiscal `2025` results and WGNSTAR transaction announcement | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2025-q4-8k.html) |
| ABM-T6 | FY2025 Q4 earnings release exhibit | 2025-12-17 | SEC exhibit HTML | Exact Q4 and full-year fiscal `2025` metrics, new-sales-booking data, and initial fiscal `2026` outlook | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2025-q4-earnings-release-sec-ex99.html) |
| ABM-T7 | FY2026 Q1 8-K | 2026-03-10 | SEC filing HTML | Wrapper filing for first-quarter fiscal `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2026-q1-8k.html) |
| ABM-T8 | FY2026 Q1 earnings release exhibit | 2026-03-10 | SEC exhibit HTML | Exact Q1 fiscal `2026` metrics, repurchase activity, WGNSTAR close, and datacenter / mission-critical demand commentary | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2026-q1-earnings-release-sec-ex99.html) |
| ABM-T9 | FY2026 Q1 Form 10-Q | 2026-03-10 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-01-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2026-q1-10q.html) |
| ABM-T10 | FY2026 Q2 8-K | 2026-06-05 | SEC filing HTML | Wrapper filing for second-quarter fiscal `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2026-q2-8k.html) |
| ABM-T11 | FY2026 Q2 earnings release exhibit | 2026-06-05 | SEC exhibit HTML | Exact Q2 fiscal `2026` metrics, first-half bookings, battery-storage and datacenter ATS demand, and Heathrow contract commentary | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2026-q2-earnings-release-sec-ex99.html) |
| ABM-T12 | FY2026 Q2 Form 10-Q | 2026-06-05 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-04-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/abm-industries-inc/2026-q2-10q.html) |

## Reconciliation notes

- ABM had been partially started under a `services/business-services` path, but the active archive should stay under `industrial-goods/business-services` because AnnualReports explicitly classifies the company there as of `2026-08-10`.
- ABM uses an October fiscal year-end, so the correct trailing-quarter set as of `2026-08-10` is `FY2026 Q2`, `FY2026 Q1`, and `FY2025 Q4`.
- The annual chain is strong because both the AnnualReports page and SEC filings support the `2025` annual package.
- The quarterlies are fully covered with `8-K` wrappers, filed earnings-release exhibits, and filed `10-Q`s.

## Missing evidence

- No official earnings-call transcript artifact was collected for FY2025 Q4, FY2026 Q1, or FY2026 Q2.
