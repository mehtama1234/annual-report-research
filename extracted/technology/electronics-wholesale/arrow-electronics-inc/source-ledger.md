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
| ARW-T1 | AnnualReports company page | 2026-08-10 collected | Aggregator company page | Confirms taxonomy, sector, industry, and current hosted annual package | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/technology/electronics-wholesale/arrow-electronics-inc/company-page.html) |
| ARW-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents lane fit and authority hierarchy | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/technology/electronics-wholesale/arrow-electronics-inc/annualreports-verification.md) |
| ARW-T3 | IR source-links note | 2026-08-10 | Official IR URL map | Preserves official IR roots and retrieval constraints | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/technology/electronics-wholesale/arrow-electronics-inc/ir-source-links.md) |
| ARW-T4 | SEC source-links note | 2026-08-10 | Filing URL map | Preserves the authoritative annual and quarter filing chain | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/sec-source-links.md) |
| ARW-T5 | `2025` annual report PDF | 2026-08-10 collected | Annual report PDF | Core annual source for business model, network scale, and strategic framing | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/technology/electronics-wholesale/arrow-electronics-inc/2025-annual-report.pdf) |
| ARW-T6 | `2025` Form `10-K` | 2026-02-11 filed | Annual filing HTML | Authoritative annual filing for segment mix, risk, working capital, and liquidity | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2025-10k.html) |
| ARW-T7 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms filing dates, accession numbers, ticker, and CIK linkage | `[Filed]` | [submissions-cik0000007536.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/submissions-cik0000007536.json) |
| ARW-T8 | `Q4 2025` result release exhibit | 2026-02-05 filed | Earnings release exhibit | Preserves year-end metrics, segment detail, cash flow, and `Q1 2026` outlook | `[Filed]` | [2025-q4-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2025-q4-results-release.html) |
| ARW-T9 | `Q4 2025` result `8-K` | 2026-02-05 filed | Results filing HTML | Filed wrapper for the year-end results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2025-q4-8k.html) |
| ARW-T10 | `Q1 2026` result release exhibit | 2026-05-07 filed | Earnings release exhibit | Preserves first-quarter metrics, segment acceleration, and `Q2 2026` outlook | `[Filed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2026-q1-results-release.html) |
| ARW-T11 | `Q1 2026` result `8-K` | 2026-05-07 filed | Results filing HTML | Filed wrapper for first-quarter results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2026-q1-8k.html) |
| ARW-T12 | `Q1 2026` Form `10-Q` | 2026-05-07 filed | Quarterly filing HTML | Authoritative first-quarter filing with receivables, inventories, liquidity, and leverage detail | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2026-q1-10q.html) |
| ARW-T13 | `Q2 2026` result release exhibit | 2026-08-06 filed | Earnings release exhibit | Preserves latest-quarter metrics, segment divergence, cash flow, and `Q3 2026` outlook | `[Filed]` | [2026-q2-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2026-q2-results-release.html) |
| ARW-T14 | `Q2 2026` result `8-K` | 2026-08-06 filed | Results filing HTML | Filed wrapper for latest-quarter results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2026-q2-8k.html) |
| ARW-T15 | `Q2 2026` Form `10-Q` | 2026-08-06 filed | Quarterly filing HTML | Authoritative latest-quarter filing with first-half balance-sheet and working-capital detail | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/technology/electronics-wholesale/arrow-electronics-inc/2026-q2-10q.html) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- Arrow’s annual and quarter materials are standard domestic issuer filings: `10-K`, `10-Q`, and `8-K`.
- Direct shell retrieval of Arrow IR HTML pages returned `429`, so the local chain relies on the hosted annual report PDF, SEC filing bodies, SEC earnings-release exhibits, and preserved official IR URL notes.
- No separate official earnings-call transcript was collected for the in-scope quarters.

## Missing evidence

- No separate official earnings-call transcript was collected for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No Arrow IR HTML root pages were mirrored locally because the investor site rate-limited direct shell retrieval in this environment.
