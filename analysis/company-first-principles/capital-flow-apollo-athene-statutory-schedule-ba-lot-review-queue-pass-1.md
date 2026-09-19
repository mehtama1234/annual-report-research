# Apollo/Athene Schedule BA same-identifier lot review queue pass 1

This queue prioritizes only the strongest quantitative continuity screens from the corrected Schedule BA Part 3 ledger. It is a review queue, not a promoted asset-lot or cash-flow conclusion.

The queue contains `4` exact-within-$1 screens and `6` near-within-$1M screens.
Six queue rows have Part 2 acquisition cost approximately twice the Part 3 disposal book value. That pattern is a multi-row or multi-lot warning, not evidence that one identifier maps to one economic lot.

The four exact-within-$1 rows have now received a page-level source-column
review in the [exact-lot page-review pass](capital-flow-apollo-athene-statutory-schedule-ba-exact-lot-page-review-pass-1.md)
and its [structured CSV](data/capital-flow-apollo-athene-statutory-schedule-ba-exact-lot-page-review-pass-1.csv).

| tier | identifier | pages P1/P2/P3 | Part 1 book | Part 3 book | delta | consideration | gain/loss | Part 3 source-row signal |
|---|---|---|---:|---:|---:|---:|---:|---|
| exact-within-$1 | `309601-AE-2` | 5817/5826/5831 | $4,000,000 | $4,000,000 | $0 | $4,000,000 | $0 | Sale; 10/10/2017 -> 09/30/2025 |
| exact-within-$1 | `05565A-DW-0` | 5819/5827/5832 | $4,499,375 | $4,499,375 | $0 | $4,499,375 | $0 | blank-or-not-visible-in-compact-row; 01/01/2025 -> 02/28/2025 |
| exact-within-$1 | `539439-BF-5` | 5819/5828/5833 | $800,000 | $800,000 | $0 | $793,592 | $-6,408 | Sale; 10/27/2025 -> 12/01/2025 |
| exact-within-$1 | `639057-AT-5` | 5820/5828/5833 | $6,245,304 | $6,245,304 | $0 | $6,245,304 | $0 | blank-or-not-visible-in-compact-row; 10/08/2025 -> 12/01/2025 |
| near-within-$1M | `401378-AB-0` | 5817/5826/5831 | $9,937,749 | $9,937,809 | $60 | $9,937,809 | $0 | Sale; 01/26/2017 -> 10/27/2025 |
| near-within-$1M | `89116C-4H-7` | 5820/5828/5834 | $35,027,139 | $35,026,679 | $-460 | $35,026,679 | $0 | blank-or-not-visible-in-compact-row; 09/12/2025 -> 09/30/2025 |
| near-within-$1M | `401378-AA-2` | 5817/5826/5831 | $3,852,349 | $3,857,948 | $5,599 | $3,857,948 | $0 | Sale; 03/07/2018 -> 11/19/2025 |
| near-within-$1M | `018820-AE-0` | 5818/5827/5832 | $45,009,348 | $45,025,653 | $16,305 | $45,025,653 | $0 | blank-or-not-visible-in-compact-row; 08/19/2025 -> 10/21/2025 |
| near-within-$1M | `05254H-AA-2` | 5818/5827/5832 | $12,564,401 | $12,835,599 | $271,198 | $12,835,599 | $0 | blank-or-not-visible-in-compact-row; 01/01/2025 -> 02/28/2025 |
| near-within-$1M | `37187A-AL-8` | 5821/5829/5834 | $1,484,423 | $1,032,840 | $-451,583 | $1,032,840 | $0 | Sale; 06/13/2023 -> 12/31/2025 |

## Required review before promotion

1. Read the exact source row on the Part 1, Part 2, and Part 3 pages and confirm identifier, issuer/description, acquisition/disposal dates, and disposal nature.
2. Determine whether the Part 3 row is a full disposal, partial sale, redemption, transfer, distribution, or tax-free exchange; a same-CUSIP book tie does not resolve that distinction.
3. Locate settlement-account, counterparty, borrower, liability-release, tax/fee, and legal-entity cash evidence. Schedule BA consideration alone does not prove any of those joins.
4. Keep any Apollo distribution or common-owner cash claim separate until the Athene legal-entity-to-parent receipt is independently evidenced.

The underlying ledger is [capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv](data/capital-flow-apollo-athene-statutory-schedule-ba-event-continuity-ledger-pass-1.csv).
