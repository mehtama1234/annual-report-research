# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| MSI-T1 | AnnualReports.com Motorola Solutions verification note | 2026-08-10 | Aggregator verification note | Confirms taxonomy and shows AnnualReports lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/annualreports/technology/diversified-communication-services/motorola-solutions-inc/annualreports-verification.md) |
| MSI-T2 | Motorola Solutions AnnualReports company page | 2026-08-10 | Aggregator page capture | Preserves the archive confirmation page | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/annualreports/technology/diversified-communication-services/motorola-solutions-inc/company-page.html) |
| MSI-T3 | Motorola Solutions IR source links note | 2026-08-10 | Official IR link map | Captures the annual and quarterly investor entry points | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/ir-source-links.md) |
| MSI-T4 | Motorola Solutions investors home | 2026-08-10 | Official IR page | Confirms the live investor-relations surface | `[Disclosed]` | [investors-home.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/investors-home.html) |
| MSI-T5 | Motorola Solutions earnings and SEC filings page | 2026-08-10 | Official IR page | Confirms the quarterly results, transcript, and filing archive | `[Disclosed]` | [earnings-and-sec-filings.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/earnings-and-sec-filings.html) |
| MSI-T6 | Motorola Solutions 2025 10-K PDF | 2026-02-12 | Annual filing PDF | Official company-hosted annual filing artifact | `[Disclosed]` | [2025-10k.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/2025-10k.pdf) |
| MSI-T7 | Motorola Solutions Q4 2025 earnings release PDF | 2026-02-13 | Earnings release PDF | Preserves the year-end sales, backlog, and cash-flow discussion | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/2025-q4-earnings-release.pdf) |
| MSI-T8 | Motorola Solutions Q4 2025 transcript PDF | 2026-02-13 | Transcript PDF | Preserves management discussion for the annual close | `[Disclosed]` | [2025-q4-earnings-call-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/2025-q4-earnings-call-transcript.pdf) |
| MSI-T9 | Motorola Solutions Q1 2026 earnings release PDF | 2026-05-01 | Earnings release PDF | Preserves record-orders and software-services growth discussion | `[Disclosed]` | [2026-q1-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/2026-q1-earnings-release.pdf) |
| MSI-T10 | Motorola Solutions Q1 2026 transcript PDF | 2026-05-01 | Transcript PDF | Preserves management discussion for the first quarter | `[Disclosed]` | [2026-q1-earnings-call-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/2026-q1-earnings-call-transcript.pdf) |
| MSI-T11 | Motorola Solutions Q2 2026 earnings release PDF | 2026-08-05 | Earnings release PDF | Preserves the latest-quarter D-Fend acquisition and raised-guidance discussion | `[Disclosed]` | [2026-q2-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/company-ir/technology/diversified-communication-services/motorola-solutions-inc/2026-q2-earnings-release.pdf) |
| MSI-T12 | Motorola Solutions SEC submissions JSON | 2026-08-10 | SEC index JSON | Verifies legal name, ticker, exchange, fiscal year-end, and filing dates | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer-imported-2026-08-10/raw/sec/technology/diversified-communication-services/motorola-solutions-inc/sec-submissions.json) |

## Reconciliation notes

- Motorola Solutions' saved evidence chain is local, but it currently lives in an imported raw workspace rather than the current repo raw tree.
- The chain is complete for the required window:
  - `2025` annual filing PDF, Q4 `2025` release, and Q4 transcript
  - Q1 `2026` release, Q1 transcript, and Q1 `10-Q`
  - Q2 `2026` release and Q2 `10-Q`
- The SEC submissions JSON is present locally; the packet's quarter filing authority is otherwise largely preserved through the company-IR PDF chain.

## Missing evidence

- The raw evidence has not been reintegrated into the current repo raw tree; the saved proof still lives in the imported raw workspace referenced by the packet's raw links.
- No local Q2 `2026` transcript was saved.
