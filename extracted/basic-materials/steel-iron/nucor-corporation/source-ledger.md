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
| NUE-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports company page | Confirms AnnualReports taxonomy for `Basic Materials` / `Steel & Iron` and shows the site still lagged at the `2024` annual package as of the collection date | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/steel-iron/nucor-corporation/company-page-annualreports.html) |
| NUE-T2 | Nucor 2025 annual report PDF | 2026-02-20 | Annual report PDF | Official annual report to stockholders for `2025` with management framing and operating overview | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/nucor-corporation/2025-annual-report.pdf) |
| NUE-T3 | Nucor 2025 Form 10-K | 2026-02-20 | SEC filing HTML | Core annual filing covering segment mix, steel capacity, demand exposure, capital expenditures, and risks | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/nucor-corporation/2025-10k.html) |
| NUE-T4 | Nucor fourth-quarter 2025 results exhibit | 2026-01-26 | SEC exhibit 99.1 | Provides `Q4 2025` earnings, net sales, EBITDA, segment comparison, and management framing for the full-year handoff into `2026` | `[Filed]` | [2025-q4-results-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/nucor-corporation/2025-q4-results-exhibit-99-1.html) |
| NUE-T5 | Q4 2025 8-K | 2026-01-26 | SEC filing HTML | Wrapper filing for the fourth-quarter `2025` results release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/nucor-corporation/2025-q4-8k.html) |
| NUE-T6 | Nucor first-quarter 2026 results exhibit | 2026-04-27 | SEC exhibit 99.1 | Provides `Q1 2026` earnings, net sales, EBITDA, segment comparison, cash position, and `Q2 2026` outlook | `[Filed]` | [2026-q1-results-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/nucor-corporation/2026-q1-results-exhibit-99-1.html) |
| NUE-T7 | Q1 2026 8-K | 2026-04-27 | SEC filing HTML | Wrapper filing for first-quarter `2026` results release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/nucor-corporation/2026-q1-8k.html) |
| NUE-T8 | Q1 2026 Form 10-Q | 2026-05-13 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-04-04`, including detailed financial statements and cash flow data | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/nucor-corporation/2026-q1-10q.html) |
| NUE-T9 | Nucor second-quarter 2026 results exhibit | 2026-07-27 | SEC exhibit 99.1 | Provides `Q2 2026` earnings, net sales, EBITDA, segment comparison, cash position, and `Q3 2026` outlook | `[Filed]` | [2026-q2-results-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/nucor-corporation/2026-q2-results-exhibit-99-1.html) |
| NUE-T10 | Q2 2026 8-K | 2026-07-27 | SEC filing HTML | Wrapper filing for second-quarter `2026` results release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/nucor-corporation/2026-q2-8k.html) |
| NUE-T11 | SEC submissions JSON | 2026-08-10 collected | SEC company feed | Preserves the filing index confirming the `2025 10-K`, `Q4 2025`, `Q1 2026`, and `Q2 2026` results chain and confirms no separately filed `Q2 2026` `10-Q` was present locally as of `2026-08-10` | `[Filed]` | [submissions-cik0000073309.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/nucor-corporation/submissions-cik0000073309.json) |

## Reconciliation notes

- The correct trailing-quarter set as of `Monday, August 10, 2026` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports remained useful for sector and industry taxonomy, but it still displayed the `2024` annual package for Nucor on `2026-08-10`, so the actual `2025` and `2026` evidence set relies mainly on Nucor investor-relations and SEC-hosted materials.
- As of `Monday, August 10, 2026`, the local SEC chain included the `Q2 2026` earnings release and wrapper `8-K`, but no separately filed `Q2 2026` `10-Q`.
- No standalone earnings-call transcript artifact is saved locally for the current Nucor pass.

## Missing evidence

- No locally saved official earnings-call transcript for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No separately filed `Q2 2026` `10-Q` artifact was present locally as of `Monday, August 10, 2026`.
