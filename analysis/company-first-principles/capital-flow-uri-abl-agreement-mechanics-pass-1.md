# Capital Flow URI ABL Agreement Mechanics Pass 1

## Purpose

This pass answers the next narrow URI question:

`Can we move from ABL balance and draw-intensity clues to actual asset-based lending agreement mechanics?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-uri-abl-agreement-mechanics-pass-1.csv`

## Source Upgrade

The prior source-locator pass treated the URI ABL agreement layer as an unresolved document-pursuit gap.

That blocker is partly resolved for the July `2025` ABL reset.

Newly cached official SEC files:

- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-07-11-8k.html`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-07-11-tm2520569d1_ex10-1.htm`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-07-11-tm2520569d1_ex10-2.htm`
- `raw/sec/industrial-goods/rental-leasing-services/united-rentals-inc/2025-07-11-tm2520569d1_ex10-3.htm`

The August `7`, `2025` 8-K was also retrieved and classified. It is a secured term-loan amendment, not the ABL reset.

## What The 8-K Says

The July `11`, `2025` 8-K reports:

- Item `1.01`: entry into a material definitive agreement
- Item `2.03`: creation of a direct financial obligation
- Fifth Amended and Restated Credit Agreement dated July `10`, `2025`
- senior secured asset-based loan facility of `4.500B USD`
- facility availability remains subject to a borrowing base
- ANZ tranche of `175M USD`
- maturity on July `10`, `2030`
- approximately `2.049B USD` drawn as of close of business July `9`, `2025`
- approximately `2.428B USD` available for additional borrowings, net of letters of credit and subject to borrowing-base limitations
- `300M USD` combined letter-of-credit sublimit
- low-spread availability-linked pricing and a `0.20%` unused line fee
- springing minimum fixed charge coverage covenant only when specified availability is below the trigger threshold

## Agreement-Term Rows

| Metric | Value | Why It Matters |
|---|---:|---|
| ABL facility size | `4.500B USD` | Legal facility scale before borrowing-base constraints. |
| Maturity date | July `10`, `2030` | Extends the asset-backed liquidity runway. |
| Drawn at July `9`, `2025` close | `2.049B USD` | Shows real facility use at reset. |
| Availability at July `9`, `2025` close | `2.428B USD` | Shows large disclosed headroom at reset, net of L/Cs. |
| Drawn / stated size | `45.5%` | Simple utilization check before borrowing-base detail. |
| Availability / stated size | `54.0%` | Simple headroom check before borrowing-base detail. |
| ANZ tranche | `175M USD` | Shows jurisdictional segmentation inside the ABL. |
| Canadian revolving-loan sublimit | `250M USD` | Shows non-U.S. borrowing channels are separately bounded. |
| ROW revolving-loan sublimit | `125M USD` | Adds another geographic borrowing constraint. |
| Combined L/C sublimit | `300M USD` | Shows the ABL also supports contingent obligations. |
| Incremental amount floor | `2.000B USD` | Large but uncommitted expansion framework. |
| Term SOFR / EURIBOR / SONIA margin range | `1.000%-1.250%` | Availability-linked ABL pricing. |
| Base-rate / Canadian-prime margin range | `0.000%-0.250%` | Low-margin base-rate path. |
| Unused line fee | `0.20%` | Cost of carrying unused capacity. |
| Springing FCCR | `1.0x` | Covenant only becomes active in low-availability conditions. |
| 10% trigger on stated size | `450M USD` | Orientation threshold, not a substitute for defined availability. |

## Mechanics That Matter

The facility is not just generic corporate debt.

The agreement and security mechanics include:

- a borrowing-base constraint
- geographic borrower and currency segmentation
- U.S., Canadian, ROW, European, and ANZ borrowing channels
- swingline sublimits by region
- a combined L/C sublimit
- an uncommitted incremental expansion framework
- availability-linked pricing
- a springing fixed-charge covenant tied to low specified availability
- cash dominion mechanics triggered by low specified availability or specified default
- U.S. collateral categories that include accounts, inventory, rental equipment, leases, documents, instruments, and supporting obligations
- Canadian collateral categories that also include accounts, inventory, rental equipment, leases, documents, instruments, supporting obligations, letter-of-credit rights, and general intangibles

## Why This Matters

This upgrades URI from:

`credit-stack-visible / ABL-draw-visible`

to:

`ABL-agreement-term-visible`

for the asset-backed lending wrapper.

That is different from the receivables purchase agreement pass. The receivables pass proves a separate AR securitization wrapper with purchaser groups, reserve formulas, receivables-only repayment language, and true-sale/non-consolidation mechanics.

This ABL pass proves the larger asset-backed revolver wrapper: facility size, maturity, disclosed draw and availability snapshot, sublimits, pricing, springing covenant trigger, cash-dominion trigger, and collateral categories that include rental equipment.

## Safe Claim

`URI now has agreement-term-visible ABL support: a 4.500B USD senior secured asset-based facility maturing July 10 2030, 2.049B USD drawn and 2.428B USD available at the July 2025 reset date, a 300M USD L/C sublimit, availability-linked pricing, a springing 1.0x FCCR covenant tied to a 10% availability trigger, cash-dominion mechanics, and U.S./Canadian collateral categories that include accounts, inventory, and rental equipment.`

## Claims Not To Make Yet

Do not say:

- the current borrowing base is known
- current legal availability is proven beyond the disclosed reset snapshot
- all stated facility size is drawable
- every fleet purchase was funded by the ABL
- advance rates, eligibility cuts, reserves, appraisals, or field-exam marks are known
- fleet ROIC or asset-class returns are proven

## Next Concrete Work

The next URI evidence gates are:

1. Borrowing-base certificates or availability schedules.
2. ABL collateral reports showing eligible rental equipment, eligible inventory, eligible accounts, reserves, and L/C usage.
3. Current legal availability roll-forward from the July `2025` reset to Q2 `2026`.
4. Fleet class utilization, age, OEC, and rental revenue bridge.
5. Growth-versus-replacement rental-capex split.
6. Purchase-level or period-level source-and-use bridge tying cash flow, used-equipment proceeds, ABL usage, AR securitization, and notes to fleet investment.

The immediate follow-on definitions pass is:

`analysis/company-first-principles/capital-flow-uri-abl-borrowing-base-definitions-pass-1.md`
