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
| SIG-T1 | AnnualReports verification note for Signet | 2026-08-10 | Aggregator verification note | Confirms `Jewelry Stores` taxonomy and records that AnnualReports was current to `2025` | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/jewelry-stores/signet-jewelers-limited/annualreports-verification.md) |
| SIG-T2 | AnnualReports company-page snapshot | 2026-08-10 | Aggregator page snapshot | Confirms ticker, exchange, sector label, and current archive timing | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/services/jewelry-stores/signet-jewelers-limited/company-page.html) |
| SIG-T3 | Signet IR source-links note | 2026-08-10 | Official-link verification note | Records official IR destinations and explains the Cloudflare block on direct shell capture | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/jewelry-stores/signet-jewelers-limited/ir-source-links.md) |
| SIG-T4 | Signet official-source-links text note | 2026-08-10 | Official-link note | Preserves the main IR destination URLs used during collection | `[Disclosed]` | [official-source-links.txt](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/jewelry-stores/signet-jewelers-limited/official-source-links.txt) |
| SIG-T5 | Signet fiscal 2026 Form 10-K | 2026-03-27 | SEC filing HTML | Core annual filing for fiscal year ended `2026-02-01` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2025-10k.html) |
| SIG-T6 | Signet Q3 FY26 Form 10-Q | 2025-12-05 | SEC filing HTML | Filed quarterly report for quarter ended `2025-11-01` | `[Filed]` | [2025-q3-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2025-q3-10q.html) |
| SIG-T7 | Signet Q3 FY26 earnings 8-K | 2025-12-04 | SEC filing HTML | Wrapper filing for third-quarter fiscal `2026` results | `[Filed]` | [2025-q3-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2025-q3-8k.html) |
| SIG-T8 | Signet Q3 FY26 earnings release exhibit | 2025-12-04 | SEC-hosted earnings exhibit | Exact quarter metrics and category commentary for `Q3 FY26` | `[Filed]` | [2025-q3-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2025-q3-press-release.html) |
| SIG-T9 | Signet Q4 FY26 earnings 8-K | 2026-03-19 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year fiscal `2026` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2025-q4-8k.html) |
| SIG-T10 | Signet Q4 FY26 earnings release exhibit | 2026-03-19 | SEC-hosted earnings exhibit | Exact quarter and full-year fiscal `2026` metrics plus management commentary | `[Filed]` | [2025-q4-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2025-q4-press-release.html) |
| SIG-T11 | Signet Q1 FY27 Form 10-Q | 2026-06-05 | SEC filing HTML | Filed quarterly report for quarter ended `2026-05-02` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2026-q1-10q.html) |
| SIG-T12 | Signet Q1 FY27 earnings 8-K | 2026-06-03 | SEC filing HTML | Wrapper filing for first-quarter fiscal `2027` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2026-q1-8k.html) |
| SIG-T13 | Signet Q1 FY27 earnings release exhibit | 2026-06-03 | SEC-hosted earnings exhibit | Exact quarter metrics, guidance, and category commentary for `Q1 FY27` | `[Filed]` | [2026-q1-press-release.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/2026-q1-press-release.html) |
| SIG-T14 | SEC submissions JSON for Signet | 2026-08-10 | SEC index JSON | Confirms filing sequence, issuer identity, and the quarter chain | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/services/jewelry-stores/signet-jewelers-limited/sec-submissions.json) |

## Reconciliation notes

- AnnualReports is useful here both for taxonomy confirmation and for confirming that the hosted annual archive was current to `2025` when checked on `2026-08-10`.
- The correct trailing-quarter set as of `2026-08-10` is `Q1 FY27`, `Q4 FY26`, and `Q3 FY26`.
- Direct shell fetches to the Signet investor site returned Cloudflare challenge pages. Because of that, the authoritative locally saved evidence chain is the SEC filing set plus the verified official IR URLs recorded in [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/services/jewelry-stores/signet-jewelers-limited/ir-source-links.md).
- The packet is still source-complete for the required window because the annual filing, the last three quarter filings, the `8-K` wrappers, and the SEC-hosted earnings-release exhibits are all saved locally.

## Missing evidence

- No clean local Signet IR HTML or PDF capture of the release pages was preserved because of Cloudflare delivery blocks.
- No local prepared remarks or full earnings-call transcript capture was collected for `Q3 FY26`, `Q4 FY26`, or `Q1 FY27`.
