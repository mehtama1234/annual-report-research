# Capital Flow All-Company Extraction Template Pass 1

## Purpose

This pass resolves `CFARQ-015`:

`Can the case-study capital-flow system scale across the full 519-company universe without losing proof discipline?`

The operating table is:

`analysis/company-first-principles/data/capital-flow-all-company-extraction-template-pass-1.csv`

## Short Answer

Yes, as a template and queue-control system.

Every company in the `519` company triage now has a row with:

- lane
- capital-flow role
- likely funding wrapper
- source availability
- current proof level
- denominator need
- next document
- safe claim
- do-not-claim boundary

This upgrades the research system from case-study evidence to scalable operating model, but it does not mean every company is source-proven.

## Row Counts

| Metric | Count |
|---|---:|
| Template rows | `519` |
| Priority status: `monitor` | `204` |
| Priority status: `high-signal-backlog` | `122` |
| Priority status: `retain-low-signal` | `122` |
| Priority status: `selected-lane-queue` | `71` |

## Lane Coverage

| Lane | Rows |
|---|---:|
| `capital_intensity_and_capex` | `148` |
| `power_grid_and_project_finance` | `125` |
| `acquisition_finance` | `99` |
| `low_signal_general_company` | `82` |
| `debt_refinancing_and_facilities` | `33` |
| `asset_backed_and_securitization` | `13` |
| `insurance_and_retirement_capital` | `11` |
| `private_credit_direct_lending` | `7` |
| `government_and_public_funding` | `1` |

## Proof Levels

| Proof Level | Rows |
|---|---:|
| `universe-radar` | `244` |
| `high-signal-radar` | `122` |
| `radar-only-low-signal` | `82` |
| `lane-queue-candidate` | `71` |

## Source Availability

| Source Availability | Rows |
|---|---:|
| `packet-and-source-pointers` | `352` |
| `packet-only` | `117` |
| `packet-analysis-and-source-pointers` | `32` |
| `packet-and-analysis` | `18` |

## Template Standard

| Field | Why It Exists |
|---|---|
| `capital_flow_role` | Converts a company from generic sector coverage into a testable capital-flow role. |
| `likely_funding_wrapper` | Names the expected financing container before source extraction. |
| `source_availability` | Separates packet-only rows from rows with analysis and source pointers. |
| `current_proof_level` | Prevents radar rows from being promoted as source-grade evidence. |
| `denominator_need` | Names the outside or internal denominator required before market-scale claims. |
| `next_document` | Turns each company into an actionable source task. |
| `safe_claim` | Gives the strongest currently allowed sentence. |
| `do_not_claim` | Blocks premature source-to-use-to-output language. |

## Claim Status

Promote:

`The 519-company universe now has a role/wrapper/proof extraction template that can route every company into a lane, expected funding wrapper, source-availability status, proof level, denominator need, next-document target, safe claim, and do-not-claim boundary.`

Do not promote:

`Every company in the 519-company universe is source-proven or representative of the final thesis.`

## Queue Decision

`CFARQ-015` outcome:

`upgrade-with-boundary - every company now has the required template fields, but most rows remain radar or queue status until primary-source extraction is run.`

## Next Best Work

The answer-resolution queue has now been worked through pass 1. The next phase should use this template to run lane-specific extraction batches, starting with the highest-impact unresolved public claims:

1. insurance statutory quality
2. bank/private-credit lane-share denominator
3. ET/Cheniere named-project source-use-return registry
4. grid/power project status and recovery mechanism
5. all-company role/wrapper/proof refresh after each new source batch

The first batch-refresh design is now:

`/cluster/capital-flow-519-company-batch-evidence-refresh-pass-1.md`

It converts the template and `71` row lane queue into lane-specific extraction packages and a balanced `35` row pilot.
