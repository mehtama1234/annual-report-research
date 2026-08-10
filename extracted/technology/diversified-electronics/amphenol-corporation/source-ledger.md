# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| APH-T1 | AnnualReports.com verification note | 2026-08-10 | Aggregator verification note | Confirms `Diversified Electronics` taxonomy and current annual archive status | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/diversified-electronics/amphenol-corporation/annualreports-verification.md) |
| APH-T2 | AnnualReports.com company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves company identity, ticker, and live annual-report availability | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/diversified-electronics/amphenol-corporation/company-page.html) |
| APH-T3 | Official IR source-links note | 2026-08-10 | Official IR source note | Logs the official annual and quarter URLs and the Cloudflare access constraint | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/diversified-electronics/amphenol-corporation/ir-source-links.md) |
| APH-T4 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, annual-plus-quarter filing sequence, and fiscal year-end | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/sec-submissions.json) |
| APH-T5 | FY2025 Form `10-K` | 2026-02-11 filed / 2026-08-10 collected | SEC filing HTML | Authoritative annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2025-10k.html) |
| APH-T6 | FY2025 Q4 earnings `8-K` | 2026-01-28 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the year-end release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2025-q4-8k.html) |
| APH-T7 | FY2025 Q4 earnings exhibit `99.1` | 2026-01-28 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the full-year `2025` and quarter-end operating narrative and figures | `[Filed]` | [2025-q4-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2025-q4-ex99.html) |
| APH-T8 | FY2026 Q1 earnings `8-K` | 2026-04-29 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the first-quarter release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2026-q1-8k.html) |
| APH-T9 | FY2026 Q1 earnings exhibit `99.1` | 2026-04-29 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the first-quarter operating narrative and figures | `[Filed]` | [2026-q1-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2026-q1-ex99.html) |
| APH-T10 | FY2026 Q1 Form `10-Q` | 2026-05-01 filed / 2026-08-10 collected | SEC filing HTML | Authoritative quarter filing for the period ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2026-q1-10q.html) |
| APH-T11 | FY2026 Q2 earnings `8-K` | 2026-07-29 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the latest reported quarter as of `2026-08-10` | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2026-q2-8k.html) |
| APH-T12 | FY2026 Q2 earnings exhibit `99.1` | 2026-07-29 filed / 2026-08-10 collected | SEC exhibit HTML | Preserves the latest reported-quarter narrative around IT datacom, acquisitions, tariffs, and signal integrity | `[Filed]` | [2026-q2-ex99.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2026-q2-ex99.html) |
| APH-T13 | FY2026 Q2 Form `10-Q` | 2026-07-31 filed / 2026-08-10 collected | SEC filing HTML | Authoritative quarter filing for the period ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-electronics/amphenol-corporation/2026-q2-10q.html) |

## Reconciliation notes

- As of Monday, August 10, 2026, the latest three reported quarters are FY2026 `Q2`, FY2026 `Q1`, and FY2025 `Q4`. The latest earnings release in the official IR chain was dated `2026-07-29`.
- AnnualReports.com was used for taxonomy and archive confirmation. SEC and official IR URLs were used as the authoritative chain whenever local direct IR fetches were blocked.
- The fiscal `2025` annual anchor is the year ended `2025-12-31`, filed on `2026-02-11`.

## Missing evidence

- No locally saved official IR HTML page was preserved for the annual-report archive or earnings-release pages because direct terminal fetches on `2026-08-10` returned Cloudflare challenge pages.
- No locally saved standalone transcript artifact is preserved for FY2025 `Q4`, FY2026 `Q1`, or FY2026 `Q2`.
