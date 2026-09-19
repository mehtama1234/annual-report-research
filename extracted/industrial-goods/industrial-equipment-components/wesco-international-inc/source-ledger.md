# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| WCC-T1 | AnnualReports.com WESCO company page | 2026-08-10 | Aggregator page | Confirms `Industrial Equipment Wholesale` classification and archive lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/industrial-equipment-components/wesco-international-inc/company-page.html) |
| WCC-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Preserves taxonomy and lag observation in repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/industrial-equipment-components/wesco-international-inc/annualreports-verification.md) |
| WCC-T3 | WESCO official IR verification note | 2026-08-10 | Verification note | Records the official annual and quarter chain | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/industrial-equipment-components/wesco-international-inc/official-ir-verification.md) |
| WCC-T4 | WESCO SEC submissions feed | 2026-08-10 | SEC metadata JSON | Authoritative chronology for the `10-Q`, `10-K`, `ARS`, and latest `8-K` filings | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-components/wesco-international-inc/sec-submissions.json) |
| WCC-T5 | WESCO SEC access verification note | 2026-08-10 | Verification note | Documents blocked direct SEC archive access while preserving chronology | `[Filed]` | [sec-access-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-components/wesco-international-inc/sec-access-verification.md) |

## Reconciliation notes

- WESCO now has a strong annual and quarter evidence chain for CLI 8 scope:
  - AnnualReports taxonomy confirmation
  - official annual and quarter result verification through the live IR stack
  - SEC chronology via the saved submissions feed
- This packet intentionally uses the `2025` annual report year requested by the frontier prompt even though AnnualReports lags at `2024`.
- The latest reported quarter as of `2026-08-10` is `Q2 2026`, filed on `2026-07-30`.

## Current repository filing artifacts

The fiscal 2025 10-K and Q2 2026 10-Q are now preserved in the current
repository SEC tree. Independent XBRL checks on the fiscal 2025 filing
reproduce $125.0M of operating cash flow, $99.8M of capex, $36.1M of net
acquisition payments, $1.233B of operating income, and $40.5M of stock
compensation. The weak post-capex/acquisition residual is therefore filed,
while working-capital normalization and backlog quality remain open.

| Artifact | Current repo path | SHA-256 |
|---|---|---|
| Fiscal 2025 10-K | [2025-10k.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/industrial-goods/industrial-equipment-components/wesco-international-inc/2025-10k.html) | `efcf58ecffc80934e6fb584f1205346dbffd2f2f4241c919911bac5e05c00a61` |
| Q2 2026 10-Q | [2026-q2-10q.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/industrial-goods/industrial-equipment-components/wesco-international-inc/2026-q2-10q.html) | `81d29d86e3d2cf32d875f05074d0d2d86cf6ce82892fca011f77992a562edb58` |

## Missing evidence

- No quarter PDF or annual-report PDF was saved locally because direct official static-file fetches stalled from this shell.
- No earnings-call transcript is saved locally for WESCO.
- No standalone SEC filing HTML is saved locally because direct archive requests failed from this shell.

## Current repository filing verification artifacts

| Artifact | Current path | SHA-256 |
|---|---|---|
| FY2025 Form 10-K | [2025-10k.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/industrial-goods/industrial-equipment-components/wesco-international-inc/2025-10k.html) | `efcf58ecffc80934e6fb584f1205346dbffd2f2f4241c919911bac5e05c00a61` |
| FY2025 companyfacts | [companyfacts.json](/home/mehtama1/git-repo/annual-report-research/raw/sec/companyfacts/industrial-goods/industrial-equipment-components/wesco-international-inc/companyfacts.json) | `f609024246c27782794d64a83e278bf7e2f2c01e03b76215e5c83b261c6779b4` |
