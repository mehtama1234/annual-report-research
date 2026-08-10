# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| AEO-T1 | AnnualReports.com AEO verification note | 2026-08-10 | Aggregator verification note | Confirms `Services / Apparel Stores` taxonomy and that AnnualReports exposed the `2025` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/apparel-stores/american-eagle-outfitters-inc/annualreports-verification.md) |
| AEO-T2 | AnnualReports.com company page snapshot | 2026-08-10 collected | Aggregator HTML snapshot | Preserves the live discovery page showing AEO taxonomy and current annual-report year | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/services/apparel-stores/american-eagle-outfitters-inc/company-page.html) |
| AEO-T3 | Official IR verification note | 2026-08-10 | Official IR verification note | Confirms the official annual-report and quarterly-results URLs and records the Cloudflare fetch constraint | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/services/apparel-stores/american-eagle-outfitters-inc/official-ir-verification.md) |
| AEO-T4 | SEC submissions index | 2026-08-10 collected | SEC submissions JSON | Verifies filer identity, filing sequence, and the correct quarter window | `[Filed]` | [submissions-cik0000919012.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/apparel-stores/american-eagle-outfitters-inc/submissions-cik0000919012.json) |
| AEO-T5 | 2025 Form `10-K` | 2026-03-30 filed / 2026-08-10 collected | SEC filing HTML | Annual filing for fiscal `2025` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/apparel-stores/american-eagle-outfitters-inc/2025-10k.html) |
| AEO-T6 | 2025 Q4 earnings `8-K` | 2026-03-04 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/apparel-stores/american-eagle-outfitters-inc/2025-q4-8k.html) |
| AEO-T7 | 2026 Q1 earnings `8-K` | 2026-05-28 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/apparel-stores/american-eagle-outfitters-inc/2026-q1-8k.html) |
| AEO-T8 | 2026 Q1 Form `10-Q` | 2026-06-03 filed / 2026-08-10 collected | SEC filing HTML | Filed first-quarter `2026` report | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/apparel-stores/american-eagle-outfitters-inc/2026-q1-10q.html) |
| AEO-T9 | 2025 Q3 earnings `8-K` | 2025-12-02 filed / 2026-08-10 collected | SEC filing HTML | Filing wrapper for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/apparel-stores/american-eagle-outfitters-inc/2025-q3-8k.html) |
| AEO-T10 | 2025 Q3 Form `10-Q` | 2025-12-09 filed / 2026-08-10 collected | SEC filing HTML | Filed third-quarter `2025` report | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/services/apparel-stores/american-eagle-outfitters-inc/2025-q3-10q.html) |

## Reconciliation notes

- American Eagle Outfitters now has a full local evidence chain for the fiscal `2025` annual filing and the latest three reported quarters in scope as of `2026-08-10`.
- The correct quarter window is `Q1 2026`, `Q4 2025`, and `Q3 2025`.
- AnnualReports.com was current here and exposed the `2025` annual package while also confirming the `Services / Apparel Stores` taxonomy.
- The key collection constraint is that AEO's IR pages were Cloudflare-blocked in-shell, so the archive preserves the SEC filing chain while recording the verified official annual-report and quarterly-results URLs in the IR verification note.
