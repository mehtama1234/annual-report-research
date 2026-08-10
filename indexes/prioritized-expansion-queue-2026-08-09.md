# Prioritized Expansion Queue

Date baseline: 2026-08-09

This file converts the current archive state into an execution queue.

It is not a wish list. Each lane below is based on evidence already present in:

- [research-master-map-2026-08-09.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/indexes/research-master-map-2026-08-09.md)
- [coverage-tracker.csv](/home/manishmehta/ui-projects/annual-report-research-new-lanes/indexes/coverage-tracker.csv)
- [consumer-interface-research-index-2026-08-09.md](/home/manishmehta/ui-projects/annual-report-research-new-lanes/indexes/consumer-interface-research-index-2026-08-09.md)
- [theme-tracker.csv](/home/manishmehta/ui-projects/annual-report-research-new-lanes/indexes/theme-tracker.csv)

## Priority logic

Priority is based on four factors:

1. analytical leverage across multiple themes
2. visible undercoverage in the current archive
3. unresolved source gaps on strategically important names
4. whether one addition would materially improve a weak comparison set

## Priority 1

These are the highest-leverage next moves.

### 1. Retail repair and expansion

Why this is first:

- `Retail` has only `2` source-taxonomy names in `coverage-tracker.csv`.
- The broader consumer-interface argument already depends heavily on retail-like operators that are currently classified under `Services`.
- The current direct `Retail` split is still too thin: `Amazon` and `NIKE` are useful but not enough to support a broad retail conclusion.

Current anchor names:

- `Amazon`
- `NIKE`
- retail-like comparison operators currently sitting under `Services`: `Costco`, `Walmart`, `Kroger`, `Dollar General`, `Dollar Tree`, `Best Buy`, `Ross`, `Home Depot`

Queue actions:

1. strengthen the direct `Retail` bucket with another platform-scale retail name
2. add another brand-led retail name to test whether the `NIKE` pattern generalizes
3. keep cross-linking the retail-like names that currently live under `Services`

Expected payoff:

- stronger retail sector synthesis
- cleaner consumer-interface comparisons
- better separation between platform retail, replenishment retail, off-price retail, and brand-led direct relationship models

### 2. Consumer-interface archive repair on strategically important names

Why this is first-tier:

- Several of the archive's most important consumer-interface names still lack direct annual-report artifacts saved locally.
- The theme logic is already strong, but the raw collection base is uneven.

Current high-value missing annual-report artifacts:

- `Amazon`
- `NIKE`
- `Costco`
- `Walmart`
- `Kroger`
- `Starbucks`
- `McDonald's`
- `Domino's`
- `Delta`
- `Caesars`
- `Dollar General`

Current high-value transcript gaps:

- `Caesars`
- `McDonald's`
- `Best Buy`
- `Ross`
- several travel and restaurant names where quarter commentary would sharpen mechanism-level comparisons

Queue actions:

1. repair missing direct annual-report artifacts where retrieval is still feasible
2. keep explicit blocker notes where environment or edge denial makes retrieval non-local
3. fill transcript gaps on the highest-leverage consumer-interface operators before broadening into weaker names

Expected payoff:

- stronger raw evidence base under the most important consumer themes
- fewer weak spots when comparing membership, stored value, ordering flow, and wallet-linked behavior

### 3. Travel, status, and wallet comparison set expansion

Why this is first-tier:

- `Delta`, `Hilton`, and `Caesars` form a strong pattern, but the travel-and-status lane is still thin.
- The repo already treats this as strategically important in the `experience-status-and-community`, `recurring-consumer-interfaces`, and `loyalty-currencies` themes.

Current anchor names:

- `Delta`
- `Hilton`
- `Caesars`
- `American Express` as the linked financial analogue

Queue actions:

1. add one more travel operator to test whether the current pattern is operator-specific or structurally broader
2. prefer a name that sharpens one of these distinctions:
   - hotel loyalty versus airline loyalty
   - travel booking versus owned stay network
   - gaming wallet behavior versus traditional travel status behavior

Expected payoff:

- more defensible experience and loyalty themes
- better comparison between partner-monetized, fee-based, and wallet-linked consumer systems

## Priority 2

These moves matter, but they should follow the first-tier work.

### 4. Consumer Goods routine-use comparison deepening

Why it matters:

- `Consumer Goods` is already relatively well packetized.
- The conceptual framework is good, but the routine-use layer would benefit from one more comparison inside staples, beverage, wellness, or indulgence.

Current anchor names:

- `PepsiCo`
- `Procter & Gamble`
- `Kimberly-Clark`
- `Colgate-Palmolive`
- `Monster`
- `Graphic Packaging`

Queue actions:

1. add one more name that sharpens routine-use behavior rather than just broad portfolio scale
2. use that addition to pressure-test the line between trusted routine use, indulgence, and functional consumption

Expected payoff:

- stronger consumer-goods interface logic
- better bridge between routine purchase behavior and the broader consumer-interface framework

### 5. Services taxonomy cleanup through interface indexing

Why it matters:

- `Services` is broad and productive, but it is carrying many retail-like names because of source taxonomy quirks.
- The archive already has the right conceptual response: interface maps and cross-sector theme files. It now needs a slightly more operational view.

Queue actions:

1. keep preserving source taxonomy in folders
2. expand the interface indexes so the mixed `Services` bucket becomes easier to navigate
3. keep using sector-plus-interface dual classification rather than trying to overwrite source taxonomy

Expected payoff:

- less confusion about what is truly a service operator versus a retail or consumer-interface operator
- better repo navigation as the archive grows

### 6. Built-environment and housing chain widening

Why it matters:

- This is already one of the better-developed cross-sector tracks.
- It still has room for a few more operators before it becomes a genuinely robust chain from materials through distribution through builder execution through maintenance and repair.

Current anchor names:

- `Builders FirstSource`
- `D.R. Horton`
- `Lennar`
- `West Fraser`
- `Sherwin-Williams`
- `Lowe's`
- `Home Depot`

Queue actions:

1. add another operator that sharpens the chain rather than duplicating an existing layer
2. prefer names that clarify affordability pressure, repair-and-remodel resilience, or professional workflow capture

Expected payoff:

- stronger housing-affordability and built-environment synthesis
- better connection between materials, channel control, builder economics, and downstream maintenance demand

## Priority 3

Useful, but not the best next move unless higher-priority work stalls.

### 7. Additional interface maps in dense mixed sectors

The current interface-map approach is already useful in:

- technology
- financials
- consumer interfaces

The next sectors most likely to justify their own structured interface map are:

- broader services
- built environment / housing chain
- experience and travel

### 8. More transcript normalization across the archive

This matters, but it is lower priority than adding missing annual-report artifacts on strategically important names.

The main reason:

- many current themes are already analytically usable
- direct annual reports and quarter artifact completeness still have higher leverage than transcript polish alone

## Working sequence

If the goal is to move the archive forward efficiently from here, the cleanest order is:

1. expand and stabilize direct `Retail`
2. repair strategically important consumer-interface artifact gaps
3. widen travel / loyalty / wallet comparisons
4. deepen Consumer Goods routine-use comparisons
5. keep improving interface-based navigation across mixed-taxonomy sectors

## Current operating stance

As of 2026-08-09, the repo no longer needs broad structural redesign.

It needs disciplined densification:

- more names where the comparison set is still thin
- better artifact completeness on the most important interface operators
- continued theme refinement where one new packet changes the broader read
