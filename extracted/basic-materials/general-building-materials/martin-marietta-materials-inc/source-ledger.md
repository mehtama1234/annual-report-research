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
| MLM-T1 | AnnualReports verification note | 2026-08-10 | Archive verification note | Documents that AnnualReports did not provide a clean company-specific page during this run | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/basic-materials/general-building-materials/martin-marietta-materials-inc/annualreports-verification.md) |
| MLM-T2 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves the annual-report, quarter-result, and official PDF URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/general-building-materials/martin-marietta-materials-inc/ir-source-links.md) |
| MLM-T3 | SEC submissions JSON | 2026-08-10 collected | SEC submissions feed | Verifies accession numbers and primary documents for the target window | `[Filed]` | [submissions-cik0000916076.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/martin-marietta-materials-inc/submissions-cik0000916076.json) |
| MLM-T4 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves the direct `10-K`, `10-Q`, and `8-K` URLs | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/martin-marietta-materials-inc/sec-source-links.md) |
| MLM-T5 | `2025` Form `10-K` HTML | 2026-08-10 collected | Direct SEC annual filing HTML | Provides the authoritative annual filing | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/martin-marietta-materials-inc/2025-10k.html) |
| MLM-T6 | `Q4 2025` earnings `8-K` HTML | 2026-08-10 collected | Direct SEC current report HTML | Provides fourth-quarter and full-year results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/martin-marietta-materials-inc/2025-q4-8k.html) |
| MLM-T7 | `Q1 2026` Form `10-Q` HTML | 2026-08-10 collected | Direct SEC quarterly filing HTML | Provides the authoritative first-quarter filing | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/martin-marietta-materials-inc/2026-q1-10q.html) |
| MLM-T8 | `Q1 2026` earnings `8-K` HTML | 2026-08-10 collected | Direct SEC current report HTML | Provides first-quarter earnings-release evidence | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/martin-marietta-materials-inc/2026-q1-8k.html) |
| MLM-T9 | `Q2 2026` Form `10-Q` HTML | 2026-08-10 collected | Direct SEC quarterly filing HTML | Provides the authoritative latest-quarter filing | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/martin-marietta-materials-inc/2026-q2-10q.html) |
| MLM-T10 | `Q2 2026` earnings `8-K` HTML | 2026-08-10 collected | Direct SEC current report HTML | Provides latest-quarter earnings-release evidence | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/general-building-materials/martin-marietta-materials-inc/2026-q2-8k.html) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- Martin Marietta IR URLs were confirmed during this run, but direct shell retrieval of those artifacts was inconsistent in this environment.
- The packet is still source-complete for the required annual and quarter window because the full SEC filing stack was collected locally and the official IR URL set was preserved in a dedicated note.

## Missing evidence

- No standalone earnings-call transcript artifact was saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No company-hosted annual-report PDF or quarter-presentation PDF was saved locally during this run despite the official IR URLs being identified.
