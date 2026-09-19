# Retail Margin and Working-Capital Normalization Matrix

Research date: `2026-09-15`

This matrix identifies the cash and margin items that must be normalized before
the retail cohort can support an owner-cash ranking. Values are source-bounded
inputs, not deductions that have already been proven recurring.

| Company | Period | OCF | Gross margin screen | Inventory cash signal | Payable cash signal | Supplier-finance obligation | Temporary or one-time support screen | Interpretation |
| --- | --- | ---: | --- | --- | --- | ---: | ---: | --- |
| TJX | H1 FY2027 | `$3.345B` | `32.376%` calculated; `31.254%` mechanical ex-support screen | Inventory used `$603M` of cash; inventory `$7.862B` | Accounts payable supplied `$470M` | Not separately populated in current bridge | `$750M` tariff-refund and interchange-settlement candidate | Cash bridge and reported margin are exposed to inventory and candidate temporary support; maintenance capex and service burden remain open. |
| Target | H1 2026 | `$4.519B` | `31.4%` reported; `29.479%` mechanical ex-support screen | Inventory balance `$13.200B`; cash effect requires roll-forward | Accounts payable supplied `$612M` | `$3.2B` eligible supplier-finance obligations | `$1.364B` source-bounded support screen | Tariff/vendor/payable effects can overstate recurring cash and margin; settlement timing remains open. |
| Walmart | H1 FY2027 | `$19.710B` | `24.9%` reported; `24.054%` mechanical ex-support screen | Inventory used `$2.660B` of cash | Accounts payable supplied `$1.648B` | `$6.4B` outstanding supplier-finance obligations | `$4.548B` source-bounded support screen | Scale cash and reported margin are visible, but inventory, payables, tariff effects, fulfillment, and capex require normalization. |

The new [cross-cohort inventory/payable balance screen](combined-investment-research-pilot-02-retail-cohort-inventory-payable-balance-screen-2026-09-15.md)
adds comparable opening and ending balance changes for TJX, Target, and Walmart
without treating them as a second cash deduction. The gross-margin fields are
included as operating-quality inputs. TJX's margin
is calculated from filed sales and cost of sales including buying and
occupancy; Target and Walmart use reported rates. The ex-support figures are
mechanical sensitivities based on disclosed or source-bounded tariff benefits,
not normalized recurring margins. The correct next calculation is a
roll-forward, not a blanket subtraction: a supplier-finance balance or
temporary support item may affect timing, margin, or classification differently
from recurring owner cash. Maintenance versus growth capital, leases, taxes,
stock compensation, and seasonality remain open.

Target now has a separate [inventory/payable balance-change screen](combined-investment-research-pilot-02-target-inventory-payable-balance-screen-2026-09-15.md).
It shows a `$945M` H1 inventory-balance increase against a `$684M` accounts-
payable increase, or a `-$261M` mechanical net signal. This is a balance-change
sensitivity only; it is not substituted for the cash-flow statement or treated
as normalized owner cash.
