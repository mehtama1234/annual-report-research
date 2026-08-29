# Capital Flow Borrower Matching Workbench

## The Deeper Question

The serious version of the private-credit question is not:

`Is private credit big?`

We already have enough evidence to say it is big and borrower-facing.

The deeper question is:

`Which specific borrowers are being financed by private credit, why did they borrow, who else financed the transaction, and would that credit otherwise have sat with banks or syndicated loan investors?`

## Local Data File

`analysis/company-first-principles/data/capital-flow-borrower-matching-workbench.csv`

First source-of-funds pass:

`analysis/company-first-principles/capital-flow-borrower-source-of-funds-pass.md`

## Why This Exists

The existing evidence stack now has four layers:

| Layer | What It Proves |
|---|---|
| Apollo and Ares platform metrics | Private credit and origination platforms are large and active. |
| FRED bank-credit denominators | Banks remain huge and still growing in aggregate. |
| BDC borrower panel | Public BDCs hold real private-company loan books. |
| BDC industry-lane evidence | Those loan books land in identifiable software, healthcare, service, logistics, insurance, and defense lanes. |

This workbench adds the missing fifth layer:

`named borrower -> lane -> exposure -> transaction purpose -> prior financing source -> claim status`

## First Borrower Targets

BXSL gives the cleanest named-borrower starting list because its Q2 2026 SEC earnings exhibit lists top portfolio companies with fair-value exposure percentages.

| Borrower | Initial Lane Read | BXSL Exposure |
|---|---|---:|
| Snoopy Bidco | not classified in this pass | `3%` |
| JSS | not classified in this pass | `3%` |
| Guidehouse | professional services / government services | `2%` |
| Auctane / Stamps.com | software / logistics software | `2%` |
| Cambium | not classified in this pass | `2%` |
| Corfin | not classified in this pass | `2%` |
| Bazaarvoice | software / marketing technology | `2%` |
| Navigator | not classified in this pass | `2%` |
| IRI Group / NPD / Circana | data / analytics / consumer insights | `1%` |
| Medallia | software / customer experience | `1%` |

ARCC adds another borrower search set from its 10-Q schedule context:

`Artifact Bidco, Auctane, Banyan Software, Borrower R365, Netsmart, Omnigo, Optimizely, Aimbridge, American Residential Services, Apex Service Partners, Belfor, Birdie Bidco`

OBDC adds the breadth denominator:

- `229` portfolio companies
- `30` industries
- `65.3M USD` average investment size at fair value

## Evidence To Claim

The current evidence supports this claim:

`Private credit is funding named private borrowers and identifiable industries, especially software, healthcare, professional services, insurance, commercial services, consumer services, logistics, and defense-related lanes.`

That is stronger than saying only that managers raised money.

It is still weaker than saying:

`Private credit replaced bank lending.`

## Claim To Evidence

To prove displacement, each borrower row needs five more fields:

| Required Field | Why It Matters |
|---|---|
| Sponsor / owner | Shows whether this is sponsor-backed acquisition finance. |
| Use of proceeds | Distinguishes acquisition, refinancing, growth, dividend recap, and rescue capital. |
| Prior debt source | Shows whether the old money came from banks, broadly syndicated loans, private credit, bonds, or sponsor equity. |
| Current lender group | Shows whether private credit is sole lender, lead lender, co-lender, or junior participant. |
| Bank facility role | Shows whether banks were displaced or still financing the private-credit vehicle through revolvers and credit facilities. |

## Decision Rules

| Evidence Found | Claim Upgrade |
|---|---|
| Private credit refinanced a bank loan or bank-led syndicated loan | Strong displacement evidence. |
| Private credit financed sponsor acquisition where banks would historically have underwritten leveraged loans | Moderate displacement evidence. |
| Private credit refinanced another private-credit loan | Parallel-channel recycling, not bank displacement. |
| Bank revolvers remain material in the same credit stack | Symbiotic bank/private-credit evidence. |
| No prior source or use-of-proceeds evidence | Borrower exposure only; do not infer displacement. |

## Practical Next Pass

Start with the overlapping names because they create faster proof:

| Borrower | Why Prioritize |
|---|---|
| Auctane / Stamps.com | Appears in both BXSL and ARCC evidence, likely large enough to have transaction history. |
| Guidehouse | Professional/government-services lane and named top BXSL exposure. |
| Bazaarvoice | Software borrower with named BXSL exposure. |
| Medallia | Software borrower with named BXSL exposure. |
| Netsmart | Healthcare software borrower in ARCC schedule context. |
| American Residential Services | Consumer/home-services lane tied to built-environment upkeep. |
| Apex Service Partners | Consumer/home-services lane tied to built-environment services. |

For each one, collect:

- SEC filing row or BDC schedule row
- sponsor owner
- acquisition/refinancing announcement
- debt amount
- lender names
- bank or syndicated loan takeout evidence
- current private-credit lender role

## First Source-Of-Funds Findings

The first completed borrower cases are Auctane/Stamps.com, Guidehouse, and Medallia.

They are useful because they split the thesis into three sharper claims:

| Borrower | What It Shows |
|---|---|
| Auctane / Stamps.com | Private credit directly financed a large software take-private deal. |
| Guidehouse | Private credit competed with banks and retained a sponsor-buyout financing role. |
| Medallia | Private credit exposure can become workout/control exposure when a software debt stack gets stressed. |

This moves the workbench from a target list to a claim-testing machine.

The claim is no longer simply "private credit is replacing banks."

The claim is now:

`Private credit is one of several borrower-financing routes for sponsor-owned software and services companies. Sometimes it competes with banks; sometimes it refinances or recycles private-credit exposure; sometimes it becomes the restructuring owner.`

## Better Claim After This Workbench

Old claim:

`Private credit is replacing banks.`

Better claim:

`The first hard evidence shows private credit operating as a borrower-level financing channel in software, healthcare, professional services, insurance, commercial services, consumer services, logistics, and defense lanes. Bank displacement should be claimed only borrower by borrower, after matching the private-credit loan to use of proceeds and prior financing source.`

## Simple Version

We now have a list of borrowers and industries to investigate.

The next proof is not another broad chart. It is matching named borrowers to actual deals:

`Who borrowed, why they borrowed, who lent, what got refinanced, and whether a bank lost the loan or stayed involved somewhere else.`
