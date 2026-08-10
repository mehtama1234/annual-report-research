# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| SYY-T1 | AnnualReports.com Sysco company page | 2026-08-10 | Aggregator page | Confirms Food Wholesale / Consumer Goods classification and AnnualReports archive lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/retail-grocery-stores/sysco-corp/company-page.html) |
| SYY-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Normalizes the taxonomy and lag observation into repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/retail-grocery-stores/sysco-corp/annualreports-verification.md) |
| SYY-T3 | Sysco annual reports page | 2026-08-10 | Official IR page | Confirms the official `2025 Annual Report` pathing | `[Disclosed]` | [annual-reports.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/annual-reports.html) |
| SYY-T4 | Sysco 2025 Annual Report | 2025-08-22 | Annual report PDF | Core annual narrative, financial framing, and management view of customer, route, and supply-chain economics | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/2025-annual-report.pdf) |
| SYY-T5 | Sysco official IR verification note | 2026-08-10 | Verification note | Confirms the annual and trailing-quarter evidence chain on the official IR stack | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/official-ir-verification.md) |
| SYY-T6 | Sysco quarterly results page | 2026-08-10 | Official IR page | Confirms FY2026 Q4, Q3, and Q2 materials and file links | `[Disclosed]` | [quarterly-results-2026.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/quarterly-results-2026.html) |
| SYY-T7 | Sysco FY2026 Q4 earnings release | 2026-08-04 | Earnings release PDF | Most recent quarter and full-year operating update with FY2027 guidance | `[Disclosed]` | [2026-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/2026-q4-earnings-release.pdf) |
| SYY-T8 | Sysco FY2026 Q4 news release page | 2026-08-04 | Official IR page | HTML source for quarter-end, full-year, and AI-efficiency language | `[Disclosed]` | [2026-q4-news-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/2026-q4-news-release.html) |
| SYY-T9 | Sysco FY2026 Q3 earnings release | 2026-04-28 | Earnings release PDF | Quarter-minus-1 financial summary and cash-flow trend | `[Disclosed]` | [2026-q3-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/2026-q3-earnings-release.pdf) |
| SYY-T10 | Sysco FY2026 Q3 news release page | 2026-04-28 | Official IR page | HTML source for Q3 volume, earnings, and working-capital signals | `[Disclosed]` | [news-release-q3-2026.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/news-release-q3-2026.html) |
| SYY-T11 | Sysco FY2026 Q2 earnings release | 2026-01-27 | Earnings release PDF | Quarter-minus-2 financial summary and guidance framing | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/2026-q2-earnings-release.pdf) |
| SYY-T12 | Sysco FY2026 Q2 news release page | 2026-01-27 | Official IR page | HTML source for Q2 volume and earnings details | `[Disclosed]` | [news-release-q2-2026.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/retail-grocery-stores/sysco-corp/news-release-q2-2026.html) |
| SYY-T13 | Sysco SEC submissions feed | 2026-08-10 | SEC metadata JSON | Authoritative filing chronology for the `10-K`, `10-Q`, and latest `8-K` | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/sysco-corp/sec-submissions.json) |
| SYY-T14 | Sysco SEC access verification note | 2026-08-10 | Verification note | Documents blocked direct archive access and preserves chronology evidence | `[Filed]` | [sec-access-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/retail-grocery-stores/sysco-corp/sec-access-verification.md) |

## Reconciliation notes

- Sysco now has a complete annual-report evidence chain for this frontier’s practical scope:
  - AnnualReports taxonomy confirmation
  - official IR annual-report page
  - official `2025` annual-report PDF
  - SEC filing chronology via the saved submissions feed
- The trailing three-quarter window as of `2026-08-10` is covered with official quarter materials for:
  - `FY2026 Q4`
  - `FY2026 Q3`
  - `FY2026 Q2`
- This packet relies on official IR content for the operating narrative because direct SEC archive fetches were blocked in the shell environment.

## Missing evidence

- No earnings-call transcript is saved locally for Sysco.
- No standalone SEC filing HTML is saved locally for Sysco because direct archive requests returned `403` in this shell environment.
