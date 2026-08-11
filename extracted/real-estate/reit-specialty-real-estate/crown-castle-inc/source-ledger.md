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
| CCI-T1 | AnnualReports verification note for Crown Castle | 2026-08-10 | Aggregator verification note | Confirms specialty-REIT taxonomy and records that AnnualReports still lagged at `2024` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers/raw/annualreports/real-estate/reit-specialty-real-estate/crown-castle-inc/annualreports-verification.md) |
| CCI-T2 | Crown Castle IR source-links note | 2026-08-10 | Official-link verification note | Records the investor home, SEC-filings page, and authoritative quarter release URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers/raw/company-ir/real-estate/reit-specialty-real-estate/crown-castle-inc/ir-source-links.md) |
| CCI-T3 | Crown Castle SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the annual / trailing-three-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/crown-castle-inc/sec-submissions.json) |
| CCI-T4 | Crown Castle 2025 Form 10-K | 2026-02-24 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/crown-castle-inc/2025-10k.html) |
| CCI-T5 | Crown Castle Q4 2025 earnings 8-K | 2026-02-25 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/crown-castle-inc/2025-q4-8k.html) |
| CCI-T6 | Crown Castle Q1 2026 Form 10-Q | 2026-04-30 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/crown-castle-inc/2026-q1-10q.html) |
| CCI-T7 | Crown Castle Q1 2026 earnings 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/crown-castle-inc/2026-q1-8k.html) |
| CCI-T8 | Crown Castle Q2 2026 Form 10-Q | 2026-07-22 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/crown-castle-inc/2026-q2-10q.html) |
| CCI-T9 | Crown Castle Q2 2026 earnings 8-K | 2026-08-05 | SEC filing HTML | Local saved `8-K` following the second-quarter period; packet uses it alongside the official investor-site supplement and `10-Q` chain | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/crown-castle-inc/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports lagged Crown Castle’s `2025` annual package as of Monday, `2026-08-10`, so company IR and SEC are the authoritative current-period chain.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `2Q26`, `1Q26`, and `4Q25`.
- The extracted packet relies on a mixed evidence chain: SEC annual and quarterly filings are saved locally, while the investor-site result pages and supplement PDFs are preserved as verified URLs in the IR source-links note rather than as local binary captures.
- Local evidence for this name also remains split across imported side trees rather than `annual-report-research/raw` on `main`.

## Missing evidence

- No local Crown Castle transcript artifact was preserved for `4Q25`, `1Q26`, or `2Q26`.
- No local Crown Castle quarter result PDFs were preserved in the current workspace; the authoritative investor-site URLs are recorded in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers/raw/company-ir/real-estate/reit-specialty-real-estate/crown-castle-inc/ir-source-links.md).
