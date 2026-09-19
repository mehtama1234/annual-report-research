# Pilot 02 retail normalized-cash screen

Research date: `2026-09-15`

This screen is deliberately narrower than a valuation conclusion. It starts
with reported operating cash flow less property spending and applies only
disclosed, identifiable adjustments. It does not claim that the resulting
figures are GAAP, company-defined, or final owner cash.

## Source-bounded screen

| Company / period | Reported cash after property | Low screen | Base screen | High screen | Adjustment logic |
| --- | ---: | ---: | ---: | ---: | --- |
| TJX FY2026 | `$4.917B` | `$4.464B` | `$4.703B` | `$4.917B` | Low removes `$239M` payable support and `$214M` SBC; base removes SBC only; high is reported bridge |
| Target H1 2026 | `$2.115B` | `$0.597B` | `$1.209B` | `$2.115B` | Low removes `$752M` after-tax tariff benefit, `$612M` payable support, and `$154M` share-based compensation; base removes tariff benefit and share-based compensation; high is reported bridge |
| Walmart H1 FY2027 | `$5.529B` | `$0.981B` | `$5.529B` | `$5.529B` | Low removes `$1.648B` accounts-payable support plus approximately `$2.9B` tariff-refund cash support; base/high retain reported bridge because pass-through is unresolved |
| TJX H1 FY2027 | `$2.186B` | `$1.631B` | `$2.101B` | `$2.186B` | Low removes `$470M` accounts-payable support and `$85M` SBC; base removes SBC only; temporary tariff/interchange benefits remain unquantified and are not deducted |

These are not directly comparable annual owner-cash values: Target and Walmart
rows are six-month periods, while TJX is fiscal-year data. The screen exposes
the direction and size of known distortions without pretending that seasonality,
maintenance capex, leases, taxes, stock compensation, inventory turns, or
attached-service costs have been solved.

## Why leases are not subtracted again

Operating-lease cash payments are already included in operating cash flow. The
lease liabilities in the burden map are therefore a balance-sheet and return-on-
capital burden, not an additional subtraction from cash-after-property. A model
that subtracts both lease cash and lease liability from the same bridge would
double count the burden. The next model should use lease-adjusted invested
capital or a clearly defined EBIT/ROIC framework alongside cash flow.

## Valuation boundary

The [temporary-support boundary memo](combined-investment-research-pilot-02-retail-temporary-support.md) records why Walmart's tariff refund is a sensitivity rather than recurring owner cash. The screen is suitable for a Damodaran-style expectations audit, not a target
price. It says Target’s apparent recovery is most sensitive to the tariff refund
and payable leverage; Walmart’s reported H1 cash is most sensitive to supplier
terms and heavy platform capex; and TJX has the cleanest annual reported bridge
but still needs inventory, lease, tax, maintenance-capex, and per-share tests.

Sources: [retail owner-cash bridge](combined-investment-research-pilot-02-retail-owner-cash-bridge.md), [retail burden map](combined-investment-research-pilot-02-retail-burden-normalization.md), [TJX 10-K](https://www.sec.gov/Archives/edgar/data/109198/000010919926000008/tjx-20260131.htm), [Target Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/27419/000002741926000042/tgt-20260801.htm), and [Walmart Q2 FY2027 10-Q](https://www.sec.gov/Archives/edgar/data/104169/000010416926000154/wmt-20260731.htm).

## TJX bounded valuation screen

The existing TJX FY2026 source-bounded screen can now populate a qualified
valuation row without calling it final owner cash. Applying illustrative `18x`,
`24x`, and `30x` cash multiples to the low/base/high screen values produces:

| Case | Cash input | Multiple | Implied value | September 15 market value |
| --- | ---: | ---: | ---: | ---: |
| Low | `$4.464B` | `18x` | `$80.352B` | `$138.810B` |
| Base | `$4.703B` | `24x` | `$112.872B` | `$138.810B` |
| High | `$4.917B` | `30x` | `$147.510B` | `$138.810B` |

At the base multiple, the market requires approximately `$5.784B` of annual
cash to support the observed market value, above the `$4.703B` base screen.
This is an expectation gap, not evidence that TJX is overvalued: the multiple,
cash screen, and market snapshot are analytical inputs, while inventory turns,
maintenance capital, leases, taxes, dilution, and per-share cash remain
unresolved. Because those gates are not closed, this sensitivity is not
inserted into the TJX valuation workbench; TJX remains explicitly
`not-comparable` there.
