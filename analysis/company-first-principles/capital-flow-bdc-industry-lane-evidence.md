# Capital Flow BDC Industry Lane Evidence

## Why This Pass Exists

The prior BDC pass proved that private credit is a real borrower-facing lending channel.

This pass asks the next question:

`Which borrower lanes are actually getting funded?`

That matters because the capital-flow thesis should not stop at AUM, fundraising, or bank-loan comparisons. A better claim needs to show where the dollars land in the real economy.

## Local Data File

`analysis/company-first-principles/data/capital-flow-bdc-industry-lane-evidence.csv`

Next borrower-level workbench:

`analysis/company-first-principles/capital-flow-borrower-matching-workbench.md`

ARCC schedule parser pass:

`analysis/company-first-principles/capital-flow-arcc-schedule-parser-pass.md`

BXSL industry percentage pass:

`analysis/company-first-principles/capital-flow-bxsl-industry-percentage-pass.md`

Cross-BDC lane comparison:

`analysis/company-first-principles/capital-flow-cross-bdc-industry-lane-comparison.md`

## What We Can Say From The Sources

BXSL now gives the cleanest percentage-based industry cut. Its Q2 2026 10-Q reports industry percentages across the full portfolio, and the extraction reconciles to `100.0%` of `13.364B USD` of total investments at fair value.

| BXSL Industry Lane | Filed Share | Converted Fair Value |
|---|---:|---:|
| Software | `18.9%` | `2.526B USD` |
| Health Care Providers & Services | `10.3%` | `1.377B USD` |
| Professional Services | `10.3%` | `1.377B USD` |
| Insurance | `10.0%` | `1.336B USD` |
| Commercial Services & Supplies | `8.3%` | `1.109B USD` |
| IT Services | `4.7%` | `0.628B USD` |
| Health Care Technology | `4.5%` | `0.601B USD` |
| Diversified Consumer Services | `4.4%` | `0.588B USD` |
| Air Freight & Logistics | `3.3%` | `0.441B USD` |
| Aerospace & Defense | `3.3%` | `0.441B USD` |

OBDC now adds exact lane-dollar evidence. Its Q2 2026 SEC earnings exhibit says the portfolio covered 229 portfolio companies across 30 industries, with about `15.0B USD` of portfolio fair value and average investment size of `65.3M USD`. Its Q2 2026 10-Q schedule subtotals then reconcile to `14.955B USD` of total investment fair value.

| OBDC Industry Lane | Fair Value |
|---|---:|
| Internet software and services | `1.733B USD` |
| Healthcare providers and services | `1.274B USD` |
| Asset based lending and fund finance | `1.111B USD` |
| Insurance | `0.911B USD` |
| Healthcare technology | `0.872B USD` |
| Food and beverage | `0.783B USD` |
| Healthcare equipment and services | `0.720B USD` |
| Buildings and real estate | `0.663B USD` |
| Manufacturing | `0.565B USD` |
| Financial services | `0.560B USD` |

ARCC adds the strongest reconciled industry table so far. Its 10-Q schedule subtotals show `6.451B USD` in software/services, `3.936B USD` in financial services, `2.895B USD` in healthcare equipment/services, `2.812B USD` in commercial and professional services, and `1.972B USD` in consumer services.

The ARCC pass now has two layers. The official industry subtotal table reconciles to ARCC's reported total investment fair value: `29.349B USD` across `24` industry buckets. The separate row-level parser extracted `1,379` investment rows and `22.456B USD` of fair value, so it remains a borrower-discovery tool marked `parser-derived-needs-reconciliation`.

The cross-BDC comparison normalizes ARCC, OBDC, and BXSL into shared lanes. The top visible combined lanes are software/services, healthcare equipment/services, commercial/professional services, financial services, insurance, and consumer services.

## What The Evidence Implies

The stronger evidence-led claim is:

`Large BDC portfolios are not generic pools of private assets. The first visible funded lanes are software, healthcare, professional services, financial services/fund finance, insurance, commercial services, IT services, healthcare technology, consumer services, logistics, materials, and aerospace/defense.`

This connects the capital-flow work back to the operating-company clusters:

| Funded Lane | Related Operating Theme |
|---|---|
| Software and IT services | Internet/software control layer |
| Healthcare providers and healthcare technology | Healthcare access and care-delivery pressure |
| Commercial, professional, and consumer services | Built-environment services, facility services, and outsourced operations |
| Air freight and logistics | Industrial distribution and physical-network throughput |
| Aerospace and defense | Industrial capacity and national-security supply chains |

## What We Should Not Claim Yet

This does not yet prove exact bank displacement.

The evidence shows private credit is funding real borrower lanes. It does not show that each borrower would otherwise have borrowed from a bank, issued public debt, used syndicated loans, or taken sponsor equity.

The next disproof checks are:

- borrower-level prior debt source
- sponsor-backed transaction type
- loan purpose, such as acquisition financing, refinancing, growth investment, or dividend recap
- overlap with bank revolver lenders
- credit quality by lane, not just at the aggregate BDC level

## Better Claim After This Pass

Old claim:

`Private credit is replacing bank lending.`

Better claim:

`Private credit is building a parallel borrower-financing channel concentrated in specific service, software, healthcare, and sponsor-backed transaction lanes. The evidence supports real funded exposure by industry, but exact bank-loan substitution still requires borrower-level matching.`

## Evidence To Claim And Claim To Evidence

Evidence to claim:

`ARCC official industry dollars + OBDC official industry dollars + BXSL official industry percentages converted to dollars -> private credit has identifiable real-economy borrower lanes.`

Claim to evidence:

`If the claim is bank displacement, the next evidence cannot just be AUM or portfolio size. It must identify borrower, loan purpose, prior lender or takeout source, bank facility role, and whether the same credit would have sat on a commercial-bank balance sheet.`

## Simple Version

The money is not just sitting in funds.

It is showing up as loans to private companies in software, healthcare, professional services, insurance, commercial services, IT services, consumer services, logistics, and defense-related lanes.

That is a real capital-flow map. The next job is proving whether those loans replaced bank loans or simply created another financing route beside the banks.

That proof now starts in the borrower-matching workbench, which turns named borrowers and lanes into explicit source-of-funds tests.
