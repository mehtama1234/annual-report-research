# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| GLW-T1 | AnnualReports.com Corning verification note | 2026-08-10 | Aggregator verification note | Confirms company identity, industry label, and the visible `2024` archive lag | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/communication-equipment/corning-inc/annualreports-verification.md) |
| GLW-T2 | AnnualReports.com company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves taxonomy, exchange, company description, and the visible most-recent archive package | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/communication-equipment/corning-inc/company-page.html) |
| GLW-T3 | Corning IR source-links note | 2026-08-10 | Official IR source note | Logs the official annual and quarter URLs used for the packet | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/communication-equipment/corning-inc/ir-source-links.md) |
| GLW-T4 | SEC filing-chain note | 2026-08-10 | SEC source note | Records the exact annual-plus-quarter SEC chain used in the packet | `[Filed]` | [sec-filing-chain.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/corning-inc/sec-filing-chain.md) |
| GLW-T5 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, fiscal year-end, and the exact annual-plus-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/communication-equipment/corning-inc/sec-submissions.json) |

## Reconciliation notes

- AnnualReports still lagged at `2024`, so it is useful for taxonomy confirmation but not for the controlling annual anchor.
- Because Corning's fiscal year ends on December 31, the correct annual anchor as of Monday, August 10, 2026 is the `2025` annual filing for the year ended `2025-12-31`.
- The latest three reported quarters as of `2026-08-10` are Q2 `2026`, Q1 `2026`, and Q4 `2025`.
- The quarter window is supported by official Corning earnings releases and by the exact SEC `10-K` / `10-Q` / `8-K` chain preserved in the saved submissions JSON and filing-chain note.
- Direct scripted retrieval of the SEC filing HTML and certain Corning IR artifacts was blocked or rate-limited from this environment, so the packet distinguishes between locally saved artifacts and externally verified official URLs.

## Missing evidence

- No local copy of the official annual-reports page HTML is saved because direct retrieval returned `429`.
- No local copy of the public `2025` Form `10-K` PDF is saved because direct retrieval returned `403`.
- No local copies of the official quarter release pages or transcripts are saved because direct retrieval became rate-limited after verification.
