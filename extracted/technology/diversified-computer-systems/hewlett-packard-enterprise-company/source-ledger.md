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
| HPE-T1 | AnnualReports legacy taxonomy verification | 2026-08-12 | Aggregator verification note | Confirms that AnnualReports still resolves through the legacy `Hewlett-Packard Company` page and is usable only for taxonomy context | `[Disclosed]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/technology/diversified-computer-systems/hewlett-packard-enterprise-company/annualreports-verification.md) |
| HPE-T2 | HPE official IR routing verification | 2026-08-12 | Official IR verification note | Confirms the official annual-reports and quarterly-results pages and records exact issuer-hosted URLs for the annual and in-scope quarter materials | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/technology/diversified-computer-systems/hewlett-packard-enterprise-company/official-ir-verification.md) |
| HPE-T3 | HPE SEC submissions index | 2026-08-12 | SEC index JSON | Confirms accession ordering for the annual anchor and latest three reported quarters | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/sec-submissions.json) |
| HPE-T4 | HPE fiscal `2025` Form 10-K | 2025-12-18 | SEC filing HTML | Core annual filing for the year ended `2025-10-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2025-10k.html) |
| HPE-T5 | HPE fiscal `2025` annual report package | 2026-02-11 | SEC filing PDF | Preserves the adjacent `ARS` annual-report package | `[Filed]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2025-annual-report.pdf) |
| HPE-T6 | HPE `Q4 FY2025` earnings release | 2025-12-04 | SEC exhibit HTML | Preserves the official fourth-quarter and full-year results release | `[Filed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2025-q4-press-release.html) |
| HPE-T7 | HPE `Q4 FY2025` 8-K | 2025-12-04 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2025-q4-8k.html) |
| HPE-T8 | HPE `Q1 FY2026` earnings release | 2026-03-09 | SEC exhibit HTML | Preserves the official first-quarter `2026` results release | `[Filed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2026-q1-press-release.html) |
| HPE-T9 | HPE `Q1 FY2026` 8-K | 2026-03-09 | SEC filing HTML | Wrapper filing for first-quarter `2026` earnings release | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2026-q1-8k.html) |
| HPE-T10 | HPE `Q1 FY2026` 10-Q | 2026-03-10 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-01-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2026-q1-10q.html) |
| HPE-T11 | HPE `Q2 FY2026` earnings release | 2026-06-01 | SEC exhibit HTML | Preserves the official second-quarter `2026` results release | `[Filed]` | [2026-q2-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2026-q2-press-release.html) |
| HPE-T12 | HPE `Q2 FY2026` 8-K | 2026-06-01 | SEC filing HTML | Wrapper filing for second-quarter `2026` earnings release | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2026-q2-8k.html) |
| HPE-T13 | HPE `Q2 FY2026` 10-Q | 2026-06-02 | SEC filing HTML | Filed quarterly report for the quarter ended `2026-04-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/technology/diversified-computer-systems/hewlett-packard-enterprise-company/2026-q2-10q.html) |

## Reconciliation notes

- The correct trailing-quarter set as of `2026-08-10` is `Q2 FY2026`, `Q1 FY2026`, and `Q4 FY2025`.
- The packet and profile are internally consistent on the filing window:
  - annual anchor: fiscal `2025`
  - latest three reported quarters as of `2026-08-10`: `Q2 FY2026`, `Q1 FY2026`, and `Q4 FY2025`
- The authority ordering is explicit:
  - AnnualReports for taxonomy and archive-lag confirmation only
  - company IR and SEC for the authoritative annual and quarter chain
- The verified chain is now strong enough for local inspection:
  - AnnualReports legacy-page verification note
  - official investor-relations routing note covering the annual and in-scope quarter pages
  - SEC submissions index, annual filing set, in-scope `8-K` wrappers, in-scope earnings-release exhibits, and in-scope `10-Q` filings
- The remaining limitation is narrow:
  - issuer-hosted `investors.hpe.com` HTML pages and PDFs are `403`-blocked to direct shell retrieval in this workspace
  - the exact official URLs are preserved in the IR verification note instead
- The packet is now `proven` because this workspace preserves a rebuilt local annual-plus-quarter evidence chain with direct SEC artifacts and a saved official-IR routing record.

## Missing evidence

- No local prepared-remarks or transcript artifact was preserved for `Q4 FY2025`, `Q1 FY2026`, or `Q2 FY2026`.
