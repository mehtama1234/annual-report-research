# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| DXCM-T1 | AnnualReports.com DexCom verification note | 2026-08-10 | Aggregator verification note | Confirms source taxonomy and that AnnualReports still lagged at the `2024` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/healthcare/medical-instruments-supplies/dexcom-inc/annualreports-verification.md) |
| DXCM-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the company-page evidence used for taxonomy and archive confirmation | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/healthcare/medical-instruments-supplies/dexcom-inc/company-page.html) |
| DXCM-T3 | DexCom IR source-links note | 2026-08-10 | Official IR verification note | Preserves official IR entry points and the verified annual and quarterly result URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/healthcare/medical-instruments-supplies/dexcom-inc/ir-source-links.md) |
| DXCM-T4 | DexCom SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms legal identity and filing sequence for the annual and quarterly chain | `[Filed]` | [CIK0001093557.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/CIK0001093557.json) |
| DXCM-T5 | DexCom 2025 Form 10-K | 2026-02-12 | SEC filing HTML | Standalone annual filing for the year ended December 31, 2025 | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2025-10k.html) |
| DXCM-T6 | DexCom Q4 2025 earnings filing | 2026-02-12 | SEC current report | Captures fourth-quarter and full-year `2025` results plus initial `2026` guidance | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2025-q4-8k.html) |
| DXCM-T7 | DexCom Q4 2025 press release exhibit | 2026-02-12 | SEC exhibit / company press release | Preserves the company-originated Q4 `2025` operating narrative and guidance | `[Filed]` | [2025-q4-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2025-q4-exhibit-99-1.html) |
| DXCM-T8 | DexCom Q1 2026 Form 10-Q | 2026-04-30 | SEC filing HTML | Filed quarterly report for March 31, 2026 | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2026-q1-10q.html) |
| DXCM-T9 | DexCom Q1 2026 earnings filing | 2026-04-30 | SEC current report | Captures first-quarter `2026` results and updated guidance | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2026-q1-8k.html) |
| DXCM-T10 | DexCom Q1 2026 press release exhibit | 2026-04-30 | SEC exhibit / company press release | Preserves the company-originated Q1 `2026` strategic and margin narrative | `[Filed]` | [2026-q1-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2026-q1-exhibit-99-1.html) |
| DXCM-T11 | DexCom Q2 2026 Form 10-Q | 2026-07-30 | SEC filing HTML | Filed quarterly report for June 30, 2026 | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2026-q2-10q.html) |
| DXCM-T12 | DexCom Q2 2026 earnings filing | 2026-07-30 | SEC current report | Captures most recent quarter results and raised guidance | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2026-q2-8k.html) |
| DXCM-T13 | DexCom Q2 2026 press release exhibit | 2026-07-30 | SEC exhibit / company press release | Preserves the company-originated Q2 `2026` narrative on consumer app experience, trial data, and long-range outlook | `[Filed]` | [2026-q2-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/medical-instruments-supplies/dexcom-inc/2026-q2-exhibit-99-1.html) |

## Reconciliation notes

- AnnualReports preserves the correct healthcare taxonomy, but the annual evidence chain itself had to be reconstructed from official IR references and SEC materials because AnnualReports lagged.
- DexCom's IR pages are verified as official entry points, but direct shell collection returned Cloudflare challenge pages rather than the substantive content.
- The SEC annual and quarterly filing chain is complete for the target window, and the company press release exhibits preserve the operating narrative that the IR pages would otherwise provide.

## Missing evidence

- No standalone IR-hosted `2025` annual-report PDF is saved locally in this pass.
- No standalone earnings-call transcript artifact is saved locally in this pass.
