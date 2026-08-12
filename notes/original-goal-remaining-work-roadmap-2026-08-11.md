# Original Goal Remaining Work Roadmap

Date baseline: `2026-08-11`

## Purpose

This note translates the original frontier goal into exact remaining work.

The main distinction is:

- some work is genuinely missing because the lane is still too thin
- some work already exists on disk, but it is not cleanly integrated into the intended lane taxonomy

That distinction matters because the next pass should not waste time rediscovering packets that already exist.

## What is already closed enough to support synthesis

The repo now has committed proof pages for the four main frontier areas:

- [CLI 4 healthcare proof page](/home/manishmehta/ui-projects/annual-report-research/analysis/themes/cli-4-healthcare-proof-page-2026-08-11.md)
- [CLI 5 connectivity proof page](/home/manishmehta/ui-projects/annual-report-research/analysis/themes/cli-5-connectivity-proof-page-2026-08-11.md)
- [CLI 6 trust and capital proof page](/home/manishmehta/ui-projects/annual-report-research/analysis/themes/cli-6-trust-and-capital-proof-page-2026-08-11.md)
- [Recreation participation proof page](/home/manishmehta/ui-projects/annual-report-research/analysis/themes/recreation-participation-proof-page-2026-08-11.md)

That means the biggest remaining problem is no longer absence of lane-level interpretation.

The remaining problem is uneven lane closure.

## Remaining work by lane

### CLI 4: Healthcare Frontier

#### Current packet depth in the targeted sub-lanes

- `managed-health-care`: `1`
- `medical-care-facilities`: `1`
- `long-term-care-facilities`: `1`
- `medical-appliances-equipment`: `2`
- `medical-instruments-supplies`: `12`
- `drug-manufacturers-general`: `2`

#### What that means

Healthcare is strong in tools, diagnostics, monitoring, and treatment-enablement.

Healthcare is still thin in the large scaled recurring-care anchors that the user explicitly wanted for comparison:

- payer systems
- hospitals
- long-term care
- large drug manufacturers

#### Highest-value remaining work

1. Deepen the payer comparison now that `The Cigna Group` gives the lane a second flagship health-plan anchor.
2. Deepen the provider comparison now that `Tenet Healthcare Corporation` gives the lane a second flagship hospital anchor.
3. Add one or two more major drug manufacturers to strengthen the comparison between recurring therapeutic demand and care-delivery burden.
4. Tighten the bridge between enabling-layer economics and burdened care-delivery economics in the existing synthesis pages.

#### Best next names

1. `Eli Lilly and Company`
2. `Merck & Co., Inc.`
3. `Universal Health Services, Inc.` only if the goal is a third large hospital comparator rather than practical closure
4. a stronger long-term-care or scaled-care comparator if broader direct-care contrast is the goal

### CLI 5: Connectivity, Telecom, And Technical Infrastructure

#### Current packet depth in the targeted sub-lanes

- `internet-software-services`: `7`
- `telecom-services-domestic`: `3`
- `wireless-communications`: `2`
- `data-storage-devices`: `4`
- `scientific-technical-instruments`: `2`
- `semiconductor-equipment-materials`: `4`
- `application-software`: `19`
- `computer-based-systems`: `1`
- `computer-peripherals`: `1`
- `diversified-computer-systems`: `1`
- `diversified-electronics`: `1`
- `information-technology-services`: `6`
- `internet-information-providers`: `11`
- `security-software-services`: `1`
- `multimedia-graphics-software`: `2`

#### Taxonomy drift that should not be mistaken for missing research

The lane has meaningful coverage that already exists under adjacent or alternate directories:

- `diversified-communication-services` exists under `technology/diversified-communication-services/`
- wireless and telecom names exist under both `services/...` and `technology/...`
- communication equipment and networking names are spread across:
  - `technology/communication-equipment/`
  - `technology/networking-communication-devices/`

This means CLI 5 is broader than a shallow directory count suggests.

#### What is actually thin

The real thin spots are not the core carrier or software-control narrative.

The real thin spots are the requested hardware and systems extensions:

- computer-based systems
- computer peripherals
- diversified computer systems
- diversified electronics
- a second clear security-software control layer inside the exact requested taxonomy

#### Highest-value remaining work

1. Strengthen the hardware-and-systems extension so the lane is not overly skewed toward software and networks.
2. Add another security control-layer anchor and tighten its comparison against networking and validation layers.
3. Do a cleanup pass that maps duplicate telecom and communications packets into a clearer shared lane view.

#### Best next names

1. `Lenovo Group Limited` or another clear computer-systems anchor
2. `HP Inc.`
3. `TE Connectivity plc`
4. `Fortinet, Inc.` or `Gen Digital Inc.`

### CLI 6: Capital Structures, Property, And Conglomerates

#### Current packet depth in the targeted sub-lanes

- regional-bank coverage is present, but split across:
  - `financial/regional-mid-atlantic-banks/`
  - `financial/regional-midwest-banks/`
  - `financial/regional-southeast-banks/`
- `life-insurance`: `1`
- `insurance-brokers`: `3`
- `reit-mortgage`: `1`
- `reit-retail`: `2`
- `reit-healthcare-facilities`: `2`
- `financial/conglomerates`: directory exists but no packet anchors inside it

#### Taxonomy drift that should not be mistaken for missing research

Some names that matter to the lane already exist, but under adjacent categories:

- `Markel Group Inc.` sits under `financial/property-casualty-insurance/`
- `Brookfield Corporation` and `KKR & Co. Inc.` sit under `financial/asset-management/`
- additional conglomerate-like coverage also exists under `industrial-goods/conglomerates/`

This means the trust-and-capital thesis is better covered than a narrow folder check implies.

#### What is actually thin

The thin areas are the exact capital-heavy archive targets:

- life insurance
- mortgage REITs now have two explicit pure anchors through `Annaly` and `AGNC`, and savings-and-loans now has an explicit thrift analog through `WaFd`, so the remaining question is comparison depth and proof quality rather than basic bucket presence
- retail REITs beyond the current pair
- healthcare-facility REIT depth
- explicit conglomerate / allocator closure under the intended lane

#### Highest-value remaining work

1. Deepen the life-insurance comparison now that `Prudential Financial, Inc.` gives the lane a second flagship anchor.
2. Add a second thrift-style or savings-and-loans analog only if the goal is a wider spread-risk comparison beyond the now-explicit `WaFd` anchor.
3. Add at least one more conglomerate or allocator packet and place it in a lane-appropriate structure.
4. Tighten the comparison between fee-like intermediaries and heavier spread-risk balance-sheet models.

#### Best next names

1. a second thrift or savings-and-loans analog only if deeper cluster depth matters more than proof tightening elsewhere
2. `Berkshire Hathaway Inc.`
3. `Apollo Global Management, Inc.`
4. a third life-insurance name only if broader closure is more valuable than another lane gap

### Recreation, Lifestyle, And Participation

#### Current packet depth in the targeted sub-lanes

- `home-furnishing-stores`: `2`
- `home-furnishings-fixtures`: present under `services/home-furnishings-fixtures/` rather than under `consumer-goods/`
- `jewelry-stores`: `1`
- `specialty-retail-other`: `1`
- `food-wholesale`: `1`
- hospitality-adjacent coverage is present across:
  - `services/lodging/`
  - `services/resorts-casinos/`
  - `real-estate/reit-hotel-motel/`

#### Taxonomy drift that should not be mistaken for missing research

This lane is stronger than one narrow directory check suggests because hospitality is split across multiple useful operating formats:

- brand and loyalty layer: `Marriott`
- heavy asset hotel owners: `Host`, `Apple Hospitality`, `Sunstone`
- destination gaming and leisure systems: `Caesars`, `Las Vegas Sands`

#### What is actually thin

The thin areas are the requested lifestyle extensions beyond lodging and gaming:

- jewelry
- food wholesale behind hospitality
- specialty retail other
- more depth in home-expression and home-fixtures

#### Highest-value remaining work

1. Add another occasion-demand or gifting anchor.
2. Add at least one more behind-the-experience food and hospitality supplier.
3. Add another home-expression name so the lane is not overly dependent on Wayfair.
4. Tighten the comparison between experience owners, relationship owners, and behind-the-scenes supply layers.

#### Best next names

1. `Signet Jewelers Limited`
2. `Sysco Corporation`
3. `Williams-Sonoma, Inc.`
4. `Chewy, Inc.`

## Cross-lane work that is still missing

### 1. Thin-sub-lane closure

The original goal asked for new frontiers that feel complete, not merely represented.

The most obvious remaining gap is still the sub-lanes with only `1` or `2` flagship packets.

### 2. Taxonomy cleanup

Several lanes already have enough raw material to support a stronger “complete lane” claim, but the packets are split across alternate sector folders.

That creates a false impression of missing research.

The highest-value integration work is:

- map telecom and communications duplicates into one shared CLI 5 view
- map regional-bank sub-lanes into one clean CLI 6 lane summary
- map hospitality-related packets into one clean recreation lane summary
- map conglomerate-like and allocator-like names into a more coherent CLI 6 ownership frame

### 3. Claim-to-evidence deepening

The new proof pages solved part of the original problem, but the strongest remaining editorial work is still:

- add more exact examples inside each big claim
- keep tying every broad pattern back to named companies, figures, and operating details
- keep separating strong conclusions from overreach

## Best exact next batch if the goal is to close the highest-value gaps fast

1. `Eli Lilly and Company`
2. `HP Inc.`
3. `TE Connectivity plc`
4. `AGNC Investment Corp.` is now the completed second pure mortgage-REIT anchor rather than a next target
5. `Sysco Corporation`
6. `Williams-Sonoma, Inc.`
7. a second pure-play healthcare-IT or hospital-workflow name only if broader CLI 5 subcluster depth is more valuable than another lane-edge gap
8. `Universal Health Services, Inc.` only if a third hospital comparator becomes more valuable than another lane gap

## Bottom line

The original goal is no longer blocked by lack of frontier material.

It is still missing:

- enough flagship depth in the thinnest requested sub-lanes
- cleaner taxonomy integration where coverage exists but is fragmented
- another pass of claim-to-evidence strengthening in the lane syntheses

That is the real remaining work.
