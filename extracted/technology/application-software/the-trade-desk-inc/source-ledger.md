# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| TTD-T1 | AnnualReports.com company page | 2026-08-10 collected | Aggregator page HTML | Confirms `Technology / Application Software` placement and shows AnnualReports lagging at `2024` | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/technology/application-software/the-trade-desk-inc/company-page.html) |
| TTD-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Records taxonomy fit and the need to bridge the `2025` annual-report gap through official IR plus SEC | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/technology/application-software/the-trade-desk-inc/annualreports-verification.md) |
| TTD-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Records the valid company IR URLs and the Cloudflare constraint on local HTML retrieval | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/the-trade-desk-inc/official-ir-verification.md) |
| TTD-T4 | SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies issuer identity, ticker `TTD`, exchange `Nasdaq`, SIC description, fiscal year-end `1231`, and the exact filing chronology in scope | `[Filed]` | [submissions-cik0001671933.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/application-software/the-trade-desk-inc/submissions-cik0001671933.json) |
| TTD-T5 | Filed FY `2025` Form `10-K` | 2026-02-27 filed / 2026-08-10 collected | SEC filing HTML | Annual-report anchor for the required `2025` window and the core source for FY `2025` cash-generation and balance-sheet metrics | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/application-software/the-trade-desk-inc/2025-10k.html) |
| TTD-T6 | FY `2025` / Q4 `2025` earnings `8-K` exhibit | 2026-02-25 released / 2026-08-10 collected | SEC earnings exhibit HTML | Gives the FY `2025` and Q4 `2025` operating narrative, revenue, profitability, customer-retention, and product-platform signals | `[Filed]` | [2025-q4-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/application-software/the-trade-desk-inc/2025-q4-ex99-1.html) |
| TTD-T7 | Q1 `2026` Form `10-Q` | 2026-05-07 filed / 2026-08-10 collected | SEC filing HTML | Verifies the first-quarter reporting period and supports the latest-three-quarters chain | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/application-software/the-trade-desk-inc/2026-q1-10q.html) |
| TTD-T8 | Q1 `2026` earnings `8-K` exhibit | 2026-05-07 released / 2026-08-10 collected | SEC earnings exhibit HTML | Gives Q1 `2026` results and management framing around open-internet buying, execution upgrades, and macro headwinds | `[Filed]` | [2026-q1-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/application-software/the-trade-desk-inc/2026-q1-ex99-1.html) |
| TTD-T9 | Q2 `2026` Form `10-Q` | 2026-08-06 filed / 2026-08-10 collected | SEC filing HTML | Verifies the most recent quarter in scope and supports the in-window chronology | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/application-software/the-trade-desk-inc/2026-q2-10q.html) |
| TTD-T10 | Q2 `2026` earnings `8-K` exhibit | 2026-08-06 released / 2026-08-10 collected | SEC earnings exhibit HTML | Gives the latest-quarter slowdown, profitability shift, customer-retention update, and CTV/data-partnership signals | `[Filed]` | [2026-q2-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/application-software/the-trade-desk-inc/2026-q2-ex99-1.html) |

## Reconciliation notes

- AnnualReports confirms identity and taxonomy, but not the required `2025` annual-report window.
- Official IR URLs are known, but local retrieval of company-hosted IR HTML was blocked by Cloudflare challenge pages.
- SEC artifacts therefore carry the authoritative annual and quarterly evidence chain.
- Based on fiscal year-end `1231` and the filing sequence in the submissions JSON, the latest three reported quarters as of Monday, August 10, 2026 are:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`

## Missing evidence

- No clean locally saved official IR content page was retrievable in this environment because the investor-relations site returned Cloudflare challenge pages.
- That does not block packet completion because the filed `10-K`, `10-Q`, `8-K`, and earnings exhibits preserve the required evidence window.
