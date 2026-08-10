# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| BTSG-T1 | AnnualReports.com BrightSpring verification note | 2026-08-10 | Aggregator verification note | Confirms the company page and records that AnnualReports lagged at the `2024` package on the collection date | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/healthcare/specialized-health-services/brightspring-health-services-inc/annualreports-verification.md) |
| BTSG-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the archive-confirmation page used for taxonomy verification | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research/raw/annualreports/healthcare/specialized-health-services/brightspring-health-services-inc/company-page.html) |
| BTSG-T3 | BrightSpring IR source-links note | 2026-08-10 | Official IR verification note | Preserves the official annual-report and quarter-result URL chain, including the Q2 `2026` press release and SEC exhibit URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/healthcare/specialized-health-services/brightspring-health-services-inc/ir-source-links.md) |
| BTSG-T4 | BrightSpring SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms issuer identity, ticker, and the `2025` annual plus `Q4 2025` / `Q1 2026` / `Q2 2026` filing chain | `[Filed]` | [submissions.json](/home/manishmehta/ui-projects/annual-report-research/raw/sec/healthcare/specialized-health-services/brightspring-health-services-inc/submissions.json) |
| BTSG-T5 | BrightSpring `2025` annual report PDF | 2026-02-27 | Official IR annual report PDF | Authoritative annual report for the year ended December 31, 2025 | `[Filed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/healthcare/specialized-health-services/brightspring-health-services-inc/ir-source-links.md) |
| BTSG-T6 | BrightSpring Q4 `2025` earnings filing and press release | 2026-02-27 | Official IR / SEC earnings filing | Captures fourth-quarter and full-year `2025` continuing-operations results and `2026` guidance setup | `[Filed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/healthcare/specialized-health-services/brightspring-health-services-inc/ir-source-links.md) |
| BTSG-T7 | BrightSpring Q1 `2026` earnings filing and press release | 2026-05-01 | Official IR / SEC earnings filing | Captures first-quarter `2026` results, Community Living close, and raised guidance | `[Filed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/healthcare/specialized-health-services/brightspring-health-services-inc/ir-source-links.md) |
| BTSG-T8 | BrightSpring Q2 `2026` earnings press release and SEC Exhibit `99.1` | 2026-07-31 | Official IR / SEC earnings filing | Captures most recent quarter results and raised full-year `2026` guidance | `[Filed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research/raw/company-ir/healthcare/specialized-health-services/brightspring-health-services-inc/ir-source-links.md) |

## Reconciliation notes

- AnnualReports is used for taxonomy and archive confirmation only.
- Official BrightSpring IR and SEC URLs are preserved in the local IR note because direct binary downloads were inconsistent in this environment even though the pages were reachable and verifiable.
- The target quarter window is standard for this calendar-year reporter as of `2026-08-10`: `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- A wrong CIK was fetched during the first BrightSpring pass and then corrected. The authoritative issuer for this packet is `CIK 0001865782`, as preserved in the local submissions JSON.

## Missing evidence

- No standalone local copy of the `2025` annual report PDF or quarterly press-release PDFs was preserved in this pass because of inconsistent IR-host download behavior.
- No standalone earnings-call transcript artifact is saved locally in this pass.

