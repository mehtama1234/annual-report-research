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
| KMI-T1 | AnnualReports.com Kinder Morgan company page | 2026-08-10 | Aggregator page | Confirms ticker, HQ, `Basic Materials` / `Oil & Gas Pipelines` taxonomy, company description, and that AnnualReports still lagged at the `2024` package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/oil-gas-pipelines/kinder-morgan-inc/company-page-annualreports.html) |
| KMI-T2 | Kinder Morgan 2025 Form 10-K | 2026-02-13 | SEC filing HTML | Core annual filing covering business mix, pipeline network, terminals, storage, capital allocation, and risks | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2025-10k.html) |
| KMI-T3 | Q4 2025 results 8-K | 2026-01-21 | SEC filing HTML | Wrapper filing for the fourth-quarter and full-year `2025` results release | `[Filed]` | [2025-q4-alt-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2025-q4-alt-8k.html) |
| KMI-T4 | Q4 2025 earnings release exhibit | 2026-01-21 | SEC Exhibit 99.1 HTML | Gives fourth-quarter and full-year `2025` earnings, adjusted EBITDA, dividend, LNG feedgas positioning, and `2026` budget | `[Filed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2025-q4-earnings-release.html) |
| KMI-T5 | Q1 2026 results 8-K | 2026-04-22 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2026-q1-8k.html) |
| KMI-T6 | Q1 2026 earnings release exhibit | 2026-04-22 | SEC Exhibit 99.1 HTML | Gives first-quarter net income, adjusted EBITDA, dividend, backlog update, budget trend, and winter-weather outperformance | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2026-q1-earnings-release.html) |
| KMI-T7 | Q1 2026 Form 10-Q | 2026-04-24 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31`, including financial detail behind the results release | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2026-q1-10q.html) |
| KMI-T8 | Q2 2026 results 8-K | 2026-07-22 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-results-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2026-q2-results-8k.html) |
| KMI-T9 | Q2 2026 earnings release exhibit | 2026-07-22 | SEC Exhibit 99.1 HTML | Gives second-quarter record results, updated budget trend, major projects placed in service, and backlog movement | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2026-q2-earnings-release.html) |
| KMI-T10 | Q2 2026 Form 10-Q | 2026-07-24 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30`, including half-year detail | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/2026-q2-10q.html) |
| KMI-T11 | SEC submissions JSON | 2026-08-10 collected | SEC company feed | Preserves the filing index and confirms the ordering of the `10-K`, `10-Q`, and `8-K` chain collected for the packet | `[Filed]` | [submissions-cik0001506307.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/oil-gas-pipelines/kinder-morgan-inc/submissions-cik0001506307.json) |

## Reconciliation notes

- As of `2026-08-10`, the correct trailing-quarter set is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports.com is useful here for taxonomy and archive confirmation, but it still lagged at the `2024` package.
- Kinder Morgan investor-relations pages were blocked by a Cloudflare challenge during collection, so the authoritative annual and quarter chain in this packet is intentionally anchored in SEC filings and Exhibit `99.1` earnings-release HTML.
- The locally saved IR pages under `raw/company-ir/basic-materials/oil-gas-pipelines/kinder-morgan-inc/` are challenge pages rather than usable content and should be treated as evidence of collection blockage, not as substantive sources.

## Missing evidence

- No locally saved official IR annual-report PDF or IR quarterly-results content because the IR host blocked automated retrieval.
- No locally saved official earnings-call transcript for `Q4 2025`, `Q1 2026`, or `Q2 2026`.

