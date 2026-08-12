# Source Ledger

Date baseline: 2026-08-10

## Sources

| ID | Source | Date | Type | Why it matters | Tag | Local path |
|---|---|---|---|---|---|---|
| CHE-T1 | AnnualReports.com Chemed verification note | 2026-08-10 | Aggregator verification note | Confirms the company page and records the scope caveat that this is a healthcare-lane packet for a mixed parent company | `[Reported]` | [annualreports-verification.md](/raw/annualreports/healthcare/specialized-health-services/chemed-corporation/annualreports-verification.md) |
| CHE-T2 | Chemed IR source-links note | 2026-08-10 | Official IR verification note | Preserves the annual-report and quarterly-results URL chain | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/healthcare/specialized-health-services/chemed-corporation/ir-source-links.md) |
| CHE-T3 | Chemed SEC submissions JSON | 2026-08-10 collected | SEC index JSON | Confirms issuer identity and the `2025` annual plus `Q4 2025` / `Q1 2026` / `Q2 2026` filing chain | `[Filed]` | [submissions.json](/raw/sec/healthcare/specialized-health-services/chemed-corporation/submissions.json) |
| CHE-T4 | Chemed `2025` annual report page | 2026-08-10 verified | Official IR annual report page | Confirms the official `2025` annual report availability on the company IR site | `[Disclosed]` | [ir-source-links.md](/raw/company-ir/healthcare/specialized-health-services/chemed-corporation/ir-source-links.md) |
| CHE-T5 | Chemed Q4 `2025` results release | 2026-02-25 | Official IR / SEC earnings release | Captures quarter and year-end hospice results plus Medicare Cap context | `[Filed]` | [ir-source-links.md](/raw/company-ir/healthcare/specialized-health-services/chemed-corporation/ir-source-links.md) |
| CHE-T6 | Chemed Q1 `2026` results release | 2026-04-23 | Official IR / SEC earnings release | Captures first-quarter results and raised full-year guidance on stronger VITAS performance | `[Filed]` | [ir-source-links.md](/raw/company-ir/healthcare/specialized-health-services/chemed-corporation/ir-source-links.md) |
| CHE-T7 | Chemed Q2 `2026` results release | 2026-07-28 | Official IR / SEC earnings release | Captures most recent quarter results and guidance increase | `[Filed]` | [ir-source-links.md](/raw/company-ir/healthcare/specialized-health-services/chemed-corporation/ir-source-links.md) |

## Reconciliation notes

- AnnualReports is used for archive confirmation only.
- The packet is archived in the healthcare lane because of `VITAS`, but Chemed is not a pure healthcare company and that mixed parent structure should remain explicit in downstream use.
- The target quarter window is standard for this calendar-year reporter as of `2026-08-10`: `Q2 2026`, `Q1 2026`, and `Q4 2025`.

## Missing evidence

- No standalone annual report PDF or quarterly result PDFs were saved locally in this pass.
- No standalone earnings-call transcript artifact is saved locally in this pass.

