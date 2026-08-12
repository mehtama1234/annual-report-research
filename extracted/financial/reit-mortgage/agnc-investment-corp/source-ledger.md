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
| AGNC-T1 | AnnualReports.com AGNC company page | 2026-08-12 | Aggregator page | Confirms `REIT - Mortgage Real Estate` taxonomy | `[Reported]` | https://www.annualreports.com/Company/agnc-investment-corp |
| AGNC-T2 | AGNC investor overview page | 2026-08-12 | Official IR page | Confirms official annual-report and quarterly-results hub | `[Disclosed]` | https://investors.agnc.com/ |
| AGNC-T3 | AGNC events and presentations page | 2026-08-12 | Official IR page | Confirms annual report, presentations, and quarterly-results availability | `[Disclosed]` | https://investors.agnc.com/events-and-presentations/upcoming-events |
| AGNC-T4 | AGNC `2025` annual report PDF | 2026-03-04 | Annual report PDF | Annual report package for the year ended `2025-12-31` | `[Disclosed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000062/annualreport-final.pdf |
| AGNC-T5 | AGNC `2025` Form 10-K | 2026-02-24 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000043/agnc-20251231.htm |
| AGNC-T6 | AGNC `Q4 2025` earnings release exhibit | 2026-01-27 | SEC exhibit HTML | Exact fourth-quarter and full-year `2025` shareholder-return and spread metrics | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000024/agnc8kexhibit991123125.htm |
| AGNC-T7 | AGNC `Q4 2025` 8-K | 2026-01-27 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000024/agnc-20260127.htm |
| AGNC-T8 | AGNC `Q1 2026` earnings release exhibit | 2026-04-20 | SEC exhibit HTML | Exact first-quarter `2026` book-value, spread-income, and leverage metrics | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000095/agnc8kexhibit99133126.htm |
| AGNC-T9 | AGNC `Q1 2026` 8-K | 2026-04-20 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000095/agnc-20260420.htm |
| AGNC-T10 | AGNC `Q1 2026` 10-Q | 2026-05-01 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000099/agnc-20260331.htm |
| AGNC-T11 | AGNC `Q2 2026` earnings release exhibit | 2026-07-20 | SEC exhibit HTML | Exact second-quarter `2026` book-value recovery, economic-return, and spread metrics | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000124/agnc8kexhibit99163026.htm |
| AGNC-T12 | AGNC `Q2 2026` 8-K | 2026-07-20 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000124/agnc-20260720.htm |
| AGNC-T13 | AGNC `Q2 2026` 10-Q | 2026-08-01 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1423689/000142368926000129/agnc-20260630.htm |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is strong on official URLs and SEC filings:
  - official investor and event pages
  - annual report PDF and SEC annual filing
  - SEC quarter-release exhibits, `8-K` wrappers, and both in-scope `10-Q` filings
- The packet is still marked `qualified` because this workspace does not yet preserve a rebuilt local raw-artifact chain comparable to the cleanest proof-standard packets.

## Missing evidence

- No clean local copies of the official quarterly presentations or transcript artifacts were rebuilt into this workspace.
- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- The authoritative filing and IR URL chain is still strong enough for thematic interpretation and mortgage-REIT comparison work.
