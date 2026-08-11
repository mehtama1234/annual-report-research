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
| MTB-T1 | AnnualReports verification note for M&T | 2026-08-10 | Aggregator verification note | Confirms `Regional - Mid-Atlantic Banks` taxonomy and archive presence | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/regional-mid-atlantic-banks/mt-bank-corporation/annualreports-verification.md) |
| MTB-T2 | M&T IR source-links note | 2026-08-10 | Official-link verification note | Records annual-report, quarterly-results, and in-scope quarter document URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-mid-atlantic-banks/mt-bank-corporation/ir-source-links.md) |
| MTB-T3 | M&T SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the annual / trailing-three-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/mt-bank-corporation/sec-submissions.json) |
| MTB-T4 | M&T 2025 Form 10-K | 2026-02-19 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/mt-bank-corporation/2025-10k.html) |
| MTB-T5 | M&T Q4 2025 earnings 8-K | 2026-01-16 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/mt-bank-corporation/2025-q4-8k.html) |
| MTB-T6 | M&T Q1 2026 Form 10-Q | 2026-05-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/mt-bank-corporation/2026-q1-10q.html) |
| MTB-T7 | M&T Q1 2026 earnings 8-K | 2026-04-14 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/mt-bank-corporation/2026-q1-8k.html) |
| MTB-T8 | M&T Q2 2026 Form 10-Q | 2026-08-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/mt-bank-corporation/2026-q2-10q.html) |
| MTB-T9 | M&T Q2 2026 earnings 8-K | 2026-07-14 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-mid-atlantic-banks/mt-bank-corporation/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation; company IR and SEC remain the authoritative current-period chain.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `2Q26`, `1Q26`, and `4Q25`.
- The local evidence chain is SEC-first. The official M&T IR document URLs are recorded in the IR source note, but the IR binaries were not preserved locally in this pass.

## Missing evidence

- No local M&T annual-report PDF, quarterly earnings PDF, or transcript capture was preserved in this workspace.
