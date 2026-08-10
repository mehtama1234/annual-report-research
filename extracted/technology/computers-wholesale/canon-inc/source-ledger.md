# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CAJ-T1 | AnnualReports.com company page | 2026-08-10 collected | Aggregator page HTML | Confirms Canon's AnnualReports taxonomy, company description, and live `2025 Annual Report` archive | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/technology/computers-wholesale/canon-inc/company-page.html) |
| CAJ-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Records the taxonomy mismatch versus the assigned lane and confirms `2025` archive presence | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/annualreports/technology/computers-wholesale/canon-inc/annualreports-verification.md) |
| CAJ-T3 | Canon investor-relations home page | 2026-08-10 collected | Official IR page HTML | Preserves the IR home page and confirms `Q2 2026` visibility on the current Canon IR chain | `[Disclosed]` | [investor-home.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/investor-home.html) |
| CAJ-T4 | Canon annual-report library | 2026-08-10 collected | Official IR page HTML | Confirms `CANON ANNUAL REPORT 2025` on the company-hosted archive | `[Disclosed]` | [annual-report-library.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/annual-report-library.html) |
| CAJ-T5 | Canon results library | 2026-08-10 collected | Official IR page HTML | Confirms the in-scope timing chain: `Q4 2025`, `Q1 2026`, `Q2 2026` | `[Disclosed]` | [results-library.html](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/results-library.html) |
| CAJ-T6 | Official IR verification note | 2026-08-10 | Official IR verification note | Records the authoritative annual-plus-quarter scope and the SEC applicability limitation | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/official-ir-verification.md) |
| CAJ-T7 | Canon `2025` annual report | 2026-08-10 collected | Official IR PDF | Core annual-report artifact for the target year | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/2025-annual-report.pdf) |
| CAJ-T8 | Canon FY `2025` results | 2026-01-29 released / 2026-08-10 collected | Official IR results PDF | Gives filed-like year-end results and forward outlook for the `Q4 2025` anchor period | `[Disclosed]` | [2025-fy-results.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/2025-fy-results.pdf) |
| CAJ-T9 | Canon FY `2025` presentation | 2026-01-29 released / 2026-08-10 collected | Official IR presentation PDF | Provides management commentary on imaging, printing, medical, industrial, and record sales | `[Disclosed]` | [2025-fy-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/2025-fy-presentation.pdf) |
| CAJ-T10 | Canon Q1 `2026` results | 2026-04-23 released / 2026-08-10 collected | Official IR results PDF | First-quarter `2026` operating and financial results in scope | `[Disclosed]` | [2026-q1-results.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/2026-q1-results.pdf) |
| CAJ-T11 | Canon Q1 `2026` presentation | 2026-04-23 released / 2026-08-10 collected | Official IR presentation PDF | Captures tariffs, memory-cost pressure, Imaging growth, and management narrative | `[Disclosed]` | [2026-q1-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/2026-q1-presentation.pdf) |
| CAJ-T12 | Canon Q2 `2026` / first-half results | 2026-07-27 released / 2026-08-10 collected | Official IR results PDF | Most recent reported period in scope | `[Disclosed]` | [2026-q2-results.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/2026-q2-results.pdf) |
| CAJ-T13 | Canon Q2 `2026` / first-half presentation | 2026-07-27 released / 2026-08-10 collected | Official IR presentation PDF | Captures second-quarter and first-half market conditions, imaging growth, and revised full-year outlook | `[Disclosed]` | [2026-q2-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/company-ir/technology/computers-wholesale/canon-inc/2026-q2-presentation.pdf) |
| CAJ-T14 | Canon SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms historical filer identity, fiscal year-end `1231`, and `Photographic Equipment & Supplies` SIC; also shows `15F-12B` deregistration context | `[Filed]` | [submissions-cik0000016988.json](/home/manishmehta/ui-projects/annual-report-research-footwear-dept-audit/raw/sec/technology/computers-wholesale/canon-inc/submissions-cik0000016988.json) |

## Reconciliation notes

- AnnualReports and official IR both provide a clean `2025` annual-report chain.
- Official IR gives the authoritative in-scope reporting chain as of Monday, August 10, 2026:
  - `Q2 2026`
  - `Q1 2026`
  - `Q4 2025`
- SEC metadata is useful for identity, SIC, and fiscal-year-end support, but not for the current-period annual-plus-quarter chain because Canon's SEC submissions history shows `15F-12B` filed on `2024-03-07`.

## Missing evidence

- No current-period SEC `20-F` or `6-K` chain is preserved for `2025-2026` because Canon's U.S. reporting status changed before the assignment window.
- That does not block packet completion because AnnualReports and Canon's official IR chain are both intact and authoritative for the required window.
