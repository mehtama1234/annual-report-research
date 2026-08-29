# Capital Flow BDC Borrower Evidence

## Why This Pass Exists

The bank denominator pass showed that Apollo and Ares are material relative to bank-credit categories.

This pass adds a borrower-facing proxy: Ares Capital Corporation (`ARCC`), a public BDC managed by Ares. BDC filings are useful because they show actual portfolio size, funded investments, portfolio company counts, sponsor exposure, yields, seniority, floating-rate mix, and non-accruals.

## Local Data Files

- BDC extraction table: `analysis/company-first-principles/data/capital-flow-bdc-borrower-evidence.csv`
- Cross-BDC panel: `analysis/company-first-principles/data/capital-flow-cross-bdc-panel.csv`
- BDC industry lane evidence: `analysis/company-first-principles/capital-flow-bdc-industry-lane-evidence.md`
- Borrower matching workbench: `analysis/company-first-principles/capital-flow-borrower-matching-workbench.md`
- ARCC Q2 2026 10-Q: `raw/primary-sources/capital-flow/ares-capital/q2-2026/arcc-2026-q2-10q.html`
- ARCC Q2 2026 SEC earnings exhibit: `raw/primary-sources/capital-flow/ares-capital/q2-2026/arcc-q2-2026-8k-exhibit-99-1.html`
- OBDC Q2 2026 SEC earnings exhibit: `raw/primary-sources/capital-flow/blue-owl-capital-corporation/q2-2026/obdc-q2-2026-8k-exhibit-99-1.html`
- BXSL Q2 2026 SEC earnings exhibit: `raw/primary-sources/capital-flow/blackstone-secured-lending-fund/q2-2026/bxsl-q2-2026-8k-exhibit-99-1.html`

## Extracted ARCC Metrics

| Metric | Q2 2026 Value | Why It Matters |
|---|---:|---|
| Portfolio investments at fair value | `29.349B USD` | Actual borrower-facing private-credit portfolio scale. |
| Portfolio company investments | `619` | Breadth of lending exposure. |
| Private equity sponsors represented | `273` | Sponsor-backed borrower network. |
| New investment commitments | `2.592B USD` | Current-quarter commitment flow. |
| Funded new investment commitments | about `2.2B USD` | Funding that actually reached borrowers. |
| Principal amount of investments funded | `2.927B USD` | 10-Q funded investment flow. |
| First-lien senior secured funded amount | `1.973B USD` | Evidence that much of the flow is senior secured lending. |
| New commitments first-lien senior secured share | `68%` | Bank-like seniority profile, not only equity or junior capital. |
| New commitments floating-rate debt share | `94%` | Shows rate-sensitive private-credit exposure. |
| Weighted average yield on new funded debt/income securities | `9.4%` | Borrower cost / lender yield signal. |
| Non-accrual loans at amortized cost | `2.4%` | Credit-quality disproof metric. |
| Non-accrual loans at fair value | `1.4%` | Credit-quality disproof metric after fair-value marks. |
| Available borrowing capacity | `6.7B USD` | Shows private-credit capacity still relies partly on financing lines. |

## What This Proves

ARCC gives concrete borrower-level evidence behind the Ares platform claim.

The important shift is from abstract Ares credit AUM to actual lending machinery:

`Ares platform -> ARCC / BDC vehicle -> private and sponsor-backed borrowers -> senior secured floating-rate loans -> yield and credit-quality monitoring`

That supports the claim that private credit is a real lending channel, not just an asset-allocation label.

## What This Does Not Prove

It still does not prove exact bank-loan displacement.

Reasons:

- ARCC is one Ares-managed BDC, not all private credit.
- Some ARCC funding comes from bank-led revolving credit facilities, so the relationship is partly symbiotic.
- A borrower receiving private credit may be refinancing another private lender, using sponsor financing, or funding M&A rather than replacing a bank revolver.
- We still need borrower-level matching or category-level flow data to prove substitution.

## Better Claim After BDC Pass

Old claim:

`Private credit is replacing part of bank lending.`

Better claim:

`Ares-managed BDC evidence shows private credit functioning as a borrower-facing lending channel with senior secured loans, sponsor-backed exposure, floating-rate debt, and credit-quality monitoring; direct bank-loan substitution remains unproven without borrower-level matching.`

## What To Do Next

The next serious pass should compare ARCC against other large BDCs:

- Blue Owl Capital Corporation
- Blackstone Secured Lending Fund
- FS KKR Capital
- Golub Capital BDC
- Sixth Street Specialty Lending

For each one, extract:

- portfolio fair value
- number of portfolio companies
- new commitments
- funded investments
- first-lien share
- floating-rate share
- weighted average yield
- non-accruals
- available liquidity

That would make a real private-credit borrower-level panel instead of a single-company case study.

## Simple Version

The Ares parent data says private credit is huge.

The ARCC BDC data shows what that looks like on the ground: hundreds of portfolio-company investments, billions of quarterly commitments/funded investments, mostly senior secured and floating-rate debt, with non-accruals tracked as the stress signal.

So the claim gets stronger but also more precise:

`Private credit is a real parallel lending channel. We can see borrower-level lending activity. We still need cross-BDC and borrower-matching data to prove exact bank displacement.`

## Cross-BDC Panel Started

The next panel now includes three public BDCs:

| BDC | Manager | Portfolio Fair Value | Portfolio Companies | Senior Secured / First-Lien Mix | Floating-Rate Mix | Non-Accrual At Fair Value |
|---|---|---:|---:|---:|---:|---:|
| ARCC | Ares | `29.349B USD` | `619` investments | `68%` of new commitments first-lien senior secured | `94%` of new commitments | `1.4%` |
| OBDC | Blue Owl | `14.955B USD` | `229` companies | `78.8%` of debt investments senior secured | `96.0%` of debt investments | `0.8%` |
| BXSL | Blackstone | about `13.4B USD` | `313` companies | `96.8%` of investments first-lien senior secured debt | `96.3%` of investments floating-rate debt | `1.8%` |

The panel strengthens the borrower-level conclusion:

`Large private-credit BDCs look like parallel loan books: diversified private-company portfolios, mostly senior secured, mostly floating-rate, with yields and non-accruals disclosed like credit-underwriting scorecards.`

The next limitation is still important: this panel shows a lending channel, not the counterfactual source of each borrower's financing.

The industry-lane pass now starts the next layer: identifying whether these loan books are concentrated in software, healthcare, professional services, insurance, commercial services, logistics, defense, and other funded borrower categories.

The borrower-matching workbench then converts named borrowers into claim tests: sponsor, use of proceeds, prior debt source, current lender group, and bank facility role.
