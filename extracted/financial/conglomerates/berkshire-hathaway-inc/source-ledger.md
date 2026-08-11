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
| BRK-T1 | AnnualReports verification note for Berkshire | 2026-08-10 | Aggregator verification note | Confirms `2025` annual availability and records that AnnualReports taxonomy is narrower than the CLI 6 use case | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/conglomerates/conglomerates/berkshire-hathaway-inc/annualreports-verification.md) |
| BRK-T2 | Berkshire IR source-links note | 2026-08-10 | Official-link verification note | Records official reports-hub links, quarter-report PDFs, and the verified `1Q26` SEC accession | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/conglomerates/conglomerates/berkshire-hathaway-inc/ir-source-links.md) |
| BRK-T3 | Berkshire reports-page snapshot | 2026-08-10 | Official IR page snapshot | Confirms the official Berkshire reports hub | `[Disclosed]` | [reports-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/conglomerates/conglomerates/berkshire-hathaway-inc/reports-page.html) |
| BRK-T4 | Berkshire 2025 annual report PDF | 2026-02-22 | Annual report PDF | Full annual report package for the year ended `2025-12-31` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/conglomerates/conglomerates/berkshire-hathaway-inc/2025-annual-report.pdf) |
| BRK-T5 | Berkshire 2025 Form 10-K | 2026-02-26 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/berkshire-hathaway-inc/2025-10k.html) |
| BRK-T6 | Berkshire Q4 2025 / full-year earnings release PDF | 2026-02-28 | IR earnings release PDF | Exact fourth-quarter and full-year `2025` metrics plus operating-earnings framing | `[Disclosed]` | [2025-q4-earnings-release.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/conglomerates/conglomerates/berkshire-hathaway-inc/2025-q4-earnings-release.pdf) |
| BRK-T7 | Berkshire Q1 2026 quarterly report PDF | 2026-05-03 | Company-posted quarterly report PDF | Primary local quarter artifact for `1Q26` | `[Disclosed]` | [2026-q1-quarterly-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/conglomerates/conglomerates/berkshire-hathaway-inc/2026-q1-quarterly-report.pdf) |
| BRK-T8 | Berkshire Q2 2026 quarterly report PDF | 2026-08-08 | Company-posted quarterly report PDF | Primary local quarter artifact for `2Q26` | `[Disclosed]` | [2026-q2-quarterly-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/conglomerates/conglomerates/berkshire-hathaway-inc/2026-q2-quarterly-report.pdf) |
| BRK-T9 | Berkshire SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the saved annual filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/berkshire-hathaway-inc/sec-submissions.json) |

## Reconciliation notes

- AnnualReports is used here for archive confirmation only. It showed `2025` as the most recent annual report when checked on Monday, `2026-08-10`, but its taxonomy still centers Berkshire in `Property & Casualty Insurance`.
- The correct trailing-quarter set as of `2026-08-10` is `2Q26`, `1Q26`, and `4Q25`.
- Berkshire's local evidence chain is company-report-first rather than SEC-first for the most recent quarters. The official Berkshire quarterly report PDFs were saved locally, while the live SEC retrieval path was incomplete or blocked for the current quarter chain.

## Missing evidence

- No local SEC HTML filing was saved for `1Q26` despite a verified accession.
- No clean local SEC HTML filing was saved for `2Q26` in this workspace.
- No local prepared remarks or full earnings-call transcript capture was collected for `4Q25`, `1Q26`, or `2Q26`.
