# Bidirectional Claims-To-Evidence Method

## Core Idea

The research should not only start from documents and collect numbers.

It should also start from the actual analytical claims we already wrote, then work backward to ask what evidence would prove, weaken, or sharpen each claim.

That creates a two-way loop:

| Direction | Starting Point | Output |
|---|---|---|
| Evidence first | Annual reports, quarterly reports, supplements, datasets | Metrics, facts, source ledger, emerging patterns |
| Claim first | Existing company analyses and cluster theses | Testable claims, missing metrics, proof requirements, source targets |

The goal is to make every major thesis auditable without killing the first-principles insight.

## Direction 1: Evidence To Claim

This is the normal extraction path.

| Step | Action |
|---|---|
| 1 | Pull annual reports, quarterly reports, earnings releases, investor decks, supplements, transcripts, and external datasets. |
| 2 | Extract repeated metrics into a structured ledger. |
| 3 | Group metrics by capital source, funding instrument, destination, bottleneck, and operating proof. |
| 4 | Look for patterns across firms and clusters. |
| 5 | Write or revise claims based on what the numbers support. |

Example:

| Evidence | Claim It Can Support |
|---|---|
| Apollo originations, AUM, SRE, Athene assets | Insurance and retirement liabilities are being converted into private-credit origination power. |
| Blackstone deployment into infrastructure, real estate, data centers, power | Private-market platforms are making physical AI infrastructure investable. |
| NextEra backlog, FPL rate base, renewables/storage origination | AI and electrification capital are showing up as power-development and rate-base opportunity. |

## Direction 2: Claim To Evidence

This is the missing reverse path.

Start with a sentence from the analysis and force it into a testable structure.

| Claim Component | Question |
|---|---|
| Actor | Who is doing the thing? |
| Mechanism | How does the thing work? |
| Destination | Where does the money, demand, or pressure go? |
| Beneficiary | Who wins if the claim is true? |
| Bottleneck | What can block it? |
| Proof metric | What number would confirm it? |
| Disproof metric | What number would weaken it? |
| Source target | Which document or dataset should contain the number? |

## Claim Decomposition Examples

## Claim: Capital Platforms Are Routing The Next Investment Cycle

| Field | Answer |
|---|---|
| Actor | BlackRock, Blackstone, Apollo, KKR, Brookfield, Ares, Carlyle |
| Mechanism | Raise and route institutional, insurance, retirement, sovereign, ETF, and wealth capital |
| Destination | Private credit, infrastructure, data centers, power, real estate, private companies, secondaries |
| Beneficiary | Capital platforms plus operating companies near funded bottlenecks |
| Proof metric | Inflows, fundraising, deployment, originations, AUM, FPAUM, dry powder, uncalled commitments |
| Disproof metric | Falling inflows, weak deployment, redemptions, poor realizations, rising credit losses |
| Source target | 10-K, 10-Q, quarterly supplement, earnings release, investor presentation, transcript |

## Claim: AI Capital Becomes A Power And Physical Infrastructure Story

| Field | Answer |
|---|---|
| Actor | Blackstone, Brookfield, KKR, Ares, BlackRock, utilities, data-center developers |
| Mechanism | Capital funds land, buildings, power, cooling, grid interconnection, backup generation, fiber |
| Destination | Data centers, power generation, grid upgrades, transmission, electrical equipment, construction |
| Beneficiary | Constellation, NextEra, Vistra, NRG, AEP, Duke, Exelon, WESCO, Ferguson, United Rentals |
| Proof metric | PPAs, MW contracted, load growth, rate-base growth, capex plan, backlog, data-center leasing |
| Disproof metric | Data-center cancellations, delayed interconnection, lower load forecasts, weak power pricing |
| Source target | Utility filings, earnings decks, FERC/EIA, ISO queues, data-center REIT reports, company transcripts |

## Claim: Private Credit Is Replacing Part Of Bank Lending

| Field | Answer |
|---|---|
| Actor | Apollo, Ares, Blackstone, KKR, Carlyle, BlackRock/HPS |
| Mechanism | Direct lending, asset-backed finance, infrastructure credit, sponsor finance, insurance-linked origination |
| Destination | Corporate borrowers, private companies, asset pools, infrastructure projects, real estate credit |
| Beneficiary | Private-credit platforms, sponsor-backed companies, borrowers needing flexible capital |
| Proof metric | Originations, direct-lending AUM, available capital, deployment, spreads, borrower growth |
| Disproof metric | Credit losses, non-accruals, fundraising slowdown, spread compression, weak deployment |
| Source target | Asset-manager supplements, BDC filings, Fed credit data, rating agency reports, private-credit datasets |

## Claim: Insurance Liabilities Are Becoming A Funding Source For Private Assets

| Field | Answer |
|---|---|
| Actor | Apollo/Athene, Brookfield, KKR/Global Atlantic, Blackstone |
| Mechanism | Insurers need long-duration yield assets; platforms originate or acquire assets to match liabilities |
| Destination | Private credit, investment-grade credit, infrastructure debt, real estate credit, asset-backed finance |
| Beneficiary | Insurance-linked asset managers, private borrowers, infrastructure owners |
| Proof metric | Insurance AUM, retirement-services inflows, spread-related earnings, asset allocation, origination volume |
| Disproof metric | Regulatory restriction, spread compression, surrender pressure, credit impairment, asset/liability mismatch |
| Source target | 10-K, insurance supplement, NAIC data, rating agency reports, asset-manager transcripts |

## Claim: Wealth Clients Are Being Pulled Into Private Markets

| Field | Answer |
|---|---|
| Actor | Blackstone, KKR, Apollo, BlackRock, Ares, Carlyle |
| Mechanism | Private-market products are distributed through advisors and semi-liquid/perpetual vehicles |
| Destination | Private credit, real estate, infrastructure, private equity, secondaries |
| Beneficiary | Asset managers with wealth distribution and perpetual capital products |
| Proof metric | Wealth fundraising, perpetual capital AUM, retail fund flows, redemptions, fee-related earnings |
| Disproof metric | Redemption queues, suitability backlash, poor performance, regulatory action, advisor pullback |
| Source target | Quarterly supplement, product filings, fund reports, transcripts, regulatory filings |

## Ledger Fields For Reverse Extraction

The evidence ledger should include claim fields, not only source fields.

```text
persistent_claim_id
claim_text
claim_type
company
cluster
capital_source
routing_platform
funding_instrument
real_economy_destination
operating_beneficiary
bottleneck
proof_metric_needed
disproof_metric_needed
source_target
source_file
period
metric_name
metric_value
units
interpretation
confidence
status
```

Suggested claim types:

- capital-source claim
- routing-platform claim
- funding-destination claim
- operating-beneficiary claim
- bottleneck claim
- proof-metric claim
- disproof-risk claim

Suggested statuses:

- claim-written-no-metric-yet
- metric-found-primary-source
- metric-found-secondary-source
- needs-quarterly-update
- contradicted
- too-vague-rewrite
- supported

## Practical Workflow

For every new or existing analysis file:

1. Extract the strongest 5 to 10 analytical claims.
2. Rewrite each as a testable claim.
3. Assign proof metrics and disproof metrics.
4. Identify likely source documents.
5. Search filings and supplements for the exact numbers.
6. Add the evidence to the ledger.
7. Revise the claim if the evidence is weaker, narrower, or more interesting than expected.

## Example Output Row

| Field | Value |
|---|---|
| claim_text | AI capital becomes a power and physical infrastructure story. |
| company | Constellation / NextEra / Blackstone / Brookfield |
| cluster | Capital flow, power scarcity, AI infrastructure |
| capital_source | Institutions, wealth, corporate buyers, infrastructure capital |
| routing_platform | Blackstone, Brookfield, KKR, Ares, BlackRock |
| funding_instrument | Infrastructure equity, private credit, real estate, PPAs |
| real_economy_destination | Data centers, power, grid interconnection |
| operating_beneficiary | Utilities, contractors, electrical distributors |
| bottleneck | Power availability and interconnection |
| proof_metric_needed | MW contracted, PPAs, rate-base growth, capex, data-center load |
| disproof_metric_needed | Canceled projects, weaker load forecast, delayed interconnection |
| source_target | Utility 10-K/10-Q, earnings deck, FERC/EIA, ISO queue |
| status | claim-written-no-metric-yet |

## Bottom Line

The right system is bidirectional.

Use documents to discover claims, but also use claims to demand better documents.

If a claim cannot be tied to a proof metric, disproof metric, and source target, it is probably too vague. If it can, it becomes a research program.
