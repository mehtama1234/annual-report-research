# Repeatable Company Analysis Process

Purpose: stop company analysis from becoming a filing summary. Each pass must explain what the company does, why customers return, who pays when pressure rises, and what proof would change the answer.

## Required Sources

1. Filings and numbers: annual report, latest 10-K, last three 10-Qs or similar quarterly reports, earnings releases, and SEC company facts when available.
2. Product and price pages: current offers, product pages, bundles, memberships, subscriptions, loyalty terms, and app-only deals.
3. Store, app, and technology pages: automation, data, AI, logistics, edge or cloud work, store tools, delivery, pickup, and customer accounts.
4. Earnings calls: prepared remarks, Q&A, conference talks, and odd comments from management.
5. Outside checks: franchisee comments, trade press, supplier pressure, traffic checks, customer complaints, and competitor responses.
6. Odd signals: product drops, memes, lawsuits, outages, collectible events, resale activity, shortages, or anything that shows what customers care about.
7. Peer checks: at least three peers or substitutes that could prove the company read wrong.

## Required Analysis

1. What are the parts that make this company work?
2. Why does each part work from the customer's point of view?
3. Who pays when the system is stressed: customer, operator, supplier, workers, parent company, lender, or shareholder?
4. Which reported number may only be a moved number, not new demand?
5. How does the business turn sales into cash, and where could that cash picture be too flattering?
6. What facts would prove the whole read wrong?
7. After each pass, what new questions, new codes, new sources, and next companies should be added?

## Writing Standard

The reader should understand the claim before seeing the detail.

Use this order for every important point:

1. `Plain answer`: say what we think in one simple sentence.
2. `Why`: give one reason for that answer.
3. `Evidence`: name the fact, number, or source that supports it.
4. `Other explanation`: say what else could explain the same fact.
5. `Next check`: say exactly what data would separate the two explanations.

Keep each block about one idea. Do not put loyalty, pricing, rent, and store technology in the same paragraph. Use ordinary words such as `more visits`, `higher prices`, `store profit`, and `less waiting`. Define a technical term before using it, or leave it out.

Do not use a table when the reader must understand the reasoning. Use a table only for simple comparisons. For a real question, use a short block with the five labels above.

The analysis is not finished when it has many facts. It is finished when each important fact leads to a clear claim, a competing explanation, and a check that could change the claim.

## McDonald's Correction

The first McDonald's pass failed because it started from filings and broad franchise logic. The corrected pass starts from concrete facts:

- Loyalty: U.S. rewards members more than double visits in the first year after joining.
- `$5 Meal Deal`: a public answer to customers who think fast food got too expensive.
- Coupons: stacked deals can bring visits but hurt restaurant profit.
- Property: rent and franchised fees explain parent-company profit better than food sales alone.
- Ready on Arrival: the store starts work because it knows a mobile-order customer is close.
- Edge computing: the useful test is shorter waits, fewer mistakes, less downtime, and lower labor per order.
- Grinch socks: a meal became a short-term collectible event.
- Q2 2026 warning: U.S. sales rose, but guest counts were down.

## Verifier Rule

`scripts/verify-company-first-principles-analysis.py` now requires:

- outside source links;
- a source-check note;
- the specific company parts being tested;
- deep questions;
- deeper insights;
- checks that local source files exist.

This verifier does not prove the analysis is good. It prevents the worst failure: a polished page that never asked what actually makes the company work.
