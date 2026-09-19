# Apollo–Athene Parent-Receipt Attribution Frontier

Research date: `2026-09-15`

This memo quantifies the unresolved Q-07 attribution variable. Apollo's FY2025
parent-only filing shows `$750M` of proceeds from dividends received matching
`$750M` of proceeds from subsidiary investing distributions. Athene's Q2 2026
filing separately shows an intended `$750M` annual regular common-dividend path,
a `$187M` dividend declared April 20 with a June 15 payment date, and `$375M`
of common dividends paid in H1. Those facts do not prove that Athene funded the
FY2025 Apollo receipt or that any amount became unrestricted common-owner cash.

## Attribution frontier

Applying an attribution rate to the `$750M` parent receipt produces the
following mechanical screen:

| Athene attribution assumption | Mechanical attributed amount |
| ---: | ---: |
| 0% | `$0M` |
| 25% | `$187.5M` |
| 50% | `$375M` |
| 75% | `$562.5M` |
| 100% | `$750M` |

The frontier is sensitivity-only. It does not establish payment date,
receiving account, Athene payer identity, intercompany elimination, ownership
percentage, regulatory availability, or common-owner residual. The
`common_owner_residual_musd` field is therefore intentionally `NA`; preferred,
NCI, debt, tax, HoldCo operating costs, dilution, and capital-allocation claims
must be joined before any residual can be calculated.

## Proof-grade result

| Gate | Result |
| --- | --- |
| Apollo parent receipt | Proven for FY2025 at parent-company context |
| Athene legal dividend path | Proven as dated and legally constrained for Q2 2026 |
| Athene attribution to FY2025 receipt | Not proven |
| Unrestricted HoldCo availability | Not proven |
| Common-owner residual | Not calculated |
| Required next proof | Dated Athene-to-AGM transfer, bank/intercompany ledger, elimination, ownership, and senior-claim waterfall |

## Source artifacts

- [FY2025 parent dividend-receipt upgrade](capital-flow-apollo-fy2025-parent-dividend-receipt-upgrade-2026-09-15.md)
- [Athene Q2 dividend schedule](capital-flow-apollo-athene-q2-dividend-schedule-upgrade-2026-09-15.md)
- [Apollo common-owner bridge](combined-investment-research-pilot-03-apollo-common-owner-bridge.md)
