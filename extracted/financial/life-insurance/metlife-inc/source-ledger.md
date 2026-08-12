# Source Ledger

Date baseline: 2026-08-12

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
| MET-T1 | AnnualReports verification note for MetLife | 2026-08-10 | Aggregator verification note | Confirms `Life Insurance` taxonomy and records that AnnualReports lagged at `2024` when checked | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/life-insurance/metlife-inc/annualreports-verification.md) |
| MET-T2 | SEC submissions JSON for MetLife | 2026-08-10 | SEC index JSON | Confirms CIK, fiscal year-end, and the annual / trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/sec-submissions.json) |
| MET-T3 | MetLife IR source-links note | 2026-08-10 | Official-link verification note | Records the official MetLife IR destinations and explains the Cloudflare block on local binary capture | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/life-insurance/metlife-inc/ir-source-links.md) |
| MET-T4 | MetLife 2025 Form 10-K | 2026-02-20 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2025-10k.html) |
| MET-T5 | MetLife Q4 2025 earnings 8-K | 2026-02-04 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2025-q4-8k.html) |
| MET-T6 | MetLife Q1 2026 10-Q | 2026-05-06 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2026-q1-10q.html) |
| MET-T7 | MetLife Q1 2026 earnings 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2026-q1-8k.html) |
| MET-T8 | MetLife Q2 2026 10-Q | 2026-08-06 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2026-q2-10q.html) |
| MET-T9 | MetLife Q2 2026 earnings 8-K | 2026-08-05 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/life-insurance/metlife-inc/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation only. As of `2026-08-10`, the hosted annual package still lagged at `2024`.
- The correct trailing-quarter set as of `2026-08-10` is `2Q26`, `1Q26`, and `4Q25`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive-lag confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- Local direct fetches to several MetLife IR assets returned Cloudflare challenge pages. Because of that, the authoritative locally saved evidence chain is the SEC filing set plus the verified official IR URLs in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/life-insurance/metlife-inc/ir-source-links.md).
- The source chain is still authoritative for reported results because the quarter wrappers and filed quarterlies are present locally from SEC.
- The packet should therefore be treated as `proven` for annual-plus-quarter coverage:
  - taxonomy confirmation exists
  - official IR routing exists and was verified
  - the annual filing and target-quarter SEC chain are locally present

## Missing evidence

- No clean local MetLife IR PDF capture was preserved for the annual report or quarterly earnings releases in this workspace because of Cloudflare delivery blocks.
- No local prepared remarks or full earnings-call transcript capture was collected for `4Q25`, `1Q26`, or `2Q26`.
