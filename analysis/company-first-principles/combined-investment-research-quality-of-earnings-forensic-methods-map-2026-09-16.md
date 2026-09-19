# Quality-of-earnings and forensic accounting methods map

Research date: `2026-09-16`

## Role in the investment system

This map connects established earnings-quality methods to the evidence already
being collected in the three pilots. It is a research protocol, not a claim
that any company manipulated its accounts. The methods are used to decide what
must be reconciled before earnings, free cash flow, or adjusted metrics enter
valuation.

## Method-to-evidence map

| Method or tradition | Core question | Inputs required | Current application | Boundary |
| --- | --- | --- | --- | --- |
| Sloan accrual-versus-cash persistence | Is reported earnings growth supported by cash, and which component is likely to persist? | Net income, OCF, accruals, assets, and multiple periods | Retail OCF/NI and cash-after-property screens; working-capital and support diagnostics | Current panel is not a persistence study because the complete multi-period accrual vector is not assembled |
| Beneish M-score family | Do changes in receivables, margins, asset quality, sales growth, depreciation, SG&A, leverage, and total accruals resemble a manipulation-risk pattern? | Two comparable periods for eight component variables, consistent taxonomy, and an industry context | Input schema identifies all required fields; current retail panel populates only a subset | No M-score or threshold is reported until receivables, SG&A, D&A, leverage, and total-accrual histories are complete and comparable |
| Schilit-style financial-shenanigans review | Are revenue, expenses, reserves, one-time items, capitalized costs, or obligations being presented in a way that obscures economics? | Footnotes, contracts, cash-flow statement, working capital, liabilities, and management adjustments | Target tariff refunds; TJX interchange/tariff support; gift cards and memberships; supplier finance; leases; Apollo fee and entity perimeter; Wheaton settlement object | A disclosed one-time benefit is not an accounting error; the test is whether it is removed from recurring valuation assumptions |
| Cash earnings / owner-cash quality | What remains after working capital, reinvestment, claims, taxes, leases, acquisitions, and dilution? | Period-matched OCF, capex classification, working-capital normalization, claims, and diluted ownership | Retail common-period surface; Wheaton Q-03 return schema; Apollo Q-07 common-owner schema | Normalized owner cash remains unpromoted where allocation or legal availability is missing |
| Revenue-quality and contract-liability review | Is reported revenue tied to delivered goods/services and collectible cash, or to timing and obligations? | Revenue disaggregation, receivables, contract liabilities, gift cards, memberships, returns, and collection evidence | Retail gift-card and membership timing; Target attached services; Wheaton metal-credit recognition and settlement objects; Apollo fee accrual versus collection | Revenue recognition policy does not prove cash collection or recurring economics |
| Related-party and perimeter review | Is the claimed return attributable to the relevant parent, legal entity, or common owner? | Entity charts, intercompany balances, statutory schedules, eliminations, distributions, and claim waterfalls | Apollo/Athene AHL-to-AGM note, parent-receipt frontier, statutory holdings, NCI/preferred claims; Wheaton BHP/Glencore separation | Consolidated balances and contractual distributions are not treated as unrestricted common-owner cash |

## Current promotion rule

A warning advances from diagnostic to thesis-breaker only when it is repeated
or economically material and changes the preferred cash, earnings, or valuation
denominator. A ratio alone is not enough. The required join is:

```text
same entity + same period + comparable accounting taxonomy
  + cash or claim perimeter + independent source route
```

If one of those joins is absent, the system records a partial or unresolved
result and names the next document. This is why the current retail panel can
show positive OCF conversion alongside a working-capital or claim warning
without calling the company deceptive.

## Primary method anchors

- [Sloan, “Do Stock Prices Fully Reflect Information in Accruals and Cash Flows About Future Earnings?”](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2598)
- [Beneish, “The Detection of Earnings Manipulation”](https://doi.org/10.2469/faj.v55.n5.2296)

The repository applies these ideas as prompts for source-backed reconciliation,
not as a mechanical trading signal or legal conclusion.

Structured implementation: [QoE overlay](combined-investment-research-quality-of-earnings-financial-shenanigans-overlay-2026-09-16.md), [composite input schema](combined-investment-research-quality-of-earnings-composite-input-schema-2026-09-16.md), and [current diagnostic ratio panel](combined-investment-research-quality-of-earnings-current-retail-diagnostic-ratio-panel-2026-09-16.md).
