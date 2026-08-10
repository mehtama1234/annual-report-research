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
| COP-T1 | AnnualReports.com ConocoPhillips company page | 2026-08-10 | Aggregator page | Confirms ticker, HQ, `Major Integrated Oil & Gas` / `Basic Materials` taxonomy, and that AnnualReports still lagged at the `2024` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/major-integrated-oil-gas/conocophillips/company-page-annualreports.html) |
| COP-T2 | ConocoPhillips annual report page | 2026-08-10 collected | Investor relations page | Confirms the official `2025` annual report is live on company IR and exposes the direct PDF link | `[Disclosed]` | [annual-report-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/major-integrated-oil-gas/conocophillips/annual-report-page.html) |
| COP-T3 | ConocoPhillips 2025 annual report PDF | 2026-08-10 collected | Official IR PDF | Official annual report artifact for fiscal `2025` saved locally from the company annual-report page | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/major-integrated-oil-gas/conocophillips/2025-annual-report.pdf) |
| COP-T4 | ConocoPhillips 2025 Form 10-K | 2026-02-17 | SEC filing HTML | Core annual filing covering business mix, production base, capital allocation, risks, and year-end financials | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/major-integrated-oil-gas/conocophillips/2025-10k.html) |
| COP-T5 | Q4 and full-year 2025 results page | 2026-02-05 | Official results page | Gives full-year `2025` earnings, CFO, capital returns, production, and `2026` guidance | `[Disclosed]` | [2025-results-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/major-integrated-oil-gas/conocophillips/2025-results-page.html) |
| COP-T6 | Q4 2025 8-K | 2026-02-05 | SEC filing HTML | Wrapper filing for the fourth-quarter and full-year `2025` results release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/major-integrated-oil-gas/conocophillips/2025-q4-8k.html) |
| COP-T7 | Q1 2026 results page | 2026-04-30 | Official results page | Gives first-quarter EPS, CFO, production, shareholder distributions, and second-quarter production guidance caveats tied to Qatar and the Middle East | `[Disclosed]` | [2026-q1-results-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/major-integrated-oil-gas/conocophillips/2026-q1-results-page.html) |
| COP-T8 | Q1 2026 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/major-integrated-oil-gas/conocophillips/2026-q1-8k.html) |
| COP-T9 | Q1 2026 Form 10-Q | 2026-04-30 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31`, including financial detail behind the results release | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/major-integrated-oil-gas/conocophillips/2026-q1-10q.html) |
| COP-T10 | Q2 2026 results page | 2026-08-06 | Official results page | Gives second-quarter EPS, operating cash flow, doubled buybacks, production, and LNG or asset-disposition commentary | `[Disclosed]` | [2026-q2-results-page.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/major-integrated-oil-gas/conocophillips/2026-q2-results-page.html) |
| COP-T11 | Q2 2026 8-K | 2026-08-06 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/major-integrated-oil-gas/conocophillips/2026-q2-8k.html) |
| COP-T12 | Q2 2026 Form 10-Q | 2026-08-06 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30`, including half-year cash flow and balance-sheet detail | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/major-integrated-oil-gas/conocophillips/2026-q2-10q.html) |
| COP-T13 | SEC submissions JSON | 2026-08-10 collected | SEC company feed | Preserves the filing index and confirms the ordering of the `10-K`, `10-Q`, and `8-K` chain collected for the packet | `[Filed]` | [submissions-cik0001163165.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/major-integrated-oil-gas/conocophillips/submissions-cik0001163165.json) |

## Reconciliation notes

- As of `2026-08-10`, the correct trailing-quarter set is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports.com is useful here for taxonomy and archive confirmation, but it still lagged at the `2024` package. The actual authoritative `2025` annual-report chain comes from company IR and SEC.
- Although AnnualReports labels ConocoPhillips as `Major Integrated Oil & Gas`, the packet remains useful for the lane mission because the operating and messaging profile is much more upstream- and capital-discipline-led than a classic downstream-heavy integrated major.

## Missing evidence

- No locally saved official earnings-call transcript for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
