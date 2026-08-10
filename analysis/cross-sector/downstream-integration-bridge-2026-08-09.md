# Downstream Integration Bridge

Date baseline: 2026-08-09

## Purpose

This note turns the current annual-report archive into an explicit routing map for the two adjacent synthesis projects already on disk:

- `/home/manishmehta/ui-projects/ibis-industries/`
- `/home/manishmehta/projects/Misc/ui-projects/strategy-under-a-force/`

The point is not to duplicate those projects here. The point is to make it obvious which annual-report artifacts should feed which existing force packs and dossier pages.

## Practical rule

- collect and packetize in `annual-report-research/`
- generalize force logic in `ibis-industries/`
- build narrative and dossier surfaces in `strategy-under-a-force/`

## Routing matrix

| Annual-report artifact | Core annual-report evidence | `ibis-industries` targets | `strategy-under-a-force` targets | Why this is the right bridge |
|---|---|---|---|---|
| Compute and infrastructure buildout | [technology-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/technology-sector-initial-brief.md), [industrial-goods-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/industrial-goods-sector-initial-brief.md), [real-estate-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/real-estate-sector-initial-brief.md), [capital-intensity-and-investment-concentration-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/capital-intensity-and-investment-concentration-initial-theme-memo.md) | `_packs/the-compute-super-cycle__the-compute-super-cycle.txt`, `_packs/the-compute-super-cycle__power-scarcity.txt`, `_packs/the-compute-super-cycle__the-data-center-rush.txt`, `_packs/the-compute-super-cycle__the-grid-bottleneck.txt`, `_packs/the-compute-super-cycle__the-electrical-trades.txt`, `_packs/the-compute-super-cycle__the-software-layer.txt` | `the-compute-buildout/the-compute-buildout.html`, `the-compute-buildout/the-capex-supercycle.html`, `the-compute-buildout/the-data-center-boom.html`, `the-compute-buildout/the-power-crunch.html`, `the-compute-buildout/cooling-and-the-plant.html`, `the-compute-buildout/the-picks-and-shovels.html` | The filings now support a stack view from chips and cloud through power, cooling, electrical gear, data centers, and implementation labor. |
| Hidden operating infrastructure | [institutional-operating-infrastructure-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/institutional-operating-infrastructure-initial-theme-memo.md), [services-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/services-sector-initial-brief.md), [cross-sector readout](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/cross-sector/2025-annuals-and-2026-quarterlies-initial-read.md) | `_packs/the-compliance-tax__the-compliance-tax.txt`, `_packs/the-compliance-tax__healthcare-admin.txt`, `_packs/the-compliance-tax__small-operator-squeeze.txt`, `_packs/the-compliance-tax__the-advisors.txt`, `_packs/the-ai-rewiring__law-and-consulting.txt`, `_packs/the-ai-rewiring__accounting-and-audit.txt` | `the-admin-burden-economy/the-admin-burden-economy.html`, `the-admin-burden-economy/complexity-as-a-service.html`, `the-admin-burden-economy/business-process-outsourcing.html`, `the-admin-burden-economy/admin-automation-ai.html`, `the-admin-burden-economy/who-profits.html` | The strongest pattern in the archive is that logistics, compliance, facilities, workflow routing, and healthcare process complexity are being outsourced to specialist operators. |
| Financial infrastructure and flow control | [financial-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/financial-sector-initial-brief.md), [financial-asset-management-flows-and-fee-rate-pressure-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/financial-asset-management-flows-and-fee-rate-pressure-initial-theme-memo.md), [financial-market-infrastructure-and-risk-transfer-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/financial-market-infrastructure-and-risk-transfer-initial-theme-memo.md) | `_packs/money-gets-unbundled__money-gets-unbundled.txt`, `_packs/money-gets-unbundled__banking-scale.txt`, `_packs/money-gets-unbundled__the-card-rails.txt`, `_packs/money-gets-unbundled__the-money-movers.txt`, `_packs/money-gets-unbundled__the-credit-graders.txt`, `_packs/money-gets-unbundled__wall-street-machine.txt`, `_packs/money-gets-unbundled__advice-commoditized.txt` | `everyones-a-bank/everyones-a-bank.html`, `everyones-a-bank/payment-rails.html`, `everyones-a-bank/the-float.html`, `passive-investing/the-big-three.html`, `passive-investing/systemic-concentration.html`, `value-migration/pharma-to-middlemen.html` | The annuals show that control of payments, benchmarks, custody, flows, ratings, ETFs, float, and alternative funding structures is compounding faster than generic balance-sheet exposure. |
| Real-estate split by function | [real-estate-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/real-estate-sector-initial-brief.md), [real-estate-reckoning-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/real-estate-reckoning-initial-theme-memo.md) | `_packs/the-real-estate-reckoning__the-real-estate-reckoning.txt`, `_packs/the-real-estate-reckoning__logistics-and-data.txt`, `_packs/the-real-estate-reckoning__the-office-crisis.txt`, `_packs/the-real-estate-reckoning__housing-squeeze.txt`, `_packs/the-real-estate-reckoning__construction-costs.txt`, `_packs/the-real-estate-reckoning__the-land-play.txt` | `real-estate-is-the-moat/real-estate-is-the-moat.html`, `real-estate-is-the-moat/warehouses-logistics.html`, `real-estate-is-the-moat/data-centers.html`, `real-estate-is-the-moat/rates-reckoning.html` | The current archive now clearly separates logistics, digital infrastructure, housing, and service intermediaries rather than treating real estate as one rate trade. |
| Labor bottlenecks and field execution | [labor-squeeze-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/labor-squeeze-initial-theme-memo.md), [immigration-squeeze-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/immigration-squeeze-initial-theme-memo.md), [industrial-goods-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/industrial-goods-sector-initial-brief.md) | `_packs/the-labor-squeeze__the-labor-squeeze.txt`, `_packs/the-labor-squeeze__skilled-trades.txt`, `_packs/the-labor-squeeze__infrastructure-hands.txt`, `_packs/the-labor-squeeze__the-builders.txt`, `_packs/the-immigration-squeeze__the-immigration-squeeze.txt`, `_packs/the-immigration-squeeze__the-trades.txt`, `_packs/the-immigration-squeeze__care-labor.txt` | `cost-disease/skilled-trades.html`, `cost-disease/infrastructure-megaprojects.html`, `cost-disease/construction-housing.html`, `care-comes-home/who-does-the-caring.html` | Comfort Systems and BrightView make labor capacity a real operating constraint rather than an abstract macro talking point. |
| Barbelled consumer and experience resilience | [consumer-goods-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/consumer-goods-sector-initial-brief.md), [experience-status-and-community-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/experience-status-and-community-initial-theme-memo.md), [consumer-goods-value-portfolio-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/consumer-goods-value-portfolio-initial-theme-memo.md) | `_packs/the-hollow-middle__the-hollow-middle.txt`, `_packs/the-hollow-middle__premium-holds.txt`, `_packs/the-hollow-middle__value-wins.txt`, `_packs/the-hollow-middle__experience-premium.txt`, `_packs/the-experience-economy__the-experience-economy.txt`, `_packs/the-experience-economy__stay-and-celebrate.txt`, `_packs/the-experience-economy__nightlife.txt` | `the-loyalty-economy/hotels-loyalty.html`, `the-loyalty-economy/credit-card-points.html`, `the-loyalty-economy/subscriptions-everything.html`, `the-loneliness-economy/experiences-over-things.html`, `last-call/premiumization.html` | The filings support a consumer split: staples and trusted daily categories on one side, premium experiences and loyalty systems on the other, with weaker middle-market exposure under pressure. |
| Aging and care complexity | [graying-market-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/graying-market-initial-theme-memo.md), [healthcare-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/healthcare-sector-initial-brief.md), [Brookdale packet](/home/manishmehta/ui-projects/annual-report-research-new-lanes/extracted/healthcare/long-term-care-facilities/brookdale-senior-living-inc/company-packet.md) | `_packs/the-graying-market__the-graying-market.txt`, `_packs/the-graying-market__senior-housing.txt`, `_packs/the-graying-market__care-comes-home.txt`, `_packs/the-graying-market__the-caregiver-shortage.txt`, `_packs/the-graying-market__who-pays.txt` | `care-comes-home/care-comes-home.html`, `care-comes-home/home-health-senior-care.html`, `care-comes-home/medicare-advantage-value-based.html`, `care-comes-home/the-home-care-rollup.html`, `the-demographic-cliff/elder-care-silver-economy.html` | Brookdale and the broader healthcare set make elder care, occupancy, reimbursement, and caregiver scarcity concrete rather than thematic. |
| Health and regulation pressure | [healthcare-policy-and-portfolio-initial-theme-memo.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/themes/healthcare-policy-and-portfolio-initial-theme-memo.md), [healthcare-sector-initial-brief.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/analysis/sectors/healthcare-sector-initial-brief.md) | `_packs/the-health-reckoning__the-health-reckoning.txt`, `_packs/the-health-reckoning__the-diet-rewires.txt`, `_packs/the-health-reckoning__the-glp1-shockwave.txt`, `_packs/the-compliance-tax__healthcare-admin.txt` | `care-comes-home/medicare-advantage-value-based.html`, `the-admin-burden-economy/prior-authorization.html`, `the-admin-burden-economy/healthcare-admin-overhead.html`, `cost-disease/hospitals-clinical-care.html` | Healthcare outcomes in the archive are being shaped by reimbursement, utilization, trust, transparency, and administrative drag rather than by simple secular demand. |

## Best immediate handoff candidates

If only a few downstream refreshes happen next, these are the highest-value ones:

1. `the-compute-buildout/`
   The annual-report archive is now rich enough to support a much stronger evidence-backed update across power, cooling, trades, data centers, and AI control layers.

2. `the-admin-burden-economy/`
   The archive now has enough company evidence to make this much more concrete across healthcare administration, workflow software, outsourced compliance, and facilities operations.

3. `money-gets-unbundled`
   The financial archive is now broad enough to separate banks, payments, insurers, traditional asset managers, alternative managers, exchanges, custody, and benchmark/data businesses.

4. `the-real-estate-reckoning`
   The archive now has a better read on logistics, data centers, housing, and the service layer around real estate than the old office-heavy framing.

## Best evidence anchors by company

Use these names first when refreshing downstream work:

- compute / infrastructure:
  - Microsoft
  - NVIDIA
  - ServiceNow
  - Cisco
  - Eaton
  - Trane
  - Equinix
  - Digital Realty
  - Prologis
  - Constellation
  - NRG
- hidden operating infrastructure:
  - Cintas
  - APi
  - ABM
  - Waste Management
  - CHRW
  - UPS
  - CBRE
  - JLL
  - UnitedHealth
  - Accenture
- financial infrastructure:
  - JPMorgan
  - American Express
  - Chubb
  - T. Rowe Price
  - BlackRock
  - Blackstone
  - Apollo
  - CME
  - State Street
  - S&P Global
- consumer / experience:
  - PepsiCo
  - P&G
  - Kimberly-Clark
  - Graphic Packaging
  - Estee Lauder
  - Live Nation
  - Hilton
- labor / immigration:
  - Comfort Systems
  - BrightView
  - ABM
  - Robert Half
- aging / care:
  - Brookdale
  - UnitedHealth
  - HCA
  - Abbott

## Working conclusion

The annual-report archive now has enough depth that downstream work should stop using purely thematic language where company evidence exists.

The immediate job is not to invent new taxonomies. It is to route the current evidence into the exact force packs and dossier pages that already exist nearby.
