# Pilot 02 retail owner-cash promotion rule

Research date: `2026-09-15`

The retail cohort now has reported OCF-less-property screens, support-adjusted
cash sensitivities, lease and dilution boundaries, annual capex references, and
a Walmart known-growth capex inference. Those inputs are not automatically a
normalized owner-cash denominator. This rule controls when a value screen may
promote a cash figure from `reported-denominator-screen` to `normalized-owner-
cash`.

## Promotion gates

A company-period cash figure may be promoted only when all five gates are
resolved or shown as explicit, bounded sensitivities:

1. **Period and seasonality:** the operating cash period and valuation period
   are comparable, or the annualization is supported by same-company history.
2. **Working capital:** inventory, payables, supplier finance, vendor income,
   tariff refunds, and other temporary support are separated from recurring
   operating cash.
3. **Reinvestment:** maintenance capital is quantified or bounded separately
   from new stores, remodels, fulfillment, automation, technology, and growth
   infrastructure.
4. **Owner claims:** leases, cash taxes, debt service, required funding,
   stock compensation, buybacks, and diluted shares are mapped without double
   counting.
5. **Attached services:** advertising, membership, cards, marketplace, and
   fulfillment revenue are not valued as standalone cash until their allocated
   costs, capital, tax, and collection are visible.

## Current cohort decision

| Company | Current status | Why promotion is withheld |
| --- | --- | --- |
| TJX | Qualified reported annual bridge | Inventory turns, maintenance versus growth capital, leases, taxes, and diluted-share cash remain open; H1 also contains temporary support candidates |
| Target | Partial source-bounded H1 screen | Tariff/vendor/payable support and H1 capex allocation are not fully separated; attached-service and annual seasonality tests remain open |
| Walmart | Partial source-bounded H1 screen | Supplier terms and tariff support remain unresolved; exact category amounts exist, but maintenance share, lease/tax/SBC burden, attached-service cost, and seasonality remain open |

The rule prevents the valuation workbench from silently treating the high end
of a cash sensitivity as recurring owner cash. The existing ranges remain
useful for expectations analysis, but their status stays `qualified`, `partial`,
or `illustrative` until the gates close.

## Q-04–Q-06 promotion action register

The [structured action register](data/combined-investment-research-retail-promotion-action-register-2026-09-17.csv)
turns the three remaining retail questions into document-specific promotion
tests. Q-04 requires settlement-date working-capital reconciliation; Q-05
requires a maintenance-versus-growth capital range carried through the same
owner-cash denominator; and Q-06 requires service-level collection plus
allocated labor, fulfillment, technology, capital, tax, and senior claims.
Each row remains `partial` until the relevant legal entity, period, denominator,
and cash or claim object are joined.

Sources: [retail normalized-cash screen](combined-investment-research-pilot-02-retail-normalized-cash-screen.md), [retail burden normalization](combined-investment-research-pilot-02-retail-burden-normalization.md), [retail capex classification](combined-investment-research-pilot-02-retail-capex-classification.md), and [Walmart known-growth capex boundary](combined-investment-research-pilot-02-walmart-known-growth-capex-boundary.md).
