# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| ICUI-T1 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Confirms the company page, `Healthcare` sector, `Medical Instruments & Supplies` industry label, and the fact that the AnnualReports annual package still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-equipment-wholesale/icu-medical-incorporated/annualreports-verification.md) |
| ICUI-T2 | ICU Medical IR source-links note | 2026-08-10 | Official-source link ledger | Preserves the official annual-reports, quarterly-results, and SEC-filings routes despite unstable local mirroring | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-equipment-wholesale/icu-medical-incorporated/ir-source-links.md) |
| ICUI-T3 | ICU Medical SEC source-links note | 2026-08-10 | SEC filing URL ledger | Preserves the authoritative annual and latest-three-quarters filing chain | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-equipment-wholesale/icu-medical-incorporated/sec-source-links.md) |
| ICUI-T4 | ICU Medical SEC submissions JSON | 2026-08-10 collected | SEC metadata JSON | Confirms filing dates, accession continuity, and issuer linkage | `[Filed]` | [submissions-cik0000883984.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-equipment-wholesale/icu-medical-incorporated/submissions-cik0000883984.json) |
| ICUI-T5 | ICU Medical `2025` annual report PDF | 2026-02-19 filed / 2026-08-10 collected | SEC-hosted annual report PDF | Preserves management framing, product mix, and annual operating context | `[Filed]` | [2025-ars.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-equipment-wholesale/icu-medical-incorporated/2025-ars.pdf) |
| ICUI-T6 | ICU Medical `2025` `10-K` | 2026-02-19 filed / 2026-08-10 collected | SEC filing HTML | Preserves route-to-market, liquidity, inventory, and annual financial detail | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-equipment-wholesale/icu-medical-incorporated/2025-10k.html) |
| ICUI-T7 | ICU Medical `Q4 2025` `8-K` and Exhibit `99.1` | 2026-02-19 filed / 2026-08-10 collected | SEC current-report chain | Preserves year-end results, annual product mix, and initial `2026` guidance framing | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-equipment-wholesale/icu-medical-incorporated/2025-q4-8k.html) |
| ICUI-T8 | ICU Medical `Q1 2026` `10-Q` and Exhibit `99.1` | 2026-05-07 filed / 2026-08-10 collected | SEC quarter-report chain | Preserves first-quarter organic-growth framing, cash flow, and divestiture-adjusted results | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-equipment-wholesale/icu-medical-incorporated/2026-q1-10q.html) |
| ICUI-T9 | ICU Medical `Q2 2026` `10-Q` and Exhibit `99.1` | 2026-08-06 filed / 2026-08-10 collected | SEC quarter-report chain | Preserves the latest quarter, margin improvement, and tariff-refund adjustment disclosure | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-equipment-wholesale/icu-medical-incorporated/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports classifies ICU Medical in `Medical Instruments & Supplies`, not in a literal wholesale label, but the company still answers the still-open provider-facing healthcare-channel gap because hospitals and distributors are the direct commercial counterparties for most of the product flow.
- The local packet path stays under `medical-equipment-wholesale` because the frontier need was a cleaner healthcare-channel extension next to `Astrana Health` and `Accendra Health`, not another generic medtech bucket.
- The evidence chain is SEC-heavy because the official IR HTML pages were unstable to mirror locally in this environment.

## Missing evidence

- No local official transcript artifacts are saved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No saved local official IR HTML mirrors beyond source-link notes are present because direct page retrieval was transport-fragile in this shell.
