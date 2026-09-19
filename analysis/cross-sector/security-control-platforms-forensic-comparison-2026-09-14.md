# Security-Control Platforms: Forensic Comparison of CrowdStrike, Palo Alto, Zscaler, and F5

Date baseline: `2026-09-14`

Evidence base: the archived company packets and filed-source chains for CrowdStrike,
Palo Alto Networks, Zscaler, and F5. The packets were collected on or before
August 10, 2026. Figures below are reported-period figures from those packets;
they are not a current market-data feed.

## Executive conclusion

All four companies sell control over digital systems, but they control different
decisions:

- CrowdStrike controls endpoint, identity, cloud, data, and threat-response
  visibility.
- Palo Alto Networks controls a broad security platform spanning network,
  cloud, security operations, identity, and data.
- Zscaler controls access and policy enforcement between users, machines,
  applications, data, and AI agents.
- F5 controls application delivery, API protection, and runtime security
  across on-premises, cloud, and edge environments.

The common thesis is strong: rising system complexity increases the value of a
trusted control layer. The companies are not interchangeable, however. Palo
Alto and CrowdStrike are trying to deepen platform ownership. Zscaler is the
most access- and policy-native model. F5 has the strongest reported GAAP
profitability in this group but carries more systems and services burden.

The cleanest economic conclusion is not “cybersecurity is attractive.” It is
more specific: security-control companies can capture recurring economics when
their data, policies, workflows, and certifications become embedded in the
customer's operating process. The main risks are trust failure, product overlap,
cloud-processing cost, acquisition integration, hardware/services burden, and
stock-based compensation.

## 1. Define the comparison

A security control point is the software or equipment used to observe activity,
decide whether it is permitted, and record or act on a security event. A
platform is broader than a point product because it connects several control
functions and is intended to reduce the number of separate vendors a customer
must operate.

The relevant chain is:

`security need -> contract -> deployment -> usage -> renewal or expansion -> collected cash`

Each company must be tested across all six steps. Annual recurring revenue,
remaining performance obligations, billings, or backlog only describe part of
the chain.

## 2. Like-for-like operating evidence

| Company | Annual or latest anchor | Recurring or visibility measure | Cash evidence | Primary control point |
|---|---|---|---|---|
| CrowdStrike | FY2026 revenue `$4.81B`; subscription revenue `$4.56B` | FY2027 Q1 ARR `$5.51B`; net new ARR `$255.8M` | FY2026 OCF `$1.61B`, FCF `$1.24B`; FY2027 Q1 OCF `$590.9M`, FCF `$468.5M` | Endpoint, identity, cloud, data, and threat-response trust |
| Palo Alto | FY2025 revenue `$9.2215B`; operating income `$1.2429B` | FY2026 Q3 Next-Generation Security ARR `$8.1B`; RPO `$18.4B` | FY2025 OCF `$3.716B`, non-GAAP FCF `$3.4698B`; Q3 adjusted FCF `$910M` | Broad security consolidation and platform standardization |
| Zscaler | FY2025 revenue `$2.6731B` | FY2026 Q3 ARR `$3.525B`; RPO about `$6.459B`; deferred revenue `$2.477B` | FY2025 OCF `$972.5M`, capex `$164.3M`; Q3 OCF about `$198M`, FCF about `$136M` | Cloud-delivered access, identity, and policy enforcement |
| F5 | FY2025 revenue about `$3.088B` | FY2025 RPO about `$2.0B`; Q3 FY2026 RPO about `$2.2B` | FY2025 OCF about `$949.7M`; Q3 FY2026 GAAP operating income `$213.3M` | Application delivery, API protection, and runtime security |

These measures cannot be combined into one ranking. ARR is annualized active
contract value. RPO is the value of contracted performance obligations not yet
recognized as revenue. Deferred revenue is cash or billing recorded before the
company has delivered all contracted service. Free cash flow is usually
operating cash flow less capital spending, but the exact company definition can
include or exclude other items.

## 3. What is actually recurring?

### CrowdStrike

Subscription revenue was approximately `95%` of fiscal 2026 revenue. This is a
strong recurring structure, but the customer must continue deploying sensors,
using detection workflows, and expanding modules. The July 19 Incident makes
retention the central quality test. If customers renew and expand after the
incident, the platform may have retained trust. If new ARR grows while renewal,
discounting, or customer support costs worsen, the headline ARR is weaker.

### Palo Alto

Subscription and support were `80.5%` of fiscal 2025 revenue. The recurring
mix is substantial, but the latest quarter also included CyberArk and
Chronosphere effects. The clean test is organic platform expansion after
acquisition accounting, integration costs, and cross-selling claims are
separated. RPO and Next-Generation Security ARR show visibility, not final
margin or owner cash.

### Zscaler

Zscaler has the clearest access-policy subscription model. Its deferred revenue
and ARR provide useful evidence that customers pre-fund service. That
prepayment supports liquidity, but it is also a future obligation. The company
must spend on data centers, cloud processing, security research, support, and
sales before the full contract value becomes earned profit.

### F5

F5 is the least pure recurring model in the group. Fiscal 2025 revenue included
about `$705.6M` of systems, `$803.1M` of software, and approximately `$1.579B`
of services. The software and RPO support recurring economics, but systems and
services create hardware refresh, implementation, support-labor, and delivery
risks. High margins do not remove that burden.

## 4. Earnings quality and financial-engineering tests

| Test | CrowdStrike | Palo Alto | Zscaler | F5 |
|---|---|---|---|---|
| Customer prepayment | Deferred revenue and subscription contracts | RPO and subscription/support | Deferred revenue is a major cash-flow item | RPO across systems, software, and services |
| Adjusted-profit risk | Incident-related costs and recurring non-GAAP exclusions | Acquisition and integration effects; non-GAAP FCF | GAAP losses despite strong non-GAAP margins | Reconciliation between GAAP and non-GAAP profit |
| SBC and dilution | Must be deducted from per-share owner cash | Must be tested against buybacks and diluted shares | Must be tested against high recurring cash flow | Must be tested against software/services profitability |
| Working-capital risk | Receivables, deferred revenue, and service obligations | Billings, RPO conversion, acquisitions | Deferred revenue, receivables, acquisitions | Systems inventory, receivables, and services timing |
| Physical burden | Low property and equipment burden; cloud dependence | Low telecom-style capex; acquisition integration burden | Cloud and data-center dependence | Highest hardware and services burden in this group |
| Trust failure | July 19 Incident and remediation | Breach, integration, or product failure | Access-policy failure or major service outage | Cybersecurity claims, litigation, and runtime failure |

The main financial-engineering risk is not necessarily illegal accounting. It is
the presentation of a favorable measure that leaves out an economically recurring
cost. A company can have legitimate adjusted metrics and still overstate owner
economics if incident remediation, acquisition integration, SBC, cloud usage,
or customer-support costs are treated as permanently exceptional.

## 5. Who captures the economics and who carries the burden?

| Economic layer | Cleaner capture | Burden carrier |
|---|---|---|
| Security data and detection | CrowdStrike and Palo Alto when data and workflows are deeply embedded | Research labor, storage, processing, false positives, missed threats, incident response |
| Access and policy | Zscaler when policy becomes the standard path for users, machines, and agents | Cloud processing, outages, identity integrations, compliance, and future service obligations |
| Application delivery and runtime | F5 when hybrid application estates require one control platform | Systems inventory, services labor, implementation, warranty, cyber claims, and product renewal |
| Platform consolidation | Palo Alto and CrowdStrike when customers reduce vendor count | Integration, product overlap, cross-selling cost, acquisition price, and execution risk |
| Recurring contract | All four when renewal and expansion are real | Discounts, support, cloud infrastructure, research, SBC, and dilution |

The companies shift the burden away from telecom-style network ownership, but
they do not eliminate it. The burden appears as specialized labor, software
quality, customer support, cloud cost, compliance, acquisitions, and dilution.

## 6. Alden lens: liquidity and durability

Security spending has a durable demand source because organizations must protect
systems, comply with requirements, and limit operational interruption. The
businesses are also more liquid than capital-heavy network owners because they
do not need to fund a national access network or a large property portfolio.

Durability still depends on the ability to fund the business through a trust
shock or budget slowdown. The stress tests are:

1. Can customers renew when security budgets are consolidated?
2. Can gross margin hold when data and AI processing increase?
3. Can research and incident-response staffing continue without excessive SBC?
4. Can acquisitions be integrated without weakening product clarity?
5. Can the balance sheet fund remediation, refunds, legal costs, or customer
   credits without new financing?

The strongest company under this lens is the one that can preserve customer
trust and cash per diluted share when the security environment becomes harder,
not only the one with the highest current ARR growth.

## 7. Damodaran lens: narrative to numbers

Management narratives in this cohort include “AI security,” “platformization,”
“Zero Trust,” “consolidation,” and “mission-critical.” Each requires a numerical
translation:

| Narrative | Required evidence |
|---|---|
| AI security | AI-related contract value, usage, retention, gross margin, and incident performance |
| Platformization | Module penetration, net retention, customer count, implementation cost, and support cost |
| Zero Trust | Renewal, policy volume, identity coverage, data protection, and customer concentration |
| Consolidation | Reduced vendor count, larger contracts, lower customer operating cost, and durable pricing |
| Mission-critical | Renewal after failures, service availability, response quality, and customer references |
| Recurring cash | Operating cash after deferred-revenue timing, cloud cost, SBC, acquisitions, and maintenance investment |

The valuation question is the same for all four: what normalized owner cash per
diluted share is the current price assuming, and how much growth and margin
expansion is required to reach it? The archive does not use a common valuation
multiple for these companies because their recurring measures, hardware mix,
acquisition cadence, and GAAP-to-cash bridges differ.

## 8. Comparative investment judgments

### CrowdStrike: highest trust-recovery sensitivity

CrowdStrike has the strongest current recurring software signal in relation to
its control point and a very strong cash record. The key uncertainty is whether
the platform can maintain trust after a visible operational incident while
keeping incident, support, cloud, and SBC costs under control.

### Palo Alto: broadest consolidation claim

Palo Alto has the broadest platformization claim and the largest reported
security-control scale in this comparison. Its main risk is that acquisitions
and product breadth create integration and product-overlap costs that reduce the
quality of organic growth.

### Zscaler: cleanest access-policy model

Zscaler has the cleanest cloud-native policy model and strong deferred-revenue
and ARR visibility. Its main risks are continued GAAP losses, acquisition-led
scope expansion, cloud processing cost, and the possibility that a broader
security bundle captures the same budget.

### F5: strongest GAAP profit with the most physical ballast

F5 shows that application-delivery and runtime security can be highly
profitable. It is also the least pure software-control case here because
systems and services remain significant. The main question is whether the
installed base produces durable software and support cash after hardware and
delivery costs.

## 9. Filing-based falsifiers

The cohort thesis weakens if:

- ARR or RPO rises while renewals, collections, or gross margin weaken;
- deferred revenue grows but future revenue and cash conversion deteriorate;
- platform expansion requires rising discounts, implementation labor, or
  customer-support cost;
- acquisition growth masks slower organic demand or reduces operating returns;
- cloud, storage, and AI-processing cost grows faster than recurring revenue;
- systems inventory or services receivables grow faster than F5 revenue;
- non-GAAP exclusions repeatedly remove incident, integration, or retention
  costs; or
- SBC and share issuance consume the reported increase in owner cash.

The next filings should therefore be read in this order: renewal and expansion,
gross margin after delivery cost, cash conversion, dilution, incident or
integration cost, and only then the size of the ARR or RPO headline.

## Conclusion

The security-control cohort confirms that the valuable layer in digital
infrastructure is often the layer that makes systems observable, permitted,
and governable. CrowdStrike, Palo Alto, Zscaler, and F5 each demonstrate part
of that control. Their differences determine who captures the cleaner economics
and who carries the cost.

CrowdStrike and Palo Alto are the strongest platform-consolidation cases.
Zscaler is the cleanest access-policy case. F5 is the clearest warning that a
profitable control point can still carry meaningful hardware and services
burden. Across all four, the decisive evidence is owner cash per diluted share
after trust maintenance, cloud processing, acquisitions, support, and SBC.
