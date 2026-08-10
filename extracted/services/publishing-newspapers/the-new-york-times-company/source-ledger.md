# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| NYT-S1 | AnnualReports.com company page | 2026-08-10 collected | Aggregator page HTML | Confirms identity and exact assigned taxonomy under `Services / Publishing - Newspapers` | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/publishing-newspapers/the-new-york-times-company/company-page.html) |
| NYT-S2 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Records exact category fit and the fact that AnnualReports.com still showed `2024` as the latest hosted annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/publishing-newspapers/the-new-york-times-company/annualreports-verification.md) |
| NYT-S3 | NYT official IR verification note | 2026-08-10 | Official IR verification note | Records that local IR collection was blocked by HTTP `429` and that SEC is the authoritative saved chain in this snapshot | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/publishing-newspapers/the-new-york-times-company/official-ir-verification.md) |
| NYT-S4 | NYT SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms filer identity and the exact annual-plus-quarter filing sequence in scope | `[Filed]` | [submissions-cik0000071691.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/submissions-cik0000071691.json) |
| NYT-S5 | NYT `2025` Form `10-K` | 2026-02-27 filed / 2026-08-10 collected | SEC filing HTML | Core annual filing for the fiscal year ended `2025-12-31` | `[Filed]` | [nyt-20251231.htm](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/nyt-20251231.htm) |
| NYT-S6 | NYT Q4 `2025` earnings `8-K` | 2026-02-04 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [nyt-20260204.htm](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/nyt-20260204.htm) |
| NYT-S7 | NYT Q4 `2025` earnings release exhibit | 2026-02-04 released / 2026-08-10 collected | SEC exhibit HTML | Full Q4 and full-year `2025` operating commentary, subscriber growth, advertising trends, and free-cash-flow data | `[Filed]` | [2025-q4-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/2025-q4-ex99-1.html) |
| NYT-S8 | NYT Q1 `2026` `10-Q` | 2026-05-06 filed / 2026-08-10 collected | SEC filing HTML | First-quarter `2026` filing for current-period operating and balance-sheet detail | `[Filed]` | [nyt-20260331.htm](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/nyt-20260331.htm) |
| NYT-S9 | NYT Q1 `2026` earnings `8-K` | 2026-05-06 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [nyt-20260506.htm](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/nyt-20260506.htm) |
| NYT-S10 | NYT Q1 `2026` earnings release exhibit | 2026-05-06 released / 2026-08-10 collected | SEC exhibit HTML | Full first-quarter `2026` narrative including subscription, digital advertising, margins, and free cash flow | `[Filed]` | [2026-q1-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/2026-q1-ex99-1.html) |
| NYT-S11 | NYT Q2 `2026` `10-Q` | 2026-08-05 filed / 2026-08-10 collected | SEC filing HTML | Most recent quarter in scope | `[Filed]` | [nyt-20260630.htm](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/nyt-20260630.htm) |
| NYT-S12 | NYT Q2 `2026` earnings `8-K` | 2026-08-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for second-quarter `2026` results | `[Filed]` | [nyt-20260805.htm](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/nyt-20260805.htm) |
| NYT-S13 | NYT Q2 `2026` earnings release exhibit | 2026-08-05 released / 2026-08-10 collected | SEC exhibit HTML | Full second-quarter `2026` narrative including subscription scale, digital ad momentum, and video emphasis | `[Filed]` | [2026-q2-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/publishing-newspapers/the-new-york-times-company/2026-q2-ex99-1.html) |

## Reconciliation notes

- AnnualReports.com is the taxonomy and archive-confirmation source here and gives a clean exact-category fit under `Publishing - Newspapers`.
- AnnualReports.com lagged the required annual-report window at collection time because the latest hosted annual package shown locally was `2024`.
- The official NYT investor-relations site returned HTTP `429` in this environment, so no reliable IR HTML capture is stored locally.
- SEC therefore serves as the authoritative saved chain for the `2025` annual filing and the latest three reported quarters in scope:
  - Q2 `2026`
  - Q1 `2026`
  - Q4 `2025`

## Missing evidence

- No standalone earnings-call transcript artifact was saved locally for the in-scope quarter chain.
- No reliable official IR page capture is stored locally because of rate limiting.
