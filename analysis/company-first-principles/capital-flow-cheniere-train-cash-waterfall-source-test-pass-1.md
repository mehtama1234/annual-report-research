# Capital Flow Cheniere Train Cash Waterfall Source Test Pass 1

This page executes cash-return source work-order row `CFCRSWO-003`.

The question is:

`Can Cheniere LNG move from source/use/output/customer-demand evidence to train-level customer-cash and project-waterfall proof using the current local source set?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-cheniere-train-cash-waterfall-source-test-pass-1.csv`

The upstream work order is:

`/cluster/capital-flow-cash-return-source-work-order-pass-1.md`

## Short Answer

`No full upgrade yet. Cheniere remains the strongest LNG source/use/output/customer-demand bridge, but current local evidence still does not prove a train-level or entity-level cash waterfall.`

The local evidence proves a strong LNG operating bridge. Cheniere shows FY `2025` revenue of `19.98B USD`, FY `2025` distributable cash flow of `5.29B USD`, Q2 `2026` revenue of `5.73B USD`, Q2 `2026` adjusted EBITDA of `1.80B USD`, and Q2 `2026` DCF of `1.17B USD`. The output side is unusually strong because company cargoes reconcile to DOE vessel rows: `670` FY `2025` company cargoes versus `674` DOE vessel rows, and `184` Q2 `2026` company cargoes versus `184` DOE vessel rows, with Q2 `2026` DOE volume of `640991.63 MMCF`.

The demand and use side is also strong. About `90%` of anticipated SPL/CCL production is contracted under SPAs and IPM agreements, the weighted-average remaining SPA/IPM life is about `15` years, CPC Taiwan is a named customer with SPA volume up to `1.2 mtpa`, CCL Stage 3 was `94.1%` complete at FY `2025`, and Corpus Christi Stage 3 Midscale Train 6 reached substantial completion in June `2026`. Funding context includes FY `2025` growth capital of `2.6B USD` with `2.3B USD` equity-funded, Q2 `2026` growth capital of about `1.1B USD` with `219M USD` equity-funded, and entity debt/contract denominators including SPL debt, CQP notes, CCH debt, parent notes, `29.0B USD` of debt plus interest payments, and `290.6B USD` estimated executed-SPA revenue.

That is not the same as project cash-waterfall proof. The current local source set still lacks a single joined train/entity row with train cost, debt draw, restricted cash, SPA price formula, customer/cargo attribution, revenue, EBITDA, distributions, debt-service coverage, and return.

## Source-Test Result

| Gate | Result | Meaning |
|---|---|---|
| Company revenue/cash baseline | Pass | Consolidated revenue, adjusted EBITDA, and DCF are visible. |
| External cargo denominator | Pass | DOE cargo rows reconcile tightly to company-reported cargoes. |
| Physical volume denominator | Pass | Q2 `2026` DOE terminal volume is visible. |
| Contracted demand | Pass | Most anticipated SPL/CCL production is contracted. |
| Named customer demand | Pass | CPC Taiwan gives a named customer SPA route. |
| Construction/use | Pass | CCL Stage 3 and Train 6 milestones are visible. |
| Funding split | Pass with boundary | Growth capital and equity-funded growth capital are visible but not train-allocated. |
| Entity debt denominator | Pass with boundary | SPL/CQP/CCH/parent debt buckets are visible but not mapped to train cash. |
| Train cost/debt draw | Hold | Current local evidence does not tie cost or debt draws to a named train. |
| SPA economics/cargo attribution | Hold | Contracted volume is visible, but price and cargo-to-contract mapping are missing. |
| EBITDA/distribution/debt service | Hold | Current local evidence does not provide train or entity cash waterfall. |
| Project return | Hold | Current evidence cannot prove project IRR, DSCR, or return. |

## Decision

`train-cash-waterfall-source-test-hold-with-strong-output-demand-proxy`

The work-order row `CFCRSWO-003` is executed from local evidence. The result is not a full promotion. Cheniere remains the strongest energy infrastructure bridge because source/use, output, customer-demand, construction, funding, debt, and cash proxies are all visible. It does not reach train-level cash-waterfall proof.

## Safe Claim

`Cheniere has strong LNG source/use/output/customer-demand evidence: FY 2025 revenue of 19.98B USD, FY 2025 DCF of 5.29B USD, Q2 2026 revenue of 5.73B USD, Q2 2026 adjusted EBITDA of 1.80B USD, Q2 2026 DCF of 1.17B USD, Q2 company/DOE cargo match at 184 cargoes, Q2 DOE volume of 640991.63 MMCF, about 90% contracted anticipated SPL/CCL production, about 15 years weighted-average SPA/IPM life, CPC Taiwan SPA volume up to 1.2 mtpa, CCL Stage 3 at 94.1% completion, Train 6 substantial completion, growth-capital and equity-funded growth-capital context, and entity debt/contract denominators. Current local evidence still does not prove train-level cost, debt draw, restricted cash, SPA price, cargo attribution, revenue, EBITDA, distributions, debt-service coverage, or project return.`

## Next Source Package

1. SPL/CQP/CCH indentures, offering memoranda, and facility agreements.
2. Train-level capex and restricted-account schedules.
3. SPA price formula and customer/entity assignment summaries.
4. Cargo-to-contract or cargo-to-terminal/train mapping.
5. Entity EBITDA, distribution, and restricted-payment bridge.
6. Debt-service waterfall, DSCR, and project return support.
