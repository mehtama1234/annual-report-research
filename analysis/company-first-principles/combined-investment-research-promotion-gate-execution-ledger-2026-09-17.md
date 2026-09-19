# Combined investment research promotion-gate execution ledger

Research date: `2026-09-18`

## Purpose

This ledger converts the current handoff into executable promotion tests. A
lane may move from qualified to promoted only when the named object is tied to
the same legal entity and period, its cash or claim is identified, and the
reconciliation path is observable. A new narrative, market screen, or nearby
proxy is not a substitute for the target object.

## September 18 continuation refresh

The latest continuation adds controlled denominator and expectation surfaces
without changing any promotion grade:

- Retail CA-06 now has separate known-growth-floor, H1 attached-services, and
  supplier-finance settlement frontiers. They preserve mixed property spending,
  consolidated service revenue, period-end obligations, and legal-owner claims
  as non-promoted inputs.
- The physical-capacity cohort now has period-aware Equinix/Digital Realty
  expectation screens; the distinction between full-year recurring-capex guide
  and H1 recurring capex is recorded explicitly.
- Materials and Applied Materials now have dated expectation screens with
  working-capital, refund, contract-liability, China, customer-concentration,
  qualification, and dilution boundaries.
- The [current expectation-screen index](combined-investment-research-current-expectation-screen-index-2026-09-18.md)
  and [structured companion](data/combined-investment-research-current-expectation-screen-index-2026-09-18.csv)
  consolidate those diagnostic screens without ranking unlike denominators.

The next promotion objects remain source-specific: BHP metal-credit receipt and
Wheaton allocation, retail settlement/capex/service/lease-tax schedules, URI
borrowing-base certificate and source-to-purchase flow, and named project or
cohort return schedules. No market screen substitutes for any of them.

## Gate register

| Gate | Current evidence | Next source object | Promotion test | Stop rule |
|---|---|---|---|---|
| Q-03 Wheaton–Antamina | Metal-credit mechanism and Wheaton receivable classes are separated; the April 1 `$4.3B` upfront payment and buyer funding mix are now joined, but no BHP-only recurring receipt is identified | BHP credit issuance, sale/receivable, Wheaton bank receipt, tax and facility-allocation ledger | Match BHP outflow/receivable or sale to Wheaton collection in the same period and allocate tax/financing | Do not repeat broad search without a new settlement, delivery, reserve, or lender document |
| CA-06 / Q-04–Q-06 retail | H1 denominator, supplier-finance, attached-service and legal-owner boundaries are controlled | Matched payment/settlement, maintenance-capital, lease/tax, or service collection/cost schedule | Reconcile the named retail cash object to OCF and common-owner cash without annualizing unmatched balances | Do not subtract period-end balances again or add service revenue one-for-one |
| Q-13 URI asset-backed | Fleet cash, resale recovery, facility capacity and stress variables are visible | Populated borrowing-base certificate, NOLV/reserve schedule, source-to-purchase draw and lifecycle return | Tie legal availability and draw proceeds to collateral, reserve and lifecycle cash return | Do not treat capacity, NBV, OEC or resale proceeds as legal availability or owner cash |
| PBF refinancing | June redemption source/use and September proposed refinancing are separated | Trustee settlement, accrued interest, cash split, fees/taxes, post-redemption liquidity and refinery cash | Reconcile settlement cash and liability cost, then test refinancing NPV and refinery-level residual | Do not treat coupon relief or company OCF as refinancing NPV |
| Private credit | Bear, Concord and Frontline role and waterfall boundaries are explicit | Credit agreement, lender allocation, custody/trustee remittance, closing funds flow, debt service and repayment | Match named lender funding through borrower receipt, debt service and repayment | Do not rank statutory interest, wrapper, fair value or arranger routes as funded cash |
| Physical capacity | URI, Equinix and Digital Realty comparison and stress workbench exist | Project commencement/yield, replacement capital, JV/private funding, dilution and residual schedule | Tie capacity to a named project, stabilized return, funding source and diluted common residual | No pooled physical-capacity multiple |
| Healthcare distribution | McKesson, Cencora and Cardinal period-labeled cash and burden controls exist | Matched quarters, OneOncology post-close cohort cash, Solaris return/legal schedule or owner allocation | Reconcile acquisition/legal claims and working capital to post-close common-owner cash | Do not rank unlike fiscal periods or treat adjusted FCF/OCF as owner cash |
| Medical devices | Stryker, Intuitive and Henry Schein funding and acquisition controls exist | Inari cohort return, lease collection, restructuring cash, collateral or diluted per-share schedule | Join the named cohort or funding route to cash realization and per-share residual | Do not promote utilization or acquisition timing without same-entity cash joins |
| KLA / semiconductor | Five-year cycle panel and installed-base filing boundary exist | Numeric systems-in-field, utilization, renewal, service-per-system and factoring unwind | Reconcile service denominator and factoring-adjusted cash across a full cycle | Do not use bookings, backlog or reported FCF as normalized owner cash |
| Power grid / insurance | Route-visible diagnostics and current packets exist | FPL category receipts, utility recovery/project obligations or named insurance remittance | Match customer/insured obligation to collected cash, cost and owner allocation | Stop on searched-negative route until a new primary schedule appears |
| Atwell infrastructure services | Advent equity and BofA-led facility route is separated from Ares/Frontline | Atwell credit agreement, draw notices, lender allocation, borrower financials and repayment | Prove facility funding, borrower receipt, debt service and repayment for Atwell itself | Do not use Atwell to fill another lender-allocation gap |
| Restaurant franchising | CAVA, RBI, Wingstop, Yum, McDonald's and Chipotle control points exist | Royalty/advertising reconciliation, franchisee health, maintenance/growth capex, support/lease burden and diluted cash | Tie franchisee economics and franchisor collections to maintenance-adjusted common-owner cash | Do not use systemwide sales, store count or mechanical OCF-less-PP&E |
| Integrated oil & gas | ConocoPhillips and Exxon H1 production, cash, capital, claims and returns are separated | Reserve replacement, maintenance/development allocation, realized price/netback, claims, debt and diluted residual | Reconcile through-cycle production economics to replacement-adjusted common-owner cash | Do not treat production, segment earnings, dividends or repurchases as owner cash |

## Operating rule

The ledger is a routing control, not a ranking table. `qualified` means the
route and confounds are understood; `promotion-ready` requires the source
object and reconciliation above; `promoted` requires the resulting cash or
claim to survive the relevant QoE, financial-shenanigans, valuation and
liquidity breakers. Until then, retain `owner-cash-open`, `receipt-open`, or
`causal-promotion-open` and record the missing source rather than impute it.

## Decision

The next execution queue is Q-03, CA-06, and URI because each can change a
specific existing proof grade. The other lanes remain live but should advance
only when a filing, agreement, trustee statement, project schedule, or matched
cash record closes its named join.
