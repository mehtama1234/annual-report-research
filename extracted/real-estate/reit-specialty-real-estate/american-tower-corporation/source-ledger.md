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
| AMT-T1 | AnnualReports verification note for American Tower | 2026-08-10 | Aggregator verification note | Confirms `REIT - Specialty Real Estate` taxonomy and that AnnualReports was current to `2025` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers/raw/annualreports/real-estate/reit-specialty-real-estate/american-tower-corporation/annualreports-verification.md) |
| AMT-T2 | American Tower IR source-links note | 2026-08-10 | Official-link verification note | Records the annual-report and quarter evidence URLs used in this collection pass | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers/raw/company-ir/real-estate/reit-specialty-real-estate/american-tower-corporation/ir-source-links.md) |
| AMT-T3 | American Tower Q4 2025 earnings release HTML | 2026-02-24 local capture | Earnings-release page | Preserves the locally saved `4Q25` release page | `[Disclosed]` | [2025-q4-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers/raw/company-ir/real-estate/reit-specialty-real-estate/american-tower-corporation/2025-q4-earnings-release.html) |
| AMT-T4 | American Tower Q1 2026 earnings release HTML | 2026-04-28 local capture | Earnings-release page | Preserves the locally saved `1Q26` release page | `[Disclosed]` | [2026-q1-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers/raw/company-ir/real-estate/reit-specialty-real-estate/american-tower-corporation/2026-q1-earnings-release.html) |
| AMT-T5 | American Tower Q2 2026 earnings release HTML | 2026-07-28 local capture | Earnings-release page | Preserves the locally saved `2Q26` release page | `[Disclosed]` | [2026-q2-earnings-release.html](/home/manishmehta/ui-projects/annual-report-research-remaining-frontiers/raw/company-ir/real-estate/reit-specialty-real-estate/american-tower-corporation/2026-q2-earnings-release.html) |
| AMT-T6 | American Tower SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the annual / trailing-three-quarter filing chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/american-tower-corporation/sec-submissions.json) |
| AMT-T7 | American Tower 2025 Form 10-K | 2026-02-25 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/american-tower-corporation/2025-10k.html) |
| AMT-T8 | American Tower Q4 2025 earnings 8-K | 2026-02-24 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/american-tower-corporation/2025-q4-8k.html) |
| AMT-T9 | American Tower Q1 2026 Form 10-Q | 2026-04-29 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/american-tower-corporation/2026-q1-10q.html) |
| AMT-T10 | American Tower Q1 2026 earnings 8-K | 2026-04-28 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/american-tower-corporation/2026-q1-8k.html) |
| AMT-T11 | American Tower Q2 2026 Form 10-Q | 2026-07-29 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/american-tower-corporation/2026-q2-10q.html) |
| AMT-T12 | American Tower Q2 2026 earnings 8-K | 2026-07-28 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-media-frontier-push/raw/sec/real-estate/reit-specialty-real-estate/american-tower-corporation/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports was current enough to confirm both taxonomy and `2025` annual availability for American Tower.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `2Q26`, `1Q26`, and `4Q25`.
- Local evidence is split across imported side trees rather than `annual-report-research/raw` on `main`. The extracted packet is integrated in `main`, while the supporting raw evidence remains in `annual-report-research-remaining-frontiers` and `annual-report-research-media-frontier-push`.
- The company-hosted IR landing pages were challenge-blocked in the CLI environment, but the earnings-release pages and SEC filing chain together provide an authoritative source-complete record.

## Missing evidence

- No standalone local call transcript artifact was preserved for `4Q25`, `1Q26`, or `2Q26`.
