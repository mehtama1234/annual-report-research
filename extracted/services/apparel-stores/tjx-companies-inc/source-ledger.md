# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| TJX-T1 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Records the live source taxonomy and the fact that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/raw/annualreports/services/apparel-stores/tjx-companies-inc/annualreports-verification.md) |
| TJX-T2 | AnnualReports shell capture | 2026-08-10 collected | Aggregator HTML snapshot | Preserves the imperfect local fetch outcome for the company page attempt | `[Reported]` | [company-page.html](/raw/annualreports/services/apparel-stores/tjx-companies-inc/company-page.html) |
| TJX-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the clean official result-page chain and the as-of-date quarter window | `[Disclosed]` | [official-ir-verification.md](/raw/company-ir/services/apparel-stores/tjx-companies-inc/official-ir-verification.md) |
| TJX-T4 | Investor relations overview page | 2026-08-10 collected | Official IR HTML snapshot | Confirms the company's high-level off-price framing, global footprint, and current IR navigation state | `[Disclosed]` | [overview.html](/raw/company-ir/services/apparel-stores/tjx-companies-inc/overview.html) |
| TJX-T5 | `Q1 FY27` results page | 2026-05-20 published / 2026-08-10 collected | Official results page HTML | Preserves the latest in-scope quarter narrative and guidance raise | `[Disclosed]` | [2026-q1-fy27-results.html](/raw/company-ir/services/apparel-stores/tjx-companies-inc/2026-q1-fy27-results.html) |
| TJX-T6 | `Q4 and full year FY26` results page | 2026-02-25 published / 2026-08-10 collected | Official results page HTML | Preserves the annual close, year-level numbers, and off-price market-share language | `[Disclosed]` | [2026-q4-fy26-results.html](/raw/company-ir/services/apparel-stores/tjx-companies-inc/2026-q4-fy26-results.html) |
| TJX-T7 | `Q3 FY26` results page | 2025-11-19 published / 2026-08-10 collected | Official results page HTML | Preserves the earlier quarter momentum and guidance raise before year-end | `[Disclosed]` | [2025-q3-fy26-results.html](/raw/company-ir/services/apparel-stores/tjx-companies-inc/2025-q3-fy26-results.html) |
| TJX-T8 | `Q2 FY27` report-date page | 2026-08-05 published / 2026-08-10 collected | Official announcement page HTML | Confirms that `Q2 FY27` was still future as of `2026-08-10` and should not be treated as reported | `[Disclosed]` | [2026-q2-fy27-report-date.html](/raw/company-ir/services/apparel-stores/tjx-companies-inc/2026-q2-fy27-report-date.html) |
| TJX-T9 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and filing sequence | `[Filed]` | [submissions-cik0000109198.json](/raw/sec/services/apparel-stores/tjx-companies-inc/submissions-cik0000109198.json) |
| TJX-T10 | SEC company facts file | 2026-08-10 collected | SEC XBRL facts JSON | Useful clean support for net income and cash figures in the annual-plus-quarter chain | `[Filed]` | [companyfacts-cik0000109198.json](/raw/sec/services/apparel-stores/tjx-companies-inc/companyfacts-cik0000109198.json) |
| TJX-T11 | Fiscal `2025` annual report PDF | 2026-04-30 filed / 2026-08-10 collected | SEC annual report PDF | Preserves the shareholder annual-report artifact for the year ended `2026-01-31` | `[Filed]` | [2025-annual-report.pdf](/raw/sec/services/apparel-stores/tjx-companies-inc/2025-annual-report.pdf) |
| TJX-T12 | Fiscal `2025` Form `10-K` | 2026-03-31 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for the year ended `2026-01-31` | `[Filed]` | [2025-10k.html](/raw/sec/services/apparel-stores/tjx-companies-inc/2025-10k.html) |
| TJX-T13 | `Q1 FY27` earnings `8-K` | 2026-05-20 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter fiscal `2027` results | `[Filed]` | [2026-q1-fy27-8k.html](/raw/sec/services/apparel-stores/tjx-companies-inc/2026-q1-fy27-8k.html) |
| TJX-T14 | `Q1 FY27` Form `10-Q` | 2026-05-29 filed / 2026-08-10 collected | SEC filing HTML | Filed first-quarter fiscal `2027` report | `[Filed]` | [2026-q1-fy27-10q.html](/raw/sec/services/apparel-stores/tjx-companies-inc/2026-q1-fy27-10q.html) |
| TJX-T15 | `Q4 FY26` earnings `8-K` | 2026-02-25 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year fiscal `2026` results | `[Filed]` | [2025-q4-fy26-8k.html](/raw/sec/services/apparel-stores/tjx-companies-inc/2025-q4-fy26-8k.html) |
| TJX-T16 | `Q3 FY26` earnings `8-K` | 2025-11-19 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for third-quarter fiscal `2026` results | `[Filed]` | [2025-q3-fy26-8k.html](/raw/sec/services/apparel-stores/tjx-companies-inc/2025-q3-fy26-8k.html) |
| TJX-T17 | `Q3 FY26` Form `10-Q` | 2025-12-02 filed / 2026-08-10 collected | SEC filing HTML | Filed third-quarter fiscal `2026` report | `[Filed]` | [2025-q3-fy26-10q.html](/raw/sec/services/apparel-stores/tjx-companies-inc/2025-q3-fy26-10q.html) |

## Reconciliation notes

- TJX now has a clean annual-plus-quarter source chain on disk for the fiscal `2025` annual package and the correct trailing-quarter window as of Monday, August 10, 2026.
- The quarter window is fiscal rather than calendar:
  - `Q1 FY27`
  - `Q4 FY26`
  - `Q3 FY26`
- AnnualReports remained useful for source taxonomy but lagged at `2024`.
- The official IR overview and direct news-release pages worked cleanly, but the menu-style annual-report and quarterly-results URLs under `investor.tjx.com/financial-information/` returned `Page Not Found` in shell collection.

## Missing evidence

- No standalone verbatim earnings-call transcript artifact is saved locally for the in-scope quarters.
- The local AnnualReports company-page HTML capture is not a reliable company-detail body, so the verification note records the live observed page state separately.
