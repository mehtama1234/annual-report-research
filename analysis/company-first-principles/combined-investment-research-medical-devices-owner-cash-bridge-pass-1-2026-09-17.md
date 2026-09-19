# Medical devices and clinical workflow owner-cash bridge — pass 1

Research date: `2026-09-17`

This pass turns the FY2025 filing observations for Stryker, Intuitive Surgical,
and Henry Schein into an explicit bridge. It is a denominator-control artifact,
not a final owner-cash ranking. The structured [bridge register](data/combined-investment-research-medical-devices-owner-cash-bridge-pass-1-2026-09-17.csv)
preserves the inputs and the unresolved claims.

## Bridge rule

The first-pass screen is:

```text
reported operating cash flow
  - visible PP&E cash spending
  - capitalized software where disclosed
  - acquisition/equity/other investing cash where the growth engine makes it material
  = cash after visible reinvestment
```

This is not automatically common-owner cash. It still requires treatment of
stock compensation, debt and lease claims, legal and regulatory exposures,
recurring restructuring, working-capital normalization, minority or preferred
claims, and diluted shares. Acquisitions are shown separately because an
investor may classify them as growth, maintenance, or a recurring cost of
defending the control point—but that classification must be earned through
post-close return evidence.

## Comparable first-pass surface

| Company | OCF | Visible reinvestment | Cash after visible reinvestment | Illustrative SBC-adjusted screen |
| --- | ---: | ---: | ---: | ---: |
| Stryker | `$5.044B` | `$0.761B` PP&E + `$4.960B` acquisitions | `$(0.677B)` | `$(0.920B)` |
| Intuitive Surgical | `$3.031B` | `$0.540B` PP&E + `$0.014B` other investing | `$2.477B` | `$1.689B` |
| Henry Schein | `$0.712B` | `$0.139B` property + `$0.052B` software + `$0.199B` acquisitions/equity | `$0.322B` | Not yet populated |

The three figures are not a ranking. Stryker's negative result reflects an
acquisition-heavy year; Intuitive's result is supported by recurring
instruments and services but remains exposed to inventory, manufacturing,
R&D, and SBC; Henry Schein's result is thin and must survive restructuring,
working-capital, debt, and repurchase claims.

## Company bridges

### Stryker

Stryker reported FY2025 operating cash of `$5.044B`, PP&E purchases of
`$0.761B`, and net acquisition cash of `$4.960B`. The direct residual is
approximately `$(0.677B)` before dividends, interest, debt service, legal or
quality claims, and dilution. Stock compensation was approximately `$0.243B`;
if treated as an owner claim rather than a free non-cash add-back, the
illustrative screen falls to approximately `$(0.920B)`.

The correct next object is not a generic “adjusted EPS reconciliation.” It is
an acquisition-cohort return table: purchase price, acquired revenue and
margin, inventory step-up, amortization, integration cash, debt funding,
incremental cash generation, impairment or remediation, and diluted-share
effect. The 2025 inventory cash use of approximately `$0.297B` is already in
operating cash flow and should not be subtracted again from this starting
bridge; it is a diagnostic for whether procedure growth is being converted
into collected cash or inventory accumulation.

### Intuitive Surgical

Intuitive reported FY2025 operating cash of `$3.031B`, PP&E purchases of
`$0.540B`, and approximately `$0.014B` of acquisitions, intellectual property,
and other investing. The first-pass residual is approximately `$2.477B`.
Inventory used approximately `$1.063B` of operating cash and stock
compensation was approximately `$0.788B`. Inventory is already reflected in
operating cash flow, so it must not be deducted a second time. Treating SBC as
an owner claim produces an illustrative, not final, `$1.689B` screen.

The critical denominator is cash per installed system and procedure, not cash
per dollar of system-placement revenue. Instruments and accessories were
approximately `$6.019B`, systems `$2.474B`, and services `$1.572B` in FY2025.
The next bridge must connect installed-base cohorts to procedure utilization,
instrument consumption, service attachment, usage-based lease collections,
manufacturing capacity, R&D, support labor, inventory turns, and diluted
shares.

### Henry Schein

Henry Schein reported FY2025 operating cash of `$0.712B`, property capex of
`$0.139B`, capitalized software of `$0.052B`, and acquisition/equity-investment
cash of `$0.199B`. The resulting first-pass residual is approximately
`$0.322B`. Cash at year-end was approximately `$0.156B` against reported debt
of approximately `$3.1B`; common-owner cash therefore cannot be inferred from
the residual without a debt and liquidity bridge. Repurchases were approximately
`$0.850B`, materially above the residual, so the analysis must identify the
funding source and whether buybacks increased leverage or consumed liquidity.

The next object is a working-capital and restructuring bridge: internal versus
acquisition growth, inventory and receivable days, supplier settlement,
restructuring cash, software, acquisition return, debt maturities, KKR-related
ownership, and diluted shares. The FY2025 GAAP/non-GAAP EPS gap of `$3.27`
versus `$4.97` is a prompt for that bridge, not proof of manipulation.

## Promotion gate

Status: `owner-cash-bridge-pass-1; comparable-inputs-preserved; no-ranking`.

Promotion requires all of the following:

1. maintenance versus growth reinvestment by company-specific control point;
2. recurring acquisition, integration, restructuring, and quality costs;
3. SBC and diluted-share treatment;
4. debt, lease, legal, regulatory, and liquidity claims; and
5. a return measure that ties cash to utilization, acquired cohorts, or
   practice/channel economics.

Primary source routes are the company [source ledgers](../../extracted/healthcare/medical-instruments-supplies/stryker-corporation/source-ledger.md),
[Intuitive Surgical source ledger](../../extracted/healthcare/medical-instruments-supplies/intuitive-surgical-inc/source-ledger.md),
and [Henry Schein source ledger](../../extracted/healthcare/medical-instruments-supplies/henry-schein-inc/source-ledger.md),
with the company dossiers providing the reconciled narrative and preserved
filing links.
