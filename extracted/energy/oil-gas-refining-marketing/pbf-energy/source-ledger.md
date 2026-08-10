# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| PBF-T1 | AnnualReports.com company page | 2026-08-10 capture | Aggregator page | Confirms the AnnualReports taxonomy and archive presence while showing the site still lagged at the `2024` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/energy/oil-gas-refining-marketing/pbf-energy/company-page-annualreports.html) |
| PBF-T2 | Annual reports page capture | 2026-08-10 capture | Official IR page capture | Preserves the official annual-reports route even though the local save is a Cloudflare challenge wrapper | `[Disclosed]` | [annual-reports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/energy/oil-gas-refining-marketing/pbf-energy/annual-reports.html) |
| PBF-T3 | Quarterly results page capture | 2026-08-10 capture | Official IR page capture | Preserves the official quarterly-results route even though the local save is a Cloudflare challenge wrapper | `[Disclosed]` | [quarterly-results.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/energy/oil-gas-refining-marketing/pbf-energy/quarterly-results.html) |
| PBF-T4 | Official `2025` annual report PDF | 2026-08-10 capture | Official IR PDF | Direct company-hosted annual report PDF linked from investor relations | `[Disclosed]` | [2025-annual-report-cloudfront.pdf](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/energy/oil-gas-refining-marketing/pbf-energy/2025-annual-report-cloudfront.pdf) |
| PBF-T5 | Form `10-K` | 2026-02-12 | SEC filing HTML | Filed annual report for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2025-10k.html) |
| PBF-T6 | `Q4 2025` Form `8-K` | 2026-02-12 | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2025-q4-8k.html) |
| PBF-T7 | `Q4 2025` earnings release exhibit | 2026-02-12 | SEC Exhibit `99.1` HTML | Preserves the fourth-quarter and full-year `2025` results release, Martinez update, and annual outlook | `[Filed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2025-q4-earnings-release.html) |
| PBF-T8 | `Q1 2026` Form `10-Q` | 2026-04-30 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2026-q1-10q.html) |
| PBF-T9 | `Q1 2026` Form `8-K` | 2026-04-30 | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2026-q1-8k.html) |
| PBF-T10 | `Q1 2026` earnings release exhibit | 2026-04-30 | SEC Exhibit `99.1` HTML | Preserves first-quarter `2026` results, Martinez restart progress, and insurance update | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2026-q1-earnings-release.html) |
| PBF-T11 | `Q2 2026` Form `10-Q` | 2026-07-30 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2026-q2-10q.html) |
| PBF-T12 | `Q2 2026` Form `8-K` | 2026-07-30 | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2026-q2-8k.html) |
| PBF-T13 | `Q2 2026` earnings release exhibit | 2026-07-30 | SEC Exhibit `99.1` HTML | Preserves second-quarter `2026` results, debt reduction, Martinez restart completion, and SBR update | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/2026-q2-earnings-release.html) |
| PBF-T14 | SEC submissions JSON | 2026-08-10 capture | SEC company feed | Preserves the filing chronology and confirms the `10-K`, `10-Q`, and `8-K` chain used in the packet | `[Filed]` | [submissions-cik0001534504.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/pbf-energy/submissions-cik0001534504.json) |

## Reconciliation notes

- As of `Monday, August 10, 2026`, the correct trailing-quarter set is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports.com was useful for taxonomy and archive confirmation, but it still lagged at the `2024 Annual Report and Form 10K` package. The authoritative `2025` annual chain therefore comes from live verification of the official annual-reports page, the direct annual-report PDF, and the filed SEC `10-K`.
- Direct local captures of PBF investor-relations pages returned Cloudflare challenge wrappers in this environment. Those captures are still preserved, but the packet relies on the direct annual-report PDF plus the SEC `10-K`, `10-Q`, `8-K`, and earnings-release exhibits for the substantive evidence base.
- The quarter interpretation requires explicit Martinez context:
  - `Q4 2025` still reflected heavy fire-related recovery and insurance-reimbursement effects.
  - `Q1 2026` still showed restart-and-turnaround pressure, despite positive GAAP income.
  - `Q2 2026` showed the first clean quarter with Martinez back at full operations and a large gross-debt reduction.
