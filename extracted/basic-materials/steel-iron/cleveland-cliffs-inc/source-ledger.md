# Source Ledger

Date baseline: 2026-08-10

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` SEC filing or exhibit
- `[Reported]` aggregator or archive source
- `[Estimated]` derived or analyst estimate
- `[Speculative]` weak or unverified
- `[verify]` found but not yet confirmed directly

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CLF-T1 | AnnualReports.com Cleveland-Cliffs company page | 2026-08-10 collected | Aggregator page | Confirms `Basic Materials` / `Steel & Iron` taxonomy and shows the `2025 Annual Report and Form 10-K` page | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/steel-iron/cleveland-cliffs-inc/company-page-annualreports.html) |
| CLF-T2 | Cleveland-Cliffs investors home | 2026-08-10 collected | Investor relations page | Preserves the top-level IR context for the company | `[Disclosed]` | [investors-home.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/cleveland-cliffs-inc/investors-home.html) |
| CLF-T3 | Cleveland-Cliffs financial results page | 2026-08-10 collected | Investor relations page | Preserves the company-hosted results navigation and links to quarter releases | `[Disclosed]` | [financial-results.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/cleveland-cliffs-inc/financial-results.html) |
| CLF-T4 | Cleveland-Cliffs financial information page | 2026-08-10 collected | Investor relations page | Preserves the annual filings and corporate financial-information navigation | `[Disclosed]` | [financial-information.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/cleveland-cliffs-inc/financial-information.html) |
| CLF-T5 | Cleveland-Cliffs 2025 filing PDF | 2026 collected | Annual filing PDF | Valid `136`-page PDF used for annual business-model and operating detail | `[Disclosed]` | [2025-10k.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/cleveland-cliffs-inc/2025-10k.pdf) |
| CLF-T6 | Cleveland-Cliffs 2025 Form 10-K | 2026-02-09 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/cleveland-cliffs-inc/2025-10k.html) |
| CLF-T7 | Q4 2025 company news page | 2026-08-10 collected | Investor relations news page | Preserves the company-hosted fourth-quarter and full-year `2025` release | `[Disclosed]` | [q4-2025-news.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/cleveland-cliffs-inc/q4-2025-news.html) |
| CLF-T8 | Q4 2025 8-K | 2026-02-09 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/cleveland-cliffs-inc/2025-q4-8k.html) |
| CLF-T9 | Q1 2026 company news page | 2026-08-10 collected | Investor relations news page | Preserves the company-hosted first-quarter `2026` release | `[Disclosed]` | [q1-2026-news.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/cleveland-cliffs-inc/q1-2026-news.html) |
| CLF-T10 | Q1 2026 8-K | 2026-04-20 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/cleveland-cliffs-inc/2026-q1-8k.html) |
| CLF-T11 | Q1 2026 Form 10-Q | 2026-04-21 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/cleveland-cliffs-inc/2026-q1-10q.html) |
| CLF-T12 | Q2 2026 company news page | 2026-08-10 collected | Investor relations news page | Preserves the company-hosted second-quarter `2026` release | `[Disclosed]` | [q2-2026-news.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/cleveland-cliffs-inc/q2-2026-news.html) |
| CLF-T13 | Q2 2026 8-K | 2026-07-23 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/cleveland-cliffs-inc/2026-q2-8k.html) |
| CLF-T14 | Q2 2026 Form 10-Q | 2026-07-23 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/cleveland-cliffs-inc/2026-q2-10q.html) |
| CLF-T15 | SEC submissions JSON | 2026-08-10 collected | SEC company feed | Preserves the filing index confirming the `2025 10-K`, `Q4 2025`, `Q1 2026`, and `Q2 2026` chain | `[Filed]` | [submissions-cik0000764065.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/cleveland-cliffs-inc/submissions-cik0000764065.json) |

## Reconciliation notes

- As of `Monday, August 10, 2026`, the correct trailing-quarter set is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports did have the `2025` package visible for Cleveland-Cliffs, but the packet still treats company IR and SEC filings as the authoritative source chain.
- The strongest quarter-level evidence comes from the company-hosted news pages plus the SEC `8-K` and filed `10-Q` reports.
- The company-hosted quarter release PDFs were inconsistent locally: the saved `Q1 2026` and `Q2 2026` release PDFs rendered as unusable `0`-page PDFs, and the attempted `Q4 2025` release PDF resolved to an access-denied XML response. The packet therefore intentionally anchors quarter evidence in the IR news pages and SEC filings instead.

## Missing evidence

- No locally saved, usable quarter earnings-release PDFs for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No locally saved Exhibit `99.1` HTML files separate from the `8-K` wrappers for the quarter releases, because the company-hosted news pages and filed `10-Q` reports were sufficient to establish the quarter facts used in the packet.
