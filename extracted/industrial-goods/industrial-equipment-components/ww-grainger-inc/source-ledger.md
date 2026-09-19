# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| GWW-T1 | AnnualReports.com Grainger company page | 2026-08-10 | Aggregator page | Confirms Industrial Equipment Wholesale / Industrial Goods classification and archive lag | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/industrial-equipment-components/ww-grainger-inc/company-page.html) |
| GWW-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Preserves taxonomy and lag observation in repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/industrial-goods/industrial-equipment-components/ww-grainger-inc/annualreports-verification.md) |
| GWW-T3 | Grainger official IR verification note | 2026-08-10 | Verification note | Records the official annual and quarter chain under shell-side rate limits | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/industrial-equipment-components/ww-grainger-inc/official-ir-verification.md) |
| GWW-T4 | Grainger 2026 Company Snapshot | 2026-02-19 | Company snapshot PDF | Official year-end `2025` operating snapshot and segment framing | `[Disclosed]` | [2026-company-snapshot.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/industrial-equipment-components/ww-grainger-inc/2026-company-snapshot.pdf) |
| GWW-T5 | Grainger 2025 Company Snapshot | 2025-02-13 | Company snapshot PDF | Prior-year comparison point for 2024 structure and end-market mix | `[Disclosed]` | [2025-company-snapshot.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/industrial-goods/industrial-equipment-components/ww-grainger-inc/2025-company-snapshot.pdf) |
| GWW-T6 | Grainger SEC submissions feed | 2026-08-10 | SEC metadata JSON | Authoritative chronology for the `10-K`, `ARS`, `10-Q`, and latest `8-K` | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-components/ww-grainger-inc/sec-submissions.json) |
| GWW-T7 | Grainger SEC access verification note | 2026-08-10 | Verification note | Documents blocked direct SEC archive access while preserving chronology | `[Filed]` | [sec-access-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/industrial-goods/industrial-equipment-components/ww-grainger-inc/sec-access-verification.md) |

## Reconciliation notes

- Grainger now has a workable annual and quarter evidence chain for CLI 8 scope:
  - AnnualReports taxonomy confirmation
  - official year-end `2025` company snapshot
  - verified official quarter-result pages for `Q2 2026`, `Q1 2026`, and `Q4 2025`
  - SEC chronology via the saved submissions feed
- This packet relies on verified official IR pages for detailed quarter metrics because direct shell capture of those pages returned `429`.
- The local annual evidence is a company snapshot rather than a full annual-report PDF, but the official IR and SEC chain prove the `2025` annual cycle and provide enough year-end operating substance for this frontier packet.

## Missing evidence

- No full `2025` annual-report PDF is saved locally for Grainger.
- No earnings-call transcript is saved locally for Grainger.
- No standalone SEC filing HTML is saved locally because direct archive requests returned `403`.

## Current repository filing verification artifacts

| Artifact | Current path | SHA-256 |
|---|---|---|
| FY2025 Form 10-K | [2025-10k.html](/home/mehtama1/git-repo/annual-report-research/raw/sec/industrial-goods/industrial-equipment-components/ww-grainger-inc/2025-10k.html) | `6d453e86ce7328e35074ce0b9f5f729fb41bfe6300647bc46ab4b26029a1949d` |
| FY2025 companyfacts | [companyfacts.json](/home/mehtama1/git-repo/annual-report-research/raw/sec/companyfacts/industrial-goods/industrial-equipment-components/ww-grainger-inc/companyfacts.json) | `8d3ec595bc350ee93c25f411d8403337bf3535f81f761009d232be61774bb52b` |
