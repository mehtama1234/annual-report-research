# Retail quality-of-earnings component screen

Research date: `2026-09-16`

## Purpose

This screen assembles the comparable components that can be calculated from
the existing three-year TJX, Target, and Walmart vectors. It advances the
financial-shenanigans review from six transition rows to a named, reproducible
component panel while preserving the fields that are not comparable.

The structured [component-screen CSV](data/combined-investment-research-quality-of-earnings-retail-component-screen-2026-09-16.csv)
is the source of truth. The indices are transition ratios: for example, the
receivables index is the ending receivables/revenue ratio divided by the
starting ratio. `accrual_proxy_current_assets` is `(net income - operating
cash flow) / current assets` for the ending period; it is deliberately not the
standard Beneish total-accruals variable because total assets are not in the
controlled comparable field set.

## What is assembled

- six same-company annual transitions;
- period-matched revenue, net income, OCF, current assets, net PP&E, D&A,
  SG&A/OSG&A, claims, and selected receivables fields;
- explicit missing-field labels for Target receivables, gross profit, total
  assets, and cash-flow tax/acquisition joins; and
- a diagnostic reading and source route for every row.

## What the screen says

TJX shows modest revenue growth in both transitions, with a small OCF-
conversion deterioration and no rising claims-index signal. Target has no
receivables denominator in the controlled vectors; its OCF conversion weakens
across both transitions and its claims burden needs separate cash and
supplier-term review. Walmart shows rising receivables and claims indices in
both transitions; OCF conversion improves in the second transition but the
perimeter, OSG&A classification, and noncontrolling-interest questions remain.

These are review prompts, not evidence of manipulation. The screen does not
calculate a Beneish M-score, Sloan score, fraud probability, or company
ranking. It also does not clear the remaining owner-cash or capital-flow
gates.

## Promotion boundary

Status: `retail-component-screen-assembled; composite-score-not-promotable`.

The screen is useful because it makes the available cross-period evidence
explicit instead of hiding it behind a missing composite score. It remains
below a composite promotion gate until gross profit, total assets, fiscal and
accounting-policy alignment, legal-entity perimeter, and cash-flow taxonomy
are joined for all three companies. Any future composite must also preserve
Target's missing receivables field rather than imputing it.

The screen therefore feeds the quality-of-earnings falsifier queue and the
owner-cash bridge; it does not establish a financial-shenanigans finding.
