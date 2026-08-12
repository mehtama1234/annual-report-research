# Source Ledger

Date baseline: `2026-08-12`

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
| CI-T1 | AnnualReports.com Cigna company page | 2026-08-12 | Aggregator page | Confirms Healthcare / Health Care Plans taxonomy and legacy naming | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/healthcare/managed-health-care/the-cigna-group/company-page.html) |
| CI-T2 | The Cigna Group official IR verification | 2026-08-12 | Official IR verification note | Confirms annual, quarterly, and event-page routing for the in-scope filing window | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/managed-health-care/the-cigna-group/official-ir-verification.md) |
| CI-T3 | The Cigna Group `2025` annual report PDF | 2026-02-05 | Annual report PDF | Official annual report package for the year ended `2025-12-31` | `[Disclosed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2025-annual-report.pdf) |
| CI-T4 | The Cigna Group `2025` Form 10-K | 2026-02-26 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2025-10k.html) |
| CI-T5 | The Cigna Group `Q4 2025` earnings release exhibit | 2026-02-05 | SEC exhibit HTML | Exact fourth-quarter and full-year `2025` metrics plus initial `2026` outlook | `[Filed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2025-q4-press-release.html) |
| CI-T6 | The Cigna Group `Q4 2025` 8-K | 2026-02-05 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2025-q4-8k.html) |
| CI-T7 | The Cigna Group `Q1 2026` earnings release exhibit | 2026-04-30 | SEC exhibit HTML | Exact first-quarter `2026` metrics and raised `2026` outlook | `[Filed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2026-q1-press-release.html) |
| CI-T8 | The Cigna Group `Q1 2026` 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2026-q1-8k.html) |
| CI-T9 | The Cigna Group `Q1 2026` 10-Q | 2026-05-02 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2026-q1-10q.html) |
| CI-T10 | The Cigna Group `Q2 2026` earnings release exhibit | 2026-07-30 | SEC exhibit HTML | Exact second-quarter `2026` metrics and raised `2026` outlook | `[Filed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2026-q2-press-release.html) |
| CI-T11 | The Cigna Group `Q2 2026` 8-K | 2026-07-30 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2026-q2-8k.html) |
| CI-T12 | The Cigna Group `Q2 2026` 10-Q | 2026-08-01 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/managed-health-care/the-cigna-group/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation. The page still uses the legacy `CIGNA Corporation` name.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is now strong enough for local inspection:
  - AnnualReports company page
  - official annual and quarterly IR pages plus official in-scope event pages
  - official annual report PDF and SEC annual filing
  - SEC quarter-release exhibits, `8-K` wrappers, and both in-scope `10-Q` filings
- The packet is now `proven` because this workspace preserves a rebuilt local annual-plus-quarter evidence chain comparable to the cleanest proof-standard packets.

## Missing evidence

- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
