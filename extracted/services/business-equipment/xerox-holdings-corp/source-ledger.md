# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| XRX-S1 | AnnualReports.com company page | 2026-08-10 collected | Aggregator page HTML | Confirms company identity and records the AnnualReports taxonomy mismatch plus archive lag | `[Reported]` | [company-page-correct.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/business-equipment/xerox-holdings-corp/company-page-correct.html) |
| XRX-S2 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Records exact frontier-fit reasoning and the fact that AnnualReports only showed `2024` as the latest hosted package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/services/business-equipment/xerox-holdings-corp/annualreports-verification.md) |
| XRX-S3 | Xerox IR verification note | 2026-08-10 | Official IR verification note | Records the corrected IR paths, saved artifact chain, and SEC access limitation | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/official-ir-verification.md) |
| XRX-S4 | Xerox SEC submissions index | 2026-08-10 collected | SEC index JSON | Confirms filer identity and the exact annual-plus-quarter filing sequence in scope | `[Filed]` | [submissions-cik0001770450.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/services/business-equipment/xerox-holdings-corp/submissions-cik0001770450.json) |
| XRX-S5 | Xerox `2025` annual report | 2026-04-07 released / 2026-08-10 collected | Official IR annual report PDF | Core annual package for the `2025` fiscal year | `[Reported]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/2025-annual-report.pdf) |
| XRX-S6 | Xerox IR-hosted `2025` `10-K` PDF | 2026-03-17 filed / 2026-08-10 collected | Official IR filing PDF | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/2025-10k.pdf) |
| XRX-S7 | Xerox Q4 `2025` earnings release | 2026-01-29 released / 2026-08-10 collected | Official IR earnings-release PDF | Full-year and fourth-quarter `2025` operating commentary, guidance, and cash-flow data | `[Reported]` | [4q2025-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/4q2025-earnings-release.pdf) |
| XRX-S8 | Xerox Q4 `2025` earnings-call transcript | 2026-01-29 released / 2026-08-10 collected | Official IR transcript PDF | Direct management commentary on macro pressure, print demand, memory costs, and integration progress | `[Disclosed]` | [4q2025-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/4q2025-transcript.pdf) |
| XRX-S9 | Xerox Q1 `2026` earnings release | 2026-04-30 released / 2026-08-10 collected | Official IR earnings-release PDF | First-quarter `2026` operating trajectory, margin recovery, pipeline, and cash-flow data | `[Reported]` | [1q2026-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/1q2026-earnings-release.pdf) |
| XRX-S10 | Xerox Q1 `2026` `10-Q` PDF | 2026-05-07 filed / 2026-08-10 collected | Official IR filing PDF | First-quarter `2026` filing for current-period detail | `[Filed]` | [1q2026-10q.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/1q2026-10q.pdf) |
| XRX-S11 | Xerox Q2 `2026` earnings release | 2026-07-30 released / 2026-08-10 collected | Official IR earnings-release PDF | Most recent quarter in scope, including guidance raise and tariff-related accounting note | `[Reported]` | [2q2026-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/2q2026-earnings-release.pdf) |
| XRX-S12 | Xerox Q2 `2026` `10-Q` PDF | 2026-08-06 filed / 2026-08-10 collected | Official IR filing PDF | Most recent filing in scope | `[Filed]` | [2q2026-10q.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/services/business-equipment/xerox-holdings-corp/2q2026-10q.pdf) |

## Reconciliation notes

- AnnualReports.com is used here for identity and archive confirmation, but not as the authoritative annual-report source because the latest hosted package shown locally was `2024`.
- Xerox IR provides a clean `2025` annual report and quarter chain for:
  - Q2 `2026`
  - Q1 `2026`
  - Q4 `2025`
- The SEC submissions JSON confirms the filing dates in scope:
  - `2026-08-06` `10-Q`
  - `2026-07-30` `8-K`
  - `2026-05-07` `10-Q`
  - `2026-04-30` `8-K`
  - `2026-04-07` `ARS`
  - `2026-03-17` `10-K`
  - `2026-01-29` `8-K`
- Direct SEC filing HTML collection was blocked locally, so the saved filing bodies in this packet are the Xerox IR-hosted PDFs plus the SEC submissions index.

## Missing evidence

- No clean local SEC HTML body files were saved for the annual and quarter filings because SEC rate-limited scripted access in this environment.
