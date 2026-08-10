# Source Ledger

Date baseline: 2026-08-09

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| AWK-T1 | AnnualReports.com verification note | 2026-08-09 | Aggregator metadata note | Confirms American Water is classified as `Utilities / Water Utilities` and that AnnualReports exposes the `2025 Annual Report and Form 10K` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/utilities/water-utilities/american-water-works-company-inc/annualreports-verification.md) |
| AWK-T2 | American Water official IR verification note | 2026-08-09 | Official IR verification note | Confirms the company identity and current official annual-report, quarterly-results, and event-page stack | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/utilities/water-utilities/american-water-works-company-inc/official-ir-verification.md) |
| AWK-T3 | American Water `2025` annual report PDF | 2026-02-18 | Annual report PDF | Core annual-report artifact for the year ended `2025-12-31` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/utilities/water-utilities/american-water-works-company-inc/2025-annual-report.pdf) |
| AWK-T4 | American Water SEC submissions JSON | 2026-08-09 | SEC index JSON | Verifies legal name, ticker, exchange, fiscal year-end, and the in-scope `10-K`, `10-Q`, and `8-K` filing dates and accession numbers | `[Filed]` | [submissions-cik0001410636.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/utilities/water-utilities/american-water-works-company-inc/submissions-cik0001410636.json) |
| AWK-T5 | American Water Q4 `2025` results release verification note | 2026-08-09 | Official results note | Captures the browser-verified year-end release facts and guidance framing after shell fetches hit a Cloudflare challenge page | `[Disclosed]` | [2025-q4-results-release-note.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/utilities/water-utilities/american-water-works-company-inc/2025-q4-results-release-note.md) |
| AWK-T6 | American Water Q4 `2025` earnings presentation | 2026-02-19 | Presentation PDF | Provides the year-end investor deck and capital-growth framing | `[Disclosed]` | [2025-q4-earnings-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/utilities/water-utilities/american-water-works-company-inc/2025-q4-earnings-presentation.pdf) |
| AWK-T7 | American Water Q1 `2026` results release verification note | 2026-08-09 | Official results note | Captures the browser-verified Q1 `2026` release facts after shell fetches hit a Cloudflare challenge page | `[Disclosed]` | [2026-q1-results-release-note.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/utilities/water-utilities/american-water-works-company-inc/2026-q1-results-release-note.md) |
| AWK-T8 | American Water Q1 `2026` earnings presentation | 2026-04-30 | Presentation PDF | Provides the Q1 `2026` investor deck and current capital / regulatory framing | `[Disclosed]` | [2026-q1-earnings-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/utilities/water-utilities/american-water-works-company-inc/2026-q1-earnings-presentation.pdf) |
| AWK-T9 | American Water Q2 `2026` results release verification note | 2026-08-09 | Official results note | Captures the browser-verified Q2 `2026` release facts after shell fetches hit a Cloudflare challenge page | `[Disclosed]` | [2026-q2-results-release-note.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/utilities/water-utilities/american-water-works-company-inc/2026-q2-results-release-note.md) |
| AWK-T10 | American Water Q2 `2026` earnings presentation | 2026-07-30 | Presentation PDF | Provides the most recent quarter slide deck and current acquisition / capital framing | `[Disclosed]` | [2026-q2-earnings-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/utilities/water-utilities/american-water-works-company-inc/2026-q2-earnings-presentation.pdf) |

## Reconciliation notes

- American Water has a clean official evidence chain for the current scope:
  - `2025` annual report PDF
  - Q4 `2025` release note and presentation
  - Q1 `2026` release note and presentation
  - Q2 `2026` release note and presentation
- SEC filing dates and accession numbers were verified through the official submissions JSON:
  - `2025` `10-K`: filed `2026-02-18`, accession `0001410636-26-000034`
  - Q4 `2025` earnings `8-K`: filed `2026-02-18`, accession `0001410636-26-000035`
  - Q1 `2026` `10-Q`: filed `2026-04-29`, accession `0001410636-26-000063`
  - Q1 `2026` earnings `8-K`: filed `2026-04-29`, accession `0001410636-26-000064`
  - Q2 `2026` `10-Q`: filed `2026-07-29`, accession `0001410636-26-000120`
  - Q2 `2026` earnings `8-K`: filed `2026-07-29`, accession `0001410636-26-000121`
- Direct shell fetches of the main IR HTML pages and release pages returned Cloudflare challenge pages, so the local release artifacts are verification notes rather than clean page captures.
- Direct SEC archive fetches from this shell returned the SEC automated-tool policy page for filing-content HTML, so the filing chain is treated as verified through submissions metadata rather than collected filing-content HTML.

## Missing evidence

- No standalone earnings-call transcript artifact is saved locally for the latest quarter.
- No standalone SEC filing-content HTML or PDF artifact is saved locally beyond the verified submissions JSON accession chain.
