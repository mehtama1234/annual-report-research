# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| GIC-T1 | AnnualReports company page | 2026-08-10 | Aggregator page | Confirms `Wholesale, Other` taxonomy and company description | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/wholesale-other/global-industrial-company/company-page.html) |
| GIC-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Normalizes the taxonomy and lag observation into repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/wholesale-other/global-industrial-company/annualreports-verification.md) |
| GIC-T3 | Global Industrial IR source-links note | 2026-08-10 | Official-source link ledger | Preserves the official IR root used and the retrieval-block note | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/wholesale-other/global-industrial-company/ir-source-links.md) |
| GIC-T4 | Global Industrial SEC source-links note | 2026-08-10 | SEC filing URL ledger | Preserves the exact annual and quarter filing URLs used for the packet | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/sec-source-links.md) |
| GIC-T5 | SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Verifies filing dates, accession numbers, CIK, and the required quarter chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/sec-submissions.json) |
| GIC-T6 | Global Industrial `2025` annual report PDF | 2026-04-22 filed / 2026-08-10 collected | SEC ARS PDF | Official annual report artifact for fiscal `2025` | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2025-annual-report.pdf) |
| GIC-T7 | Global Industrial `2025` Form `10-K` | 2026-02-27 filed / 2026-08-10 collected | SEC filing HTML | Filed annual report for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2025-10k.html) |
| GIC-T8 | Global Industrial Q4 `2025` earnings-release exhibit | 2026-02-24 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for late-`2025` results and full-year read | `[Filed]` | [2025-q4-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2025-q4-results-release.html) |
| GIC-T9 | Global Industrial Q4 `2025` earnings `8-K` | 2026-02-24 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the late-`2025` release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2025-q4-8k.html) |
| GIC-T10 | Global Industrial Q1 `2026` earnings-release exhibit | 2026-05-05 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2026-q1-results-release.html) |
| GIC-T11 | Global Industrial Q1 `2026` earnings `8-K` | 2026-05-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q1 `2026` release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2026-q1-8k.html) |
| GIC-T12 | Global Industrial Q1 `2026` Form `10-Q` | 2026-05-05 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2026-q1-10q.html) |
| GIC-T13 | Global Industrial Q2 `2026` earnings-release exhibit | 2026-08-04 filed / 2026-08-10 collected | SEC exhibit HTML | Filed release text for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-results-release.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2026-q2-results-release.html) |
| GIC-T14 | Global Industrial Q2 `2026` earnings `8-K` | 2026-08-04 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for the Q2 `2026` release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2026-q2-8k.html) |
| GIC-T15 | Global Industrial Q2 `2026` Form `10-Q` | 2026-08-04 filed / 2026-08-10 collected | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/wholesale-other/global-industrial-company/2026-q2-10q.html) |

## Reconciliation notes

- Global Industrial now has a coherent annual-plus-quarter filing chain for the required `2025` annual package and the last three reported quarters as of `2026-08-10`.
- AnnualReports still lagged at `2024`, so the `2025` annual package is intentionally anchored to the SEC `ARS` and `10-K` chain.
- The quarter set uses the filed earnings `8-K` wrappers, filed release exhibits, and filed `10-Q` documents because the official investor-relations host returned a browser challenge during this pass.
- Q2 `2026` results include a one-time tariff-refund benefit tied to `IEEPA` tariffs paid in `2025`, so any margin comparison should normalize that item rather than treat the reported `40.2%` gross margin as steady-state operating structure.

## Missing evidence

- No local earnings-call transcript artifacts are saved.
- No mirrored IR HTML pages are saved because the official IR host was challenge-blocked in this shell environment.
