# Apollo–Athene named issuer source-acquisition boundary

Research date: `2026-09-16`

This pass preserves two public issuer/wrapper documents that sit directly
behind the highest-leverage same-CUSIP routes: Apollo's AMAPS product
description and Concord's 2025 music-rights ABS announcement.

| Route | What the local artifact establishes | What remains unproven |
| --- | --- | --- |
| AMAPS | Apollo describes AMAPS as a structured-credit vehicle intended to combine diversified corporate and asset-backed collateral with less leverage; the document supplies product-level wrapper context for the Athene `02300A-AA-8` route | Tranche-level collateral, borrower identities, Athene allocation, remittance, liability cost, and asset-level return |
| Concord | Concord reports a `$1.765B` senior-note issuance secured by a catalog of more than `1.3M` copyrights; the document supplies issuer-level collateral and transaction context for the Athene `20633K-AN-8` route | Athene-specific trade/receipt, noteholder remittance, redemption ledger, royalty collections, liability cost, and realized return |
| MF1 2025-B2 / related servicing packet | The public servicing exhibit names `MF1 2026-FL21 LLC` and provides collection-account, record-keeping, default-collateral, and servicing-compensation mechanics; the Athene statutory candidate is separately labeled MF1 2025-B2 / `592918-AA-4` | The 2026-FL21 servicing route cannot be joined to the 2025-B2 statutory row without an offering/CUSIP/legal-owner crosswalk; loan-level collateral, trustee remittance, note waterfall, Athene allocation, liability cost, and property-level borrower cash remain open |
| MF1 2025-B2 data procedures | A public SEC exhibit identifies `23` collateral interests and `74` related mortgaged properties and enumerates loan-level compared/recomputed attributes | The underlying data tape, loan cash flows, trustee remittance, Athene allocation, liability cost, and realized return |
| MF1 2026-FL21 CTSLink | The live MF1CAP page shows the August 18 current cycle, September 18 next cycle, and restricted distribution, bond, collateral, loan, and servicer reports | It is not joined to MF1 2025-B2 / `592918-AA-4`; report access, offering/CUSIP crosswalk, borrower cash, trustee remittance, Athene allocation, and return remain open |

These documents improve the issuer/wrapper and broad use-of-proceeds layer;
they do not turn a statutory disposal row into borrower cash or common-owner
cash. The source paths are recorded in the structured manifest below and are
checked for signature markers by the combined-pilot verifier.

## Primary sources

- [Apollo AMAPS overview](https://www.apollo.com/insights-news/insights/2026/05/introducing-amaps)
- [Concord 2025 ABS announcement](https://concord.com/news/concord-closes-1-765-billion-abs-to-fuel-continued-growth/)

Structured control: [named issuer source manifest](data/capital-flow-apollo-athene-named-issuer-source-acquisition-2026-09-16.csv).

The separate [MF1 remittance-access boundary](capital-flow-apollo-athene-mf1-remittance-access-boundary-2026-09-16.md)
records the current CTSLink report route as located but access-controlled.
The [Concord 2022-1 public-source refresh](capital-flow-apollo-athene-concord-2022-1-public-source-refresh-2026-09-16.md)
adds exact `20633K-AA-6` issuer/instrument cross-checks and official collateral
and use-of-proceeds context, while preserving the Athene settlement boundary.
The [AA Infrastructure Fund 2 public-source refresh](capital-flow-apollo-athene-aa-infrastructure-public-source-refresh-2026-09-16.md)
adds a historical Athene legal-entity and infrastructure-wrapper observation
for `00024D-AL-7`, without inferring current ownership or cash.
The [PK AirFinance public-source refresh](capital-flow-apollo-athene-pk-airfinance-public-source-refresh-2026-09-16.md)
adds the strongest platform-level join so far: Apollo acquired the platform,
Athene acquired its existing loan portfolio, and PK publicly describes the
aircraft/engine collateral and ABS servicing perimeter.

The central map now also includes seven additional named routes: AP Hansel,
AOP Finance Partners, ATLAS Funding 1, AA MMF 1, Apollo Debt Solutions BDC,
VMC Finance 2023-PV1, and FASST 2022-S5. They span a land-rights vehicle,
Apollo-controlled credit wrappers, an exact Apollo BDC debt instrument, a
Varde-linked CMBS, and an RMBS trustee route. Their statuses remain partial or
evidence-insufficient because exact Athene settlement, collateral/borrower
cash, remittance, liability cost, and common-owner residuals are not uniformly
joined.

The highest-leverage next acquisition targets are AP Hansel's settlement and
share-transfer records, Apollo Debt Solutions' trustee/payment history, AOP's
current lot and paydown records, ATLAS Funding 1's offering and waterfall, and
the controlled MF1/FASST trustee reports. These should be acquired in that
order if authorized records become available; public wrapper evidence should
not be mistaken for a completed cash loop.
