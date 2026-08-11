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
| RF-T1 | AnnualReports verification note for Regions | 2026-08-10 | Aggregator verification note | Confirms `Regional - Southeast Banks` taxonomy and records that AnnualReports lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/regional-southeast-banks/regions-financial-corp/annualreports-verification.md) |
| RF-T2 | AnnualReports company page snapshot for Regions | 2026-08-10 | Aggregator page snapshot | Preserves the local archive confirmation page | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/regional-southeast-banks/regions-financial-corp/company-page.html) |
| RF-T3 | Regions IR source-links note | 2026-08-10 | Official-link verification note | Records annual-report and quarter release URLs plus capture caveats | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-southeast-banks/regions-financial-corp/ir-source-links.md) |
| RF-T4 | Regions annual-reports page snapshot | 2026-08-10 | Official IR page snapshot | Confirms the official annual-report hub | `[Disclosed]` | [annual-reports.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-southeast-banks/regions-financial-corp/annual-reports.html) |
| RF-T5 | Regions quarterly-investor-info page snapshot | 2026-08-10 | Official IR page snapshot | Confirms the quarterly results hub used to verify the current quarter chain | `[Disclosed]` | [quarterly-investor-info.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/regional-southeast-banks/regions-financial-corp/quarterly-investor-info.html) |
| RF-T6 | Regions SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the annual / trailing-three-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-southeast-banks/regions-financial-corp/sec-submissions.json) |
| RF-T7 | Regions 2025 Form 10-K | 2026-02-20 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-southeast-banks/regions-financial-corp/2025-10k.html) |
| RF-T8 | Regions Q4 2025 earnings 8-K | 2026-01-16 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-southeast-banks/regions-financial-corp/2025-q4-8k.html) |
| RF-T9 | Regions Q1 2026 Form 10-Q | 2026-05-02 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-southeast-banks/regions-financial-corp/2026-q1-10q.html) |
| RF-T10 | Regions Q1 2026 earnings 8-K | 2026-04-17 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-southeast-banks/regions-financial-corp/2026-q1-8k.html) |
| RF-T11 | Regions Q2 2026 Form 10-Q | 2026-07-18 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-southeast-banks/regions-financial-corp/2026-q2-10q.html) |
| RF-T12 | Regions Q2 2026 earnings 8-K | 2026-07-17 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/regional-southeast-banks/regions-financial-corp/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports lagged the required annual package as of Monday, `2026-08-10`, so Regions IR and SEC are the authoritative current-period chain.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `2Q26`, `1Q26`, and `4Q25`.
- Local evidence is mixed but adequate: official IR hub pages were saved, the result-page URLs were verified in the IR source note, and the SEC annual and quarter chain is locally present.

## Missing evidence

- No local Regions quarter result-page binaries or transcript artifacts were preserved beyond the verified URL chain and SEC filings.
