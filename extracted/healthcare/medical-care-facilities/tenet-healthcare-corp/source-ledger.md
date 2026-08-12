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
| THC-T1 | AnnualReports.com Tenet company page | 2026-08-11 | Aggregator page | Confirms Healthcare / Medical Care Facilities taxonomy and shows the current annual archive entry | `[Reported]` | https://www.annualreports.com/Company/tenet-healthcare-corp |
| THC-T2 | Tenet financials and SEC filings page | 2026-08-11 | Official IR page | Confirms the official annual and quarterly financial materials hub | `[Disclosed]` | https://investor.tenethealth.com/financials-and-sec-filings/default.aspx |
| THC-T3 | Tenet press releases page | 2026-08-11 | Official IR page | Confirms the official press-release archive for the trailing quarter chain | `[Disclosed]` | https://investor.tenethealth.com/press-releases/default.aspx |
| THC-T4 | Tenet `2025` Form 10-K | 2026-02-17 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000012/thc-20251231.htm |
| THC-T5 | Tenet `Q4 2025` official press release page | 2026-08-11 | Official IR press page | Confirms the official fourth-quarter and full-year `2025` results page | `[Disclosed]` | https://investor.tenethealth.com/press-releases/press-release-details/2026/Tenet-Reports-Strong-Fourth-Quarter-and-FY-2025-Results-Provides-2026-Financial-Outlook/default.aspx |
| THC-T6 | Tenet `Q4 2025` earnings release exhibit | 2026-02-11 | SEC exhibit HTML | Exact fourth-quarter and full-year `2025` metrics plus initial `2026` outlook | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000007/thc-20251231ex991earningsr.htm |
| THC-T7 | Tenet `Q4 2025` 8-K | 2026-02-11 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000007/thc-20260211.htm |
| THC-T8 | Tenet `Q1 2026` official press release page | 2026-08-11 | Official IR press page | Confirms the official first-quarter `2026` results page | `[Disclosed]` | https://investor.tenethealth.com/press-releases/press-release-details/2026/Tenet-Reports-Strong-First-Quarter-2026-Results/default.aspx |
| THC-T9 | Tenet `Q1 2026` earnings release exhibit | 2026-04-30 | SEC exhibit HTML | Exact first-quarter `2026` metrics and initial `2026` outlook | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000023/thc-20260331ex991earningsr.htm |
| THC-T10 | Tenet `Q1 2026` 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000023/thc-20260430.htm |
| THC-T11 | Tenet `Q1 2026` 10-Q | 2026-04-30 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000026/thc-20260331.htm |
| THC-T12 | Tenet `Q2 2026` official press release page | 2026-08-11 | Official IR press page | Confirms the official second-quarter `2026` results page | `[Disclosed]` | https://investor.tenethealth.com/press-releases/press-release-details/2026/Tenet-Reports-Strong-Second-Quarter-2026-Results-Raises-2026-Financial-Outlook/default.aspx |
| THC-T13 | Tenet `Q2 2026` earnings release exhibit | 2026-07-23 | SEC exhibit HTML | Exact second-quarter `2026` metrics and raised `2026` outlook | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000032/thc-20260630ex991earningsr.htm |
| THC-T14 | Tenet `Q2 2026` 8-K | 2026-07-23 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000032/thc-20260723.htm |
| THC-T15 | Tenet `Q2 2026` 10-Q | 2026-07-28 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/70318/000007031826000037/thc-20260630.htm |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is strong on official URLs and SEC filings:
  - official financials and press-release pages
  - SEC annual filing, quarter release exhibits, `8-K` wrappers, and both in-scope `10-Q` filings
- The packet is still marked `qualified` because this workspace does not yet preserve a rebuilt local raw-artifact chain comparable to the cleanest proof-standard packets.

## Missing evidence

- No clean local copies of the official annual report PDF, quarterly supplements, or transcript artifacts were rebuilt into this workspace.
- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- The authoritative filing and IR URL chain is still strong enough for thematic interpretation and hospital comparison work.
