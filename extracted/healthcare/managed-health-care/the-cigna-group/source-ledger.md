# Source Ledger

Date baseline: 2026-08-11

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
| CI-T1 | AnnualReports.com Cigna company page | 2026-08-11 | Aggregator page | Confirms Healthcare / Health Care Plans taxonomy and shows the current annual archive entry | `[Reported]` | https://www.annualreports.com/Company/cigna-corporation |
| CI-T2 | The Cigna Group annual reports page | 2026-08-11 | Official IR page | Confirms the official `2025` annual report PDF entry | `[Disclosed]` | https://investors.thecignagroup.com/financials/annual-reports/default.aspx |
| CI-T3 | The Cigna Group quarterly results page | 2026-08-11 | Official IR page | Confirms the official quarterly-results hub for the trailing quarter chain | `[Disclosed]` | https://investors.thecignagroup.com/financials/quarterly-results/default.aspx |
| CI-T4 | The Cigna Group `2025` annual report PDF | 2026-02-05 | Annual report PDF | Official annual report package for the year ended `2025-12-31` | `[Disclosed]` | https://s202.q4cdn.com/757723766/files/doc_financials/2025/ar/2025-Annual-Report.pdf |
| CI-T5 | The Cigna Group `2025` Form 10-K | 2026-02-26 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000173994026000006/ci-20251231.htm |
| CI-T6 | The Cigna Group `Q4 2025` earnings event page | 2026-08-11 | Official IR event page | Confirms the official Q4 2025 release, supplement, and transcript hub | `[Disclosed]` | https://investors.thecignagroup.com/events-and-presentations/events/event-details/2026/Fourth-Quarter-2025-Earnings-Release-2026-IIqVH76Mhy/default.aspx |
| CI-T7 | The Cigna Group `Q4 2025` earnings release exhibit | 2026-02-05 | SEC exhibit HTML | Exact fourth-quarter and full-year `2025` metrics plus initial `2026` outlook | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000114036126003768/ef20064751_ex99-1.htm |
| CI-T8 | The Cigna Group `Q4 2025` 8-K | 2026-02-05 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000114036126003768/ef20064751_8k.htm |
| CI-T9 | The Cigna Group `Q1 2026` earnings event page | 2026-08-11 | Official IR event page | Confirms the official Q1 2026 release hub | `[Disclosed]` | https://investors.thecignagroup.com/events-and-presentations/events/event-details/2026/First-Quarter-2026-Earnings-Release-2026-PXT1F9-YaI/default.aspx |
| CI-T10 | The Cigna Group `Q1 2026` earnings release exhibit | 2026-04-30 | SEC exhibit HTML | Exact first-quarter `2026` metrics and raised `2026` outlook | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000114036126017971/ef20071317_ex99-1.htm |
| CI-T11 | The Cigna Group `Q1 2026` 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000114036126017971/ef20071317_8k.htm |
| CI-T12 | The Cigna Group `Q1 2026` 10-Q | 2026-05-02 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000173994026000043/ci-20260331.htm |
| CI-T13 | The Cigna Group `Q2 2026` earnings event page | 2026-08-11 | Official IR event page | Confirms the official Q2 2026 release hub | `[Disclosed]` | https://investors.thecignagroup.com/events-and-presentations/events/event-details/2026/Second-Quarter-2026-Earnings-Release-2026-MLPNK-N11I/default.aspx |
| CI-T14 | The Cigna Group `Q2 2026` earnings release exhibit | 2026-07-30 | SEC exhibit HTML | Exact second-quarter `2026` metrics and raised `2026` outlook | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000114036126030135/ef20078875_ex99-1.htm |
| CI-T15 | The Cigna Group `Q2 2026` 8-K | 2026-07-30 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000114036126030135/ef20078875_8k.htm |
| CI-T16 | The Cigna Group `Q2 2026` 10-Q | 2026-08-01 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1739940/000173994026000065/ci-20260630.htm |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation. As of `2026-08-11`, it showed `CIGNA Corporation` in `Health Care Plans` and listed `2025 Annual Report and Form 10K`.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is strong on official URLs and SEC filings:
  - official `2025` annual report page and annual report PDF
  - official quarterly-results and event pages for `Q4 2025`, `Q1 2026`, and `Q2 2026`
  - SEC annual filing, quarter release exhibits, `8-K` wrappers, and both in-scope `10-Q` filings
- The packet is still marked `qualified` because this workspace does not yet preserve a rebuilt local raw-artifact chain comparable to the cleanest proof-standard packets.

## Missing evidence

- No clean local copies of the official annual report PDF, quarterly supplements, or transcript artifacts were rebuilt into this workspace.
- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- The authoritative filing and IR URL chain is still strong enough for thematic interpretation and managed-care comparison work.
