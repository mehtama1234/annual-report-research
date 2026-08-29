# Capital Flow Cash Return Source Work Order Pass 1

## Purpose

This page converts the executed money-movement synthesis into an acquisition work order.

The question is:

`What exact source package should we pursue next for each executed money-movement case to upgrade proxy evidence into cash-return proof, or to prove that the upgrade is not available?`

The structured companion table is:

`analysis/company-first-principles/data/capital-flow-cash-return-source-work-order-pass-1.csv`

The upstream synthesis is:

`/cluster/capital-flow-executed-money-movement-synthesis-pass-1.md`

## Short Answer

`The next work is a ranked proof-acquisition program, not another summary. Wheaton, FPL, Cheniere, URI, and Sterling are the highest-leverage targets because their current evidence already has source/use/output/cash-proxy structure. The work order defines the decisive source package and pass/hold test for all 16 executed cases.`

## Top Five Proof Hunts

| Priority | Case | Decisive Source Package | Upgrade Sought | Boundary If Missing |
|---:|---|---|---|---|
| 1 | Wheaton Antamina | Delivered-ounce/cash-receipt, tax, interest, debt-service, reserve-life, IRR/NPV support | Named PMPA cash-return proof | Executed as `/cluster/capital-flow-wheaton-antamina-full-return-source-test-pass-1.md`; remains strongest proxy, not full return proof. |
| 2 | FPL Distribution Inspection | 2027 SPPCRC actual/estimated filing, billing determinants, category allocation, financing support | Category customer receipts and funding allocation | Executed as `/cluster/capital-flow-fpl-distribution-inspection-customer-receipt-source-test-pass-1.md`; remains regulated recovery proxy. |
| 3 | Cheniere LNG | Train/entity waterfall, SPA economics, cargo mapping, capex, debt-service support | Train-level source/use/customer-cash proof | Executed as `/cluster/capital-flow-cheniere-train-cash-waterfall-source-test-pass-1.md`; remains company/entity-level output and demand proxy. |
| 4 | URI fleet | Fleet-class OEC, utilization, growth/replacement capex, collateral certificates, segment profit | Fleet-class cash-yield/ROIC proof | Executed as `/cluster/capital-flow-uri-fleet-cash-yield-source-test-pass-1.md`; remains company-level fleet cash-yield proxy. |
| 5 | Sterling backlog | Owner funding, retainage/receivables, bonded backlog, actual L/C/surety use, project margin | Project cash-collection proof | Executed as `/cluster/capital-flow-sterling-project-cash-collection-source-test-pass-1.md`; remains backlog-to-company-cash proxy. |

## Work Order Logic

Every row has the same decision structure:

`target source package -> fields to extract -> pass test -> hold/disproof test -> next artifact`

The important discipline is that a row is allowed to stay bounded. A missing source is not a failure of the system; it is the evidence boundary that prevents an overclaim.

## Execution Update

`CFCRSWO-001` is now executed as:

`/cluster/capital-flow-wheaton-antamina-full-return-source-test-pass-1.md`

The result is `full-return-source-test-hold-with-strong-proxy`. Wheaton Antamina still has the strongest named source/use/cash-return proxy in the system, but full PMPA return remains unproven because delivered-ounce cash receipts, Antamina-specific tax, Antamina-specific interest, debt-service waterfall, lender allocation, reserve-life sufficiency, IRR, and NPV are not visible in the current local source set.

`CFCRSWO-002` is now executed as:

`/cluster/capital-flow-fpl-distribution-inspection-customer-receipt-source-test-pass-1.md`

The result is `customer-receipt-source-test-hold-with-regulated-recovery-proxy`. FPL Distribution Inspection still has the strongest regulated recovery bridge in the system, but category customer-receipt and funding-allocation proof remain unproven because billing determinant allocation, category receipt support, source-of-funds allocation, project IRR, and earned shareholder return are not visible in the current local source set.

`CFCRSWO-003` is now executed as:

`/cluster/capital-flow-cheniere-train-cash-waterfall-source-test-pass-1.md`

The result is `train-cash-waterfall-source-test-hold-with-strong-output-demand-proxy`. Cheniere remains the strongest energy infrastructure source/use/output/customer-demand bridge in the system, but train/entity cash-waterfall proof remains unproven because train cost, debt draw, restricted cash, SPA economics, cargo attribution, revenue, EBITDA, distributions, debt-service coverage, and project return are not joined in the current local source set.

`CFCRSWO-004` is now executed as:

`/cluster/capital-flow-uri-fleet-cash-yield-source-test-pass-1.md`

The result is `fleet-cash-yield-source-test-hold-with-strong-company-fleet-proxy`. URI remains the cleanest operating-company fleet conversion bridge in the system, but fleet-class cash-yield and ROIC proof remain unproven because growth/replacement capex, fleet-class OEC, true utilization, rate/time/mix, segment operating profit, legal borrowing-base availability, reserves, advance rates, source-to-purchase allocation, and ROIC are not visible in the current local source set.

`CFCRSWO-005` is now executed as:

`/cluster/capital-flow-sterling-project-cash-collection-source-test-pass-1.md`

The result is `project-cash-collection-source-test-hold-with-strong-backlog-cash-proxy`. Sterling remains a strong project-execution cash proxy, but project cash-collection proof remains unproven because named owner funding, project margin, retainage collection, bonded backlog, actual L/C usage, source-to-project allocation, and project return are not visible in the current local source set.

`CFCRSWO-006` is now executed as:

`/cluster/capital-flow-energy-transfer-named-project-cash-source-test-pass-1.md`

The result is `named-project-cash-source-test-hold-with-strong-company-project-proxy`. Energy Transfer remains a strong company-level project proxy, but named-project cash-realization proof remains unproven because project cost, source allocation, customer cash, billing volume, utilization, project EBITDA, DCF contribution, debt-service allocation, and project return are not visible in the current local source set.

## Decision

`cash-return-source-work-order-ready`

The completed `16/16` money-movement synthesis now has an executable next-source work order. The next action is to execute the highest-leverage source package first, not expand the company universe.

## Safe Claim

`The current capital-flow system can answer where money appears to move across 16 executed cases, and it now has a ranked work order for the missing source packages needed to test actual cash return. The work order does not itself prove cash return; it defines what evidence would upgrade, hold, or disprove each case.`

## Next Work

1. Execute `CFCRSWO-001` for Wheaton Antamina if local source coverage is enough.
2. Execute `CFCRSWO-002` for FPL in parallel as a time-gated monitor/fetch path.
3. Execute `CFCRSWO-003` or `CFCRSWO-004` next if Wheaton/FPL cannot be fully upgraded from current sources.
