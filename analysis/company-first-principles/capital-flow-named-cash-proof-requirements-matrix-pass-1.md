# Capital Flow Named Cash Proof Requirements Matrix Pass 1

## Purpose

This pass turns the broad named-cash question into a promotion matrix:

`who paid -> who received -> where booked -> what use -> what cash came back -> who got paid -> what return`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-named-cash-proof-requirements-matrix-pass-1.csv`

The upstream source locator is:

`/cluster/capital-flow-named-cash-proof-source-locator-pass-1.md`

The current closest two-sided bridge is:

`/cluster/capital-flow-bhp-antamina-streaming-proceeds-use-boundary-pass-1.md`

## Short Answer

`Yes. We have a way to find named cash proof, but it is a document-acquisition problem, not a generic research problem. Full proof requires the same named row to join payer cash out, recipient cash receipt, legal-entity booking, source-to-use allocation, debt or collateral waterfall, customer/project/settlement cash back, and a source-backed return model. Current public evidence gives several partial bridges, led by Wheaton/BHP Antamina, but no case yet clears every gate.`

## Required Proof Layers

| Gate | What It Must Answer | Decisive Source Family | First Chase |
|---:|---|---|---|
| 1 | Who paid cash and through what instrument? | cash-flow statement, closing statement, purchase/payment schedule | Wheaton Antamina |
| 2 | Who received the cash and when? | counterparty note, receipt notice, cash-flow source line | BHP Antamina |
| 3 | Which legal entity booked the asset, liability, income, or obligation? | statutory schedule, subsidiary financials, liability rollforward | BHP / Apollo / KKR |
| 4 | Which dollars funded which use? | treasury source/use ledger, board allocation memo, borrowing notice | BHP / PBF |
| 5 | Did cash repay capital providers? | debt-service waterfall, lender schedule, restricted-account waterfall | Wheaton / Cheniere |
| 6 | Did customers or ratepayers pay cash? | billing determinants, rate-class usage, customer receipt ledger | FPL Distribution Inspection |
| 7 | Was collateral legally available? | borrowing-base certificate, eligible collateral schedule, LTV certificate | URI / Liberty |
| 8 | What cash did the funded asset generate? | project EBITDA/DCF, asset cash ledger, billing attribution | Cheniere / Energy Transfer |
| 9 | Did deliveries settle in units and cash? | invoices, metal-credit ledger, realized-price bridge | Wheaton/BHP Antamina |
| 10 | Was the investment paid back or value-accretive? | IRR, NPV, payback, ROIC, earned-return workpaper | Wheaton / FPL |
| 11 | Did backlog or revenue become cash? | receivable aging, retainage, contract asset/liability rollforward | MasTec / Sterling |
| 12 | Can one named row join every gate? | joined proof package | Antamina first, FPL second, PBF third |

## Current Closest Case

Wheaton/BHP Antamina is the closest end-to-end candidate because it now has both sides of the initial cash transfer:

`Wheaton paid 4.300B USD -> BHP received 4.300B USD -> BHP recorded a financing cash inflow and streaming liability`

That is still not full named cash proof. The missing Antamina package is:

1. BHP use-of-proceeds allocation.
2. Wheaton/BHP PMPA-only delivery and settlement ledger.
3. Lender schedule, borrowing notices, and debt-service waterfall.
4. Antamina production forecast, reserve/resource support, silver-price assumptions, and discount rate.
5. IRR, NPV, payback, and after-tax/after-financing return model.

## Why Receipts And Waterfalls Matter

The system cannot safely answer `who is investing where and how does the money move` by stopping at AUM, capex, backlog, debt balances, aggregate revenue, or company EBITDA. Those are route clues.

Named cash proof requires documents that reconcile dollars:

- receipts and billing records prove cash collection
- debt waterfalls prove capital-provider payback
- legal-entity schedules prove where assets, liabilities, and income sit
- collateral certificates prove borrowing availability
- settlement ledgers prove contractual delivery/cash mechanics
- return models prove whether cash recovery is enough for the capital and duration

## Promotion Rule

`Promote only when one named row joins source instrument, recipient, legal entity, named use, cash receipt or settlement, payback/legal availability, and return support.`

## Hold Rule

`Hold if any required layer is missing, proxy-only, aggregated above the named asset/project/borrower/facility/legal entity, or visible only as management narrative without reconciliation support.`

## Decision

`named-cash-proof-requirements-matrix-ready-no-full-proof-yet`

The method is explicit and machine-readable. The next work is not another broad scan; it is a targeted acquisition pass against the missing Antamina, FPL, and PBF proof packages.

## Safe Claim

`The capital-flow system now has a named-cash proof requirements matrix. It can identify the document families needed to prove receipts, billing, debt waterfalls, legal-entity schedules, collateral certificates, settlement ledgers, and return models. Current evidence supports partial money-path bridges, especially Wheaton/BHP Antamina, but no case yet proves cash all the way through source, use, receipt or settlement, payback/legal availability, and return.`

## Next Work

1. Run an Antamina proof package acquisition pass for BHP use of proceeds, PMPA settlement ledger, debt waterfall, and return model.
2. Run an FPL proof package acquisition pass for billing determinants, category receipt ledger, source-of-funds allocation, and earned-return workpapers.
3. Run a PBF proof package acquisition pass for redemption settlement, accrued interest, fee/tax treatment, cash-on-hand bridge, and post-redemption liquidity.
