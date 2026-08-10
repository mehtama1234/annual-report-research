# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| URI-T1 | AnnualReports.com United Rentals company page | 2026-08-10 | Aggregator page | Confirms Rental & Leasing Services / Industrial Goods classification and archive lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/business-services/united-rentals-inc/company-page.html) |
| URI-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Preserves taxonomy and lag observation in repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/business-services/united-rentals-inc/annualreports-verification.md) |
| URI-T3 | United Rentals official IR verification note | 2026-08-10 | Verification note | Records the official annual and quarter URLs and the shell-side `429` limitation | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/business-services/united-rentals-inc/official-ir-verification.md) |
| URI-T4 | United Rentals 2025 Annual Report | 2026-03-25 | Annual report PDF | Core annual narrative on rental access, specialty growth, capital efficiency, and 2025 financial results | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/business-services/united-rentals-inc/2025-annual-report.pdf) |
| URI-T5 | United Rentals events and presentations page | 2026-08-10 | Official IR page | Confirms the IR route structure and financial navigation despite rate limits on some direct endpoints | `[Disclosed]` | [events-and-presentations.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/business-services/united-rentals-inc/events-and-presentations.html) |
| URI-T6 | United Rentals press releases page | 2026-08-10 | Official IR page | Confirms press-release routing for the official quarter updates | `[Disclosed]` | [press-releases.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/business-services/united-rentals-inc/press-releases.html) |
| URI-T7 | United Rentals Q2 2026 earnings release | 2026-07-22 | Earnings release PDF | Most recent quarter financial and guidance update | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/business-services/united-rentals-inc/2026-q2-earnings-release.pdf) |
| URI-T8 | United Rentals SEC submissions feed | 2026-08-10 | SEC metadata JSON | Authoritative chronology for the `10-K`, `ARS`, `10-Q`, and latest `8-K` | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/united-rentals-inc/sec-submissions.json) |
| URI-T9 | United Rentals SEC access verification note | 2026-08-10 | Verification note | Documents blocked direct SEC archive access while preserving filing chronology | `[Filed]` | [sec-access-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/business-services/united-rentals-inc/sec-access-verification.md) |

## Reconciliation notes

- United Rentals now has a strong annual evidence chain for practical CLI 8 scope:
  - AnnualReports taxonomy confirmation
  - official `2025` annual-report PDF
  - verified official IR annual and quarter URLs
  - SEC chronology via the saved submissions feed
- The trailing three-quarter window as of `2026-08-10` is covered through:
  - local official Q2 2026 release PDF
  - verified official IR pages for Q1 2026 and Q4 2025
  - SEC chronology for the matching `10-Q` and `10-K`
- The company is suitable for frontier-level interpretation even though some raw HTML captures were blocked.

## Missing evidence

- No earnings-call transcript is saved locally for United Rentals.
- No standalone SEC filing HTML is saved locally because direct archive requests returned `403`.
- No raw local capture of the Q1 2026 and Q4 2025 press-release detail pages is saved because shell-side direct pulls of some IR routes returned `429`.
