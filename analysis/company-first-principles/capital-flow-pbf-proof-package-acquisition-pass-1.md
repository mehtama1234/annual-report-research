# Capital Flow PBF Proof Package Acquisition Pass 1

## Purpose

This pass executes the next named-cash acquisition path after Antamina:

`PBF 2028 note redemption -> 2034 note source -> available cash bridge -> settlement and refinancing economics`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-pbf-proof-package-acquisition-pass-1.csv`

The upstream requirements matrix is:

`/cluster/capital-flow-named-cash-proof-requirements-matrix-pass-1.md`

The prior PBF bridge is:

`/cluster/capital-flow-pbf-redemption-settlement-bridge-pass-1.md`

## Question

`Can PBF move from completed-redemption-visible status to settlement-ledger and refinancing-value proof?`

## Short Answer

`Partial upgrade, not full proof. PBF now has a tighter transaction cash bridge. Public SEC sources confirm 500.0M USD of 2034 7.25% senior notes, 492.1M USD of net proceeds, a conditional full-redemption notice for all 801.6M USD of 2028 6.00% senior notes, completed redemption on June 25 2026, and use of 2034 note proceeds plus available cash. The 2028 indenture also makes accrued interest contractually derivable because the notes pay on February 15 and August 15 and use a 360-day year of twelve 30-day months. That produces a derived accrued-interest proxy of about 17.368M USD and a derived total redemption cash proxy of about 818.968M USD before any undisclosed settlement details. This is still not trustee settlement-ledger proof or after-tax refinancing-value proof.`

## Cash Bridge

| Step | Evidence | Amount / Result | Status |
|---|---|---:|---|
| New note source | 2034 `7.250%` Senior Notes issued by PBF Holding / PBF Finance. | `500.0M USD` | `new-note-source-visible` |
| Net proceeds | Q2 2026 10-Q net proceeds after initial purchaser discount and offering expenses. | `492.1M USD` | `gross-to-net-proceeds-visible` |
| Old note principal | 2028 `6.00%` Senior Notes fully redeemed. | `801.6M USD` | `completed-redemption-visible` |
| Redemption price | Conditional notice and 10-Q say par plus accrued and unpaid interest. | `100% + accrued interest` | `redemption-formula-visible` |
| Accrued interest proxy | 2028 indenture: Feb. 15/Aug. 15 interest dates; 30/360 convention; redemption June 25 excluding redemption date. | `~17.368M USD` | `contractual-accrued-interest-proxy-visible` |
| Total redemption cash proxy | Principal plus derived accrued-interest proxy. | `~818.968M USD` | `total-redemption-cash-proxy-visible` |
| Available cash proxy | Total redemption cash proxy less `492.1M USD` net proceeds. | `~326.868M USD` | `available-cash-bridge-proxy-visible` |
| Simple annual coupon relief | Old annual coupon `48.096M USD`; new annual coupon `36.250M USD`. | `~11.846M USD` | `simple-coupon-relief-visible` |
| Cost markers | Deferred financing costs/other plus extinguishment loss. | `7.9M USD`; `2.2M USD` | `cost-markers-visible` |
| Legal ranking | New notes are senior unsecured and effectively subordinated to secured debt to collateral value. | boundary visible | `legal-ranking-visible` |

## What Improved

PBF no longer sits at a principal-only cash bridge. The public record now supports this bounded estimate:

`500.0M USD gross notes -> 492.1M USD net proceeds -> 801.6M USD old-note principal + ~17.368M USD accrued interest proxy -> ~326.868M USD available-cash contribution proxy`

That is materially stronger than saying only that PBF refinanced debt.

## What Still Blocks Full Named Cash Proof

The exact settlement layer is still not public/current:

1. trustee redemption statement
2. paying-agent cash transfer
3. final accrued-interest amount paid
4. exact available-cash account source
5. fee amortization schedule
6. tax treatment of extinguishment loss and fees
7. pro forma interest schedule and after-tax NPV
8. ABL availability or borrowing-base certificate before and after the redemption
9. refinery-level recurring cash contribution

## Decision

`pbf-refinancing-proof-package-partial-upgrade-settlement-npv-hold`

PBF improves to a principal-plus-accrued-interest proxy bridge. It is still not full settlement-ledger, ABL availability, after-tax refinancing-value, or refinery-return proof.

## Safe Claim

`PBF's 2026 refinancing now has a tighter public cash bridge. SEC filings show 500.0M USD of 2034 7.25% notes, 492.1M USD of net proceeds, full redemption of 801.6M USD of 2028 6.00% notes on June 25 2026, and use of new-note proceeds plus available cash. The 2028 indenture supports a derived accrued-interest proxy of about 17.368M USD, implying a total redemption cash proxy of about 818.968M USD and an available-cash bridge proxy of about 326.868M USD. This still does not prove trustee settlement cash, exact available-cash source, fee/tax treatment, ABL availability, after-tax NPV, or refinery-level return.`

## Next Source Package

1. Trustee redemption statement or paying-agent confirmation for the 2028 notes.
2. Final accrued-interest cash paid at redemption.
3. Treasury source/use ledger showing exact available-cash account contribution.
4. Debt issuance cost and fee amortization schedule.
5. Tax treatment for extinguishment loss and financing costs.
6. Pro forma debt-service and after-tax refinancing NPV model.
7. ABL borrowing-base certificate, availability schedule, and collateral cushion.
8. Refinery-level normalized cash contribution.
