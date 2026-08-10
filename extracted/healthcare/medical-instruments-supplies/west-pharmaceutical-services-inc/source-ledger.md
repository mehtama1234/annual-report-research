# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| WST-T1 | AnnualReports.com West verification note | 2026-08-10 | Aggregator verification note | Confirms source taxonomy and that AnnualReports still lagged at the `2024` annual package | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/annualreports-verification.md) |
| WST-T2 | AnnualReports company page HTML | 2026-08-10 collected | Aggregator page HTML | Preserves the company-page evidence used for taxonomy and archive confirmation | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/company-page.html) |
| WST-T3 | West IR source-links note | 2026-08-10 | Official IR verification note | Preserves official IR entry points and the verified annual and quarterly result URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/ir-source-links.md) |
| WST-T4 | West SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms legal identity and filing sequence for the annual and quarterly chain | `[Filed]` | [CIK0000105770.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/CIK0000105770.json) |
| WST-T5 | West 2025 Form 10-K | 2026-02-17 | SEC filing HTML | Standalone annual filing for the year ended December 31, 2025 | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/2025-10k.html) |
| WST-T6 | West Q4 2025 earnings filing | 2026-02-12 | SEC current report | Captures fourth-quarter and full-year `2025` results plus 2026 guidance setup | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/2025-q4-8k.html) |
| WST-T7 | West Q1 2026 Form 10-Q | 2026-04-23 | SEC filing HTML | Filed quarterly report for March 31, 2026 | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/2026-q1-10q.html) |
| WST-T8 | West Q1 2026 earnings filing | 2026-04-23 | SEC current report | Captures first-quarter `2026` results and raised guidance | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/2026-q1-8k.html) |
| WST-T9 | West Q2 2026 Form 10-Q | 2026-07-23 | SEC filing HTML | Filed quarterly report for June 30, 2026 | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/2026-q2-10q.html) |
| WST-T10 | West Q2 2026 earnings filing | 2026-07-23 | SEC current report | Captures most recent quarter results and delivery-system demand | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/medical-instruments-supplies/west-pharmaceutical-services-inc/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports preserves the correct healthcare taxonomy, but the annual evidence chain itself had to be reconstructed from official IR and SEC materials.
- The SEC annual and quarterly filing chain is complete for the target window.
- The only remaining artifact gap is the locally saved official IR-hosted `2025` annual-report PDF, whose verified source URL is preserved in `ir-source-links.md`.

## Missing evidence

- No locally saved `2025` annual-report PDF in this pass because repeated official IR static-file fetches timed out.
- No standalone earnings-call transcript artifact is saved locally in this pass.
