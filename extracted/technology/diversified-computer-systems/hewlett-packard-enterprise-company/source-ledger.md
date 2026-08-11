# Source Ledger

Date baseline: `2026-08-11`

Use evidence tags:

- `[Disclosed]` company filing, press release, or official investor-relations material
- `[Filed]` SEC filing or exhibit
- `[Reported]` credible press or transcript provider
- `[verify]` found but not currently re-openable from this workspace

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Current state |
|---|---|---|---|---|---|---|
| HPE-T1 | AnnualReports legacy company-page reference | inherited | Aggregator reference | Preserves the original taxonomy trail, including lag and legacy naming context | `[verify]` | referenced by inherited packet files, but the linked raw page is not currently inspectable from this workspace |
| HPE-T2 | AnnualReports verification note | inherited | Aggregator verification note | Preserves the original note that current-year AnnualReports coverage lagged and used legacy naming | `[verify]` | referenced by inherited packet files, but the linked raw note is not currently inspectable from this workspace |
| HPE-T3 | Official IR routing and Juniper-close note | inherited | Official-source note | Was intended to preserve issuer-hosted routing links and post-close context | `[verify]` | referenced by inherited packet files, but the linked raw note is not currently inspectable from this workspace |
| HPE-T4 | SEC submissions and companyfacts references | inherited | SEC index references | Support accession ordering and annual metric extraction in the inherited packet build | `[verify]` | referenced by inherited packet files, but the linked raw SEC files are not currently inspectable from this workspace |
| HPE-T5 | Fiscal `2025` annual anchor | `2025-12-18` `10-K`; `2026-02-11` annual-report package | Annual filing set | Establishes the target annual evidence year used in the packet | `[verify]` | packet and profile consistently point to this annual anchor, but the raw annual files need re-collection or path repair before they can be treated as locally proven here |
| HPE-T6 | `Q2 FY2026`, `Q1 FY2026`, and `Q4 FY2025` quarter chain | reported by inherited packet build | Quarterly filing set | Defines the latest three reported quarters used in the packet as of `2026-08-10` | `[verify]` | packet and profile consistently point to this quarter chain, but the raw quarter files need re-collection or path repair before they can be treated as locally proven here |

## Reconciliation notes

- This company packet was inherited with a coherent analytical interpretation but without a currently inspectable local raw chain in this workspace.
- The packet and profile are internally consistent on the filing window:
  - annual anchor: fiscal `2025`
  - latest three reported quarters as of `2026-08-10`: `Q2 FY2026`, `Q1 FY2026`, and `Q4 FY2025`
- The current problem is not lane fit or company relevance.
- The current problem is evidence portability: the packet still points to raw-path references that are no longer locally openable from the present workspace.

## Missing evidence

- The inherited AnnualReports, IR, and SEC raw files referenced by older path links are not currently inspectable from this workspace.
- Until that raw chain is rebuilt or the correct live local paths are restored, this company should not be used as a proof-standard case for the filing-window or source-authority rule.
