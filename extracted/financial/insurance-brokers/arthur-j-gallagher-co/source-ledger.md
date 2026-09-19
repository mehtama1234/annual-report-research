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
| AJG-T1 | AnnualReports verification note for Arthur J. Gallagher | 2026-08-10 | Aggregator verification note | Confirms `Insurance Brokers` taxonomy and records that AnnualReports already showed `2025` availability | `[Reported]` | [annualreports-verification.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/annualreports/financial/insurance-brokers/arthur-j-gallagher-co/annualreports-verification.md) |
| AJG-T2 | Gallagher IR source-links note | 2026-08-10 | Official-link verification note | Records the investor home, financials, news pages, and all in-scope release URLs | `[Disclosed]` | [ir-source-links.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/company-ir/financial/insurance-brokers/arthur-j-gallagher-co/ir-source-links.md) |
| AJG-T3 | Gallagher SEC submissions JSON | 2026-08-10 | SEC index JSON | Confirms issuer identity and the annual / trailing-three-quarter filing sequence | `[Filed]` | [sec-submissions.json](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/sec-submissions.json) |
| AJG-T4 | Gallagher 2025 Form 10-K | 2026-02-07 | SEC filing HTML | Core annual filing for the year ended `2025-12-31` | `[Filed]` | [2025-10k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/2025-10k.html) |
| AJG-T5 | Gallagher Q4 2025 earnings 8-K | 2026-01-29 | SEC filing HTML | Wrapper filing for fourth-quarter and full-year `2025` results | `[Filed]` | [2025-q4-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/2025-q4-8k.html) |
| AJG-T6 | Gallagher Q1 2026 Form 10-Q | 2026-05-01 | SEC filing HTML | Filed quarterly report for quarter ended `2026-03-31` | `[Filed]` | [2026-q1-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/2026-q1-10q.html) |
| AJG-T7 | Gallagher Q1 2026 earnings 8-K | 2026-04-30 | SEC filing HTML | Wrapper filing for first-quarter `2026` results | `[Filed]` | [2026-q1-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/2026-q1-8k.html) |
| AJG-T8 | Gallagher Q2 2026 Form 10-Q | 2026-07-31 | SEC filing HTML | Filed quarterly report for quarter ended `2026-06-30` | `[Filed]` | [2026-q2-10q.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/2026-q2-10q.html) |
| AJG-T9 | Gallagher Q2 2026 earnings 8-K | 2026-07-30 | SEC filing HTML | Wrapper filing for second-quarter `2026` results | `[Filed]` | [2026-q2-8k.html](/home/manishmehta/ui-projects/annual-report-research-new-lanes/raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/2026-q2-8k.html) |

## Reconciliation notes

- AnnualReports is current enough to confirm both taxonomy and `2025` annual availability for Gallagher, but company IR and SEC remain the authoritative filing chain.
- The correct trailing-quarter set as of Monday, `2026-08-10`, is `2Q26`, `1Q26`, and `4Q25`.
- The local evidence chain is SEC-heavy in this pass. The official Gallagher IR release URLs were verified and preserved in the IR source note, but the result pages themselves were not saved locally.

## Missing evidence

- No local Gallagher IR HTML or PDF capture was preserved for the `4Q25`, `1Q26`, or `2Q26` release pages in this workspace.
- No local prepared remarks or full earnings-call transcript capture was collected for `4Q25`, `1Q26`, or `2Q26`.

## Current-workspace artifact verification

| Artifact | SHA-256 | Use |
|---|---|---|
| [Gallagher 2025 Form 10-K](/home/mehtama1/git-repo/annual-report-research/raw/sec/financial/insurance-brokers/arthur-j-gallagher-co/2025-10k.html) | `a2fe0864e63cfa5ede50936c866d153ae03f0a5063aeeb661b994aaf427b00ef` | Filed operating, acquisition, goodwill, debt, and cash-flow evidence |
| [Gallagher companyfacts](/home/mehtama1/git-repo/annual-report-research/raw/sec/companyfacts/financial/insurance-brokers/arthur-j-gallagher-co/companyfacts.json) | `4d63033074d3b50107567dc7e5375d7c9d94db490a3ff0d4463503e703dbcf99` | Machine-readable denominator checks |
| [Gallagher company packet](/home/mehtama1/git-repo/annual-report-research/extracted/financial/insurance-brokers/arthur-j-gallagher-co/company-packet.md) | local packet | Organic-growth and business-model context |

The local filing gives the controlling cash bridge: 2025 operating cash flow
of $1.930B, capital expenditures of $145M, and cash paid for acquisitions net
of cash and restricted cash acquired of $15.766B. The $15.766B acquisition
number is not represented consistently in the FY2025 standard companyfacts
tags, so the memo treats the filing table as authoritative and the validator
checks the standard tags that are actually reported.
