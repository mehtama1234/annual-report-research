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
| USB-T1 | AnnualReports verification note for U.S. Bancorp | 2026-08-10 | Aggregator verification note | Confirms `Regional - Midwest Banks` taxonomy and `2025` annual availability | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/regional-midwest-banks/us-bancorp/annualreports-verification.md) |
| USB-T2 | U.S. Bancorp IR source-links note | 2026-08-10 | Official-link verification note | Records official annual-reports and quarterly-results pages plus in-scope release URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-midwest-banks/us-bancorp/ir-source-links.md) |
| USB-T3 | U.S. Bancorp SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the annual / trailing-three-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-midwest-banks/us-bancorp/sec-submissions.json) |
| USB-T4 | U.S. Bancorp 2025 Form 10-K | 2026-02-20 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-midwest-banks/us-bancorp/2025-10k.html) |
| USB-T5 | U.S. Bancorp Q4 2025 earnings 8-K | 2026-01-20 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-midwest-banks/us-bancorp/2025-q4-8k.html) |
| USB-T6 | U.S. Bancorp Q1 2026 Form 10-Q | 2026-04-17 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-midwest-banks/us-bancorp/2026-q1-10q.html) |
| USB-T7 | U.S. Bancorp Q1 2026 earnings 8-K | 2026-04-16 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-midwest-banks/us-bancorp/2026-q1-8k.html) |
| USB-T8 | U.S. Bancorp Q2 2026 Form 10-Q | 2026-07-17 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-midwest-banks/us-bancorp/2026-q2-10q.html) |
| USB-T9 | U.S. Bancorp Q2 2026 earnings 8-K | 2026-07-16 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-midwest-banks/us-bancorp/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports already showed `2025` availability for USB, but company IR and SEC remain the authoritative current-period chain.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `2Q26`, `1Q26`, and `4Q25`.
- The local evidence chain is SEC-heavy in this pass. The official USB IR release URLs were verified and preserved in the IR source note, but the result pages themselves were not saved locally.

## Missing evidence

- No local U.S. Bancorp IR binary captures or transcript artifacts were preserved for `4Q25`, `1Q26`, or `2Q26` in this workspace.
