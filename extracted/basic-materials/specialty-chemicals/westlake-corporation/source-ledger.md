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
| WLK-T1 | AnnualReports company page | 2026-08-10 collected | AnnualReports company page | Confirms source taxonomy and shows AnnualReports lagged at `2024` | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/basic-materials/specialty-chemicals/westlake-corporation/company-page.html) |
| WLK-T2 | AnnualReports verification note | 2026-08-10 | Aggregator verification note | Documents AnnualReports lag and taxonomy | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/basic-materials/specialty-chemicals/westlake-corporation/annualreports-verification.md) |
| WLK-T3 | IR source-link note | 2026-08-10 | Official IR URL map | Preserves the annual-report, quarterly-results, filing, and presentation URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |
| WLK-T4 | SEC source-link note | 2026-08-10 | Filing URL map | Preserves the official `10-K` and `10-Q` filing references | `[Filed]` | [sec-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/sec/basic-materials/specialty-chemicals/westlake-corporation/sec-source-links.md) |
| WLK-T5 | `2025` annual report PDF | 2026-08-10 verified | Official annual report PDF | Provides the annual strategic reset, segment shape, and capital-allocation frame | `[Disclosed]` | verified remotely via URL in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |
| WLK-T6 | `Q4 2025` results release page | 2026-02-24 | Official results release page | Provides fourth-quarter and full-year 2025 financial results and shutdown context | `[Disclosed]` | verified remotely via URL in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |
| WLK-T7 | `Q1 2026` results release page | 2026-05-05 | Official results release page | Provides first-quarter 2026 financial results and segment commentary | `[Disclosed]` | verified remotely via URL in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |
| WLK-T8 | `Q1 2026` earnings presentation PDF | 2026-05-05 | Official presentation PDF | Adds detailed commentary on HIP and PEM drivers, including litigation and shutdown context | `[Disclosed]` | verified remotely via URL in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |
| WLK-T9 | `Q1 2026` filing page and company-hosted `10-Q` PDF | 2026-05-06 | Filing reference | Preserves the official quarter filing reference path | `[Filed]` | verified remotely via URLs in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |
| WLK-T10 | `Q2 2026` results release page | 2026-08-04 | Official results release page | Provides second-quarter 2026 financial results and rebound commentary | `[Disclosed]` | verified remotely via URL in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |
| WLK-T11 | `Q2 2026` earnings presentation PDF | 2026-08-04 | Official presentation PDF | Adds detailed pricing, segment, and profitability-improvement commentary | `[Disclosed]` | verified remotely via URL in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |
| WLK-T12 | `Q2 2026` filing page and company-hosted `10-Q` PDF | 2026-08-05 | Filing reference | Preserves the official latest-quarter filing reference path | `[Filed]` | verified remotely via URLs in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/basic-materials/specialty-chemicals/westlake-corporation/ir-source-links.md) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- AnnualReports taxonomy still uses the older corporate name and lagged annual package, so official Westlake IR is the correct source of truth for current-year materials.
- Some official Westlake artifacts were verified through web retrieval and source URLs rather than saved locally because the IR delivery path was unreliable from the current shell environment.

## Missing evidence

- No standalone transcript artifact saved locally for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
- No fully saved local company-hosted PDF set yet despite verified official URLs.
