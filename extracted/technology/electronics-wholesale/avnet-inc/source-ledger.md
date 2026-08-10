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
| AVT-T1 | AnnualReports company page | 2026-08-10 collected | Aggregator company page | Confirms taxonomy, sector, industry, and hosted annual package | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/technology/electronics-wholesale/avnet-inc/company-page.html) |
| AVT-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents lane fit and authority hierarchy | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/technology/electronics-wholesale/avnet-inc/annualreports-verification.md) |
| AVT-T3 | IR source-links note | 2026-08-10 | Official IR URL map | Preserves official annual and quarter source chain | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/technology/electronics-wholesale/avnet-inc/ir-source-links.md) |
| AVT-T4 | SEC source-links note | 2026-08-10 | Filing URL map | Preserves authoritative annual and quarter chronology | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/avnet-inc/sec-source-links.md) |
| AVT-T5 | `2025` annual report PDF | 2026-08-10 collected | Annual report PDF | Core annual source for business model, segment mix, and strategic framing | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/technology/electronics-wholesale/avnet-inc/2025-annual-report.pdf) |
| AVT-T6 | `2025` Form `10-K` | 2025-08-15 filed | Annual filing HTML | Authoritative annual filing for segment economics, risk, and working capital | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/avnet-inc/2025-10k.html) |
| AVT-T7 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms filing dates, accession numbers, ticker, and CIK linkage | `[Filed]` | [submissions-cik0000008858.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/avnet-inc/submissions-cik0000008858.json) |
| AVT-T8 | `Q2 FY2026` results page | 2026-01-28 published | Official IR results page | Preserves growth rebound, segment detail, cash flow, and margin trajectory | `[Disclosed]` | [2026-q2-results.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/technology/electronics-wholesale/avnet-inc/2026-q2-results.html) |
| AVT-T9 | `Q2 FY2026` results `8-K` | 2026-01-28 filed | Results filing HTML | Filed wrapper for second-quarter results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/avnet-inc/2026-q2-8k.html) |
| AVT-T10 | `Q2 FY2026` Form `10-Q` | 2026-01-30 filed | Quarterly filing HTML | Authoritative second-quarter filing with inventories, receivables, and liquidity detail | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/avnet-inc/2026-q2-10q.html) |
| AVT-T11 | `Q3 FY2026` results page | 2026-04-29 published | Official IR results page | Preserves acceleration, return on working capital improvement, and regional breadth | `[Disclosed]` | [2026-q3-results.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/technology/electronics-wholesale/avnet-inc/2026-q3-results.html) |
| AVT-T12 | `Q3 FY2026` results `8-K` | 2026-04-29 filed | Results filing HTML | Filed wrapper for third-quarter results | `[Filed]` | [2026-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/avnet-inc/2026-q3-8k.html) |
| AVT-T13 | `Q3 FY2026` Form `10-Q` | 2026-05-01 filed | Quarterly filing HTML | Authoritative third-quarter filing with balance-sheet and working-capital detail | `[Filed]` | [2026-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/avnet-inc/2026-q3-10q.html) |
| AVT-T14 | `Q4 FY2026` results page | 2026-08-05 published | Official IR results page | Preserves record quarterly sales, fiscal `2026` full-year summary, and inventory-days improvement | `[Disclosed]` | [2026-q4-results.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/technology/electronics-wholesale/avnet-inc/2026-q4-results.html) |
| AVT-T15 | `Q4 FY2026` results `8-K` | 2026-08-05 filed | Results filing HTML | Filed wrapper for latest-quarter and fiscal-year-end results | `[Filed]` | [2026-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/avnet-inc/2026-q4-8k.html) |

## Reconciliation notes

- The correct trailing-quarter set as of Monday, 2026-08-10 is `Q4 FY2026`, `Q3 FY2026`, and `Q2 FY2026`.
- The latest quarter is represented by the filed `8-K` results release because the year-end `10-K` was not yet due as of 2026-08-10.
- Avnet’s annual and quarter materials were available through both official IR and SEC paths, which makes this one of the cleaner CLI 8 evidence chains.
- No separate official earnings-call transcript was collected for the in-scope quarters.

## Missing evidence

- No separate official earnings-call transcript was collected for `Q2 FY2026`, `Q3 FY2026`, or `Q4 FY2026`.
- The fiscal `2026` year-end `10-K` was not yet due as of Monday, 2026-08-10, so the latest-quarter filing chain ends with the filed `8-K`.
