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
| SPG-T1 | AnnualReports verification note for Simon | 2026-08-10 | Aggregator verification note | Confirms `REIT - Retail` taxonomy and records that AnnualReports lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/real-estate/reit-retail/simon-property-group-inc/annualreports-verification.md) |
| SPG-T2 | SEC submissions JSON for Simon | 2026-08-10 | SEC index JSON | Confirms issuer identity, filing sequence, and the date-specific quarter chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/real-estate/reit-retail/simon-property-group-inc/sec-submissions.json) |
| SPG-T3 | Simon IR source-links note | 2026-08-10 | Official-link verification note | Records official IR entry points and the key timing note that `2Q26` had not yet been reported as of `2026-08-10` | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/real-estate/reit-retail/simon-property-group-inc/ir-source-links.md) |
| SPG-T4 | Simon 2025 Form 10-K | 2026-02-10 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/real-estate/reit-retail/simon-property-group-inc/2025-10k.html) |
| SPG-T5 | Simon Q3 2025 Form 10-Q | 2025-11-07 | SEC filing HTML | Filed quarterly report for quarter ended `2025-09-30` | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/real-estate/reit-retail/simon-property-group-inc/2025-q3-10q.html) |
| SPG-T6 | Simon Q3 2025 earnings 8-K | 2025-11-04 | SEC filing HTML | Wrapper filing for third-quarter `2025` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/real-estate/reit-retail/simon-property-group-inc/2025-q3-8k.html) |
| SPG-T7 | Simon Q4 2025 earnings 8-K | 2026-02-04 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/real-estate/reit-retail/simon-property-group-inc/2025-q4-8k.html) |
| SPG-T8 | Simon Q1 2026 Form 10-Q | 2026-05-12 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/real-estate/reit-retail/simon-property-group-inc/2026-q1-10q.html) |
| SPG-T9 | Simon Q1 2026 earnings 8-K | 2026-05-12 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/real-estate/reit-retail/simon-property-group-inc/2026-q1-8k.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy confirmation only. As of `2026-08-10`, it still lagged at `2024`.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `1Q26`, `4Q25`, and `3Q25` because Simon had not yet reported `2Q26`; its earnings event was later that same day.
- The authoritative evidence chain for the current research window is therefore Simon IR for timing verification plus the locally saved SEC annual and quarter filings.

## Missing evidence

- No local Simon IR HTML or PDF capture of the result pages was preserved in this workspace.
- No local prepared remarks or full earnings-call transcript capture was collected for `3Q25`, `4Q25`, or `1Q26`.
