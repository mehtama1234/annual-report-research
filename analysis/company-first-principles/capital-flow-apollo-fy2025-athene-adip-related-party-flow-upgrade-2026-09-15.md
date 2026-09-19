# Apollo FY2025 Athene/ADIP Related-Party Flow Upgrade

Research date: `2026-09-15`

This pass joins the rendered related-party table to its XBRL context. The table
is titled `Contributions from ADIP` and `Distributions to ADIP`; the relevant
facts use context `c-1454`, whose dimensions identify:

- related party: `SubsidiariesMember`
- counterparty: `ApolloAtheneDedicatedInvestmentProgramsMember`
- legal entity: `AtheneMember`

Primary source:

`raw/primary-sources/capital-flow/apollo/fy-2025/apollo-2025-10k.html`

## Filed flow rows

| Related-party row | FY2025 | FY2024 | FY2023 |
| --- | ---: | ---: | ---: |
| Contributions from ADIP | `$466M` | `$954M` | `$996M` |
| Distributions to ADIP | `$444M` | `$920M` | `$539M` |

The FY2025 net direction within this table is mechanically `$22M` more
contributions from ADIP than distributions to ADIP. That arithmetic is only a
within-table flow screen; it is not a cash-return measure and is not netted
against the separate `$750M` parent-company dividend receipt.

## What this adds

This is stronger than a generic related-party exposure label because the annual
filing names both the flow categories and the Athene/ADIP legal-entity context.
It provides a source-backed affiliate-flow route for testing how Apollo/Athene
dedicated investment programs interact with the retirement-services platform.

## Boundary

The table does not establish that the `$444M` distribution was an Athene common
dividend to AGM. It is labeled as a distribution to ADIP, not a parent-company
receipt, and the filing does not join it to the `$750M` parent receipt, an AGM
bank account, an intercompany elimination, regulated capital availability, or a
common-owner residual. It also does not identify underlying borrower cash,
liability cost, or asset-level return.

## Safe grade

`athene-adip-related-party-flow-visible` — named related-party flow rows and
their Athene/ADIP XBRL dimensions are source-backed. Parent attribution,
settlement, liability allocation, and common-owner cash remain open.
