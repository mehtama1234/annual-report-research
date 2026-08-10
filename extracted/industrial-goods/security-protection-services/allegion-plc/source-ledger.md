# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| ALLE-T1 | AnnualReports.com Allegion company-page capture | 2026-08-10 | Aggregator company-page HTML | Confirms AnnualReports taxonomy and `2025` archive availability | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/security-protection-services/allegion-plc/company-page.html) |
| ALLE-T2 | AnnualReports.com Allegion verification note | 2026-08-10 | Aggregator verification note | Records the archive trail and taxonomy check | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/security-protection-services/allegion-plc/annualreports-verification.md) |
| ALLE-T3 | Allegion IR source-links note | 2026-08-10 | Official-source link ledger | Preserves the verified official annual and quarter artifact URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/ir-source-links.md) |
| ALLE-T4 | Allegion 2025 annual report PDF | 2026-08-10 collected | Annual report PDF | Official annual-report artifact for fiscal `2025` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2025-annual-report.pdf) |
| ALLE-T5 | Allegion 2025 Form 10-K PDF | 2026-08-10 collected | Filed annual report PDF | Filed annual report for fiscal `2025` | `[Filed]` | [2025-10k.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2025-10k.pdf) |
| ALLE-T6 | Allegion Q4 FY2025 results release | 2026-02-17 released / 2026-08-10 collected | Official IR PDF | Most direct local quarterly release artifact for late `2025` results | `[Disclosed]` | [2025-q4-results-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2025-q4-results-release.pdf) |
| ALLE-T7 | Allegion Q4 FY2025 earnings presentation | 2026-02-17 released / 2026-08-10 collected | Official IR PDF | Preserves the quarter framing and segment slides | `[Disclosed]` | [2025-q4-earnings-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2025-q4-earnings-presentation.pdf) |
| ALLE-T8 | Allegion Q1 2026 results release | 2026-04-28 released / 2026-08-10 collected | Official IR PDF | Most direct local quarterly release artifact for the quarter ended `2026-03-31` | `[Disclosed]` | [2026-q1-results-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2026-q1-results-release.pdf) |
| ALLE-T9 | Allegion Q1 2026 earnings presentation | 2026-04-28 released / 2026-08-10 collected | Official IR PDF | Preserves the quarter framing and segment slides | `[Disclosed]` | [2026-q1-earnings-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2026-q1-earnings-presentation.pdf) |
| ALLE-T10 | Allegion Q1 2026 Form 10-Q PDF | 2026-04-28 released / 2026-08-10 collected | Filed quarterly report PDF | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2026-q1-10q.pdf) |
| ALLE-T11 | Allegion Q2 2026 results release | 2026-07-23 released / 2026-08-10 collected | Official IR PDF | Most direct local quarterly release artifact for the quarter ended `2026-06-30` | `[Disclosed]` | [2026-q2-results-release.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2026-q2-results-release.pdf) |
| ALLE-T12 | Allegion Q2 2026 earnings presentation | 2026-07-23 released / 2026-08-10 collected | Official IR PDF | Preserves the latest quarter framing and segment slides | `[Disclosed]` | [2026-q2-earnings-presentation.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2026-q2-earnings-presentation.pdf) |
| ALLE-T13 | Allegion Q2 2026 Form 10-Q PDF | 2026-07-23 released / 2026-08-10 collected | Filed quarterly report PDF | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/security-protection-services/allegion-plc/2026-q2-10q.pdf) |
| ALLE-T14 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms SEC company identity and filing chronology when direct SEC filing-body retrieval is unstable | `[Filed]` | [submissions-cik0001579241.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/security-protection-services/allegion-plc/submissions-cik0001579241.json) |

## Reconciliation notes

- Allegion now has a clean annual-plus-quarterly evidence chain on disk for the `2025` annual package and the last three reported quarters as of Monday, `2026-08-10`.
- The official IR site exposes the annual report, results releases, presentations, and filed quarter-report PDFs directly, which makes the source chain stronger than several earlier protection-services names.
- Direct SEC filing-body HTML retrieval was still `403`-blocked in this shell environment, so the SEC side is preserved through the saved submissions JSON while the filed report PDFs are anchored from the official IR site.

## Missing evidence

- Local transcript artifacts for the `Q4 FY2025`, `Q1 2026`, and `Q2 2026` earnings calls.
- Direct saved SEC filing-body HTMLs for the in-scope `10-K` and `10-Q` chain.
