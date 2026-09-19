# Retail quality-of-earnings transition panel

Research date: `2026-09-16`

## Purpose

This panel turns the three controlled annual QoE vectors into six
same-company, adjacent-period transitions. It exposes the raw ratio movement
that a financial-shenanigans or quality-of-earnings review would investigate:
cash conversion, cash after property, working-capital ratios, capital
intensity, contractual claims, and stock compensation.

The structured [transition-panel CSV](data/combined-investment-research-quality-of-earnings-retail-transition-panel-2026-09-16.csv)
is the source of truth. Every change is calculated from the corresponding
company vector; Target's unavailable consolidated receivables field remains
explicitly unavailable rather than being replaced with another current-asset
category.

This is a six same-company transition panel, not a pooled fraud score.

## How to read it

The flags are document-review prompts, not manipulation findings. A falling
OCF-to-earnings ratio can reflect working-capital timing, taxes, acquisitions,
or operating volatility. A rising claims or SBC ratio can reflect financing,
growth, or compensation design. Inventory and payable movements can be
seasonal or supplier-term driven. The panel therefore preserves the raw start,
end, and change values and routes each flag to the next filing test.

It is not a manipulation finding.

The panel finds six diagnostic transitions:

- TJX has one transition with simultaneous OCF/post-property softening and
  rising inventory, payables, capex intensity, and SBC; its later transition
  improves post-property cash and claims while inventory and SBC continue to
  rise.
- Target has OCF softening in both transitions, a sharp later post-property
  deterioration, rising claims in both periods, and no disclosed receivables
  denominator.
- Walmart has a sharp first-transition OCF/post-property deterioration with
  rising claims and SBC; the later transition improves cash and claims but SBC
  rises and the receivables-to-revenue ratio increases.

## Promotion boundary

Status: `diagnostic-panel-assembled; composite-score-not-promotable`.

This panel advances the QoE work beyond a start/end summary, but it does not
assemble a Beneish score, Sloan score, fraud probability, or cross-company
ranking. The cohort still has incomplete receivable, expense-taxonomy,
lease/claim, transaction, fiscal-calendar, and legal-entity joins. Promotion
requires period-matched source support for those fields and an independent
cash-perimeter reconciliation. Until then, the flags are only a prioritized
falsifier and document-acquisition queue.

Source vectors: [TJX history](data/combined-investment-research-quality-of-earnings-tjx-historical-vector-2026-09-16.csv),
[Target history](data/combined-investment-research-quality-of-earnings-target-historical-vector-2026-09-16.csv),
and [Walmart history](data/combined-investment-research-quality-of-earnings-walmart-historical-vector-2026-09-16.csv).
