# Restaurant-franchise owner-cash promotion workbench — 2026-09-17

This workbench turns the restaurant-franchise synthesis and filing panel into
a promotion test. It does not rank CAVA, Restaurant Brands International,
Wingstop, or Yum.

## Required bridge

```text
systemwide sales / unit activity
  -> franchisee sales and corporate-store sales
  -> royalties, fees, property income, company-store revenue,
     advertising-fund inflows, and other reported revenue
  -> franchisee receivables, collections, support, closures, and fund spending
  -> corporate OCF
  -> maintenance/remodel/new-store/technology capex
  -> acquisitions, integration, legal, leases, taxes, and debt funding
  -> SBC, NCI/other claims, repurchases, dividends, and diluted shares
  -> common-owner residual
```

## Field-level promotion matrix

| Gate | CAVA | RBI | Wingstop | Yum | Promotion requirement |
| --- | --- | --- | --- | --- | --- |
| Same-period OCF and PP&E | FY2025 present | FY2025 present | FY2025 present | FY2025 present | Proven as a mechanical diagnostic |
| Unit-count denominator | `439` | `33,041` | `3,056` | Not promoted from selected fact set | Company-specific scale only |
| Royalty/franchise revenue | Not comparable in selected standard facts | Franchise tag available | Franchise tag available | Franchise tag available | Need amount, definition, and collection perimeter |
| Advertising-fund inflow/outflow | Not joined | Expense and accrued liability visible | Expense visible | Advertising/cooperative expense visible | Need matched fund collections, spending, restrictions, and legal entity |
| Franchisee health / support | Open | Open | Open | Open | Need closures, receivables, support, unit economics, and same period |
| Maintenance versus growth capex | Open | Open | Open | Open | Need project/category schedule or bounded range |
| Debt, lease, tax, acquisition claims | Open | Open | Open | Open | Must be period-matched and assigned to the franchisor residual |
| Diluted common-owner cash | Not calculated | Not calculated | Not calculated | Not calculated | All applicable claims and share dilution must be joined |

## QoE and shenanigans decision rules

- A rise in systemwide sales without a corresponding royalty collection or
  franchisor cash improvement is a conversion warning, not a growth proof.
- A refranchising gain or margin improvement must be separated from recurring
  royalty economics and the capital burden shifted to franchisees.
- Advertising revenue and advertising expense cannot be netted or promoted
  until the fund's restricted-use and collection mechanics are reconciled.
- OCF less total PP&E is a screen only; it cannot be called owner cash while
  maintenance, support, leases, debt, acquisitions, or dilution are unassigned.
- Buybacks and dividends are outputs of a capital-allocation decision, not
  proof that the underlying cash was surplus or sustainably recurring.

## Current decision

`qualified-control-point; allocation-sensitivity-only; no-ranking`

The next promotion object is a same-period royalty and advertising-fund
schedule tied to franchisee health and cash collection. If that schedule is
not public, the lane remains useful as a falsifiable diagnostic but must not be
converted into a normalized owner-cash ranking.

Sources: [restaurant-franchise synthesis](annual-report-restaurant-franchise-first-principles-synthesis-pass-1-2026-09-17.md),
[filing evidence panel](combined-investment-research-restaurant-franchise-filing-evidence-panel-2026-09-17.md),
and [restaurant-franchise denominator verifier](../../scripts/verify-restaurant-franchise-filing-denominators.py).

