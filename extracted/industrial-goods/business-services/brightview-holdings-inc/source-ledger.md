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
| BV-T1 | AnnualReports.com BrightView company page metadata | 2026-08-09 | Aggregator page verification | Confirms `Industrial Goods` / `Business Services` classification plus the current `2025 Annual Report and Form 10K` label | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/industrial-goods/business-services/brightview-holdings-inc/annualreports-verification.md) |
| BV-T2 | Official BrightView IR verification | 2026-08-09 | IR verification note | Confirms the live IR stack still exposed the `2026-08-04` Q3 FY2026 results release and related current-quarter cadence even though direct HTML capture was blocked in this environment | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/business-services/brightview-holdings-inc/official-ir-verification.md) |
| BV-T3 | SEC submissions JSON for BrightView | 2026-08-09 | SEC index JSON | Confirms CIK, ticker, NYSE listing, September fiscal year-end, and the authoritative annual plus trailing-three-quarter filing chain | `[Filed]` | [submissions-cik0001734713.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/business-services/brightview-holdings-inc/submissions-cik0001734713.json) |
| BV-T4 | BrightView 2025 Form 10-K | 2025-11-19 | SEC filing HTML | Filed annual package for the year ended `2025-09-30`, covering operating model, segment economics, labor disclosures, and the direct `H-2B` seasonal-worker evidence | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/business-services/brightview-holdings-inc/2025-10k.html) |
| BV-T5 | BrightView 2025 annual report / ARS | 2026-01-15 | SEC annual-report PDF | Companion annual report package filed with the SEC for the year ended `2025-09-30` | `[Filed]` | [2025-annual-report-sec-ars.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/industrial-goods/business-services/brightview-holdings-inc/2025-annual-report-sec-ars.pdf) |
| BV-T6 | Q1 FY2026 Form 8-K | 2026-02-03 | SEC filing HTML | Wrapper filing for first-quarter fiscal `2026` results and proof that an official company press release was furnished as Exhibit `99.1` | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/business-services/brightview-holdings-inc/2026-q1-8k.html) |
| BV-T7 | Q1 FY2026 Form 10-Q | 2026-02-03 | SEC filing HTML | Filed quarterly report for the quarter ended `2025-12-31`; used for revenue, net-loss, and segment-mix extraction | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/business-services/brightview-holdings-inc/2026-q1-10q.html) |
| BV-T8 | Q2 FY2026 Form 8-K | 2026-05-05 | SEC filing HTML | Wrapper filing for second-quarter fiscal `2026` results and proof that an official company press release was furnished as Exhibit `99.1` | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/business-services/brightview-holdings-inc/2026-q2-8k.html) |
| BV-T9 | Q2 FY2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31`; used for revenue, net-income, snow-removal, and development-timing extraction | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/business-services/brightview-holdings-inc/2026-q2-10q.html) |
| BV-T10 | Q3 FY2026 Form 8-K | 2026-08-04 | SEC filing HTML | Wrapper filing for third-quarter fiscal `2026` results and proof that an official company press release was furnished as Exhibit `99.1` | `[Filed]` | [2026-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/business-services/brightview-holdings-inc/2026-q3-8k.html) |
| BV-T11 | Q3 FY2026 Form 10-Q | 2026-08-04 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30`; used for the latest quarter revenue, net income, and segment-margin changes | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/industrial-goods/business-services/brightview-holdings-inc/2026-q3-10q.html) |

## Reconciliation notes

- BrightView fits best under `industrial-goods/business-services`, consistent with the AnnualReports classification observed on `2026-08-09`.
- The official company IR stack was verified through live search results, but direct IR HTML capture was blocked by a Cloudflare challenge page in this environment.
- The `8-K` wrapper filings confirm that official quarter press releases existed for all three trailing quarters in scope, but direct `Exhibit 99.1` HTML fetches from SEC were blocked by the SEC automated-tool policy page in this environment.
- The packet therefore relies on the filed `10-Q` operating tables and text blocks for quarter-level metrics rather than on locally saved press-release exhibits.

## Missing evidence

- No official standalone earnings-call transcript artifact was collected for Q1 FY2026, Q2 FY2026, or Q3 FY2026.
- No local HTML copy of the BrightView IR pages was saved because the site returned a Cloudflare challenge page from this environment.
- No local HTML copy of the AnnualReports company page was saved because the site was unreachable from this shell environment during collection.
