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
| PRU-T1 | AnnualReports.com Prudential company page | 2026-08-12 | Aggregator page | Confirms Financial / Life Insurance taxonomy and shows that the hosted annual package still lagged at `2024` | `[Reported]` | https://www.annualreports.com/Company/prudential-financial-inc |
| PRU-T2 | Prudential annual reports page | 2026-08-12 | Official IR page | Confirms the official annual-report access page | `[Disclosed]` | https://investor.prudential.com/financials/proxy-statement-annual-report-and-voting-results/default.aspx |
| PRU-T3 | Prudential quarterly results page | 2026-08-12 | Official IR page | Confirms the official quarterly-results hub for the trailing quarter chain | `[Disclosed]` | https://investor.prudential.com/financials/quarterly-results/default.aspx |
| PRU-T4 | Prudential `2025` Form 10-K | 2026-02-12 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1137774/000113777426000048/pru-20251231.htm |
| PRU-T5 | Prudential `Q4 2025` official results page | 2026-08-12 | Official IR page | Confirms the official fourth-quarter and full-year `2025` results page | `[Disclosed]` | https://investor.prudential.com/news/news-details/2026/Prudential-Financial-Inc--Announces-Full-Year-and-Fourth-Quarter-2025-Results/default.aspx |
| PRU-T6 | Prudential `Q4 2025` earnings release exhibit | 2026-02-03 | SEC exhibit HTML | Exact fourth-quarter and full-year `2025` metrics and capital-return framing | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1137774/000113777426000012/exhibit991-4q25earningspre.htm |
| PRU-T7 | Prudential `Q4 2025` 8-K | 2026-02-03 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1137774/000113777426000012/pru-20260203.htm |
| PRU-T8 | Prudential `Q1 2026` official results page | 2026-08-12 | Official IR page | Confirms the official first-quarter `2026` results page | `[Disclosed]` | https://investor.prudential.com/news/news-details/2026/Prudential-Financial-Inc--Announces-First-Quarter-2026-Results/default.aspx |
| PRU-T9 | Prudential `Q1 2026` earnings release exhibit | 2026-05-05 | SEC exhibit HTML | Exact first-quarter `2026` metrics and segment-level operating results | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1137774/000113777426000093/exhibit991-1q26earningspre.htm |
| PRU-T10 | Prudential `Q1 2026` 8-K | 2026-05-05 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1137774/000113777426000093/pru-20260505.htm |
| PRU-T11 | Prudential `Q1 2026` 10-Q | 2026-05-06 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1137774/000113777426000095/pru-20260331.htm |
| PRU-T12 | Prudential `Q2 2026` preliminary update | 2026-07-15 | SEC filing HTML | Shows PGIM assets under management and estimated one-time assumption-update impacts ahead of full results | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1137774/000113777426000157/pru-20260715.htm |
| PRU-T13 | Prudential `Q2 2026` official results page | 2026-08-12 | Official IR page | Confirms the official second-quarter `2026` results page | `[Disclosed]` | https://www.investor.prudential.com/news/news-details/2026/Prudential-Financial-Inc--Announces-Second-Quarter-2026-Results/default.aspx |
| PRU-T14 | Prudential `Q2 2026` 10-Q | 2026-08-05 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1137774/000113777426000176/pru-20260630.htm |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation only. As of `2026-08-12`, the hosted annual package still lagged at `2024`.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is strong on official URLs and SEC filings:
  - official annual-report and quarterly-results pages
  - official results pages for `Q4 2025`, `Q1 2026`, and `Q2 2026`
  - SEC annual filing, quarter-release exhibit chain, `8-K` wrappers, and both in-scope `10-Q` filings
- The packet is still marked `qualified` because this workspace does not yet preserve a rebuilt local raw-artifact chain comparable to the cleanest proof-standard packets.

## Missing evidence

- No clean local copies of the official annual report PDF, quarterly supplements, or transcript artifacts were rebuilt into this workspace.
- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- The authoritative filing and IR URL chain is still strong enough for thematic interpretation and life-insurance comparison work.
