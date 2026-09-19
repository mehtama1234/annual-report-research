# Wheaton–Antamina Q-03 quantity-proxy boundary

Research date: `2026-09-18`

## Purpose

This note separates the current BHP-specific contractual and mine-production
denominators from Wheaton's combined Antamina operating table. It is an input
boundary for a future return model, not a delivery or cash-receipt ledger.

The structured companion is the [quantity-proxy CSV](data/capital-flow-wheaton-antamina-q03-quantity-proxy-boundary-2026-09-18.csv).

## Safe mechanical inputs

| Input | Public value | Mechanical use | Boundary |
|---|---:|---|---|
| BHP Antamina interest | `33.75%` | BHP-side mine-production denominator | Not a Wheaton credit or delivery quantity |
| Initial BHP stream share | `33.75%` of payable silver | Contractual pre-threshold share | Still subject to metal-credit issuance and settlement |
| Payable factor | `90%` | Initial mechanical entitlement is `30.375%` of mine production | Not an observed invoice or cash receipt |
| Post-threshold stream share | `22.5%` of payable silver | Post-threshold mechanical entitlement is `20.25%` of mine production | Threshold timing is not disclosed |
| Initial threshold | `100M` delivered ounces | Step-down condition | No minimum/fixed delivery schedule is disclosed |
| BHP FY2026 payable silver | `5.588M` ounces on BHP's `33.75%` interest basis | Mechanical `90%` equivalent: `5.0292M` ounces | Mine production, not BHP-PMPA delivered credits |
| BHP-interest P&P contained silver | `65.7M` ounces | Mechanical `90%` equivalent: `59.13M` ounces | Contained reserves are not payable ounces or a delivery curve |
| Wheaton combined Q2 production | `2.319M` ounces | Combined operating context only | Includes BHP and legacy Glencore streams |
| Wheaton combined Q2 sales | `2.063M` ounces | Combined timing context only | Does not identify BHP-only sold credits |

## Interpretation

The BHP-specific contractual quantity screen is now explicit:

```text
pre-threshold entitlement = mine production × 33.75% × 90%
                         = mine production × 30.375%

post-threshold entitlement = mine production × 22.5% × 90%
                          = mine production × 20.25%
```

Applying the payable factor to BHP's FY2026 `5.588M` mine-production figure
gives `5.0292M` ounces as a mechanical denominator. It does not establish that
Wheaton received that quantity, when any credit was issued, what price was
realized, or when cash was collected.

The `2.319M` produced and `2.063M` sold figures in Wheaton's Q2 table remain
combined BHP/Glencore figures. They must not be allocated to BHP using the
`67.5%` combined share increase, because the filing does not provide the
BHP-only production, credit, sale, invoice, or bank-collection split.

## Promotion boundary

This artifact upgrades quantity-input discipline only. Q-03 still requires a
BHP-PMPA metal-credit issuance, sale/receivable, and cash-collection ledger,
plus financing/tax allocation and a reserve-backed delivery curve, before the
quantity inputs can support an after-cost IRR or NPV.

Status: `quantity-proxy-separated; receipt-and-return-unproven`

## Sources

- [BHP FY2026 Form 20-F](https://www.sec.gov/Archives/edgar/data/811809/000119312526354647/bhp-20260630.htm)
- [Wheaton Q2 2026 results exhibit](https://www.sec.gov/Archives/edgar/data/1323404/000119312526338641/d15525dex991.htm)
- [Q-03 metal-credit receipt boundary](capital-flow-wheaton-antamina-q03-metal-credit-receipt-boundary-2026-09-17.md)
