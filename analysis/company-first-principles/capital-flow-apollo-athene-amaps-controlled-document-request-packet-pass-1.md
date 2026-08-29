# Capital Flow Apollo Athene AMAPS Controlled-Document Request Packet Pass 1

## Purpose

This pass converts the AMAPS named-cash proof gaps into a request-grade controlled-document packet.

The question is:

`What exact documents are needed to move AMAPS from Apollo/Athene wrapper-and-alignment evidence to collateral, remittance, legal-entity, and return proof?`

The request table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-amaps-controlled-document-request-packet-pass-1.csv`

The diagnostic table is:

`analysis/company-first-principles/data/capital-flow-apollo-athene-amaps-controlled-document-request-packet-diagnostic-pass-1.csv`

The builder is:

`scripts/build-athene-amaps-controlled-document-request-packet.py`

## Current Evidence Base

The upstream AMAPS source acquisition pass already supports:

| Evidence | Value |
|---|---:|
| Athene AMAPS 1 CUSIP | `02300A-AA-8` |
| Athene AMAPS 1 cash-like consideration | `268.000000M USD` |
| Athene AMAPS 1 year-end book value | `1.917500000B USD` |
| Athene AMAPS 1 year-end interest income | `48.871440M USD` |
| Athene AMAPS 1 disposal interest/dividends | `3.986842M USD` |
| Apollo/Athene public AMAPS 1 concentration | `2.550B USD` |
| Current AMAPS status | `platform-wrapper-visible-underlying-collateral-hold` |

That is enough to justify a targeted document request. It is not enough to claim underlying borrower receipt, trustee remittance, Athene allocation, liability spread, or final return.

## Controlled Document Requests

| Rank | Document Family | Cash-Loop Link | Likely Controller |
|---:|---|---|---|
| 1 | AMAPS 1 offering memorandum | legal instrument and source-to-wrapper | Apollo, AMAPS 1 LLC issuer files, Athene investment files, placement agents, rating agencies, note purchasers |
| 2 | tranche supplement and note purchase agreement | CUSIP-specific allocation and trade route | Apollo, AMAPS 1 LLC, Athene investment accounting, broker/dealer, custodian, legal counsel |
| 3 | full rating rationale reports | credit quality, collateral, and waterfall support | rating agencies, Apollo, Athene, state insurance examiners, NAIC/SVO filing route |
| 4 | collateral tape or portfolio schedule | underlying borrower/collateral destination | Apollo manager files, collateral administrator, trustee, rating agencies, investors |
| 5 | trustee remittance and noteholder reports | cash-back and debt-service receipt | trustee, collateral administrator, Apollo manager files, noteholders, custodian |
| 6 | payment waterfall and LTV test support | legal payback route and waterfall | Apollo manager files, trustee, collateral administrator, rating agencies, legal counsel |
| 7 | Athene allocation, trade, and custodian support | Athene receipt and legal-entity cash movement | Athene investment accounting, Apollo insurance asset management, custodian, broker/dealer, state examiners |
| 8 | statutory subsidiary reconciliation | legal-entity booking and consolidation bridge | Athene statutory reporting, Apollo/Athene SEC reporting, auditors, state examiners |
| 9 | liability-cost and return model support | return model | Athene ALM, investment accounting, actuarial, Apollo insurance asset management, auditors |

## Promotion Tests

AMAPS can move beyond wrapper/alignment proof only if the documents show:

1. AMAPS 1 CUSIP `02300A-AA-8` tranche terms, issuance amount, payment dates, maturity, pricing, and noteholder rights
2. Athene legal-entity allocation or trade support for the exact CUSIP
3. AMAPS 1-specific collateral or portfolio schedule
4. underlying obligors or asset groups, balances, marks, and eligibility
5. dated trustee or noteholder cash distributions
6. payment waterfall, LTV test, collateral value, trigger, and reserve mechanics
7. reconciliation between the local `1.917500000B USD` Athene year-end book value and the public `2.550B USD` AMAPS 1 concentration
8. liability-cost, reserve, mark, impairment, and earned-spread support
9. IRR, NPV, ROIC, cash-on-cash, payback, or other return model evidence

## Hold Tests

AMAPS must stay below full named-cash proof if we only have:

1. Apollo product description
2. broad collateral-category language
3. AMAPS market/alignment language
4. AMAPS 5 analog reports instead of AMAPS 1-specific reports
5. consolidated AMAPS 1 concentration without subsidiary allocation
6. statutory CUSIP row without trade/custodian support
7. gross interest income without liability-cost support
8. fair value without cash receipt
9. private-letter-rating context without rating rationale details

## What This Tells Us In Simple Terms

The AMAPS route is now request-ready.

The likely chain is:

`Athene legal entity -> AMAPS 1 Tranche A CUSIP 02300A-AA-8 -> Apollo AMAPS structured-credit wrapper -> pooled corporate and asset-backed credit collateral -> AMAPS payment waterfall -> noteholder remittance -> Athene legal entity -> spread after liability cost`

The current public and statutory evidence proves the early and middle map:

`Athene row -> AMAPS 1 note -> Apollo AMAPS wrapper -> public AMAPS 1 concentration`

The current evidence does not prove the final cash loop:

`underlying borrower cash -> trustee waterfall -> Athene remittance -> spread/return`

## What This Proves

This pass proves:

1. the exact AMAPS document package needed for full proof is identifiable
2. all `9` request rows remain controlled-document-needed
3. all `9` cash-loop links have a request row
4. AMAPS is a platform-wrapper proof case, not a simple borrower/use case
5. the public evidence is strong enough to target AMAPS 1-specific documents, but too weak for final receipt or return claims

## What It Does Not Prove

This pass does not prove:

1. the requested documents have been obtained
2. AMAPS 1 collateral tape
3. underlying borrower receipt or use of proceeds
4. trustee remittance to Athene
5. Athene trade settlement or custodian cash movement
6. subsidiary-level reconciliation to the public AMAPS 1 concentration
7. liability-cost spread
8. payment waterfall performance
9. IRR, NPV, ROIC, payback, or platform profit

## Safe Claim

`The AMAPS named-cash proof route is now request-ready. Public and local evidence identify Athene's AMAPS 1 CUSIP 02300A-AA-8, 268.000000M USD of same-CUSIP cash-like consideration, 1.917500000B USD of year-end book value, 48.871440M USD of year-end interest income, 3.986842M USD of disposal interest/dividends, Apollo's AMAPS wrapper and Athene-alignment description, and Apollo/Athene's 2.550B USD public AMAPS 1 concentration. Full proof now requires nine controlled document families: AMAPS 1 offering memorandum, tranche supplement and purchase support, full rating rationale reports, collateral tape, trustee/remittance reports, payment waterfall and LTV support, Athene allocation/trade/custodian support, statutory subsidiary reconciliation, and liability-cost/return model support.`

## Decision

`amaps-controlled-document-request-packet-ready`

The next move is to execute acquisition attempts in this order:

1. AMAPS 1 full rating rationale reports
2. AMAPS 1 offering memorandum and tranche supplement
3. collateral tape or portfolio schedule
4. trustee/remittance reports and payment waterfall support
5. Athene allocation, custodian, subsidiary reconciliation, and liability-cost support
