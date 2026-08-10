# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| HSIC-T1 | AnnualReports lag verification | 2026-08-10 | Aggregator verification note | Confirms AnnualReports still lagged at the `2024` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-instruments-supplies/henry-schein-inc/annualreports-verification.md) |
| HSIC-T2 | Henry Schein IR source-links note | 2026-08-10 | Official-source link ledger | Preserves the annual report, release pages, quarterly-results page, and transcript URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/henry-schein-inc/ir-source-links.md) |
| HSIC-T3 | Henry Schein 2025 annual report PDF | 2026-08-10 collected | Annual report PDF | Official annual-report artifact for fiscal `2025` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/henry-schein-inc/2025-annual-report.pdf) |
| HSIC-T4 | Henry Schein Q4 2025 results release | 2026-02-24 released | Official IR release page | Preserves late-`2025` results, 2026 guidance, and segment detail | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/henry-schein-inc/ir-source-links.md) |
| HSIC-T5 | Henry Schein Q1 2026 results release | 2026-05-05 released | Official IR release page | Preserves first-quarter growth, mix, and guidance reaffirmation | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/henry-schein-inc/ir-source-links.md) |
| HSIC-T6 | Henry Schein Q2 2026 results release | 2026-08-04 released | Official IR release page | Preserves second-quarter strength, updated guidance, and current mix detail | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/henry-schein-inc/ir-source-links.md) |
| HSIC-T7 | Henry Schein Q2 2026 earnings presentation | 2026-08-04 collected | Official IR PDF | Gives current quarter framing and supporting summary detail | `[Disclosed]` | [2026-q2-earnings-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/henry-schein-inc/2026-q2-earnings-presentation.pdf) |
| HSIC-T8 | Henry Schein Q2 2026 earnings call transcript | 2026-08-04 collected | Official transcript PDF | Preserves direct management commentary for the latest quarter | `[Disclosed]` | [2026-q2-earnings-call-transcript.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/henry-schein-inc/2026-q2-earnings-call-transcript.pdf) |
| HSIC-T9 | Henry Schein SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms filing dates, accession numbers, SIC classification, and recent document names | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/henry-schein-inc/sec-submissions.json) |
| HSIC-T10 | Henry Schein SEC source-links note | 2026-08-10 | SEC filing URL ledger | Preserves the exact 10-K, 10-Q, and 8-K URLs after direct shell retrieval was blocked | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/henry-schein-inc/sec-source-links.md) |

## Reconciliation notes

- Henry Schein now has a coherent annual-plus-quarterly evidence base for CLI 8 even though two retrieval paths were imperfect.
- AnnualReports lagged at `2024`, so the `2025` annual package had to come from the official company annual-reports page.
- Direct shell retrieval of SEC filing HTMLs was blocked by SEC automated-tool controls. The authoritative filing URLs and accession chain are therefore preserved through `sec-submissions.json` plus `sec-source-links.md`.
- This packet is still strong because the official company annual report, all three official quarter release pages, the Q2 earnings presentation, the Q2 transcript, and the SEC metadata chain are all in place.

## Missing evidence

- Local standalone Q4 `2025` and Q1 `2026` transcript files are not yet saved.
- Direct SEC filing-body HTML artifacts were blocked in the shell and are preserved as authoritative URLs rather than as full local filing copies.
