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
| STLD-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports company page | Confirms AnnualReports taxonomy for `Basic Materials` / `Steel & Iron` and shows that the site already displayed the `2025 Annual Report and Form 10K` package as of `Monday, August 10, 2026`, although the report was locked in the saved view | `[Reported]` | [company-page-annualreports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/annualreports/basic-materials/steel-iron/steel-dynamics-inc/company-page-annualreports.html) |
| STLD-T2 | Steel Dynamics overview IR page | 2026-08-10 collected | Investor-relations page | Confirms the official investor-relations host, headquarters detail, and the embedded B2i annual-report widget route used by the company site | `[Disclosed]` | [overview.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/steel-dynamics-inc/overview.html) |
| STLD-T3 | Steel Dynamics annual-reports IR page | 2026-08-10 collected | Investor-relations page | Confirms the official annual-reports route, although the saved page is mostly a B2i shell and did not expose a clean downloadable annual-report file in this pass | `[Disclosed]` | [annual-reports.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/steel-dynamics-inc/annual-reports.html) |
| STLD-T4 | Steel Dynamics SEC-filings IR page | 2026-08-10 collected | Investor-relations page | Confirms the official company-hosted filing route for annual and quarterly documents | `[Disclosed]` | [sec-filings.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/steel-dynamics-inc/sec-filings.html) |
| STLD-T5 | Steel Dynamics 2025 Form 10-K | 2026-02-27 | SEC filing HTML | Core annual SEC filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/steel-dynamics-inc/2025-10k.html) |
| STLD-T6 | Q4 2025 results page | 2026-01-26 | Earnings-results page | Official `Q4 2025` and annual `2025` results release with annual net sales, earnings, shipments, liquidity, and segment commentary | `[Disclosed]` | [q4-2025-results.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/steel-dynamics-inc/q4-2025-results.html) |
| STLD-T7 | Q4 2025 Form 8-K | 2026-01-27 | SEC filing HTML | SEC wrapper filing confirming the `Q4 2025` earnings release under Item `2.02` | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/steel-dynamics-inc/2025-q4-8k.html) |
| STLD-T8 | Q1 2026 results page | 2026-04-21 | Earnings-results page | Official `Q1 2026` results release with spread, shipment, backlog, and end-market commentary | `[Disclosed]` | [q1-2026-results.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/steel-dynamics-inc/q1-2026-results.html) |
| STLD-T9 | Q1 2026 Form 8-K | 2026-04-21 | SEC filing HTML | SEC wrapper filing confirming the `Q1 2026` earnings release under Item `2.02` | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/steel-dynamics-inc/2026-q1-8k.html) |
| STLD-T10 | Q1 2026 Form 10-Q | 2026-04-27 | SEC filing HTML | Core quarterly SEC filing for `Q1 2026`, including updated statements and balance-sheet detail | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/steel-dynamics-inc/2026-q1-10q.html) |
| STLD-T11 | Q2 2026 results page | 2026-07-21 | Earnings-results page | Official `Q2 2026` results release with first-half metrics, spread expansion, fabrication backlog, and aluminum-project update | `[Disclosed]` | [q2-2026-results.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/steel-dynamics-inc/q2-2026-results.html) |
| STLD-T12 | Q2 2026 Form 8-K | 2026-07-21 | SEC filing HTML | SEC wrapper filing confirming the `Q2 2026` earnings release under Item `2.02` | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/steel-dynamics-inc/2026-q2-8k.html) |
| STLD-T13 | Q2 2026 Form 10-Q | 2026-07-28 | SEC filing HTML | Core quarterly SEC filing for `Q2 2026`, including first-half statements and updated asset and debt detail | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/steel-dynamics-inc/2026-q2-10q.html) |
| STLD-T14 | SEC submissions JSON | 2026-08-10 collected | SEC company feed | Preserves the filing index confirming the `2025 10-K` and the `Q4 2025`, `Q1 2026`, and `Q2 2026` filing chain | `[Filed]` | [submissions-cik0001022671.json](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/sec/basic-materials/steel-iron/steel-dynamics-inc/submissions-cik0001022671.json) |
| STLD-T15 | B2i widget fetch attempts | 2026-08-10 collected | Investor-relations artifact | Documents that direct B2i `Showapi` fetches for the annual-report widget were attempted but blocked by a Cloudflare challenge, explaining why the packet relies on SEC annual filings rather than a saved official annual-report PDF | `[verify]` | [annual-reports-showapi.js](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/steel-dynamics-inc/annual-reports-showapi.js) and [annual-reports-showapi-with-key.js](/home/manishmehta/ui-projects/annual-report-research-energy-buildout/raw/company-ir/basic-materials/steel-iron/steel-dynamics-inc/annual-reports-showapi-with-key.js) |

## Reconciliation notes

- The correct trailing-quarter set as of `Monday, August 10, 2026` is `Q2 2026`, `Q1 2026`, and `Q4 2025` because Steel Dynamics has a `December` fiscal year-end.
- AnnualReports was useful here for both taxonomy confirmation and archive confirmation because the page already displayed the `2025` annual package. However, the saved view kept that report locked, so it was not sufficient by itself as the annual evidence chain.
- The official IR annual-reports route was preserved locally, but the visible HTML is mainly a B2i shell. Direct widget fetches were attempted and saved, but they hit a Cloudflare challenge rather than returning a usable annual-report document.
- The substantive annual evidence therefore comes from the SEC `10-K`, with the annual and quarterly results pages supplying management framing, operating metrics, shipments, spreads, backlog commentary, and project updates.
- The `Q4 2025`, `Q1 2026`, and `Q2 2026` `8-K` wrappers were directly verified as Item `2.02` results filings.

## Missing evidence

- No clean standalone annual-report PDF was captured from the official IR route because the B2i annual-report widget did not yield a usable document in this pass.
- No earnings-call transcript was collected locally for Steel Dynamics in this pass.
