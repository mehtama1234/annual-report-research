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
| MLI-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports company page | Confirms `Industrials` / `Metal Fabrication` taxonomy and AnnualReports lag | `[Reported]` | [company-page.html](/raw/annualreports/industrials/metal-fabrication/mueller-industries-inc/company-page.html) |
| MLI-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents AnnualReports lag and taxonomy use | `[Reported]` | [annualreports-verification.md](/raw/annualreports/industrials/metal-fabrication/mueller-industries-inc/annualreports-verification.md) |
| MLI-T3 | Financial results page | 2026-08-10 collected | Investor relations page HTML | Confirms the official annual and quarter stack | `[Disclosed]` | [financial-results.html](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/financial-results.html) |
| MLI-T4 | SEC filings page | 2026-08-10 collected | Investor relations page HTML | Confirms the latest filing stack and filing dates | `[Disclosed]` | [sec-filings.html](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/sec-filings.html) |
| MLI-T5 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves annual-report, quarter, and filing URLs | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/ir-source-links.md) |
| MLI-T6 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves direct SEC `10-K`, `10-Q`, and earnings `8-K` references | `[Filed]` | [sec-source-links.md](/raw/sec/industrials/metal-fabrication/mueller-industries-inc/sec-source-links.md) |
| MLI-T7 | `2025` annual report booklet PDF | 2026-08-10 collected | Annual report booklet PDF | Adds shareholder-letter framing, capital allocation, and strategic-plan context | `[Disclosed]` | [2025-annual-report.pdf](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/2025-annual-report.pdf) |
| MLI-T8 | `2025` company-hosted Form `10-K` PDF | 2026-08-10 collected | Company-hosted filing PDF | Core annual narrative, segment shape, and financial statements | `[Disclosed]` | [2025-10k-company-hosted.pdf](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/2025-10k-company-hosted.pdf) |
| MLI-T9 | `Q4 2025` earnings release | 2026-02-03 | Earnings release PDF | Provides fourth-quarter and full-year 2025 financial results and management commentary | `[Disclosed]` | [2025-q4-earnings-release.pdf](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/2025-q4-earnings-release.pdf) |
| MLI-T10 | `Q1 2026` earnings release | 2026-04-21 | Earnings release PDF | Provides first-quarter 2026 results and demand commentary | `[Disclosed]` | [2026-q1-earnings-release.pdf](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/2026-q1-earnings-release.pdf) |
| MLI-T11 | `Q1 2026` company-hosted `10-Q` PDF | 2026-08-10 collected | Company-hosted filing PDF | Preserves the first-quarter filing locally | `[Disclosed]` | [2026-q1-10q-company-hosted.pdf](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/2026-q1-10q-company-hosted.pdf) |
| MLI-T12 | `Q2 2026` earnings release | 2026-07-21 | Earnings release PDF | Provides second-quarter 2026 results, demand trends, and acquisition commentary | `[Disclosed]` | [2026-q2-earnings-release.pdf](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/2026-q2-earnings-release.pdf) |
| MLI-T13 | `Q2 2026` company-hosted `10-Q` PDF | 2026-08-10 collected | Company-hosted filing PDF | Preserves the latest quarter filing locally | `[Disclosed]` | [2026-q2-10q-company-hosted.pdf](/raw/company-ir/industrials/metal-fabrication/mueller-industries-inc/2026-q2-10q-company-hosted.pdf) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports is usable for source taxonomy here, but the main evidence set is official Mueller IR material plus direct SEC filing references.
- `2026` quarter earnings per share and share-count comparisons require care because the two-for-one stock split took effect on `2026-06-30`, and quarter releases note that diluted EPS and dividends per share were adjusted retroactively.
- Quarter profitability includes event noise such as the `Q1 2026` Sherwood sale gain and the prior-period insurance gain recognized in `Q2 2025`, so the packet interprets both reported and underlying operating patterns.

## Missing evidence

- No standalone earnings-call transcript artifact was identified or saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
