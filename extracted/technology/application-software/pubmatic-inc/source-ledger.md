# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| PUBM-T1 | AnnualReports.com company page | 2026-08-10 collected | Aggregator page HTML | Confirms PubMatic's saved archive placement under `Technology / Application Software` and shows AnnualReports lagging at `2023` | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/technology/application-software/pubmatic-inc/company-page.html) |
| PUBM-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Records taxonomy fit and archive lag versus the required `2025` evidence window | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/technology/application-software/pubmatic-inc/annualreports-verification.md) |
| PUBM-T3 | PubMatic investor-relations home page | 2026-08-10 collected | Official IR page HTML | Preserves the company-hosted IR chain for annual, quarterly, and SEC filing navigation | `[Disclosed]` | [investor-home.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/pubmatic-inc/investor-home.html) |
| PUBM-T4 | PubMatic annual-reports page | 2026-08-10 collected | Official IR page HTML | Confirms the `2025` annual anchor through the company-hosted `10-K` entry filed `2026-02-26` | `[Disclosed]` | [annual-reports.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/pubmatic-inc/annual-reports.html) |
| PUBM-T5 | PubMatic quarterly-results page | 2026-08-10 collected | Official IR page HTML | Confirms the latest three reported periods in scope: `Q2 2026`, `Q1 2026`, and `Q4 2025` | `[Disclosed]` | [quarterly-results.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/pubmatic-inc/quarterly-results.html) |
| PUBM-T6 | PubMatic SEC filings page | 2026-08-10 collected | Official IR page HTML | Confirms the exact filing dates and company-hosted links for the in-scope `10-K`, `10-Q`, and `8-K` chain | `[Disclosed]` | [sec-filings.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/pubmatic-inc/sec-filings.html) |
| PUBM-T7 | Official IR verification note | 2026-08-10 | Official IR verification note | Records the annual-plus-quarter timing chain for packet scope | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/pubmatic-inc/official-ir-verification.md) |
| PUBM-T8 | SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Verifies filer identity, ticker `PUBM`, exchange `Nasdaq`, SIC description, and fiscal year-end `1231` | `[Filed]` | [submissions-cik0001422930.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/application-software/pubmatic-inc/submissions-cik0001422930.json) |
| PUBM-T9 | PubMatic Q4 `2025` and FY `2025` earnings release | 2026-02-26 released / 2026-08-10 collected | Official IR release HTML | Full year-end operating narrative covering CTV, AgenticOS, underlying growth excluding political and legacy DSP pressure, and capital allocation | `[Disclosed]` | [2025-q4-results.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/pubmatic-inc/2025-q4-results.html) |
| PUBM-T10 | PubMatic Q1 `2026` earnings release | 2026-05-07 released / 2026-08-10 collected | Official IR release HTML | First-quarter `2026` operating narrative covering AI adoption, mobile app growth, emerging revenue growth, and underlying growth excluding the legacy DSP | `[Disclosed]` | [2026-q1-results.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/pubmatic-inc/2026-q1-results.html) |
| PUBM-T11 | PubMatic Q2 `2026` earnings release | 2026-08-06 released / 2026-08-10 collected | Official IR release HTML | Most recent quarter in scope covering double-digit growth, AI campaign adoption, CTV/mobile mix, and buy-side diversification | `[Disclosed]` | [2026-q2-results.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/application-software/pubmatic-inc/2026-q2-results.html) |

## Reconciliation notes

- AnnualReports confirms company identity and placement, but the saved page still tops out at `2023`.
- Official IR and SEC close the annual-report gap through the company-hosted `2025` `10-K` entry filed `2026-02-26`.
- SEC submissions confirm fiscal year-end `1231`, so the latest three reported quarters as of Monday, August 10, 2026 are:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`

## Missing evidence

- No standalone company-hosted glossy annual-report PDF was exposed in the saved annual-reports artifact; the filed `10-K` is the annual anchor used for this packet.
- No standalone transcript artifacts were saved locally, even though the quarterly-results page exposes webcast and prepared-remarks materials.
- Those gaps do not block packet completion because the company-hosted IR timing chain, releases, and SEC filing metadata are preserved.
