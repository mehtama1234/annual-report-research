# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| MCK-T1 | AnnualReports.com McKesson company page | 2026-08-10 | Aggregator page | Confirms Drugs Wholesale / Services classification and archive lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/drug-stores/mckesson-corporation/company-page.html) |
| MCK-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Preserves taxonomy and lag observation in repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/drug-stores/mckesson-corporation/annualreports-verification.md) |
| MCK-T3 | McKesson official IR verification note | 2026-08-10 | Verification note | Records the official annual and quarter chain | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/drug-stores/mckesson-corporation/official-ir-verification.md) |
| MCK-T4 | McKesson 2025 Annual Report | 2025-05-08 | Annual report PDF | Core annual narrative and segment structure for fiscal `2025` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/drug-stores/mckesson-corporation/2025-annual-report.pdf) |
| MCK-T5 | McKesson Q1 FY2027 earnings release | 2026-08-05 | Earnings release PDF | Most recent quarter financial update and raised FY2027 outlook | `[Disclosed]` | [2026-q1-fy2027-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/drug-stores/mckesson-corporation/2026-q1-fy2027-earnings-release.pdf) |
| MCK-T6 | McKesson Q4 FY2026 earnings release | 2026-05-07 | Earnings release PDF | Quarter and full-year FY2026 operating update | `[Disclosed]` | [2026-q4-fy2026-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/drug-stores/mckesson-corporation/2026-q4-fy2026-earnings-release.pdf) |
| MCK-T7 | McKesson Q3 FY2026 presentation | 2026-02-04 | Earnings presentation PDF | Quarter-minus-2 metrics and trend support for Q3 FY2026 | `[Disclosed]` | [2026-q3-fy2026-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/drug-stores/mckesson-corporation/2026-q3-fy2026-presentation.pdf) |
| MCK-T8 | McKesson SEC submissions feed | 2026-08-10 | SEC metadata JSON | Authoritative chronology for the `10-Q`, `10-K`, `ARS`, and latest `8-K` | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/drug-stores/mckesson-corporation/sec-submissions.json) |
| MCK-T9 | McKesson SEC access verification note | 2026-08-10 | Verification note | Documents blocked direct SEC archive access while preserving chronology | `[Filed]` | [sec-access-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/drug-stores/mckesson-corporation/sec-access-verification.md) |

## Reconciliation notes

- McKesson now has a strong annual and quarter evidence chain for CLI 8 scope:
  - AnnualReports taxonomy confirmation
  - official `2025` annual-report PDF
  - official quarter materials for `Q1 FY2027`, `Q4 FY2026`, and `Q3 FY2026`
  - SEC chronology via the saved submissions feed
- This packet intentionally uses the `2025` annual report year requested by the frontier prompt, even though McKesson’s official IR site is now current through the `2026` annual cycle.
- The latest reported quarter as of `2026-08-10` is `Q1 FY2027`, filed on `2026-08-05`.

## Missing evidence

- No earnings-call transcript is saved locally for McKesson.
- No standalone SEC filing HTML is saved locally because direct archive requests returned `403`.
