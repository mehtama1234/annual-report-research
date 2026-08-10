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
| PFE-T1 | AnnualReports.com Pfizer company page | 2026-08-08 | Aggregator page | Confirms Healthcare / Drug Manufacturers - General classification and shows AnnualReports currently lagging at `2024` for the hosted annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/healthcare/drug-manufacturers-general/pfizer-inc/company-page-annualreports.html) |
| PFE-T2 | SEC submissions JSON for Pfizer | 2026-08-08 | SEC index JSON | Confirms CIK, fiscal year-end, and the authoritative filing chain for the annual and trailing three quarters | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/sec-submissions.json) |
| PFE-T3 | Pfizer 2025 annual report to security holders | 2026-03-12 | Annual report PDF | Core annual narrative and annual financial package for the year ended `2025-12-31` | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/drug-manufacturers-general/pfizer-inc/2025-annual-report-sec-ars.pdf) |
| PFE-T4 | Pfizer 2025 Form 10-K | 2026-02-26 | SEC filing HTML | Standalone annual filing covering portfolio structure, risks, and 2025 financial framing | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2025-10k.html) |
| PFE-T5 | Q4 2025 8-K | 2026-02-03 | SEC filing HTML | Wrapper filing for fourth-quarter 2025 earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2025-q4-8k.html) |
| PFE-T6 | Q4 2025 earnings release exhibit | 2026-02-03 | SEC exhibit HTML | Exact Q4 and full-year 2025 metrics plus initial 2026 guidance reaffirmation | `[Filed]` | [2025-q4-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2025-q4-earnings-release-sec-ex99.html) |
| PFE-T7 | Q1 2026 8-K | 2026-05-05 | SEC filing HTML | Wrapper filing for first-quarter 2026 earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2026-q1-8k.html) |
| PFE-T8 | Q1 2026 earnings release exhibit | 2026-05-05 | SEC exhibit HTML | Exact Q1 2026 metrics, launched-and-acquired growth data, and guidance reaffirmation | `[Filed]` | [2026-q1-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2026-q1-earnings-release-sec-ex99.html) |
| PFE-T9 | Q1 2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-29` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2026-q1-10q.html) |
| PFE-T10 | Q2 2026 8-K | 2026-08-04 | SEC filing HTML | Wrapper filing for second-quarter 2026 earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2026-q2-8k.html) |
| PFE-T11 | Q2 2026 earnings release exhibit | 2026-08-04 | SEC exhibit HTML | Exact Q2 2026 metrics, raised revenue guidance, and productivity-program expansion | `[Filed]` | [2026-q2-earnings-release-sec-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2026-q2-earnings-release-sec-ex99.html) |
| PFE-T12 | Q2 2026 Form 10-Q | 2026-08-04 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-28` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/drug-manufacturers-general/pfizer-inc/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is useful here for classification only. It still lagged at `2024`, so the authoritative `2025` annual evidence chain comes from SEC-hosted annual-report and `10-K` materials.
- The correct trailing-quarter set as of `2026-08-08` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The trailing-three-quarter scope is fully covered using SEC `8-K` wrappers, filed earnings-release exhibits, and quarterly reports.
- Pfizer investor-relations pages were behind a Cloudflare challenge during this pass, so SEC-hosted materials were the practical source of truth for document capture.

## Missing evidence

- No official latest-quarter earnings-call transcript was collected for `Q2 2026`.
