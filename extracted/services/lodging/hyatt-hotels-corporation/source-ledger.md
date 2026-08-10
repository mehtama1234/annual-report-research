# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| H-T1 | AnnualReports.com Hyatt company page | 2026-08-10 | Aggregator page | Confirms Lodging / Consumer Goods classification and archive lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/lodging/hyatt-hotels-corporation/company-page.html) |
| H-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Preserves taxonomy and lag observation in repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/services/lodging/hyatt-hotels-corporation/annualreports-verification.md) |
| H-T3 | Hyatt official IR verification note | 2026-08-10 | Verification note | Records the official annual and quarter chain | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/official-ir-verification.md) |
| H-T4 | Hyatt 2025 Annual Report | 2026-02-13 | Annual report PDF | Core annual narrative on brand platform, room network, and 2025 financial results | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/2025-annual-report.pdf) |
| H-T5 | Hyatt Q4 2025 earnings release | 2026-02-12 | Earnings release PDF | Quarter and full-year 2025 operating update | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/2025-q4-earnings-release.pdf) |
| H-T6 | Hyatt Q1 2026 earnings release | 2026-04-30 | Earnings release PDF | Quarter-minus-1 travel, fee, and pipeline update | `[Disclosed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/2026-q1-earnings-release.pdf) |
| H-T7 | Hyatt Q2 2026 earnings release | 2026-07-30 | Earnings release PDF | Most recent quarter travel, fee, and guidance update | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/services/lodging/hyatt-hotels-corporation/2026-q2-earnings-release.pdf) |
| H-T8 | Hyatt SEC submissions feed | 2026-08-10 | SEC metadata JSON | Authoritative chronology for the `10-K`, `ARS`, `10-Q`, and latest `8-K` | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/lodging/hyatt-hotels-corporation/sec-submissions.json) |
| H-T9 | Hyatt SEC access verification note | 2026-08-10 | Verification note | Documents blocked direct SEC archive access while preserving chronology | `[Filed]` | [sec-access-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/services/lodging/hyatt-hotels-corporation/sec-access-verification.md) |

## Reconciliation notes

- Hyatt now has a strong annual and quarter evidence chain for CLI 8 scope:
  - AnnualReports taxonomy confirmation
  - official `2025` annual-report PDF
  - official earnings-release PDFs for `Q4 2025`, `Q1 2026`, and `Q2 2026`
  - SEC chronology via the saved submissions feed
- Hyatt is the first completed service-layer physical interface case in this frontier, giving the branch direct coverage of branded hospitality as a middle-layer operating network.

## Missing evidence

- No earnings-call transcript is saved locally for Hyatt.
- No standalone SEC filing HTML is saved locally because direct archive requests returned `403`.
