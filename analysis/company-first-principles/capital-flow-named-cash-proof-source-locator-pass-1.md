# Capital Flow Named Cash Proof Source Locator Pass 1

## Purpose

This pass answers the practical question:

`Do we have a way to find named cash proof, and where should we look first?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-named-cash-proof-source-locator-pass-1.csv`

The upstream answer brief is:

`/cluster/capital-flow-cfnsaq-publication-safe-answer-brief-pass-1.md`

## Short Answer

`Yes. The method is now explicit: pick a named case, identify the missing proof layer, pursue the specific document family for that layer, and upgrade only when the row joins source, use, cash back, payback/legal availability, and return evidence at named asset, project, borrower, facility, or legal-entity level.`

The current system does not yet have full named cash proof. It does have a source locator that tells us where the proof should live.

## Named Proof Layers

| Rank | Proof Layer | First Target | Needed Document |
|---|---|---|---|
| 1 | Customer receipts and billing | FPL Distribution Inspection | Billing determinants, tariff/factor billing workpapers, category receipt support |
| 2 | Collateral availability certificate | United Rentals fleet | Borrowing Base Certificate, eligible collateral schedule, NOLV/reserve/availability support |
| 3 | Debt waterfall and payback | Wheaton Antamina | Debt-service waterfall, lender allocation, PMPA receipt/paydown support |
| 4 | Project or asset cash contribution | Cheniere / Energy Transfer | Train/entity waterfall, project EBITDA/DCF, SPA or shipper billing attribution |
| 5 | Legal-entity statutory schedule | Apollo/Athene and KKR/Global Atlantic | Schedule D/BA, legal-entity investment income, liability-cost/spread bridge |
| 6 | Borrower facility use of proceeds | Ares / Frontline and private-credit borrowers | Credit agreement, lender schedule, funded tranche, use-of-proceeds, collateral package |
| 7 | Return model | Wheaton / FPL / URI | IRR, NPV, ROIC, reserve life, earned-return, fleet-class return support |
| 8 | Transaction funds flow and source/use | Matador / PBF / Liberty / Devon | Closing funds-flow, redemption settlement, borrowing notice, treasury source/use ledger |

## Closest Public Targets

FPL is closest for customer cash because the local file set already shows Distribution Inspection output, costs, recovery components, aggregate SPPCRC revenue, true-up collection/refund mechanics, and factor authority. The missing proof is narrower: billing determinants, category allocation, and billed or collected cash tied to Distribution Inspection.

URI is closest for collateral availability because the filed ABL agreement already defines the missing Borrowing Base Certificate fields and proves a May `31`, `2025` certificate was delivered as a closing condition. The missing proof is the populated certificate or equivalent lender/rating disclosure.

Wheaton Antamina is closest for named asset economics because the local evidence already ties the `4.300B USD` PMPA use to financing context and stream revenue/cash-cost proxy. The missing proof is the delivered-ounce receipt schedule, tax/interest allocation, lender waterfall, reserve-life support, and full PMPA return model.

## Pass Test

A row reaches named cash proof only if it joins:

1. capital source or provider
2. instrument or channel
3. named destination
4. customer/project/borrower cash back
5. debt-service, payback, or legal-availability evidence
6. return model or earned-return support

Proxy evidence does not pass. AUM, backlog, capex, route rates, aggregate revenue, liquidity, pledged collateral, and company EBITDA are useful clues, but they cannot replace named proof documents.

## Decision

`named-cash-proof-source-locator-ready`

The system now has a concrete source locator for the named cash proof documents: receipts, billing, debt waterfalls, legal-entity schedules, collateral certificates, and return models.

## Safe Claim

`Named cash proof is not yet complete, but the proof route is now defined. The strongest next public targets are FPL billing/receipt support, URI borrowing-base/collateral availability support, and Wheaton Antamina debt-waterfall plus return-model support.`

## Next Work

1. Execute the FPL billing determinant and category receipt search.
2. In parallel or next, execute the URI borrowing-base certificate and collateral availability search.
3. Promote a case only if the named proof document joins the row-level money path end to end.
