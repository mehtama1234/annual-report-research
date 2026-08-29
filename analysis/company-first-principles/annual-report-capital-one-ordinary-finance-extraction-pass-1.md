# Annual Report Capital One Ordinary Finance Extraction Pass 1

## Purpose

This pass executes the ordinary-finance company-to-theme row:

`ARCTM-073: Capital One consumer lending and card credit`

The question is:

`Can Capital One move from theme candidate to source-visible ordinary-finance evidence without pretending that card balances, auto loans, deposits, charge-offs, reserve builds, Discover integration, or payment-network language proves consumer health, credit recovery, or acquisition return?`

The companion table is:

`analysis/company-first-principles/data/annual-report-capital-one-ordinary-finance-extraction-pass-1.csv`

## Source Boundary

Unlike JPMorgan and American Express, this workspace did not contain a local Capital One company packet under `extracted/`.

This pass therefore uses official Capital One investor-relations source routes:

- Capital One official annual reports page, which lists the `2025 Annual Report`
- Capital One official Q1 2026 earnings release
- Capital One official Q2 2026 earnings release and presentation route

The result is source-visible with boundary, not a locally mirrored packet extraction.

## Verdict

`capital-one-consumer-credit-and-loss-pressure-source-visible-with-boundary`

Yes. Capital One can be upgraded from theme candidate to source-visible ordinary-finance evidence.

The extraction supports this plain-English claim:

`Capital One is the consumer-credit stress and payment-network expansion anchor in the ordinary-finance theme. Official Capital One investor sources show that the 2025 Annual Report source route exists, Q1 2026 net income was 2.2B USD, Q1 diluted EPS was 3.34 USD, Q1 adjusted diluted EPS was 4.42 USD, Q1 total net revenue was 15.2B USD, Q1 pre-provision earnings were 6.8B USD, Q1 provision for credit losses was 4.1B USD, Q1 net charge-offs were 3.8B USD, Q1 loan reserve build was 230M USD, Q1 net interest margin was 7.87%, Q1 CET1 was 14.4%, period-end loans held for investment were 447.8B USD, Credit Card loans were 270.6B USD, Domestic Card loans were 254.0B USD, Consumer Banking loans were 86.9B USD, Auto loans were 85.7B USD, Commercial Banking loans were 90.3B USD, period-end deposits were 489.1B USD, average deposits were 480.0B USD, the interest-bearing deposit rate paid was 3.00%, Q2 2026 net income was 3.0B USD, Q2 diluted EPS was 4.73 USD, Q2 total net revenue was 15.9B USD, Q2 adjusted EPS was 5.81 USD, and Capital One framed itself after Discover as a technology-based financial services company, global payments provider, card lender, consumer bank, and commercial bank. This supports Capital One as the ordinary-finance case for card lending, auto credit, deposits, funding cost, credit losses, provisions, capital, and payment-network expansion. It does not prove consumer health, borrower repayment quality, acquisition return, charge-off normalization, reserve adequacy, deposit stickiness, payment-network economics, or loss-adjusted profitability.`

## Extracted Evidence

| Field | Period | Value | Meaning |
|---|---|---:|---|
| Annual report availability | 2025 | `2025 Annual Report listed` | The official annual-report source route exists. |
| Net income and diluted EPS | Q1 2026 | `2.2B USD / 3.34 USD / 4.42 USD adjusted EPS` | Capital One remained profitable after adjusting-item context. |
| Total net revenue | Q1 2026 | `15.2B USD, down 2% sequentially` | Consumer credit and banking revenue scale is visible. |
| Pre-provision earnings | Q1 2026 | `6.8B USD, up 8% sequentially` | Pre-credit-loss earning power is visible. |
| Provision for credit losses | Q1 2026 | `4.1B USD` | Credit-loss cost is explicit and large. |
| Net charge-offs and reserve build | Q1 2026 | `3.8B USD / 230M USD` | Realized losses and reserve movement are visible. |
| Net interest margin | Q1 2026 | `7.87%, down 39 bps` | Funding cost and loan-yield pressure are visible. |
| CET1 ratio | 2026-03-31 | `14.4%` | Capital buffer visibility exists. |
| Loans held for investment | 2026-03-31 | `447.8B USD total / 270.6B USD Credit Card / 85.7B USD Auto` | Capital One gives the theme direct card, auto, and commercial loan exposure. |
| Deposits and deposit rate | 2026-03-31 | `489.1B USD deposits / 480.0B USD average deposits / 3.00% rate paid` | Deposit funding and funding-cost evidence are visible. |
| Q2 profitability and revenue | Q2 2026 | `3.0B USD net income / 4.73 USD EPS / 15.9B USD revenue / 5.81 USD adjusted EPS` | The latest official source route shows higher profitability and revenue. |
| Discover and payment-network framing | Q1-Q2 2026 | `Discover integration / global payments provider / Credit Card, Consumer Banking, Global Payment Network, Commercial Banking` | Capital One now sits across card credit, deposits, auto, commercial banking, and payments-network expansion. |

## What Capital One Is Doing In Simple Words

Start with a credit card balance.

The customer spends now and promises to repay later. Capital One earns interest, fees, and interchange, but the money is only good if the customer actually pays. When customers do not pay, the lender records charge-offs. When the lender expects future losses, it builds reserves and records provisions.

Now add auto loans and deposits.

Auto loans are another promise to repay over time. Deposits are the funding base: customers give Capital One money to hold, and Capital One uses funding to support lending and banking activity. But deposits are not free. If customers demand higher rates, the bank pays more. That pressure shows up in net interest margin.

That is why Capital One matters for ordinary finance. It sits closer to consumer credit stress than JPMorgan or American Express. JPMorgan shows broad bank scale. American Express shows premium card membership and spend. Capital One shows the harder credit question: what happens when card and auto lending meet real charge-offs, provisions, reserves, and funding cost?

## Money Path

The safe money path is:

`consumer or business wants credit, a card, an auto loan, a deposit account, or payment access -> Capital One provides card lending, auto lending, deposits, consumer banking, commercial banking, and payment-network services -> interest, interchange, fees, and banking revenue appear -> funding cost, provisions, charge-offs, reserve builds, integration expense, marketing, and operating cost absorb part of the revenue -> net income, capital, and loss-adjusted profitability remain only if borrowers repay and deposits stay fundable`

The pressure path is:

`stretched consumer, higher rates, higher deposit cost, rising delinquencies, higher charge-offs, auto credit weakness, Discover integration cost, or payment-network execution risk -> revenue can stay large while credit cost and expenses consume earnings -> evidence remains bounded until delinquency rates, charge-off rates, allowance coverage, loan vintages, funding beta, segment margin, and payment-network economics are extracted`

## Why This Matters For Ordinary Finance

Capital One adds the consumer-credit stress layer.

| Channel | Plain Meaning | What To Watch |
|---|---|---|
| Credit Card loans | card spending that has become a loan balance | repayment, delinquencies, charge-offs, yield, loss rate |
| Domestic Card | the U.S. card book | household stress, rewards cost, marketing, allowance |
| Auto loans | vehicle finance promises | used-car values, borrower credit, charge-offs, collateral recovery |
| Deposits | customer funding for the bank | deposit cost, stability, rate paid, funding mix |
| Net interest margin | spread between loan/assets yield and funding cost | rate pressure, deposit beta, credit pricing |
| Provision and charge-offs | expected and realized credit losses | consumer stress, underwriting, reserve adequacy |
| Discover integration | acquired card/payment network expansion | integration cost, network economics, synergy, credit quality |

## Safe Claim

`Capital One is source-visible as an ordinary-finance consumer-credit and loss-pressure anchor: official Capital One investor sources show Q1 2026 net income of 2.2B USD, Q1 diluted EPS of 3.34 USD, Q1 adjusted diluted EPS of 4.42 USD, Q1 total net revenue of 15.2B USD, Q1 pre-provision earnings of 6.8B USD, Q1 provision for credit losses of 4.1B USD, Q1 net charge-offs of 3.8B USD, Q1 loan reserve build of 230M USD, Q1 net interest margin of 7.87%, Q1 CET1 of 14.4%, period-end loans held for investment of 447.8B USD, Credit Card loans of 270.6B USD, Domestic Card loans of 254.0B USD, Auto loans of 85.7B USD, period-end deposits of 489.1B USD, average deposits of 480.0B USD, an interest-bearing deposit rate paid of 3.00%, Q2 2026 net income of 3.0B USD, Q2 diluted EPS of 4.73 USD, Q2 total net revenue of 15.9B USD, and Q2 adjusted EPS of 5.81 USD.`

## Do Not Overclaim

Do not say Capital One proves consumers are healthy.

Do not say card-loan growth proves good lending.

Do not say charge-offs are normalized without charge-off rates, delinquencies, vintages, and allowance coverage.

Do not say deposits prove low-cost or sticky funding.

Do not say Discover integration proves acquisition return.

Do not say payment-network language proves network economics.

Do not say NIM proves durable spread without funding-cost and credit-cost detail.

Do not say CET1 proves stress-cycle safety without loss scenarios.

## Upgrade Test

Capital One moves from source-visible theme evidence to stronger ordinary-finance cash proof only if the next pass extracts:

1. card-loan balances by segment
2. purchase volume or card spend
3. net interest income
4. net interest margin bridge
5. deposit cost and deposit beta
6. delinquencies by segment
7. net charge-off rates by segment
8. allowance for credit losses
9. provision roll-forward
10. auto-loan credit metrics
11. commercial-loan credit metrics
12. Discover integration expense and synergy evidence
13. Discover/payment-network revenue and margin
14. segment revenue and segment income
15. capital-generation and stress-capital support

## Matrix Update

The company-to-theme matrix row for Capital One should now read:

`source-visible-with-boundary`

The boundary is strict: Capital One is visible as a consumer-credit, card-loan, auto-loan, deposit, funding-cost, provision, charge-off, capital, and payment-network expansion example, not as proof of consumer health, repayment quality, acquisition return, reserve adequacy, deposit durability, or loss-adjusted profitability.

## Decision Marker

`annual-report-capital-one-ordinary-finance-extraction-pass-1-ready`
