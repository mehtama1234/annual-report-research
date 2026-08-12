# Source Ledger

Date baseline: 2026-08-12

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
| WAFD-T1 | AnnualReports.com WaFd / Washington Federal company page | 2026-08-12 | Aggregator page | Confirms `Savings & Loans` taxonomy and shows archive lag versus official sources | `[Reported]` | https://www.annualreports.com/Company/washington-federal-inc |
| WAFD-T2 | WaFd investor overview page | 2026-08-12 | Official IR page | Confirms annual-report link and official investor entry point | `[Disclosed]` | https://www.wafdbank.com/about-us/investor-relations |
| WAFD-T3 | WaFd financial news page | 2026-08-12 | Official IR page | Confirms quarter-by-quarter earnings PDF chain and investor presentations | `[Disclosed]` | https://www.wafdbank.com/about-us/investor-relations/financial-news |
| WAFD-T4 | WaFd `2025` annual report PDF | 2026-08-12 verified | Official annual report PDF | Company-hosted annual report for the fiscal year ended `2025-09-30` | `[Disclosed]` | https://www.wafdbank.com/documents/wfsl-financial-data/wafd-bank-2025-annual-report.pdf |
| WAFD-T5 | SEC annual report filing index (`ARS`) | 2025-12-19 | SEC filing index | Confirms SEC-hosted annual-report PDF and period of report | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652825000122/0000936528-25-000122-index.htm |
| WAFD-T6 | SEC annual report PDF | 2025-12-19 | SEC annual report PDF | SEC-hosted annual report package for fiscal `2025` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652825000122/wafdarfinal.pdf |
| WAFD-T7 | WaFd `2025` Form 10-K | 2025-11-18 | SEC filing HTML | Core annual filing for the fiscal year ended `2025-09-30` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652825000117/wfsl-20250930.htm |
| WAFD-T8 | WaFd `Q1 FY2026` earnings PDF | 2026-01-15 | Official earnings PDF | Gives exact `Q1 FY2026` EPS, margin, credit, and repurchase metrics | `[Disclosed]` | https://www.wafdbank.com/documents/financial-news/2026/wafd-bank-press-release-20260115.pdf |
| WAFD-T9 | WaFd `Q1 FY2026` 8-K | 2026-01-15 | SEC filing HTML | Wrapper filing for the quarter ended `2025-12-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652826000011/wfsl-20260115.htm |
| WAFD-T10 | WaFd `Q1 FY2026` 10-Q | 2026-02-03 | SEC filing HTML | Filed quarterly report for the quarter ended `2025-12-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652826000020/wfsl-20251231.htm |
| WAFD-T11 | WaFd `Q2 FY2026` earnings PDF | 2026-04-16 | Official earnings PDF | Gives exact `Q2 FY2026` EPS, NIM, credit-improvement, and repurchase metrics | `[Disclosed]` | https://www.wafdbank.com/documents/financial-news/2026/wafd-bank-press-release-20260416.pdf |
| WAFD-T12 | WaFd `Q2 FY2026` 8-K | 2026-04-16 | SEC filing HTML | Wrapper filing for the quarter ended `2026-03-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652826000038/wfsl-20260416.htm |
| WAFD-T13 | WaFd `Q2 FY2026` 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652826000043/wfsl-20260331.htm |
| WAFD-T14 | WaFd `Q3 FY2026` earnings PDF | 2026-07-16 | Official earnings PDF | Gives exact `Q3 FY2026` EPS, efficiency, reserve, and balance-sheet metrics | `[Disclosed]` | https://www.wafdbank.com/documents/financial-news/2026/wafd-bank-press-release-20260716.pdf |
| WAFD-T15 | WaFd `Q3 FY2026` 8-K | 2026-07-16 | SEC filing HTML | Wrapper filing for the quarter ended `2026-06-30` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652826000055/wfsl-20260716.htm |
| WAFD-T16 | WaFd `Q3 FY2026` 10-Q filing index | 2026-08-04 | SEC filing index | Confirms filed `10-Q` for the quarter ended `2026-06-30` and the document name `wfsl-20260630.htm` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/936528/000093652826000061/0000936528-26-000061-index.htm |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation.
- The correct trailing-quarter set as of `2026-08-10` is `Q3 FY2026`, `Q2 FY2026`, and `Q1 FY2026`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The evidence also captures a useful taxonomy mismatch:
  - AnnualReports still places WaFd in `Savings & Loans`
  - the SEC filing chain presents the company under `National Commercial Banks`
  - management language makes clear the business is intentionally shifting away from mortgage-lending dependence toward business banking
- The packet is still marked `qualified` because this workspace does not yet preserve a rebuilt local raw-artifact chain comparable to the cleanest proof-standard packets.

## Missing evidence

- No clean local copies of call transcripts or prepared remarks were rebuilt into this workspace.
- The `Q3 FY2026` `10-Q` is confirmed through the SEC filing index in this workspace rather than through a separately re-opened direct HTML page.
- The official annual and quarterly PDF chain plus the SEC filing chain are still strong enough for thematic interpretation and thrift-analog comparison work.
