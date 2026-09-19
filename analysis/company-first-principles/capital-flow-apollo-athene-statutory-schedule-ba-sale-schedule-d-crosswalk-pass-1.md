# Apollo/Athene BA Sale to Schedule D disposal crosswalk pass 1

The queue contains `57` coordinate-controlled BA rows whose disposal-nature column is `Sale`. `3` distinct BA identifiers have one or more same-CUSIP Schedule D disposal-parser rows; the crosswalk contains `3` identifier matches.

The matched Schedule D parser rows sum to `$112,535,178` of schedule-positioned consideration. This is not a consolidated cash total: duplicate identifiers, parser-derived columns, differing dates, transfers, and lot boundaries remain unresolved.

| BA page | CUSIP | BA dates | BA consideration | Schedule D part/page | D date | D disposition | D consideration | D cash-likeness |
|---:|---|---|---:|---|---|---|---:|---|
| 5830 | `00455*-AA-8` | 01/01/2025 → 03/27/2025 | 50,908,577 | Schedule D Part 4/6275 | 01/01/2025 | Security Withdraw | 50,955,599 | noncash-or-transfer-hold |
| 5830 | `00455*-AB-6` | 01/01/2025 → 03/27/2025 | 37,629,644 | Schedule D Part 4/6275 | 01/01/2025 | Security Withdraw | 37,389,504 | noncash-or-transfer-hold |
| 5834 | `225401-BJ-6` | 02/05/2025 → 12/01/2025 | 5,156,849 | Schedule D Part 5/6306 | 10/08/2025 | UBS 10/14/2025 MORGAN STANLEY & CO INTERNATI | 24,190,075 | cash-like-candidate |

## Interpretation boundary

A same-CUSIP match is a useful route-finding clue because the BA population includes debt-style assets transferred from Schedule D. It does not establish same-lot identity, chronological direction, cash settlement, borrower repayment, legal-entity cash receipt, liability release, tax/fee treatment, or Apollo distribution. The Schedule D disposal parser itself remains subject to its documented positional-column boundaries.

The underlying queues are [BA Sale queue](capital-flow-apollo-athene-statutory-schedule-ba-sale-review-queue-pass-1.md) and the [Schedule D disposal parser data](data/capital-flow-apollo-athene-statutory-schedule-d-disposal-proceeds-parser-pass-1.csv).
