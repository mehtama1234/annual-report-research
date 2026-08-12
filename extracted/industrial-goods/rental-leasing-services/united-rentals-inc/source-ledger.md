# Source Ledger

Date baseline: 2026-08-10

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
| URI-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports company page | Confirms `Industrial Goods` / `Rental & Leasing Services` taxonomy and `2024` lag | `[Reported]` | [company-page.html](/raw/annualreports/industrial-goods/rental-leasing-services/united-rentals-inc/company-page.html) |
| URI-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents taxonomy use and AnnualReports lag | `[Reported]` | [annualreports-verification.md](/raw/annualreports/industrial-goods/rental-leasing-services/united-rentals-inc/annualreports-verification.md) |
| URI-T3 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves annual, quarter, and events URLs | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/ir-source-links.md) |
| URI-T4 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves direct SEC annual and quarter filing references | `[Filed]` | [sec-source-links.md](/raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/sec-source-links.md) |
| URI-T5 | `2025` annual report PDF | 2026-08-10 collected | Annual report PDF | Provides shareholder letter, category mix, and annual strategic framing | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/2025-annual-report.pdf) |
| URI-T6 | `2025` Form `10-K` HTML | 2026-01-28 filed | SEC filing HTML | Core annual narrative, risk framing, and financial statements | `[Filed]` | [2025-10k.html](/raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-10k.html) |
| URI-T7 | `Q2 2026` official results page URL note | 2026-08-10 verified | Official IR URL note | Preserves the direct release URL after the shell capture hit a Cloudflare challenge | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/ir-source-links.md) |
| URI-T8 | `Q2 2026` earnings release PDF | 2026-07-22 | Earnings release PDF | Preserves the latest quarter release locally | `[Disclosed]` | [2026-q2-earnings-release.pdf](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-earnings-release.pdf) |
| URI-T9 | `Q2 2026` investor presentation | 2026-07-22 | Investor presentation PDF | Adds fleet, market-share, and specialty-mix context | `[Disclosed]` | [2026-q2-presentation.pdf](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-presentation.pdf) |
| URI-T10 | `Q2 2026` Form `10-Q` HTML | 2026-07-22 filed | SEC filing HTML | Latest reported quarter filing | `[Filed]` | [2026-q2-10q.html](/raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-10q.html) |
| URI-T11 | `Q2 2026` earnings `8-K` HTML | 2026-07-22 filed | SEC filing HTML | Confirms the quarter release attachment | `[Filed]` | [2026-q2-8k.html](/raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q2-8k.html) |
| URI-T12 | `Q1 2026` official results page | 2026-04-22 | Official result page HTML | Provides first-quarter summary and raised guidance | `[Disclosed]` | [2026-q1-results.html](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q1-results.html) |
| URI-T13 | `Q1 2026` earnings release PDF | 2026-04-22 | Earnings release PDF | Preserves the first-quarter release locally | `[Disclosed]` | [2026-q1-earnings-release.pdf](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q1-earnings-release.pdf) |
| URI-T14 | `Q1 2026` investor presentation | 2026-04-22 | Investor presentation PDF | Adds specialty mix, restructuring, and historical return context | `[Disclosed]` | [2026-q1-presentation.pdf](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q1-presentation.pdf) |
| URI-T15 | `Q1 2026` Form `10-Q` HTML | 2026-04-22 filed | SEC filing HTML | Filing support for the first quarter | `[Filed]` | [2026-q1-10q.html](/raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q1-10q.html) |
| URI-T16 | `Q1 2026` earnings `8-K` HTML | 2026-04-22 filed | SEC filing HTML | Confirms the first-quarter release attachment | `[Filed]` | [2026-q1-8k.html](/raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-q1-8k.html) |
| URI-T17 | `Q4 2025` official results page | 2026-01-28 | Official result page HTML | Provides fourth-quarter and full-year results plus `2026` outlook | `[Disclosed]` | [2025-q4-results.html](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q4-results.html) |
| URI-T18 | `Q4 2025` earnings release PDF | 2026-01-28 | Earnings release PDF | Preserves the fourth-quarter/full-year release locally | `[Disclosed]` | [2025-q4-earnings-release.pdf](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q4-earnings-release.pdf) |
| URI-T19 | `Q4 2025` earnings `8-K` HTML | 2026-01-28 filed | SEC filing HTML | Confirms the fourth-quarter/full-year release attachment | `[Filed]` | [2025-q4-8k.html](/raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-q4-8k.html) |
| URI-T20 | IR hub-page challenge captures | 2026-08-10 collected | Shell HTML captures | Documents that the canonical IR hub pages were Cloudflare-gated from the shell at collection time | `[Disclosed]` | [annual-reports.html](/raw/company-ir/industrial-goods/rental-leasing-services/united-rentals-inc/annual-reports.html) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- United Rentals’ annual report PDF, quarter release PDFs, investor presentations, direct IR URL map, and SEC filings form a complete evidence set for the annual report and latest three reported quarters.
- The canonical IR hub pages were Cloudflare-gated from the current shell environment, and the attempted local `Q2 2026` release-page capture also resolved to a Cloudflare challenge, so the packet relies on the preserved release PDF, presentation PDF, direct IR URL note, and SEC filings for that quarter.

## Missing evidence

- No standalone earnings-call transcript artifact was identified or saved locally for `Q2 2026`, `Q1 2026`, or `Q4 2025`.
- No direct `Q4 2025` investor presentation PDF was confirmed and saved locally from the current environment, although the official `Q4 2025` results page explicitly references that presentation.
