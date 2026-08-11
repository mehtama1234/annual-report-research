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
| L-T1 | AnnualReports verification note for Loews | 2026-08-10 | Aggregator verification note | Confirms company identity, lagging `2024` annual availability, and the insurance-centric archive framing | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/conglomerates/conglomerates/loews-corporation/annualreports-verification.md) |
| L-T2 | SEC submissions JSON for Loews | 2026-08-10 | SEC index JSON | Confirms issuer identity, fiscal year-end, and the annual / trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/loews-corporation/sec-submissions.json) |
| L-T3 | Loews IR source-links note | 2026-08-10 | Official-link verification note | Records official IR entry points and the current annual / quarterly result-page chain | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/conglomerates/conglomerates/loews-corporation/ir-source-links.md) |
| L-T4 | Loews 2025 Form 10-K | 2026-02-10 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/loews-corporation/2025-10k.html) |
| L-T5 | Loews Q4 2025 earnings 8-K | 2026-02-10 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/loews-corporation/2025-q4-8k.html) |
| L-T6 | Loews Q1 2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/loews-corporation/2026-q1-10q.html) |
| L-T7 | Loews Q1 2026 earnings 8-K | 2026-05-05 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/loews-corporation/2026-q1-8k.html) |
| L-T8 | Loews Q2 2026 Form 10-Q | 2026-08-04 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/loews-corporation/2026-q2-10q.html) |
| L-T9 | Loews Q2 2026 earnings 8-K | 2026-08-04 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/conglomerates/conglomerates/loews-corporation/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy confirmation and lag tracking only. As of Monday, `2026-08-10`, it still showed `2024` as the most recent annual report and leaned on an insurance-centric framing.
- The correct trailing-quarter set as of `2026-08-10` is `2Q26`, `1Q26`, and `4Q25`.
- The local evidence chain is SEC-first, with Loews IR preserved as verified entry-point links rather than locally captured result PDFs.

## Missing evidence

- No local Loews IR HTML or PDF capture of the quarter result pages was preserved in this workspace.
- No local prepared remarks or full earnings-call transcript capture was collected for `4Q25`, `1Q26`, or `2Q26`.
