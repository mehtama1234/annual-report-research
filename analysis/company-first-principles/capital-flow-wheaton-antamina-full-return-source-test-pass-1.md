# Capital Flow Wheaton Antamina Full Return Source Test Pass 1

This page executes cash-return source work-order row `CFCRSWO-001`.

The question is:

`Can Wheaton Antamina move from strongest named source/use/cash-return proxy to full PMPA return proof using the current local source set?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-wheaton-antamina-full-return-source-test-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-cash-return-source-work-order-pass-1.md`

## Short Answer

`No full upgrade yet. Wheaton Antamina remains the strongest named source/use/cash-return proxy, but current local evidence still does not prove full PMPA return.`

The current local stack proves the strongest source/use/cash-proxy chain in the system: Wheaton paid `4.300B USD` for the BHP Antamina PMPA, funded the period with cash on hand, a `1.500B USD` term loan, and revolver borrowings, and reports Antamina stream-level H1 `2026` revenue, cost, depletion, profit, operating cash flow, and asset carrying value.

The critical proxy metrics remain:

- `277.563M USD` H1 `2026` Antamina revenue
- `55.340M USD` H1 `2026` cost of sales excluding depletion
- `51.322M USD` H1 `2026` depletion
- `170.901M USD` H1 `2026` profit after depletion
- `222.223M USD` H1 `2026` operating cash flow
- `4.708329B USD` Antamina asset carrying amount at `2026-06-30`
- `10.336%` mechanical annualized OCF/upfront-payment proxy
- `7.949%` mechanical annualized profit/upfront-payment proxy

That is not the same as full return proof. The current local source set still lacks delivered-ounce schedule, cash receipt detail, Antamina-specific income tax, Antamina-specific interest expense, debt-service waterfall, lender allocation, reserve-life sufficiency, IRR, and NPV.

## Source-Test Result

| Gate | Result | Meaning |
|---|---|---|
| Named cash use | Pass | The `4.300B USD` Antamina PMPA payment is visible. |
| Financing context | Pass | Term loan, revolver, bank debt drawn/repaid, and cash context are visible. |
| Stream economics | Pass | Revenue, cash cost, depletion, profit, OCF, and asset denominator are visible. |
| Return proxy | Pass with boundary | OCF/upfront-payment and profit/upfront-payment proxies are derivable. |
| Delivered ounces/cash receipts | Hold | Actual Antamina delivery and receipt schedule is missing. |
| Tax and interest allocation | Hold | Only company-level tax and finance costs are visible. |
| Debt-service waterfall | Hold | Principal-scale comparisons exist, but DSCR and waterfall are missing. |
| Reserve-life and valuation model | Hold | Life-of-mine language exists, but mine plan, reserve profile, IRR, and NPV are missing. |

## Decision

`full-return-source-test-hold-with-strong-proxy`

The work-order row `CFCRSWO-001` is executed from local evidence. The result is not a full promotion. It confirms that Wheaton Antamina is the best current end-to-end cash-return proxy and defines the exact source package still needed for full PMPA return proof.

## Safe Claim

`Wheaton Antamina has the strongest current named source/use/cash-return proxy in the capital-flow system: a 4.300B USD Antamina PMPA payment, same-period bank-debt funding context, stream-level H1 2026 revenue, cash cost, depletion, profit, operating cash flow, asset carrying value, and bounded annualized cash/profit yield proxies. Current local evidence still does not prove delivered-ounce cash receipts, Antamina-specific tax, Antamina-specific interest, debt-service waterfall, lender allocation, reserve-life sufficiency, IRR, NPV, or full PMPA return.`

## Next Source Package

1. Antamina delivery schedule and cash receipt support.
2. Antamina realized price and delivered-ounce bridge.
3. Antamina-specific tax allocation or explicit company disclosure that no asset-level allocation is available.
4. Term-loan and revolver debt-service schedule with borrowing notices.
5. Lender allocation and funds-flow support for the Antamina payment.
6. Antamina reserve/mine-life support and a PMPA valuation model.
