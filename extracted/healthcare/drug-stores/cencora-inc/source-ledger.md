# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| COR-T1 | AnnualReports.com Cencora company page | 2026-08-10 | Aggregator page | Confirms company taxonomy and the availability of the `2025` annual package | `[Reported]` | [company-page.html](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/drug-stores/cencora-inc/company-page.html) |
| COR-T2 | AnnualReports verification note | 2026-08-10 | Verification note | Preserves taxonomy and archive confirmation in repo format | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/annualreports/healthcare/drug-stores/cencora-inc/annualreports-verification.md) |
| COR-T3 | Cencora 2025 Annual Report | 2025-11-25 / 2026-08-10 local save | Annual report PDF | Core annual narrative and strategic direction for fiscal `2025` | `[Reported]` | [2025-annual-report.pdf](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/drug-stores/cencora-inc/2025-annual-report.pdf) |
| COR-T4 | Cencora official IR verification note | 2026-08-10 | Verification note | Records the official trailing quarter chain and preserves live official URLs | `[Disclosed]` | [official-ir-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/company-ir/healthcare/drug-stores/cencora-inc/official-ir-verification.md) |
| COR-T5 | Cencora SEC submissions feed | 2026-08-10 | SEC metadata JSON | Authoritative chronology for the `10-K`, `ARS`, `10-Q`, and supporting `8-K` filings | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/drug-stores/cencora-inc/sec-submissions.json) |
| COR-T6 | Cencora SEC access verification note | 2026-08-10 | Verification note | Documents blocked direct SEC archive access while preserving chronology | `[Filed]` | [sec-access-verification.md](/home/manishmehta/ui-projects/annual-report-research-cli8-middle-layer/raw/sec/healthcare/drug-stores/cencora-inc/sec-access-verification.md) |

## Reconciliation notes

- Cencora now has a usable CLI 8 evidence chain:
  - AnnualReports taxonomy and archive confirmation
  - saved `2025` annual-report PDF
  - official IR quarter verification for `Q3 FY2026`, `Q2 FY2026`, and `Q1 FY2026`
  - SEC chronology via the saved submissions feed
- Official Cencora IR pages were rate-limited from this shell, so live quarter evidence is preserved in the official IR verification note rather than in locally saved quarter PDFs.
- The latest reported quarter as of `2026-08-10` is `Q3 FY2026`, filed on `2026-08-05`.

## Missing evidence

- No quarter PDF or earnings-call transcript is saved locally for Cencora.
- No standalone SEC filing HTML is saved locally because direct archive requests failed from this shell.
