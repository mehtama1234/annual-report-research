# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BN-T1 | AnnualReports.com Brookfield verification note | 2026-08-10 | Aggregator verification note | Confirms taxonomy and archive status on AnnualReports.com | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/asset-management/brookfield-corporation/annualreports-verification.md) |
| BN-T2 | Brookfield IR source-links note | 2026-08-10 | Official-source link ledger | Preserves the official annual, quarter, and shareholder-letter URLs used for the packet, including the 2Q26 timing note | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/brookfield-corporation/ir-source-links.md) |
| BN-T3 | Brookfield 3Q25 shareholder letter page | 2026-08-10 collected | Official IR HTML snapshot | Preserves one directly saved IR artifact inside the in-scope quarter chain | `[Disclosed]` | [2025-q3-letter.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/asset-management/brookfield-corporation/2025-q3-letter.html) |
| BN-T4 | Brookfield SEC submissions JSON | 2026-08-10 collected | SEC submissions file | Verifies filer identity and the 40-F / 6-K reporting sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/brookfield-corporation/sec-submissions.json) |
| BN-T5 | Brookfield 2025 Form 40-F | 2026-02-12 filed / 2026-08-10 collected | SEC filing HTML | Annual filing anchor for fiscal 2025 | `[Filed]` | [2025-40f.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/brookfield-corporation/2025-40f.html) |
| BN-T6 | Brookfield 3Q25 6-K | 2025-11-06 filed / 2026-08-10 collected | SEC filing HTML | Quarter-minus-2 filing wrapper for the late-2025 results chain | `[Filed]` | [2025-q3-6k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/brookfield-corporation/2025-q3-6k.html) |
| BN-T7 | Brookfield 4Q25 6-K | 2026-02-13 filed / 2026-08-10 collected | SEC filing HTML | Quarter-minus-1 filing wrapper for full-year 2025 results | `[Filed]` | [2025-q4-6k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/brookfield-corporation/2025-q4-6k.html) |
| BN-T8 | Brookfield 4Q25 6-K amendment | 2026-02-24 filed / 2026-08-10 collected | SEC filing HTML | Preserves the amended year-end filing wrapper in the local chain | `[Filed]` | [2025-q4-6k-amend.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/brookfield-corporation/2025-q4-6k-amend.html) |
| BN-T9 | Brookfield 1Q26 6-K | 2026-05-08 filed / 2026-08-10 collected | SEC filing HTML | Latest reported quarter filing wrapper as of 2026-08-10 | `[Filed]` | [2026-q1-6k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/brookfield-corporation/2026-q1-6k.html) |

## Reconciliation notes

- Brookfield is one of the lighter local IR captures in this batch. The durable on-disk chain is primarily the SEC foreign-issuer filing sequence plus the IR link ledger.
- The packet's time window is anchored to 2026-08-10. The IR links note explicitly records that 2Q26 had not yet been reported on that date.
- A later [2026-q2-6k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/asset-management/brookfield-corporation/2026-q2-6k.html) artifact exists in the sibling raw tree, but it is outside the packet's in-scope window and was not used as evidence for the 2026-08-10 read.

## Missing evidence

- No local Brookfield annual-report PDF artifact is saved in the linked raw tree.
- No local saved copies of the 4Q25 or 1Q26 shareholder letters or the 1Q26 interim-report PDF are present in the linked raw tree.
- No locally saved earnings-call transcript artifact is present for the in-scope quarters.
