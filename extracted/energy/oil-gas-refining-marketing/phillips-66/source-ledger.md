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
| PSX-T1 | AnnualReports.com Phillips 66 company page | 2026-08-10 | Aggregator page | Confirms company page, taxonomy, and that AnnualReports still lagged at the `2024` annual package | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/energy/oil-gas-refining-marketing/phillips-66/company-page-annualreports.html) |
| PSX-T2 | Phillips 66 financial information page | 2026-08-10 collected | Investor relations page | Preserves the official IR route used for annual-publication and quarterly-results navigation, even though the saved artifact is a Cloudflare challenge wrapper | `[Disclosed]` | [financial-information.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/energy/oil-gas-refining-marketing/phillips-66/financial-information.html) |
| PSX-T3 | Phillips 66 2025 Form 10-K | 2026-02-20 | SEC filing HTML | Core annual filing covering segment mix, asset base, risks, and year-end financials | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2025-10k.html) |
| PSX-T4 | Q4 and full-year 2025 8-K | 2026-02-04 | SEC filing HTML | Wrapper filing for the fourth-quarter and full-year `2025` results release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2025-q4-8k.html) |
| PSX-T5 | Q4 and full-year 2025 earnings release exhibit | 2026-02-04 | SEC Exhibit 99.1 HTML | Gives full-year earnings, operating cash flow, record NGL volumes, refining utilization, debt reduction, and portfolio-reshaping commentary | `[Filed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2025-q4-earnings-release.html) |
| PSX-T6 | Q4 2025 supplemental data | 2026-02-04 | SEC earnings supplement HTML | Adds detailed operating metrics and segment-level context behind the fourth-quarter release | `[Filed]` | [2025-q4-supplemental.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2025-q4-supplemental.html) |
| PSX-T7 | Q1 2026 Form 10-Q | 2026-04-29 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31`, including balance-sheet and segment detail | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2026-q1-10q.html) |
| PSX-T8 | Q1 2026 8-K | 2026-04-29 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2026-q1-8k.html) |
| PSX-T9 | Q1 2026 earnings release exhibit | 2026-04-29 | SEC Exhibit 99.1 HTML | Gives first-quarter earnings, capacity additions at Sweeny and Freeport, refining metrics, dividend increase, and strategic updates including Western Gateway, Iron Mesa, and Lindsey | `[Filed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2026-q1-earnings-release.html) |
| PSX-T10 | Q1 2026 supplemental data | 2026-04-29 | SEC earnings supplement HTML | Adds segment earnings, operating metrics, and cash / debt ratios for the first quarter | `[Filed]` | [2026-q1-supplemental.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2026-q1-supplemental.html) |
| PSX-T11 | Q2 2026 Form 10-Q | 2026-08-05 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30`, including second-quarter and half-year detail | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2026-q2-10q.html) |
| PSX-T12 | Q2 2026 8-K | 2026-08-05 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2026-q2-8k.html) |
| PSX-T13 | Q2 2026 earnings release exhibit | 2026-08-05 | SEC Exhibit 99.1 HTML | Gives second-quarter earnings surge, large debt reduction, record NGL fractionation and LPG export volumes, and project progress across Midstream, Refining, and Chemicals | `[Filed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2026-q2-earnings-release.html) |
| PSX-T14 | Q2 2026 supplemental data | 2026-08-05 | SEC earnings supplement HTML | Adds segment earnings, refining margins, NGL metrics, cash generation, and return-of-capital detail for the second quarter | `[Filed]` | [2026-q2-supplemental.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/2026-q2-supplemental.html) |
| PSX-T15 | SEC submissions JSON | 2026-08-10 collected | SEC company feed | Preserves the filing index and confirms the ordering of the `10-K`, `10-Q`, and `8-K` chain used in the packet | `[Filed]` | [submissions-cik0001534701.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/energy/oil-gas-refining-marketing/phillips-66/submissions-cik0001534701.json) |

## Reconciliation notes

- As of `Monday, August 10, 2026`, the correct trailing-quarter set is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports.com is useful here for taxonomy and archive confirmation, but it still lagged at the `2024` annual package. The authoritative `2025` annual chain comes from the SEC `10-K`.
- The official Phillips 66 IR route was verified and saved locally, but the captured file is only a Cloudflare challenge wrapper in this environment. Quarter-level and annual-report evidence are therefore intentionally anchored in the SEC filing and exhibit chain.
- The SEC earnings-release exhibits and supplemental files are especially important for this packet because they preserve the detailed segment, utilization, NGL, LPG-export, and capital-allocation metrics that explain the integrated downstream model.

## Missing evidence

- No locally saved official Phillips 66-hosted `2025` annual-report PDF distinct from the SEC `10-K`.
- No locally saved official earnings-call transcript for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
