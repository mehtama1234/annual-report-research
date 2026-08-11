# Expanded Goal Plan

Date: 2026-08-10
Repo: `annual-report-research`
Branch: `cli4-healthcare-frontier-batch`

## Packet Inputs Used

- the branch-level healthcare frontier scope that pairs company-packet completion with cross-company interpretation
- the standard source chain of `2025` annual report, annual filing, and latest three reported quarters as of `2026-08-10`
- the repo-wide requirement that each covered company must produce both filing coverage and thematic interpretation
- the broader lane-expansion instruction that adjacent sectors should be added when they sharpen recurring consumer, societal, industrial, or operating patterns
- the batch-output expectation that company profiles, source ledgers, packets, and at least one real cross-company memo should all come out of the same run

## Working objective

The active objective is no longer just to collect annual reports and quarter chains.
The required output is a set of coherent, source-complete company packets plus cross-company interpretation that explains the recurring consumer, cultural, societal, industrial, and operating patterns revealed by those packets.

This branch should therefore be treated as:

1. an evidence-collection workflow
2. a company-packet workflow
3. a thematic pattern-finding workflow

## Core collection rule

For every flagship company covered in this branch:

- use the `2025` annual report and annual filing
- use the latest three reported quarters as of `2026-08-10`
- use AnnualReports.com for taxonomy and archive confirmation
- use official company IR and SEC sources as authoritative when AnnualReports lags

Each covered company must produce both:

- a source-complete packet
- a thematic interpretation

## Lane expansion now in scope

### 1. Healthcare frontier

Direct coverage requested:

- Biotechnology
- Diagnostic Substances
- Drug Manufacturers - Other
- Drug Delivery
- Drug Related Products
- Drugs - Generic
- Medical Laboratories & Research
- Specialized Health Services

This work must explicitly identify:

- consumer behavior around treatment adherence, trust, convenience, affordability, and care access
- cultural and societal shifts around aging, chronic disease burden, specialty therapies, home-based care, and diagnostic dependence
- industrial and operating pressures including reimbursement, utilization, site-of-care migration, pipeline concentration, patent cliffs, manufacturing complexity, sterile fill-finish, supply-chain reliability, and labor intensity
- repeated higher-order patterns including franchise and IP monetization, recurring care complexity, diagnostic-infrastructure dependence, and the physical delivery layer behind modern therapies

Current flagship set chosen for this lane:

- `Regeneron Pharmaceuticals, Inc.` for biotechnology, franchise concentration, and pipeline dependence
- `Labcorp Holdings Inc.` for diagnostic substances plus medical laboratories and research infrastructure
- `Teva Pharmaceutical Industries Ltd.` for drugs-generic and drug-manufacturers-other coverage
- `West Pharmaceutical Services, Inc.` for drug delivery and drug-related-products exposure
- `Option Care Health, Inc.` for specialized health services and recurring care complexity outside the acute-hospital frame

Why this set works:

- it avoids collapsing the lane into big pharma and hospitals
- it covers both molecule risk and service-layer complexity
- it captures the physical, diagnostic, and recurring-care infrastructure around treatment

### 2. Energy / extractives expansion

Additional areas requested:

- Synthetics
- Cement
- Metal Fabrication
- Pollution & Treatment Controls
- Farm Products
- Rubber & Plastics

Why this matters:

- extends raw-material chains into downstream physical inputs
- adds environmental infrastructure and treatment-control exposure
- improves coverage of construction, industrial-input, agricultural, and materials-processing dependence
- helps the archive connect extraction and processing to real-world physical infrastructure systems

Planned interpretation focus for this lane:

- commodity pass-through versus conversion-margin pressure
- downstream environmental compliance and treatment demand
- capital intensity, maintenance burden, and utilization sensitivity
- construction and industrial-cycle dependence
- agricultural demand, volume risk, and biological or seasonal variability

### 3. CLI 2 mobility / vehicles / freight expansion

Additional areas requested:

- Industrial Equipment Wholesale
- Building Materials Wholesale
- Basic Materials Wholesale
- Computers Wholesale
- Electronics Wholesale
- Rental & Leasing Services

Why this matters:

- adds the distributor layer between manufacturers and end markets
- shows how vehicles, equipment, materials, and technology actually move through the economy
- captures fleet access, rental utilization, replacement timing, inventory turns, and working-capital discipline
- broadens mobility from OEM and freight operators into channel, access, and equipment-flow economics

Planned interpretation focus for this lane:

- fleet and equipment utilization
- channel inventory and reseller economics
- replacement-cycle sensitivity
- working-capital and receivables discipline
- pricing power versus service intensity in distribution models

## Operating rules for this branch

- Aim for `3-5` flagship companies per coherent batch, not dozens of shallow starts.
- Do not update shared repo-wide indexes continuously during exploration.
- Update repo-wide indexes only after a batch is source-complete or hand the work back for integration.
- Keep the source taxonomy in folders when the archive source disagrees with operating reality, but correct the economic interpretation inside packets and memos.

## Required outputs for each coherent batch

Each finished batch should end with:

- commit hash
- companies completed
- companies partial
- industry lane summary
- next recommended names

Each finished batch should also produce:

- company profiles
- source ledgers
- company packets
- at least one cross-company memo or theme memo that explains the recurring pattern set

## Immediate next batch

The first coherent batch on this branch should be the healthcare frontier set listed above.

Reason:

- it already has a branch started
- the company set is stable
- it is the most clearly defined unmet scope in the current conversation
- it establishes the packet-plus-theme standard that the later energy and mobility expansions can reuse

## Insight-System Maintenance

When you need to confirm that this expanded goal plan, the continuation stack, and the broader note layer still line up before reusing it as an operator reference, use:

- `bash scripts/run-insight-audit-stack.sh`
- `bash scripts/refresh-note-layer-boundary.sh`
- `bash scripts/audit-audit-stack-terminology.sh`
- `bash scripts/audit-maintenance-doc-stack.sh`
- `bash scripts/audit-continuation-mode-links.sh`
- `bash scripts/audit-remaining-brief-links.sh`
- `bash scripts/audit-remaining-stack-links.sh`
- `bash scripts/audit-browser-review-links.sh`
- `bash scripts/verify-insight-system.sh`

## Skeptical Reader Test

- Does this plan make clear that the branch is supposed to produce evidence collection, company packets, and pattern-finding together?
- Can a skeptical reader tell which exact outputs are required before the batch counts as coherent?
- Does the note explain why lane expansion is allowed and what standard those added areas must meet?
- What would show that the branch is still collecting source material without converting it into cross-company understanding?
