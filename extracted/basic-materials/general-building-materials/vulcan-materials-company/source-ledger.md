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
| VMC-T1 | AnnualReports company page | 2026-08-10 | AnnualReports company page | Confirms `Basic Materials` / `General Building Materials` taxonomy | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/basic-materials/general-building-materials/vulcan-materials-company/company-page.html) |
| VMC-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents how AnnualReports is being used for taxonomy confirmation | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/basic-materials/general-building-materials/vulcan-materials-company/annualreports-verification.md) |
| VMC-T3 | Vulcan annual reports page | 2026-08-10 collected | Investor relations page HTML | Confirms the official annual-report stack | `[Disclosed]` | [annual-reports.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/annual-reports.html) |
| VMC-T4 | Vulcan quarterly results page | 2026-08-10 collected | Investor relations page HTML | Confirms the current quarterly-results stack | `[Disclosed]` | [quarterly-results.html](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/quarterly-results.html) |
| VMC-T5 | `2025` annual report PDF | 2026-08-10 collected | Annual report PDF | Core annual narrative, business description, and financial overview | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2025-annual-report.pdf) |
| VMC-T6 | `2025` company-hosted Form `10-K` PDF | 2026-08-10 collected | Company-hosted filing PDF | Annual filing artifact preserved locally despite SEC shell blocking | `[Disclosed]` | [2025-form-10k-pdf.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2025-form-10k-pdf.pdf) |
| VMC-T7 | SEC filing URL note | 2026-08-10 verified | SEC URL note | Preserves the authoritative `10-K`, `10-Q`, and `8-K` URLs and documents the SEC automation challenge | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/vulcan-materials-company/sec-source-links.md) |
| VMC-T8 | `Q4 2025` earnings release | 2026-02-17 | Earnings release PDF | Provides quarter and full-year operating and financial results | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2025-q4-earnings-release.pdf) |
| VMC-T9 | `Q4 2025` supplemental information | 2026-02-17 | Earnings supplemental PDF | Adds unit-profitability and segment detail | `[Disclosed]` | [2025-q4-supplemental-information.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2025-q4-supplemental-information.pdf) |
| VMC-T10 | `Q1 2026` earnings release | 2026-04-29 | Earnings release PDF | Provides first-quarter results and demand commentary | `[Disclosed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2026-q1-earnings-release.pdf) |
| VMC-T11 | `Q1 2026` supplemental information | 2026-04-29 | Earnings supplemental PDF | Adds price, cost, and shipment detail | `[Disclosed]` | [2026-q1-supplemental-information.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2026-q1-supplemental-information.pdf) |
| VMC-T12 | `Q1 2026` company-hosted `10-Q` PDF | 2026-08-10 collected | Company-hosted filing PDF | Preserves the quarter filing locally when direct SEC shell fetch was blocked | `[Disclosed]` | [2026-q1-10q-company-hosted.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2026-q1-10q-company-hosted.pdf) |
| VMC-T13 | `Q2 2026` earnings release | 2026-07-29 | Earnings release PDF | Provides second-quarter results, pricing detail, and cost headwinds | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2026-q2-earnings-release.pdf) |
| VMC-T14 | `Q2 2026` supplemental information | 2026-07-29 | Earnings supplemental PDF | Adds unit economics and segment detail | `[Disclosed]` | [2026-q2-supplemental-information.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2026-q2-supplemental-information.pdf) |
| VMC-T15 | `Q2 2026` company-hosted `10-Q` PDF | 2026-08-10 collected | Company-hosted filing PDF | Preserves the latest quarter filing locally when direct SEC shell fetch was blocked | `[Disclosed]` | [2026-q2-10q-company-hosted.pdf](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/vulcan-materials-company/2026-q2-10q-company-hosted.pdf) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports is usable for source taxonomy here, but the working evidence set depends mainly on official Vulcan IR artifacts plus authoritative SEC URLs.
- Direct shell retrieval from SEC on `2026-08-10` returned the SEC automation challenge page rather than the filing content, so challenged HTML responses were discarded rather than stored as if they were valid filings.

## Missing evidence

- No standalone earnings-call transcript artifact saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No locally saved direct SEC HTML filings yet because the SEC blocked scripted fetches without a declared company-specific user agent.
