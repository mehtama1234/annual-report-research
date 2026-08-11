# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| GLW-T1 | AnnualReports.com Corning verification note | 2026-08-10 | Aggregator verification note | Confirms Corning taxonomy and shows AnnualReports lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/annualreports/technology/communication-equipment/corning-incorporated/annualreports-verification.md) |
| GLW-T2 | Corning AnnualReports company page | 2026-08-10 | Aggregator page capture | Preserves the archive confirmation page | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/annualreports/technology/communication-equipment/corning-incorporated/company-page.html) |
| GLW-T3 | Corning IR source links note | 2026-08-10 | Official IR link map | Captures the verified annual and quarterly IR URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/communication-equipment/corning-incorporated/ir-source-links.md) |
| GLW-T4 | Corning SEC submissions JSON | 2026-08-10 | SEC index JSON | Verifies legal name, ticker, exchange, fiscal year-end, and the filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/sec-submissions.json) |
| GLW-T5 | Corning 2025 10-K HTML | 2026-01-28 | Annual filing HTML | Official annual filing for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/2025-10k.html) |
| GLW-T6 | Corning Q4 2025 8-K HTML | 2026-01-28 | Current-report HTML | Official SEC wrapper for the year-end release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/2025-q4-8k.html) |
| GLW-T7 | Corning Q1 2026 10-Q HTML | 2026-04-28 | Quarterly filing HTML | Official first-quarter filing in scope | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/2026-q1-10q.html) |
| GLW-T8 | Corning Q1 2026 8-K HTML | 2026-04-28 | Current-report HTML | Official SEC wrapper for the first-quarter release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/2026-q1-8k.html) |
| GLW-T9 | Corning Q1 2026 earnings exhibit HTML | 2026-04-28 | Earnings exhibit HTML | Preserves the first-quarter optical-communications growth details | `[Filed]` | [2026-q1-earnings-ex99-1.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/2026-q1-earnings-ex99-1.html) |
| GLW-T10 | Corning Q2 2026 10-Q HTML | 2026-07-28 | Quarterly filing HTML | Official latest-quarter filing in scope | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/2026-q2-10q.html) |
| GLW-T11 | Corning Q2 2026 8-K HTML | 2026-07-28 | Current-report HTML | Official SEC wrapper for the latest-quarter release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/2026-q2-8k.html) |
| GLW-T12 | Corning Q2 2026 earnings exhibit HTML | 2026-07-28 | Earnings exhibit HTML | Preserves the latest-quarter Amazon and NVIDIA agreement discussion | `[Filed]` | [2026-q2-earnings-ex99.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/communication-equipment/corning-incorporated/2026-q2-earnings-ex99.html) |

## Reconciliation notes

- Corning's saved evidence chain is local, but it currently lives in an imported raw workspace rather than the current repo raw tree.
- The chain is complete for the required window:
  - `2025` `10-K` and Q4 `2025` `8-K`
  - Q1 `2026` `10-Q`, `8-K`, and earnings exhibit
  - Q2 `2026` `10-Q`, `8-K`, and earnings exhibit
- Direct shell-side IR capture was challenge-limited, so the ledger relies on the verified IR source-links note plus the SEC filing chain.

## Missing evidence

- The raw evidence has not been reintegrated into the current repo raw tree; the saved proof still lives in the imported raw workspace referenced by the packet's raw links.
- No local transcript was saved for the covered quarters.
