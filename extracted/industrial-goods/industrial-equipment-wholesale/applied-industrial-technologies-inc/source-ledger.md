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
| AIT-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports company page | Confirms company identity and `Industrial Goods` taxonomy | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/company-page.html) |
| AIT-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents archive role and authority hierarchy | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/annualreports-verification.md) |
| AIT-T3 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves the annual-report and quarter-result URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/ir-source-links.md) |
| AIT-T4 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves the authoritative `10-K`, `10-Q`, and `8-K` exhibit references | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/sec-source-links.md) |
| AIT-T5 | `2025` annual report PDF | 2026-08-10 collected | Official annual report PDF | Provides the annual strategic frame, mix shift, and capital-allocation context | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/2025-annual-report.pdf) |
| AIT-T6 | SEC submissions file | 2026-08-10 collected | SEC metadata JSON | Confirms the correct filing chain for `CIK 0000109563` after replacing an earlier mistaken company capture | `[Filed]` | [submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/submissions.json) |
| AIT-T7 | Fiscal `Q1 2026` earnings release exhibit | 2025-10-28 | SEC `8-K` exhibit | Provides quarter headline metrics, guidance, and management commentary | `[Filed]` | verified via URL in [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/sec-source-links.md) |
| AIT-T8 | Fiscal `Q1 2026` Form `10-Q` | 2025-10-28 filed | SEC filing | Provides first-quarter filing support and detailed financial statements | `[Filed]` | verified via URL in [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/sec-source-links.md) |
| AIT-T9 | Fiscal `Q2 2026` earnings release exhibit | 2026-01-27 | SEC `8-K` exhibit | Provides quarter headline metrics, acquisition commentary, and dividend increase | `[Filed]` | verified via URL in [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/sec-source-links.md) |
| AIT-T10 | Fiscal `Q2 2026` Form `10-Q` | 2026-01-27 filed | SEC filing | Provides second-quarter filing support and detailed financial statements | `[Filed]` | verified via URL in [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/sec-source-links.md) |
| AIT-T11 | Fiscal `Q3 2026` earnings release exhibit | 2026-04-28 | SEC `8-K` exhibit | Provides latest-quarter headline metrics, buyback authorization, and raised guidance | `[Filed]` | verified via URL in [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/sec-source-links.md) |
| AIT-T12 | Fiscal `Q3 2026` Form `10-Q` | 2026-04-28 filed | SEC filing | Provides latest reported quarter filing support and balance-sheet context | `[Filed]` | verified via URL in [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-wholesale/applied-industrial-technologies-inc/sec-source-links.md) |

## Reconciliation notes

- Because Applied’s fiscal year ends on `June 30`, the correct latest three reported quarters as of `2026-08-10` are fiscal `Q3 2026`, fiscal `Q2 2026`, and fiscal `Q1 2026`.
- The annual packet is anchored to the `2025` annual report and `10-K` for the fiscal year ended `2025-06-30`.
- The local SEC submissions file originally contained the wrong issuer because `CIK 0000006951` belongs to Applied Materials; it was replaced with the correct `CIK 0000109563` submissions file on `2026-08-10`.
- Applied IR pages were useful for annual-report retrieval and link verification, but SEC quarter exhibits and `10-Q` filings provide the cleanest authoritative chain for the quarter window.

## Missing evidence

- No standalone earnings-call transcript artifact was saved locally for fiscal `Q1 2026`, fiscal `Q2 2026`, or fiscal `Q3 2026`.
- Direct shell preservation of SEC filing HTML was incomplete because later requests from the current environment hit SEC automation controls, so the packet relies on preserved filing URLs plus the locally saved submissions metadata and annual report PDF.
- The packet is still materially source-complete for the target annual plus trailing three-quarter window because the authoritative annual, release, and filing references are all preserved.
