# Industrial uptime QoE diagnostic register — 2026-09-17

## Purpose and rule

This register applies Sloan-, Schilit-, and Beneish-style quality-of-earnings
questions to the industrial-uptime candidates. It is a diagnostic register,
not a fraud score. The ratios are useful only when the entity, period,
taxonomy, denominator, and cash/claim perimeter match.

The field-level companion is the [industrial uptime evidence register](data/combined-investment-research-industrial-uptime-evidence-register-2026-09-17.csv).
It is the machine-readable source for the values and promotion boundaries in
this memo.

## Period-matched reported screen

Amounts are USD millions from the locally preserved Q2 2026 Form 10-Q filings.

| Company | H1 revenue | H1 operating income | H1 OCF | H1 property/productive-asset spend | H1 SBC | OCF / revenue | OCF less spend / revenue | Initial diagnostic |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| WESCO | 12,745.2 | 675.7 | 275.1 | 51.6 | 35.2 | 2.16% | 1.75% | Operating income is much larger than operating cash flow; receivables and inventory grew materially, so conversion requires a working-capital and acquisition/timing explanation. |
| Fastenal | 4,588.6 | 949.4 | 644.1 | 123.0 | 5.2 | 14.04% | 11.36% | Cash conversion is stronger, but inventory, service burden, customer mix, and recurring maintenance/service costs remain separate owner-cash questions. |
| Sterling | See backlog and conversion packets | See filing chain | H1 OCF less capex = 258.375 | Company capex in conversion packet | Acquisition/SBC and dilution require separate treatment | Not recomputed here | Not promoted | Percentage-of-completion accounting, contract assets/retainage, acquisition contribution, and customer funding are the decisive diagnostics. |

The balance-sheet bridge from the conversion screen is retained as a diagnostic
only:

- WESCO operating working capital increased by approximately `$314.8M` from
  2025 year-end to June 30, 2026.
- Fastenal operating working capital increased by approximately `$216.3M`.

These changes are not subtracted again from reported OCF. Doing so would risk
double counting the same-period cash-flow effect.

## Diagnostic register

| ID | Candidate | Diagnostic family | Current signal | What must be reconciled | Status |
| --- | --- | --- | --- | --- | --- |
| IQOE-001 | WESCO | Cash earnings quality | H1 OCF/revenue is 2.16% against operating margin of approximately 5.30%; OCF less productive-asset spend is 1.75% of revenue | Receivables, inventory, payables, other current assets/liabilities, acquisition effects, and project-channel timing | Warning / investigate |
| IQOE-002 | WESCO | SBC and owner claim | H1 SBC is `$35.2M`; tax-withholding share settlement is separately disclosed | Diluted shares, repurchases, SBC valuation, and common-owner residual | Range input only |
| IQOE-003 | Fastenal | Cash earnings quality | H1 OCF/revenue is 14.04%; OCF less property spending is 11.36% | Whether cash conversion persists after inventory/service investment and normalized customer terms | Preliminary positive; not promoted |
| IQOE-004 | Fastenal | Working-capital timing | Receivables rose `$312.1M`; inventory fell `$12.8M`; payables rose `$83.0M` | Customer collection, inventory availability, vendor terms, and service-cost explanation | Reconciliation open |
| IQOE-005 | Fastenal | SBC and dilution | H1 SBC is `$5.2M` | Diluted-share count, repurchases, and per-share owner claim | Range input only |
| IQOE-006 | Sterling | Revenue timing / percentage of completion | Revenue and margin depend on estimates of total cost, gross profit, incentives, penalties, and change orders | Estimate revisions, approved versus unapproved claims, job losses, rework, warranty, contract assets, and retainage to cash | High-value open test |
| IQOE-007 | Sterling | Backlog quality | Signed backlog `$4.33B`; combined backlog `$5.62B`; future phases `$1.4B+` | Conversion by layer, cancellation/scope change, customer funding, billing, and collection | Separated; not equivalent |
| IQOE-008 | Sterling | Acquisition / organic boundary | CEC and Stone Ridge contribute `$2.56B` to signed plus unsigned backlog; acquisition revenue contribution is `21.5%` of Q2 revenue | Post-close revenue, margin, cash, earn-outs, integration, dilution, and working capital | Acquisition-adjusted case required |

## Thesis-breaker routing

- WESCO: persistent OCF under conversion despite revenue and backlog growth
  routes to a working-capital/project-channel thesis breaker.
- Fastenal: falling onsite/digital retention, rising service cost, or weaker
  inventory economics routes to an embedded-replenishment thesis breaker.
- Sterling: unfavorable estimate revisions, contract-asset growth without
  collection, or acquisition cash below the return hurdle routes to the
  project-conversion/acquisition thesis breakers.

No breaker activates from a ratio alone. Each requires a same-entity,
same-period cash or claim reconciliation.
The dedicated [industrial thesis-breaker register](combined-investment-research-industrial-uptime-thesis-breaker-register-2026-09-17.md)
now records seven measurable Sterling, WESCO/Fastenal, and URI tests with
next-document routes.

## Promotion boundary

The register supports `industrial-qoe-diagnostic-grade`. It does not support a
pooled Beneish score, a fraud conclusion, normalized owner cash, or an
investment ranking. The next evidence bundle is the same one specified in the
industrial valuation handoff: maintenance-capital classification, tax/lease
cash, supplier-finance and acquisition treatment, contract-asset/collection
joins, and a period-matched diluted-owner claim.

## Source routes

- [WESCO Q2 2026 Form 10-Q](../../raw/sec/industrial-goods/industrial-equipment-components/wesco-international-inc/2026-q2-10q.html)
- [Fastenal Q2 2026 Form 10-Q](../../raw/sec/industrial-goods/industrial-supply/fastenal-company/2026-q2-10q.html)
- [Sterling deep company page](../../analysis/deep-company-pages/sterling-infrastructure-inc.md)
- [Sterling backlog-quality separation](combined-investment-research-industrial-uptime-sterling-backlog-quality-separation-2026-09-17.md)
- [Industrial valuation and macro handoff](combined-investment-research-industrial-uptime-valuation-macro-handoff-2026-09-17.md)

## Status

`industrial-qoe-register-complete; diagnostic-only; promotion-open`
