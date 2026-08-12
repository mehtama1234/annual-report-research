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
| THC-T1 | AnnualReports.com Tenet company page | 2026-08-12 | Aggregator page | Confirms Healthcare / Medical Care Facilities taxonomy and archive entry | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/healthcare/medical-care-facilities/tenet-healthcare-corp/company-page.html) |
| THC-T2 | Tenet official IR verification | 2026-08-12 | Official IR verification note | Confirms the issuer financials hub and in-scope press-release routing | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/healthcare/medical-care-facilities/tenet-healthcare-corp/official-ir-verification.md) |
| THC-T3 | Tenet `2025` Form 10-K | 2026-02-17 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2025-10k.html) |
| THC-T4 | Tenet `Q4 2025` earnings release exhibit | 2026-02-11 | SEC exhibit HTML | Exact fourth-quarter and full-year `2025` metrics plus initial `2026` outlook | `[Filed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2025-q4-press-release.html) |
| THC-T5 | Tenet `Q4 2025` 8-K | 2026-02-11 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` earnings release | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2025-q4-8k.html) |
| THC-T6 | Tenet `Q1 2026` earnings release exhibit | 2026-04-30 | SEC exhibit HTML | Exact first-quarter `2026` metrics and initial `2026` outlook | `[Filed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2026-q1-press-release.html) |
| THC-T7 | Tenet `Q1 2026` 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2026-q1-8k.html) |
| THC-T8 | Tenet `Q1 2026` 10-Q | 2026-04-30 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2026-q1-10q.html) |
| THC-T9 | Tenet `Q2 2026` earnings release exhibit | 2026-07-23 | SEC exhibit HTML | Exact second-quarter `2026` metrics and raised `2026` outlook | `[Filed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2026-q2-press-release.html) |
| THC-T10 | Tenet `Q2 2026` 8-K | 2026-07-23 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2026-q2-8k.html) |
| THC-T11 | Tenet `Q2 2026` 10-Q | 2026-07-28 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/healthcare/medical-care-facilities/tenet-healthcare-corp/2026-q2-10q.html) |

## Reconciliation notes

- AnnualReports is used here for taxonomy and archive confirmation.
- The correct trailing-quarter set as of `2026-08-10` is `Q2 2026`, `Q1 2026`, and `Q4 2025`.
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive confirmation
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is now strong enough for local inspection:
  - AnnualReports company page
  - official IR verification note for financials and press-release routing
  - SEC annual filing
  - SEC quarter release exhibits, `8-K` wrappers, and both in-scope `10-Q` filings
- The remaining limitation is narrow:
  - direct shell retrieval attempts to `investor.tenethealth.com` returned `429` in this workspace
  - the official routing and page-level confirmations are preserved in the IR verification note instead
- The packet is now `proven` because this workspace preserves a rebuilt local annual-plus-quarter evidence chain comparable to the cleanest proof-standard packets.

## Missing evidence

- No local prepared-remarks or transcript artifact was preserved for `Q4 2025`, `Q1 2026`, or `Q2 2026`.
