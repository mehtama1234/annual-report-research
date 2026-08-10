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

## Missing evidence

- No quarter PDF or annual-report PDF was saved locally because direct official static-file fetches stalled from this shell.
- No earnings-call transcript is saved locally for WESCO.
- No standalone SEC filing HTML is saved locally because direct archive requests failed from this shell.
