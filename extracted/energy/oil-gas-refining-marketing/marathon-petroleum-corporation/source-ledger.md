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
| MPC-T1 | AnnualReports.com Marathon Petroleum company page | 2026-08-10 | Aggregator page | Confirms ticker, HQ, `Energy` / `Oil & Gas Refining & Marketing` taxonomy, and that AnnualReports still lagged at the `2024` package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/company-page-annualreports.html) |
| MPC-T2 | Marathon Petroleum investors home page | 2026-08-10 collected | Investor relations page | Preserves the official IR landing page for the company and confirms the host used for annual-report and filing navigation | `[Disclosed]` | [investors-home.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/investors-home.html) |
| MPC-T3 | Marathon Petroleum annual report and proxy statement page | 2026-08-10 collected | Investor relations page | Confirms the official `2025` annual report is live on company IR and exposes the direct annual-report PDF link even though direct PDF retrieval returned an access-protection page during collection | `[Disclosed]` | [annual-report-proxy-statement.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/annual-report-proxy-statement.html) |
| MPC-T4 | Marathon Petroleum 2025 Form 10-K | 2026-02-26 | SEC filing HTML | Core annual filing covering business mix, refining system, MPLX relationship, financials, and year-end risks | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2025-10k.html) |
| MPC-T5 | Q4 and full-year 2025 8-K | 2026-02-03 | SEC filing HTML | Wrapper filing for the fourth-quarter and full-year `2025` results release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2025-q4-8k.html) |
| MPC-T6 | Q4 and full-year 2025 earnings release exhibit | 2026-02-03 | SEC Exhibit 99.1 HTML | Gives full-year `2025` net income, operating cash flow, adjusted EBITDA, refining utilization, margin capture, and MPLX support commentary | `[Filed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2025-q4-earnings-release.html) |
| MPC-T7 | Q1 2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31`, including first-quarter financial detail | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2026-q1-10q.html) |
| MPC-T8 | Q1 2026 8-K | 2026-05-05 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2026-q1-8k.html) |
| MPC-T9 | Q1 2026 earnings release exhibit | 2026-05-05 | SEC Exhibit 99.1 HTML | Gives first-quarter EPS, operating cash flow, turnaround progress, project timing, capital return, and MPLX distribution-growth framing | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2026-q1-earnings-release.html) |
| MPC-T10 | Q2 2026 Form 10-Q | 2026-08-04 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30`, including balance-sheet and half-year financial detail | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2026-q2-10q.html) |
| MPC-T11 | Q2 2026 8-K | 2026-08-04 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2026-q2-8k.html) |
| MPC-T12 | Q2 2026 earnings release exhibit | 2026-08-04 | SEC Exhibit 99.1 HTML | Gives second-quarter earnings surge, adjusted EBITDA, refining margin per barrel, utilization, throughput, project completion, and capital-return updates | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/2026-q2-earnings-release.html) |
| MPC-T13 | SEC submissions JSON | 2026-08-10 collected | SEC company feed | Preserves the filing index and confirms the ordering of the `10-K`, `10-Q`, and `8-K` chain collected for the packet | `[Filed]` | [submissions-cik0001510295.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/marathon-petroleum-corporation/submissions-cik0001510295.json) |

## Reconciliation notes

- As of `2026-08-10`, the correct trailing-quarter set is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports.com is useful here for taxonomy and archive confirmation, but it still lagged at the `2024` package. The authoritative `2025` annual-report chain comes from company IR and SEC.
- The official IR annual-report page clearly presents the `2025` annual report and direct PDF link, but direct PDF retrieval during collection returned an access-protection HTML response rather than the report PDF. The packet therefore relies on the IR page plus the SEC `10-K` as the authoritative annual-report evidence preserved locally.
- The IR host also returned `429 Too Many Requests` on some filing and quarterly-results pages during collection, so the quarter-level evidence chain is intentionally anchored in SEC filings and Exhibit `99.1` earnings-release HTML.

## Missing evidence

- No locally saved official annual-report PDF artifact because the IR host blocked direct retrieval during collection.
- No locally saved official earnings-call transcript for `Q4 2025`, `Q1 2026`, or `Q2 2026`.

