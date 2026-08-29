# Capital Flow Capital-Intensive Credit Document Source Locator Pass 1

## Purpose

This pass turns the credit-stack findings into a document-pursuit map.

The operating table is:

`analysis/company-first-principles/data/capital-flow-capital-intensive-credit-document-source-locator-pass-1.csv`

The question is:

`Which exact filings, exhibits, or source families have to be retrieved before the credit-stack evidence can become agreement-term or project-finance-waterfall evidence?`

## What Was Added

| Item | Count |
|---|---:|
| Source locator rows | `17` |
| Energy Transfer rows | `4` |
| Cheniere rows | `4` |
| United Rentals rows | `5` |
| Sterling rows | `3` |
| Cross-company governance rows | `1` |

## Theme And Subtheme Interpretation

This pass deepens the same theme:

`capital-intensive real-economy buildout`

The active subtheme is now:

`agreement-document pursuit`

That subtheme sits between:

`credit-stack-visible`

and:

`agreement-term-grade / project-finance-waterfall-grade`

The practical ladder is:

`debt table -> source locator -> agreement exhibit -> term extraction -> covenant/collateral/waterfall mapping -> project source-of-funds`

The lane is now at the second step for many documents and the first step for others.

## What We Learned

| Company | Best Current Source Status | Main Gap |
|---|---|---|
| ET | Q2 2026 10-Q debt/facility summary is cached; Item `1.01`/`2.03` 8-K candidates are identified. | Full Five-Year Credit Facility, commercial-paper backstop, note indentures, and maturity-ladder documents are not yet extracted. |
| Cheniere | Q2 2026 10-Q entity debt table is cached; several 2026 Item `1.01`/`2.03` candidates are identified. | SPL/CQP/CCH/parent agreement terms, waterfalls, restrictions, and project construction-account mechanics are not yet extracted. |
| URI | Q2 2026 10-Q debt table is cached; June `2026` AR securitization amendment and July `2025` ABL reset exhibits have now been retrieved and extracted; August `2025` has been classified as a secured term-loan amendment. | Current borrowing-base certificates, AR monthly reports, advance rates, reserves, legal availability, and fleet collateral marks are not yet extracted. |
| Sterling | Q2 2026 10-Q exhibit index identifies the exact Exhibit `10.1` credit agreement URL. | The agreement text was not retrieved locally; pricing, covenants, guarantors, and use-of-proceeds remain open. |

## Retrieval Boundary

An SEC direct retrieval attempt was made for representative agreement candidates.

The local files created under:

`raw/primary-sources/capital-flow/capital-intensive-credit-agreements/`

currently contain the SEC automated-tool response, not the underlying filings.

Therefore:

`Those downloaded files are retrieval-attempt artifacts, not evidence artifacts.`

The usable evidence in this pass is:

- cached local 10-Q/10-K/8-K filings already in `raw/sec`
- SEC submission metadata stored in local `submissions-cik*.json` files
- an exact official SEC exhibit URL visible inside Sterling's cached Q2 2026 10-Q exhibit index

## Energy Transfer: Agreement Targets

| Target | Status | Why It Matters |
|---|---|---|
| Q2 2026 10-Q Five-Year Credit Facility summary | Cached locally | Confirms `5.00B USD` borrowing capacity, `4.84B USD` later capacity, `7.00B USD` possible accordion, and `1.21B USD` outstanding borrowings. |
| January 27 2026 8-K, accession `0001193125-26-024378` | Candidate identified; direct download blocked | Likely financing event around material agreement/new debt. |
| January 13 2026 8-K, accession `0001193125-26-011876` | Candidate identified; not retrieved | Likely related to financing or note event. |
| January 2026 note issuance summary | Cached in Q2 2026 10-Q | Confirms `3.00B USD` senior notes and refinancing use-of-proceeds language. |

ET's next standard:

`Can we map the revolver, commercial paper, and notes to maturity management versus growth-project funding?`

## Cheniere: Agreement Targets

| Target | Status | Why It Matters |
|---|---|---|
| Q2 2026 10-Q SPL/CQP debt table | Cached locally | Separates `5.027B USD` SPL debt and `9.550B USD` CQP debt. |
| July 2 2026 8-K, accession `0001193125-26-294777` | Candidate identified; direct download blocked | Likely financing event after Q2 close. |
| June 9 2026 8-K, accession `0001193125-26-263943` | Candidate identified; not retrieved | Material definitive agreement candidate in the buildout window. |
| March 19 2026 8-K, accession `0001193125-26-115956` | Candidate identified; not retrieved | Debt-agreement/debt-obligation candidate. |

Cheniere's next standard:

`Can we map SPL, CQP, CCH, and parent debt to specific trains, terminals, restricted accounts, and cash-flow waterfalls?`

## United Rentals: Agreement Targets

| Target | Status | Why It Matters |
|---|---|---|
| Q2 2026 10-Q debt table | Cached locally | Confirms AR securitization, ABL, term loan, senior notes, and finance-lease layers. |
| June 18 2026 8-K, accession `0001104659-26-075708` | Retrieved and extracted after source-locator pass | Actual 8-K and Exhibit `10.1` now support URI receivables-agreement mechanics pass. |
| July 11 2025 8-K, accession `0001104659-25-067406` | Retrieved and extracted after source-locator pass | Actual 8-K and Exhibits `10.1`, `10.2`, and `10.3` now support URI ABL agreement-mechanics pass. |
| December 1 2025 8-K, accession `0001104659-25-117306` | Candidate identified; not retrieved | May explain FY2025 to Q2 2026 debt-structure changes. |
| August 7 2025 8-K, accession `0001104659-25-075201` | Retrieved and classified after source-locator pass | Secured term-loan amendment; not the ABL reset. |

URI's next standard:

`Can we map ABL and receivables securitization to collateral, advance rates, borrowing-base capacity, and fleet growth versus replacement spending?`

## Sterling: Agreement Targets

| Target | Status | Why It Matters |
|---|---|---|
| Q2 2026 10-Q exhibit index | Cached locally | Identifies Exhibit `10.1` for the July 2 2026 Second Amended and Restated Credit Agreement. |
| Official SEC Exhibit `10.1` URL | Identified; direct download blocked | This is the agreement needed for pricing, covenants, guarantors, and maturity terms. |
| June 9 2025 8-K, accession `0000874238-25-000089` | Candidate identified; not retrieved | Relevant to pre-reset debt structure and acquisition financing. |

Sterling's next standard:

`Can we extract the July 2026 credit agreement terms and compare them to the 2025 term-loan/revolver structure?`

## Simple Bottom Line

In simple words:

`We now know exactly what document layer is missing. The credit-stack numbers are real, but the agreement documents are the next gate. Sterling is closest because its Q2 filing points to the exact Exhibit 10.1 credit agreement. ET, Cheniere, and URI have good 10-Q debt tables and identified 8-K candidates, but the actual agreement exhibits still need clean retrieval.`

The important boundary:

`A source locator is not the same as extracted agreement terms.`

## Claim Status

This pass strengthens the research process, not the ultimate claim grade.

Promote only:

`The capital-intensive lane now has a first-pass agreement-document pursuit map.`

Do not promote:

`The lane has full covenant, collateral, borrowing-base, waterfall, or project source-of-funds proof.`

## Next Pass

The next useful pass is:

`capital-flow-capital-intensive-credit-agreement-term-extraction-pass-1.md`

It should extract actual agreement terms after compliant retrieval:

- borrower and guarantor entities
- facility amount
- maturity
- pricing grid
- collateral
- borrowing base or availability mechanics
- covenant package
- use of proceeds
- permitted acquisitions or project spend language
- restricted payments and distributions
- debt-service or waterfall mechanics
