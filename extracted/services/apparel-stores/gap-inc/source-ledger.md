# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| GAP-T1 | AnnualReports.com Gap verification note | 2026-08-10 | Aggregator verification note | Confirms `Services / Apparel Stores` taxonomy and that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/apparel-stores/gap-inc/annualreports-verification.md) |
| GAP-T2 | AnnualReports.com company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves the live discovery page showing Gap taxonomy and lagging annual-report year | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/apparel-stores/gap-inc/company-page.html) |
| GAP-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official annual-report and quarterly-results URLs and records the Cloudflare fetch constraint | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/apparel-stores/gap-inc/official-ir-verification.md) |
| GAP-T4 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, filing sequence, and the correct quarter window | `[Filed]` | [submissions-cik0000039911.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/submissions-cik0000039911.json) |
| GAP-T5 | 2025 Form `10-K` | 2026-03-17 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for fiscal `2025` | `[Filed]` | [gap-20260131.htm](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/gap-20260131.htm) |
| GAP-T6 | 2025 Q4 earnings `8-K` | 2026-03-05 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [gps-20260305.htm](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/gps-20260305.htm) |
| GAP-T7 | 2025 Q4 earnings Exhibit `99.1` | 2026-03-05 filed / 2026-08-10 collected | SEC-hosted earnings release HTML | Preserves the fourth-quarter and full-year `2025` results narrative and brand-level comp detail | `[Filed]` | [2025-q4-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/2025-q4-exhibit-99-1.html) |
| GAP-T8 | 2026 Q1 earnings `8-K` | 2026-05-28 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [gps-20260528.htm](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/gps-20260528.htm) |
| GAP-T9 | 2026 Q1 earnings Exhibit `99.1` | 2026-05-28 filed / 2026-08-10 collected | SEC-hosted earnings release HTML | Preserves the first-quarter `2026` results narrative including the brand-level comp split and non-recurring-item adjustment | `[Filed]` | [2026-q1-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/2026-q1-exhibit-99-1.html) |
| GAP-T10 | 2026 Q1 Form `10-Q` | 2026-05-29 filed / 2026-08-10 collected | SEC filing HTML | Filed first-quarter `2026` report | `[Filed]` | [gap-20260502.htm](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/gap-20260502.htm) |
| GAP-T11 | 2025 Q3 earnings `8-K` | 2025-11-20 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [gps-20251120.htm](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/gps-20251120.htm) |
| GAP-T12 | 2025 Q3 earnings Exhibit `99.1` | 2025-11-20 filed / 2026-08-10 collected | SEC-hosted earnings release HTML | Preserves the third-quarter `2025` results narrative and the pre-year-end brand split | `[Filed]` | [2025-q3-exhibit-99-1.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/2025-q3-exhibit-99-1.html) |
| GAP-T13 | 2025 Q3 Form `10-Q` | 2025-11-25 filed / 2026-08-10 collected | SEC filing HTML | Filed third-quarter `2025` report | `[Filed]` | [gap-20251101.htm](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/apparel-stores/gap-inc/gap-20251101.htm) |

## Reconciliation notes

- Gap now has a full local evidence chain for the fiscal `2025` annual filing and the latest three reported quarters in scope as of `2026-08-10`.
- The key timing correction is that the correct quarter window is `Q1 2026`, `Q4 2025`, and `Q3 2025`.
- The key aggregator correction is that AnnualReports.com still lagged at `2024`, even though the current official IR and SEC chain already ran through fiscal `2025`.
- The key collection constraint is that Gap's IR pages were Cloudflare-blocked in-shell, so the archive preserves the SEC filing and SEC-hosted Exhibit `99.1` chain while recording the verified official URLs in the IR verification note.
