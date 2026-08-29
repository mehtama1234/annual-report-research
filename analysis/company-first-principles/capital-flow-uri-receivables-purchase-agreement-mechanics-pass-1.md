# Capital Flow URI Receivables Purchase Agreement Mechanics Pass 1

## Purpose

This pass answers the next narrow URI question:

`Can we move from debt-note collateral clues to actual receivables facility agreement mechanics?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-receivables-purchase-agreement-mechanics-pass-1.csv`

## Source Upgrade

The prior source-locator pass treated the June `18`, `2026` URI 8-K as blocked because the local retrieval artifact was the SEC automated-tool page.

That blocker is resolved for this document family.

Newly cached official SEC files:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-06-18-8k.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2026-06-18-ex10-1-receivables-purchase-amendment.html`

## What The 8-K Says

The 8-K reports:

- Item `1.01`: entry into a material definitive agreement
- Item `2.03`: creation of a direct financial obligation or off-balance-sheet obligation
- Amendment No. `18` to the Third Amended and Restated Receivables Purchase Agreement
- extension of the amended A/R facility expiration to June `18`, `2027`
- possible further extension on a `364`-day basis by mutual agreement
- advances remain constrained by eligible receivables in the collateral pool exceeding outstanding loans by a specified amount
- receivables in the collateral pool remain the lenders' only repayment source
- early termination stops new advances and uses collections on securing receivables to repay outstanding advances
- termination events include payment failure, default, delinquency, dilution, days-sales-outstanding covenants, and breach of the URNA credit-facility financial-ratio covenant

## Agreement-Term Rows

| Metric | Value | Why It Matters |
|---|---:|---|
| Purchase Limit | `1.500B USD` | Legal cap for receivables-interest purchases, before availability constraints. |
| Bank commitment sum | `1.500B USD` | Named bank commitments reconcile to the purchase limit. |
| Scotia Capital commitment | `455.0M USD` | Largest named bank commitment; Scotia is also administrative agent and Liberty purchaser agent. |
| PNC commitment | `162.5M USD` | Named bank and purchaser agent for itself. |
| MUFG commitment | `310.0M USD` | Named bank and purchaser agent for Gotham. |
| Truist commitment | `162.5M USD` | Named bank and purchaser agent for itself. |
| TD commitment | `310.0M USD` | Named bank and purchaser agent for GTA and Reliant. |
| Regions commitment | `100.0M USD` | Named bank and purchaser agent for itself. |
| Commitment termination date | June `18`, `2027` | Confirms one-year extension from the expiring facility. |
| Upfront fee | `5 bps` | Effectiveness condition based on each related bank commitment. |

## Mechanics That Matter

The facility is not a generic revolver.

The agreement mechanics include:

- seller: United Rentals Receivables LLC II
- originator: United Rentals (North America), Inc.
- collection agent: United Rentals, Inc.
- purchaser groups: Liberty Street, Gotham, GTA, and Reliant
- banks and purchaser agents: Scotia, PNC, MUFG, Truist, TD, and Regions
- purchase limit and bank commitment caps
- receivables-interest formula using capital, yield reserve, loss reserve, collection-agent fee reserve, dilution reserve, and net receivables pool balance
- loss reserve with stress-factor and minimum-reserve mechanics
- dilution reserve with expected-dilution, dilution-volatility, and dilution-horizon mechanics
- concentration percentage table by obligor rating class
- default, delinquency, dilution, and days-sales-outstanding tests
- true-sale and non-consolidation opinions as effectiveness conditions

## Why This Matters

This upgrades URI from:

`credit-stack-visible`

to:

`receivables-agreement-term-visible`

for the AR securitization wrapper.

That is different from Sterling's L/C and surety wrapper.

URI has reusable fleet assets and receivables. Its public funding proof now includes a legally structured receivables purchase facility with purchaser groups, bank commitments, reserve formulas, and receivables-only repayment language.

Sterling's proof is about backlog, contract timing, revolver flexibility, L/C capacity, and surety/bonding mechanics.

## Safe Claim

`URI now has agreement-term-visible support for the receivables securitization wrapper: a 1.500B USD purchase limit, named bank commitments, June 18 2027 commitment termination date, receivables-only repayment source, reserve formulas, reporting mechanics, and termination tests.`

## Claims Not To Make Yet

Do not say:

- the ABL borrowing base is fully proven
- URI's full legal availability is known
- all AR excess collateral is drawable cash
- fleet purchases can be assigned to the receivables facility
- fleet ROIC or asset-class returns are proven
- the current monthly report inputs are known

## Next Concrete Work

The next URI evidence gates are:

1. ABL agreement extraction.
2. ABL borrowing-base certificates or availability schedules.
3. Annex E monthly report values for the receivables facility.
4. Collateral reports showing eligible receivables, reserves, loss ratio, dilution ratio, delinquency ratio, and DSO.
5. Fleet class utilization, growth/replacement capex, and return bridge.
