# Capital Flow Borrower Source-Of-Funds Pass

## What This Adds

The industry-lane work shows where private-credit money is landing.

This pass asks the next question:

`When we can identify the borrower, what does the transaction history say about how the company was funded?`

Local data file:

`analysis/company-first-principles/data/capital-flow-borrower-source-of-funds-evidence.csv`

Fact extraction file:

`analysis/company-first-principles/data/capital-flow-borrower-transaction-fact-extractions.csv`

Claim-strength matrix:

`analysis/company-first-principles/data/capital-flow-borrower-claim-strength-matrix.csv`

Local raw transaction sources:

- `raw/primary-sources/capital-flow/borrower-transactions/auctane-stamps-com/paul-hastings-stamps-com-unitranche.html`
- `raw/primary-sources/capital-flow/borrower-transactions/auctane-stamps-com/stamps-com-2021-acquisition-exhibit-99-1.html`
- `raw/primary-sources/capital-flow/borrower-transactions/auctane-stamps-com/stamps-com-2021-preliminary-proxy-prem14a.html`
- `raw/primary-sources/capital-flow/borrower-transactions/auctane-stamps-com/stamps-com-2021-closing-8k-credit-termination.html`
- `raw/primary-sources/capital-flow/borrower-transactions/guidehouse/guidehouse-bain-close.html`
- `raw/primary-sources/capital-flow/borrower-transactions/guidehouse/bloomberg-law-guidehouse-private-loan.html`
- `raw/primary-sources/capital-flow/borrower-transactions/medallia/thoma-bravo-medallia-acquisition.html`
- `raw/primary-sources/capital-flow/borrower-transactions/medallia/medallia-2026-lender-led-ownership-transition.html`
- `raw/primary-sources/capital-flow/borrower-transactions/medallia/medallia-2021-preliminary-proxy-prem14a.html`
- `raw/primary-sources/capital-flow/borrower-transactions/medallia/medallia-2021-acquisition-8k-debt-commitment.html`
- `raw/primary-sources/capital-flow/borrower-transactions/guidehouse/yahoo-guidehouse-port-private-loan.html`

## First Three Borrower Cases

| Borrower | Lane | BDC Evidence | Transaction Evidence | Claim Status |
|---|---|---|---|---|
| Auctane / Stamps.com | Software and Services | BXSL top-ten borrower at `2%`; ARCC parser row shows `241.6M USD` fair value in a first-lien senior secured loan | Thoma Bravo acquired Stamps.com for about `6.6B USD`; named private-credit lenders included Blackstone Credit, Ares-managed credit funds, PSP Investments, and Thoma Bravo Credit; counsel source describes `2.775B USD` unitranche/direct-loan financing; SEC proxy says debt-financing proceeds would fund amounts required to terminate a bank-led Stamps.com credit facility; SEC closing 8-K confirms that termination occurred at closing | Strong private-credit acquisition-finance evidence plus primary-source-confirmed bank-facility termination; final credit documents are still needed to map every post-close bank role |
| Guidehouse | Commercial and Professional Services | BXSL top-ten borrower at `2%` | Bain acquired Guidehouse from Veritas for `5.3B USD`; Bloomberg Law reported Blackstone-led private lenders held off banks competing to finance the buyout and referenced a `3.075B USD` debt facility; the Yahoo mirror attempt returned only a rate-limit page and is not used | Strongest current bank-competition evidence, but still needs primary credit-document support |
| Medallia | Software and Services | BXSL top-ten borrower at `1%` | Thoma Bravo agreed to acquire Medallia for `6.4B USD`; SEC acquisition 8-K states lenders committed approximately `1.8B USD` of debt financing and an equity commitment up to approximately `5B USD`; debt financing was provided by Blackstone Credit, Apollo-managed funds, KKR Credit, Thoma Bravo Credit, and Antares in the transaction announcement; SEC proxy separately says merger funding would repay Medallia's existing Wells Fargo-administered credit agreement; in 2026 Medallia announced ownership transition to a group led by Blackstone, Apollo, and FSK with `150M USD` of new capital | Strong evidence of acquisition-debt funding and workout/control risk plus medium-high bank-credit-takeout evidence; not a clean bank-competition case |

## Provenance Check

The borrower case table now points to local source files first.

| Source Group | Local Status | Use In Claim |
|---|---|---|
| Auctane / Stamps.com | Downloaded and checksummed | Paul Hastings supports the private-credit lender group and `2.775B USD` unitranche claim; the SEC proxy supports debt-financing proceeds intended to take out a named bank-led credit facility; the SEC closing 8-K confirms the credit agreement was terminated at closing. |
| Guidehouse | Downloaded and checksummed for company and Bloomberg Law sources; Yahoo mirror blocked | Guidehouse supports transaction value and sponsor/owner context; Bloomberg Law supports the bank-competition claim. The Yahoo mirror returned only `Edge: Too Many Requests` and is excluded from evidence. |
| Medallia | Downloaded and checksummed | Thoma Bravo supports acquisition lender identity; the SEC proxy supports repayment of an existing Wells Fargo-administered credit agreement; the SEC acquisition 8-K gives approximately `1.8B USD` of debt financing and approximately `5B USD` of equity commitment; Medallia supports the 2026 lender-led ownership transition and `150M USD` new-capital claim. |

## Extracted Fact Markers

These are the fact-level markers pulled from the local raw files.

| Borrower | Fact | Local Evidence Marker | Claim Effect |
|---|---|---|---|
| Auctane / Stamps.com | `6.6B USD` transaction value | Paul Hastings local file marker: `6.6 billion` | Shows this was a mega direct-lending-capacity test, not only ordinary middle-market lending. |
| Auctane / Stamps.com | Blackstone Credit, Ares, and PSP lender group | Paul Hastings local file markers: Blackstone Credit, Ares Corporation, PSP Investments | Supports private-credit lender identity. |
| Auctane / Stamps.com | `2.775B USD` unitranche financing | Paul Hastings local file markers: `unitranche`, `2.775 billion` | Supports the large direct-loan/unitranche claim. |
| Auctane / Stamps.com | Bank-led credit facility takeout | SEC proxy local markers: `Debt Commitment Letter`; `terminate`; `Credit Facility`; Wells Fargo Bank; BOFA Securities; JPMorgan Chase Bank | Upgrades Auctane from direct private-credit financing only to a borrower-level bank-facility takeout case. |
| Auctane / Stamps.com | Credit facility termination at closing | SEC closing 8-K local markers: `terminated the credit agreement`; Wells Fargo; JPMorgan Chase Bank; Bank of America; all outstanding obligations and security interests | Confirms that the bank-facility takeout described in the proxy actually happened at closing. |
| Guidehouse | `5.3B USD` Bain acquisition from Veritas | Guidehouse local file marker: `5.3 billion`; Bain Capital; Veritas Capital | Supports sponsor-backed transaction context. |
| Guidehouse | Blackstone-led private lenders held off banks | Bloomberg Law local file markers: Private lenders led by Blackstone; held off banks; banks vying | Supports bank-competition claim, but as secondary-source evidence. |
| Guidehouse | `3.075B USD` debt/facility reference | Bloomberg Law local file marker: `3.075`; HPS Investment Partners | Supports financing size, still needs primary credit-document confirmation. |
| Guidehouse | Blocked source check | Yahoo local file content: `Edge: Too Many Requests` | Keeps the Guidehouse claim tied to the existing Bloomberg Law source until another usable source is obtained. |
| Medallia | `6.4B USD` transaction value | Thoma Bravo local file marker: `6.4 billion` | Supports large software take-private context. |
| Medallia | `1.8B USD` debt commitment and `5B USD` equity commitment | SEC acquisition 8-K local markers: debt commitment letter; July 25, 2021; approximately `$1.8 billion`; equity contribution up to approximately `$5 billion` | Adds a primary-source acquisition-financing amount while keeping lender identity tied to the transaction announcement. |
| Medallia | Blackstone, Apollo, KKR, Thoma Bravo Credit, and Antares lender group | Thoma Bravo local file markers for each lender | Supports private-credit lender identity for original acquisition financing. |
| Medallia | Existing credit agreement repayment | SEC proxy local markers: repayment of all obligations; existing credit agreement; Wells Fargo Bank as administrative agent | Adds bank-credit-takeout evidence, while keeping lender identity tied to the separate transaction announcement. |
| Medallia | Ownership transition to lender group | Medallia local file markers: change ownership; Blackstone, Apollo, and FS KKR | Supports workout/control risk claim. |
| Medallia | `150M USD` new capital | Medallia local file markers: `150 million` | Supports recapitalization/new-money component. |

## Evidence To Claim

The borrower cases sharpen the claim in three different directions:

| Evidence Pattern | Claim It Supports |
|---|---|
| Auctane | Private credit can finance large software take-private transactions directly, and in this case the deal closed with termination of a named bank-led credit facility. |
| Guidehouse | Private credit can compete with banks for sponsor buyout financing; this is currently supported by Bloomberg Law and still needs primary credit-document confirmation. |
| Medallia | Private credit can finance a software take-private with a primary-source `1.8B USD` debt commitment, repay an existing bank-administered credit agreement, and later become the control path when the debt stack gets stressed. |

## Claim Strength Matrix

| Borrower | Private-Credit Lender Evidence | Bank-Competition / Displacement Evidence | Workout / Control Evidence | Safest Claim |
|---|---|---|---|---|
| Auctane / Stamps.com | Strong | Strong | None found | Private credit directly financed a large sponsor-backed software take-private through a unitranche/direct-loan structure, and the deal closed with termination of an existing bank-led credit facility. |
| Guidehouse | Medium-high | Strong, but secondary-source-backed | None found | Private credit competed directly with banks for a large sponsor-to-sponsor professional-services buyout financing. |
| Medallia | Strong | Medium-high | Strong | Private credit financed a software take-private with approximately `1.8B USD` of committed debt financing, repaid an existing Wells Fargo-administered credit agreement, and later became the ownership/control path through recapitalization. |

This matters because the three examples should not be collapsed into one claim.

- Auctane is now the strongest primary-source bank-facility-termination case.
- Guidehouse is the best bank-competition case so far.
- Medallia is a bank-credit-takeout plus credit-cycle/lender-control case.

That means the better thesis is no longer just:

`Private credit is funding software and services.`

It is:

`Private credit is funding sponsor-owned software and service businesses through acquisition loans, refinancings, and restructurings. In some cases it competes with banks; in other cases it functions as a parallel capital channel or becomes the workout owner.`

## Claim To Evidence

The strongest displacement claim still needs one more proof layer.

For each borrower, the required fields are:

| Field | Needed To Prove |
|---|---|
| Original credit agreement or lender presentation | Facility size, tranche type, pricing, maturity, collateral, and lender group |
| Prior debt source | Whether a bank/syndicated loan/bond/private-credit facility was repaid |
| Use of proceeds | Acquisition financing, refinancing, dividend recap, growth capital, or rescue capital |
| Bank role | Whether banks lost the loan, arranged competing financing, kept a revolver, or funded the private-credit vehicle indirectly |
| BDC/fund holding history | Which public vehicles carried exposure over time, whether fair value was marked down, and whether non-accrual/workout status emerged |

## Two-Way Claim Discipline

This page should be used in both directions.

| Direction | How To Use It | Current Example |
|---|---|---|
| Evidence -> claim | Start with the actual source text, then make only the claim the source can carry. | Stamps.com's proxy says debt-financing proceeds would be used to terminate a credit facility naming Wells Fargo, BofA Securities, and JPMorgan; the safe claim is bank-credit-facility takeout, not total bank exclusion. |
| Claim -> evidence | Start with a stronger claim, then list the documents required before using it. | To say private credit displaced banks, we still need final credit documents, lender allocations, payoff letters, and post-close bank ancillary roles. |
| Conflict check | If two sources support different parts of the story, keep them separate. | Medallia's proxy supports repayment of a Wells Fargo-administered credit agreement; the Thoma Bravo announcement supports Blackstone/Apollo/KKR/Antares lender identity. |

## Simple Version

We now have the first borrower-level evidence that connects the broad capital-flow map to real deals.

Auctane shows private credit funding a large software buyout where the closing 8-K confirms an existing bank-led credit facility was terminated.

Guidehouse shows private credit competing with banks for a buyout financing.

Medallia shows three things at once: the acquisition used approximately `1.8B USD` of committed debt financing, the merger funding repaid an existing Wells Fargo-administered credit agreement, and private credit can later end up owning the company when the debt stack fails.

So the simple answer is:

`The money is not just moving into private credit funds. It is moving into specific sponsor-owned companies, often through large acquisition loans. The next proof is borrower by borrower: did private credit replace a bank, refinance another private lender, or become the restructuring owner?`
