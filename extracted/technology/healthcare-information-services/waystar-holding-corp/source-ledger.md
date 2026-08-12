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
| WAY-T1 | Waystar investor-relations overview | 2026-08-12 | Official IR page | Confirms company identity, mission, and IR hub | `[Disclosed]` | https://investors.waystar.com/investor-relations/ |
| WAY-T2 | Waystar SEC filings page | 2026-08-12 | Official IR page | Confirms the official annual and quarterly filing chain | `[Disclosed]` | https://investors.waystar.com/financial-information/sec-filings/ |
| WAY-T3 | Waystar `2025` Form 10-K | 2026-02-17 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1990354/000199035426000011/way-20251231.htm |
| WAY-T4 | Waystar `Q4 2025` official results page | 2026-08-12 | Official IR page | Confirms official fourth-quarter and full-year `2025` results | `[Disclosed]` | https://investors.waystar.com/news-releases/news-release-details/waystar-reports-fourth-quarter-and-fiscal-year-2025-results/ |
| WAY-T5 | Waystar `Q4 2025` 8-K | 2026-02-17 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1990354/000199035426000012/way-20260217.htm |
| WAY-T6 | Waystar `Q1 2026` official results page | 2026-08-12 | Official IR page | Confirms official first-quarter `2026` results | `[Disclosed]` | https://investors.waystar.com/news-releases/news-release-details/waystar-reports-first-quarter-2026-results/ |
| WAY-T7 | Waystar `Q1 2026` 8-K | 2026-04-29 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1990354/000199035426000024/way-20260429.htm |
| WAY-T8 | Waystar `Q1 2026` 10-Q | 2026-04-29 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1990354/000199035426000025/way-20260331.htm |
| WAY-T9 | Waystar `Q2 2026` official results page | 2026-08-12 | Official IR page | Confirms official second-quarter `2026` results | `[Disclosed]` | https://investors.waystar.com/news-releases/news-release-details/waystar-reports-second-quarter-2026-results/ |
| WAY-T10 | Waystar `Q2 2026` 8-K | 2026-07-29 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1990354/000199035426000034/way-20260729.htm |
| WAY-T11 | Waystar `Q2 2026` 10-Q | 2026-07-29 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | https://www.sec.gov/Archives/edgar/data/1990354/000199035426000035/way-20260630.htm |

## Reconciliation notes

- No usable AnnualReports company page surfaced during the `2026-08-12` check, so taxonomy and authority were taken from the company's official description and SEC chain instead.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - company IR and SEC for the authoritative annual and quarter chain
  - no usable AnnualReports company page was available to serve as taxonomy confirmation
- The verified chain is strong on official URLs and SEC filings:
  - official investor-relations and filings pages
  - official results pages for `Q4 2025`, `Q1 2026`, and `Q2 2026`
  - SEC annual filing, `8-K` wrappers, and both in-scope `10-Q` filings
- The packet is still marked `qualified` because this workspace does not yet preserve a rebuilt local raw-artifact chain comparable to the cleanest proof-standard packets.

## Missing evidence

- No clean local copies of the official annual report PDF, quarterly supplements, or transcript artifacts were rebuilt into this workspace.
- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- The authoritative filing and IR URL chain is still strong enough for thematic interpretation and healthcare-information workflow comparison work.
