# Annual Report Research and IBIS Industries Alignment

Date baseline: 2026-08-09

## What I checked

I reviewed:

- [README.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/README.md)
- [coverage-tracker.csv](/home/manishmehta/ui-projects/annual-report-research-new-lanes/indexes/coverage-tracker.csv)
- [theme-tracker.csv](/home/manishmehta/ui-projects/annual-report-research-new-lanes/indexes/theme-tracker.csv)
- [force-map.csv](/home/manishmehta/ui-projects/annual-report-research-new-lanes/indexes/force-map.csv)
- [README.md](/home/manishmehta/ui-projects/ibis-industries/README.md)
- [ECONOMIC_INTELLIGENCE_FRAMEWORK.md](/home/manishmehta/ui-projects/ibis-industries/ECONOMIC_INTELLIGENCE_FRAMEWORK.md)
- [ECONOMY_2025_2026_NARRATIVE.md](/home/manishmehta/ui-projects/ibis-industries/ECONOMY_2025_2026_NARRATIVE.md)

## Clean read

`ibis-industries` and `annual-report-research` are complementary, not redundant.

- `ibis-industries` is the broad US-industry interpretation layer.
- `annual-report-research-new-lanes` is the dated company-evidence layer built from `2025` annual reports plus the latest three reported quarters in scope as of `2026-08-09`.

The practical relationship is:

1. `ibis-industries` gives the macro force map.
2. `annual-report-research` proves or refines those forces with company filings, earnings releases, and management commentary.
3. Sector synthesis in `annual-report-research` can then flow back into stronger force and theme writeups.

## What already lines up well

The mapping is already structurally sound.

### Force and theme overlap

The annual-report repo already uses force labels and theme logic that clearly match the `ibis-industries` framework:

- `the-ai-rewiring`
- `the-compute-super-cycle`
- `the-breach-economy`
- `the-compliance-tax`
- `money-gets-unbundled`
- `atoms-strike-back`
- `the-electrification`
- `the-margin-vise`
- `the-channel-shift`
- `the-health-reckoning`
- `the-pricing-power-collapse`
- `the-hollow-middle`
- `the-great-consolidation`

That means the annual-report archive is already using the right conceptual backbone rather than inventing a second taxonomy.

### Sector evidence already strong

As of `2026-08-09`, the annual-report repo has meaningful sector synthesis for:

- `Technology`
- `Financial`
- `Healthcare`
- `Industrial Goods`
- `Services`
- `Real Estate`
- `Consumer Goods` at the theme stage, with packet coverage already present

This is enough to support real cross-sector reading rather than isolated company summaries.

### Best current overlap by force

The strongest current proof points are:

- `the-ai-rewiring` and `the-compute-super-cycle`
  - Technology
  - Industrial Goods
  - selected Services
- `money-gets-unbundled`
  - large banks
  - card rails
  - exchanges
  - ratings and data
  - asset managers and alternatives
- `the-health-reckoning` and `the-pricing-power-collapse`
  - managed care
  - providers
  - biopharma
  - devices
  - life-science tools
- `institutional-operating-infrastructure`
  - ServiceNow
  - Accenture
  - UPS
  - Cintas
  - APi
  - ABM
  - Waste Management
  - UnitedHealth

## What the annual-report repo is adding that IBIS alone cannot

`ibis-industries` is broad, but the annual-report repo adds several things it does not naturally provide:

- exact annual and quarterly reporting windows
- company-by-company source ledgers
- management commentary tied to a specific quarter
- balance-sheet and capital-allocation context
- evidence for whether a force is helping revenue, margin, backlog, pricing, utilization, or guidance
- direct comparison between business models inside the same sector

This is the main value of keeping the annual-report archive separate and organized.

## Current gaps

The biggest gaps are not taxonomy gaps. They are coverage gaps.

### 1. Consumer is underbuilt relative to the force map

`ibis-industries` has a much richer consumer and cultural structure than the current annual-report archive proves.

The main under-covered areas are:

- experience economy
- hollow middle beyond staples
- channel shift in retail and commerce
- health-reckoning effects inside food, beverage, alcohol, dining, and wellness-adjacent consumer categories
- premium versus value bifurcation outside household staples

This is the clearest next expansion area.

### 2. Cultural and social themes still lean indirect

The annual-report repo already has a cross-sector memo on value, trust, and automation, but its company set is still skewed toward large institutional operators.

Missing cultural-economy evidence likely includes:

- entertainment and live experiences
- travel and leisure
- restaurant or beverage demand shifts
- platform-native commerce behavior
- labor-model changes in service businesses

### 3. Real estate is good, but still concentrated in infrastructure-tilted names

The current real-estate coverage is strong for:

- logistics
- data-center infrastructure
- real-estate services
- residential demand

It is weaker on:

- office distress as a standalone earnings problem
- retail-property economics
- hospitality property exposure

### 4. Energy and materials are still light

`ibis-industries` has stronger force language around commodity exposure, fuels, fertilizer, metals, and agricultural cycles than the annual-report archive currently proves with filings.

This matters if the goal is to speak confidently about:

- commodity whiplash
- physical input inflation
- energy-linked capex and margin dynamics
- industrial policy spillovers

## Best next collection targets

If the goal is to strengthen the combined system efficiently, the next targets should be chosen by force-gap, not by random sector completion.

Recommended order:

1. `Consumer`
   - add experience, premium, value, and health-shift names
   - this closes the biggest gap between the macro force map and company evidence
2. `Energy and Materials`
   - add commodity and physical-input names
   - this makes `atoms-strike-back`, `commodity-whiplash`, and infrastructure repricing more defensible
3. `Additional Real Estate edge cases`
   - one office-stress name
   - one retail or hospitality property name
4. `More culturally exposed Services`
   - leisure, entertainment, travel, or labor-model-sensitive operators

## Practical implication

The archive is already organized correctly:

- separate git repo
- clean raw / extracted / analysis split
- source-ledger discipline
- sector and theme trackers
- explicit force mapping

So the main issue is no longer structure. It is selective expansion.

The highest-value move now is to use the existing `ibis-industries` force map as the shopping list for what company packets to add next, starting with consumer and then commodity-and-energy exposure.
