# Capital Flow PBF Official 8-K Financing Mechanics Pass 2

## Purpose

This pass strengthens the PBF refinancing route with the contemporaneous
closing filing and legal-party map. It is an evidence upgrade, not a claim
that a trustee settlement ledger has been obtained.

## Question

`What does the official transaction record prove about issuer, agents, stated use, and financing cash-flow classification?`

## Answer

On May 28, 2026, PBF Holding Company LLC and PBF Finance Corporation issued
$500.0M of 7.250% senior notes due 2034 under an indenture with Wilmington
Trust, National Association as trustee and Deutsche Bank Trust Company
Americas as paying agent, registrar, transfer agent, and authenticating agent.
The closing 8-K reported approximately $492.7M of net proceeds; the later Q2
10-Q reports $492.1M after the subsequent period-end accounting of discount
and offering expenses. The Q2 10-Q also reports that the company redeemed all
$801.6M of 2028 notes on June 25, 2026 at par plus accrued and unpaid interest,
financed with the new-note proceeds and available cash.

The PBF Holding Q2 filing additionally classifies first-half financing cash
flows: $801.6M redemption, $100.0M net revolver repayment, $7.9M deferred
financing costs and other, $36.5M member distributions, and $6.0M finance-lease
payments, offset by $500.0M new-note proceeds, $127.0M PBF LLC contributions,
and $57.5M insurance-premium financing. This is a financing-activities
reconciliation, not an account-level settlement ledger.

## Evidence ledger

| Gate | Official evidence | Current grade | Boundary |
|---|---|---|---|
| Legal issuer | PBF Holding and PBF Finance are co-issuers; named guarantors are listed in the 8-K. | `issuer-and-guarantor-visible` | Does not prove which operating subsidiary supplied settlement cash. |
| Transaction agents | Wilmington Trust is trustee; Deutsche Bank Trust Company Americas is paying agent, registrar, transfer agent, and authenticating agent. | `agent-route-visible` | Does not prove the agent’s actual payment file or holder-level distribution. |
| New debt source | $500.0M 7.250% senior notes due 2034 issued May 28, 2026. | `source-instrument-visible` | Does not prove investor allocation or final cash receipt by account. |
| Net proceeds reconciliation | Closing 8-K: ~$492.7M; Q2 10-Q: $492.1M after discount and offering expenses. | `gross-to-net-period-reconciled` | Difference is not decomposed into a final fee schedule here. |
| Stated use | Net proceeds plus available cash funded full redemption of 2028 notes. | `documented-source-use-visible` | Does not prove source priority or precise available-cash account. |
| Redemption mechanics | $801.6M principal redeemed June 25, 2026 at 100% plus accrued and unpaid interest through, but excluding, redemption date. | `redemption-formula-visible` | Does not prove exact accrued-interest amount paid. |
| Financing cash-flow classification | Q2 PBF Holding filing reconciles issuance, redemption, revolver, costs, distributions, contributions, and insurance-premium financing. | `financing-activity-reconciled` | Does not prove trustee settlement cash, bank wires, or post-close liquidity headroom. |

## Investment-analysis implication

PBF now has documented issuer/agent/source/use and financing-activity
mechanics. This supports a stronger financial-shenanigans control: issuance,
old-note retirement, revolver movement, fees, distributions, contributions,
and insurance-premium financing can be tested as one financing bridge rather
than as isolated favorable facts.

It still does not establish economic value creation. Coupon relief, principal
reduction, reported operating cash flow, and liquidity are not equivalent to
after-tax refinancing NPV or recurring refinery owner cash. Exact settlement,
accrued-interest payment, available-cash source, fee amortization, tax effect,
ABL borrowing-base headroom, and refinery-level normalized return remain open.

## Decision

`pbf-official-mechanics-upgrade-settlement-ledger-and-refinancing-npv-hold`

## Official sources

- [PBF Energy Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1534504/000153450426000030/pbf-20260630.htm)
- [PBF Holding Q2 2026 Form 10-Q](https://www.sec.gov/Archives/edgar/data/1566097/000156601126000009/pbf-20260630.htm)
- [PBF May 28, 2026 closing 8-K](https://www.sec.gov/Archives/edgar/data/1534504/000119312526245390/d16410d8k.htm)
- [PBF pricing announcement, Exhibit 99.1](https://www.sec.gov/Archives/edgar/data/1534504/000119312526239766/d149642dex991.htm)
