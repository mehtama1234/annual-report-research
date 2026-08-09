# Source Ledger

Date baseline: 2026-08-09

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
| FCX-T1 | AnnualReports company page | 2026-08-09 | AnnualReports company page | Confirms AnnualReports taxonomy for `Basic Materials` / `Copper` and shows the site still lagged at the `2024` annual package as of the collection date | `[Disclosed]` | not saved locally; verified via https://www.annualreports.com/Company/freeport-mcmoran-copper-gold-inc |
| FCX-T2 | Freeport-McMoRan 2025 Form 10-K | 2026-02-14 | SEC filing HTML | Core annual filing covering operations, segment mix, copper growth strategy, Grasberg exposure, and capital allocation | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/copper/freeport-mcmoran-copper-gold-inc/2025-10k.html) |
| FCX-T3 | Freeport 2025 annual report PDF | 2026-02-14 | Annual report PDF | Official annual report to stockholders for `2025`; useful for management framing and operating overview | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/copper/freeport-mcmoran-inc/2025-annual-report.pdf) |
| FCX-T4 | Freeport fourth-quarter and year-ended 2025 results exhibit | 2026-01-22 | SEC exhibit 99.1 | Provides `Q4 2025` and full-year `2025` earnings, cash flow, capex, production, sales, and realized-price data | `[Filed]` | [2025-q4-results-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/copper/freeport-mcmoran-inc/2025-q4-results-exhibit-99-1.html) |
| FCX-T5 | Q4 2025 8-K | 2026-01-22 | SEC filing HTML | Wrapper filing for the fourth-quarter and full-year `2025` results package | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/copper/freeport-mcmoran-copper-gold-inc/2025-q4-8k.html) |
| FCX-T6 | Freeport first-quarter 2026 results exhibit | 2026-04-23 | SEC exhibit 99.1 | Provides `Q1 2026` earnings, operating cash flow, capex, production, sales, and 2026 operating outlook updates | `[Filed]` | [2026-q1-results-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/copper/freeport-mcmoran-inc/2026-q1-results-exhibit-99-1.html) |
| FCX-T7 | Q1 2026 8-K | 2026-04-23 | SEC filing HTML | Wrapper filing for first-quarter `2026` results release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/copper/freeport-mcmoran-copper-gold-inc/2026-q1-8k.html) |
| FCX-T8 | Q1 2026 Form 10-Q | 2026-04-24 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31`, including detailed cash flow and balance sheet data | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/copper/freeport-mcmoran-copper-gold-inc/2026-q1-10q.html) |
| FCX-T9 | Freeport second-quarter and six-month 2026 results exhibit | 2026-07-23 | SEC exhibit 99.1 | Provides `Q2 2026` earnings, cash flow, capex, production, sales, realized-price data, and updated 2026 outlook | `[Filed]` | [2026-q2-results-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/copper/freeport-mcmoran-inc/2026-q2-results-exhibit-99-1.html) |
| FCX-T10 | Q2 2026 8-K | 2026-07-23 | SEC filing HTML | Wrapper filing for second-quarter and six-month `2026` results release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/copper/freeport-mcmoran-copper-gold-inc/2026-q2-8k.html) |
| FCX-T11 | Q2 2026 Form 10-Q | 2026-07-24 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30`, including year-to-date cash flow, debt, and liquidity detail | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/copper/freeport-mcmoran-copper-gold-inc/2026-q2-10q.html) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-09` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports remained useful for sector and industry taxonomy, but it still displayed the `2024` annual package for Freeport on `2026-08-09`, so the actual `2025` and `2026` evidence set relies mainly on SEC-hosted annual and quarterly materials.
- Freeport investor-relations pages were confirmed via search results and titles, but the site rate-limited direct shell fetches behind Cloudflare during this pass. SEC-hosted Exhibit `99.1` result releases were saved locally instead.
- No standalone earnings-call transcript artifact is saved locally for the current Freeport pass.

## Missing evidence

- No locally saved AnnualReports company page artifact for Freeport-McMoRan Inc.
- No locally saved verbatim earnings-call transcript for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
