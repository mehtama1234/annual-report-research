#!/usr/bin/env python3
"""Build cross-framework company analysis pages from the annual-report roster."""

from __future__ import annotations

import csv
import html
import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DAMODARAN_ROOT = ROOT.parent / "aswath-damodaran-courses-concepts-research"
DAMODARAN_LIBRARY = DAMODARAN_ROOT / "analysis" / "damodaran-method-library.json"
COMPANIES_CSV = ROOT / "indexes" / "companies.csv"
OUTPUT_ROOT = ROOT / "site" / "cross-framework-companies"
OUTPUT_COMPANIES = OUTPUT_ROOT / "companies"
OUTPUT_DATA = OUTPUT_ROOT / "data"
REGISTRY_JSON = ROOT / "analysis" / "cross-framework-company-method-registry.json"
REPORT_MD = ROOT / "analysis" / "cross-framework-company-method-report.md"
DEEP_MEMO_ROOT = ROOT / "analysis" / "deep-company-pages"

DEEP_EXEMPLARS = {
    "mcdonalds-corporation": {
        "paired_slug": "chipotle-mexican-grill",
        "paired_name": "Chipotle Mexican Grill",
        "template_role": "restaurant company that earns from franchisees, rent, and brand fees",
        "one_line_thesis": (
            "McDonald's does not only make money by selling burgers. Many restaurants are run by franchisees, "
            "and McDonald's earns rent, fees, and royalties from those restaurants while also using its brand, "
            "locations, app, and speed to bring customers back."
        ),
        "analysis_result": (
            "Result: McDonald's is a strong business for the parent company because it collects cash from a large "
            "restaurant system. The main question for an investor is whether customers are actually visiting more "
            "often, or whether sales are being held up by higher prices, discounts, and pressure on franchisees."
        ),
        "result_verdict": "Strong business, but not automatically a good stock purchase unless customer visits and franchisee profits hold up.",
        "result_read": (
            "The analysis says McDonald's parent company is in a strong position because it earns money from a huge "
            "network of restaurants, many of which are run by franchisees. It also turned reported profit into cash "
            "very well in FY2025. The concern is the kind of growth it is showing. In Q2 2026, U.S. sales at comparable "
            "restaurants were up, but customer visits were down. That means the next check is simple: are more people "
            "coming back, and are franchisees still making enough money after paying wages, food costs, rent, fees, "
            "discounts, remodel costs, and technology costs?"
        ),
        "what_must_be_true": [
            "The rewards program must make people visit more often, not just sign up people who already visited often.",
            "Cheap meal offers must bring people back later for normal orders, not only for the cheapest discounted meal.",
            "Franchisees must still make enough money after paying rent, fees, workers, food suppliers, remodel bills, and technology bills.",
            "Store technology must make restaurants faster, more accurate, or easier to run; otherwise it is just another cost.",
        ],
        "evidence_basis": [
            "In FY2025, McDonald's had $26.9B of revenue, $8.563B of net income, $11.95 of diluted EPS, and $10.551B of operating cash flow.",
            "In Q2 2026, global comparable sales rose 1.3% and U.S. comparable sales rose 0.8%, but U.S. customer visits were negative.",
            "Over the trailing twelve months, loyalty members generated about $40B of systemwide sales, and McDonald's had nearly 220M active loyalty users.",
            "The local first-principles packet separates five issues: the rewards app, cheap meal offers, rent and fees, store technology, and marketing events.",
        ],
        "plain_memo": [
            (
                "The main result is that McDonald's is a strong parent-company business, but the strength is not simply "
                "that people recognize the brand. The stronger explanation is that McDonald's sits on top of a very large "
                "restaurant system. Customers buy meals. Franchisees operate many of the restaurants. Those franchisees pay "
                "McDonald's rent, royalty fees, and other fees. That means McDonald's can earn a lot of cash from restaurants "
                "it does not directly run every day."
            ),
            (
                "The FY2025 numbers support that view. McDonald's reported $26.9B of revenue and $8.563B of net income, "
                "but the more important number is $10.551B of operating cash flow. Operating cash flow is cash produced by "
                "normal business activity. When that number is higher than net income, it tells us the accounting profit is "
                "showing up as cash, not just as paper earnings. After $3.365B of capital spending, McDonald's still had "
                "about $7.186B before dividends and buybacks."
            ),
            (
                "The risk is in the customer-visit data. In Q2 2026, U.S. comparable sales rose 0.8%, but U.S. customer "
                "visits were negative. That is a mixed signal. Sales rose, but fewer people came. That can happen when prices "
                "are higher, customers buy a different mix of items, or promotions change what people buy. Growth from more "
                "visits is stronger than growth from fewer visits paying more."
            ),
            (
                "This is why the rewards app and value meals matter. The rewards app is valuable only if it makes people "
                "come more often, buy orders that still make money, and keep returning after discounts fade. The $5 Meal Deal "
                "matters because it tells customers that McDonald's can still be affordable. But cheap meals can either repair "
                "trust or train customers to wait for discounts. Those are very different outcomes."
            ),
            (
                "The investment conclusion is therefore conditional. McDonald's looks like a high-quality cash producer. "
                "But the next review should not just celebrate the brand or the app. It should check whether customer visits "
                "recover, whether loyalty causes extra visits, and whether franchisees still make enough money after rent, "
                "fees, wages, food costs, discounts, remodels, and technology spending."
            ),
        ],
        "number_interpretation": [
            (
                "Revenue tells us how much money came into the company. Net income tells us what profit was left "
                "after expenses under accounting rules. Operating cash flow tells us how much cash the business "
                "actually produced from normal operations. McDonald's produced $10.551B of operating cash flow in "
                "FY2025 versus $8.563B of net income. That is a strong sign because the reported profit showed up "
                "as real cash."
            ),
            (
                "The Q2 2026 U.S. sales number needs careful reading. U.S. comparable sales were up 0.8%, but "
                "guest counts were negative. Guest counts mean customer visits. So sales went up even though fewer "
                "customers came in. That can happen if customers pay higher prices, buy a different mix of items, "
                "or respond to promotions. This is weaker than growth caused by more people visiting."
            ),
            (
                "The loyalty numbers are very large: about $40B of trailing-twelve-month sales to loyalty members "
                "and nearly 220M active loyalty users. But a large app program is not automatically proof of a "
                "stronger business. The important question is whether the app changes behavior. Do customers come "
                "more often because of the app, buy orders that make good profit, and keep returning after coupons "
                "or launch offers fade? If not, the app may mostly be counting customers who already liked McDonald's."
            ),
            (
                "Capital spending was $3.365B in FY2025. Capital spending means money spent on things such as "
                "restaurants, equipment, remodels, and technology. After that spending, McDonald's still had about "
                "$7.186B of cash before dividends and share buybacks. That is good for the parent company, but the "
                "system can keep working only if franchisees can also afford their own store spending and still make money."
            ),
        ],
        "approach_rationale": [
            (
                "The first-principles approach starts by breaking the business into plain parts. For McDonald's, "
                "those parts are customer visits, dollars spent per order, how many orders a restaurant can handle, "
                "rent, franchise fees, royalty fees, franchisee profit, and cash left for the parent company."
            ),
            (
                "The Damodaran approach is used because a good story still has to become a valuation. In plain terms, "
                "the analysis must ask how fast cash can grow, how much profit stays after costs, how much money must "
                "be put back into the business, how risky the cash flows are, and what the business may be worth many "
                "years from now."
            ),
            (
                "The Lyn Alden-style macro check is used because customers do not buy meals in a vacuum. Wages, rent, "
                "food prices, interest rates, and household budgets affect how often people eat out and how sensitive "
                "they are to price."
            ),
            (
                "Owner earnings are used to ask how much cash might truly belong to shareholders after the business "
                "keeps its restaurants and systems in good shape. Industry structure is used to ask who has power: "
                "McDonald's, franchisees, suppliers, workers, landlords, competitors, or customers."
            ),
        ],
        "approach_findings": [
            {
                "approach": "First-principles breakdown",
                "question": "What is the business really doing underneath the simple label 'restaurant chain'?",
                "evidence_used": "FY2025 cash flow, Q2 2026 customer-visit data, the franchise/rent/fee model, loyalty disclosures, and store-technology claims.",
                "what_was_found": (
                    "McDonald's is not mainly a simple food seller from the parent company's point of view. "
                    "The parent company gets paid through a large restaurant system: customer visits create restaurant sales; "
                    "franchisees run many stores; franchisees pay McDonald's rent, royalty fees, and other fees."
                ),
                "why_it_matters": (
                    "This explains why McDonald's can report strong parent-company cash even when restaurant operators face "
                    "wages, food costs, discounts, remodel spending, and technology spending."
                ),
                "what_would_change_the_answer": (
                    "The answer would weaken if franchisee profit fell, franchisees slowed new openings or remodels, "
                    "or customer visits kept falling even while McDonald's reported higher sales."
                ),
            },
            {
                "approach": "Damodaran valuation discipline",
                "question": "If this business is valuable, which future cash flows have to happen to justify that value?",
                "evidence_used": "Revenue, net income, operating cash flow, capital spending, comparable sales, customer visits, and loyalty-member sales.",
                "what_was_found": (
                    "The story cannot stop at 'McDonald's is a famous brand.' The value depends on future customer visits, "
                    "average order size, store count, parent-company cash, required spending, and risk."
                ),
                "why_it_matters": (
                    "This keeps the analysis from treating brand strength or loyalty size as automatically making the stock attractive."
                ),
                "what_would_change_the_answer": (
                    "The answer would improve if visits grew without heavy discounting. It would weaken if growth required more spending, "
                    "more promotions, or more franchisee burden than the cash flows can support."
                ),
            },
            {
                "approach": "Lyn Alden-style macro check",
                "question": "How do household budgets, inflation, food costs, wages, rent, and interest rates affect this company?",
                "evidence_used": "The Q2 2026 weak U.S. guest-count signal, the $5 Meal Deal, McValue offers, and cost pressures that affect restaurants.",
                "what_was_found": (
                    "McDonald's depends on everyday household spending. When food, rent, debt payments, and other living costs rise, "
                    "customers become more careful about fast-food prices."
                ),
                "why_it_matters": (
                    "This explains why the $5 Meal Deal and value offers matter. They are not side promotions; they are McDonald's response "
                    "to customers questioning whether fast food is still worth the price."
                ),
                "what_would_change_the_answer": (
                    "The answer would improve if value offers led to repeat normal-price visits. It would weaken if customers came only for deals "
                    "or if franchisees had to pay too much of the discount cost."
                ),
            },
            {
                "approach": "Owner cash test",
                "question": "How much real cash did the business produce after the spending needed to keep it running?",
                "evidence_used": "FY2025 operating cash flow of $10.551B and capital spending of $3.365B.",
                "what_was_found": (
                    "FY2025 operating cash flow was $10.551B and capital spending was $3.365B, leaving about $7.186B before dividends and buybacks."
                ),
                "why_it_matters": (
                    "That is a strong parent-company cash result, but the analysis still has to ask whether franchisees also have enough cash "
                    "to keep stores updated and profitable."
                ),
                "what_would_change_the_answer": (
                    "The answer would weaken if future cash flow fell, capital spending rose sharply, or franchisees needed more financial support "
                    "from McDonald's to keep the system healthy."
                ),
            },
            {
                "approach": "Industry power check",
                "question": "Who has power in the system: McDonald's, franchisees, suppliers, workers, landlords, competitors, or customers?",
                "evidence_used": "The franchise model, value offers, customer-visit weakness, and the fact that customers can choose many substitute meals.",
                "what_was_found": (
                    "McDonald's has power from brand, locations, habit, speed, and scale. Customers still have power because they can trade down, "
                    "eat at home, choose grocery food, or wait for discounts."
                ),
                "why_it_matters": (
                    "This is why positive sales with falling customer visits is not fully comforting. Customers may be resisting price even while "
                    "reported sales still rise."
                ),
                "what_would_change_the_answer": (
                    "The answer would improve if customer visits grew without larger discounts. It would weaken if customers kept trading down "
                    "or if franchisees had to absorb more of the pain to keep prices attractive."
                ),
            },
        ],
        "plain_english_walkthrough": [
            (
                "Start with what McDonald's really sells. A customer thinks they are buying a meal, but an investor "
                "has to see a larger machine: recognizable brand, convenient real estate, franchise contracts, rent, "
                "royalties, menu pricing, mobile ordering, and repeat customer behavior. The parent company does not "
                "need to own every restaurant to make money. Franchisees run many McDonald's restaurants, and they "
                "pay McDonald's rent, royalty fees, and other fees for using the brand and locations."
            ),
            (
                "That is why the difference between the parent company and the restaurant operator matters. The parent can "
                "report strong cash flow while the people operating restaurants face wage inflation, food inflation, "
                "discount pressure, remodel requirements, and technology spending. The analysis therefore does not stop "
                "at McDonald's corporate profit. It asks whether the whole system is healthy enough to keep producing "
                "that profit."
            ),
            (
                "Comparable sales, or comps, mean sales at restaurants that have been open long enough to compare "
                "against the prior period. A positive comp is good only after asking what caused it. If more customers "
                "visited, the business may be strengthening. If fewer customers visited but paid more per order, the "
                "headline sales number can hide demand weakness."
            ),
            (
                "The rewards app matters only if it changes what customers do. A big user count is not enough. "
                "The stronger proof would be this: after joining, customers visit more often than they did before, "
                "their orders still make money for the restaurant, and they keep coming back after coupons fade. "
                "Without that proof, the app may mostly be a way to track customers who already liked McDonald's."
            ),
        ],
        "reader_glossary": [
            ("Comparable sales", "Sales growth at existing restaurants. It helps separate real store performance from growth caused only by opening new restaurants."),
            ("Guest counts", "The number of customer visits. If guest counts fall while sales rise, customers may be paying more but visiting less."),
            ("Average check", "The average dollars spent per order. It can rise because of price increases, menu mix, or larger baskets."),
            ("Franchise model", "A structure where local operators run many restaurants while McDonald's collects rent, royalties, and fees from them."),
            ("Free cash flow", "Cash left after capital spending needed to maintain and grow the business. It is closer to what owners can ultimately use than revenue or EPS alone."),
            ("Systemwide sales", "Sales made by all restaurants in the system, including restaurants run by franchisees. This is larger than McDonald's own reported revenue."),
            ("Did the app cause more visits?", "The key loyalty question: did customers visit more because of the app, or were frequent customers simply the first people to join?"),
        ],
        "company_conclusion": (
            "McDonald's is best understood as a restaurant system owner. The parent company benefits from the brand, "
            "busy locations, rent, royalty fees, and customer data from the app. The main risk is that the parent "
            "company can keep looking strong while customer visits weaken or franchisees carry more of the cost burden."
        ),
        "investment_posture": (
            "McDonald's is a strong cash-producing business, but the next review must prove that loyalty and value "
            "offers create lasting customer visits and do not simply cover up weak traffic or franchisee pressure."
        ),
        "key_metrics": [
            ("FY2025 scale", "Revenue $26.9B; net income $8.563B; diluted EPS $11.95."),
            ("Cash produced", "Operating cash flow $10.551B; capital spending $3.365B; cash before payouts about $7.186B."),
            ("Q2 2026 demand", "Global comparable sales +1.3%; U.S. comparable sales +0.8%; U.S. customer visits were negative."),
            ("Loyalty size", "Trailing-twelve-month loyalty-member systemwide sales about $40B; nearly 220M active users."),
            ("System pressure point", "Discounts, remodels, labor, food, and technology costs can land first on franchisees."),
        ],
        "framework_lenses": [
            ("First principles", "Break the business into customer visits, dollars per order, restaurant speed, store costs, rent, fees, and parent-company cash."),
            ("Damodaran", "Turn the story into numbers: cash growth, profit level, required reinvestment, risk, and long-term value."),
            ("Lyn Alden", "Ask how household budgets, inflation, food costs, wages, and interest rates affect restaurant visits and costs."),
            ("Owner earnings", "Start with cash from operations, subtract needed store and technology spending, then judge what cash is really left."),
            ("Industry structure", "Ask who has power in the system: customers, franchisees, suppliers, workers, landlords, competitors, or McDonald's."),
            ("Expectations", "Ask what future the stock price seems to assume, then test whether the evidence supports that future."),
        ],
        "mispricing_questions": [
            "The market may give too much credit to loyalty users before proving those users visit more often because of the app.",
            "The parent company may look healthier than the franchisees who run many of the restaurants.",
            "Sales can rise while customer visits fall, so higher prices or different order mix must not be confused with stronger demand.",
            "A short-term marketing event can create attention without proving customers will keep coming back.",
        ],
        "disconfirming_tests": [
            "Rewards members do not keep visiting more often after their first year in the program.",
            "$5 Meal Deal buyers come back only for the cheapest meal and do not buy extra items that help restaurant profit.",
            "Franchisees make less money, struggle with debt, delay remodels, close stores, or stop opening new stores.",
            "Store technology does not reduce waiting time, order mistakes, broken equipment time, or worker time per order.",
            "Customer visits keep falling while sales depend on higher prices, different menu items, or promotions.",
        ],
        "watchlist": [
            "In the next three U.S. quarters, check whether sales are rising because more customers visit or because each customer pays more.",
            "For loyalty members, compare how often they visited before joining with how often they visit after joining.",
            "Check whether franchisees are still making enough money after rent, royalty fees, remodels, wages, and food costs.",
            "Check whether digital ordering improves waiting time, order accuracy, and worker time per order.",
            "Check whether share buybacks are happening at sensible prices after McDonald's funds restaurant needs.",
        ],
        "comparison_bridge": (
            "Compared with Chipotle, McDonald's pushes more store work and store cost onto franchisees. "
            "McDonald's then earns rent and fees from those franchisees. That can make the parent company look "
            "very strong, but the key question is whether franchisees are still healthy after paying those costs."
        ),
    },
    "chipotle-mexican-grill": {
        "paired_slug": "mcdonalds-corporation",
        "paired_name": "McDonald's Corporation",
        "template_role": "restaurant company that owns and runs almost all of its stores",
        "one_line_thesis": (
            "Chipotle makes money by owning and running restaurants itself. Its story depends on whether new stores, "
            "digital ordering, and pickup lanes bring in enough extra customer spending to cover food, workers, rent, "
            "construction, and operating problems."
        ),
        "analysis_result": (
            "Result: Chipotle can keep growing if each new restaurant makes enough profit after all store costs. "
            "The warning sign is that customer visits only recently improved while restaurant profit as a percentage "
            "of sales fell. Growth is valuable only if the new stores create new demand and do not weaken older stores."
        ),
        "result_verdict": "Good growth story, but only if customer visits keep recovering and each new store earns enough after costs.",
        "result_read": (
            "The analysis says Chipotle is easier to read than McDonald's in one way: Chipotle owns and runs almost "
            "all of its stores, so the store results show up directly in the parent company numbers. That also makes "
            "the risk more direct. In FY2025, customer visits were weak. In Q2 2026, visits improved. But restaurant "
            "profit as a share of sales fell. That means growth is not enough by itself. We need proof that new stores "
            "and Chipotlanes add sales that remain profitable after food, labor, rent, construction, and operating costs."
        ),
        "what_must_be_true": [
            "New restaurants must bring in new customer visits instead of mostly taking visits from older nearby Chipotle restaurants.",
            "Chipotlanes must add enough sales or store profit to justify their extra construction and operating cost.",
            "Customer visits must keep growing, rather than sales growth coming mostly from customers paying more per order.",
            "Restaurant profit must recover even while food costs, worker costs, rent, and digital-order work remain high.",
        ],
        "evidence_basis": [
            "In FY2025, comparable sales fell 1.7%, customer transactions fell 2.9%, and average spending per order rose 1.2%.",
            "In Q2 2026, comparable sales rose 2.2%, customer transactions rose 1.0%, and average spending per order rose 1.2%.",
            "In Q2 2026, restaurant-level margin fell to 25.2% from 27.4%, meaning store profit took up a smaller share of sales.",
            "Digital sales were 38.3% of Q2 food and beverage revenue, and 80 of 100 new Q2 stores had Chipotlanes.",
        ],
        "plain_memo": [
            (
                "The main result is that Chipotle has a believable growth story, but it is not proven by revenue growth alone. "
                "Chipotle owns and runs almost all of its restaurants. That makes the analysis more direct than McDonald's. "
                "When food costs rise, worker costs rise, rent rises, or store service gets harder, those problems show up "
                "inside Chipotle's own results."
            ),
            (
                "The FY2025 numbers show why the story needs caution. Comparable sales fell 1.7%. Customer transactions fell "
                "2.9%. Average spending per order rose 1.2%. In plain English, customers came less often, and higher spending "
                "per order softened the damage. That is not the same as a healthy traffic story."
            ),
            (
                "Q2 2026 was better. Comparable sales rose 2.2%, customer transactions rose 1.0%, and average spending per "
                "order rose 1.2%. That is a better signal because visits improved. But at the same time, restaurant-level "
                "margin fell to 25.2% from 27.4%. Restaurant-level margin means store profit as a share of store sales. "
                "So the company got more customer activity, but each dollar of store sales left less store profit than before."
            ),
            (
                "The new-store and Chipotlane story has to be tested store by store. Opening 100 restaurants in Q2 2026 is "
                "impressive, and 80 of them had Chipotlanes. But a new store helps shareholders only if it brings in new demand "
                "and earns back the money spent to build it. If a new Chipotle mostly takes customers from an older nearby "
                "Chipotle, total company revenue can rise while the actual business improvement is weaker."
            ),
            (
                "The investment conclusion is therefore also conditional. Chipotle can be attractive if customer visits keep "
                "recovering, restaurant profit recovers, and new stores produce enough profit after food, workers, rent, "
                "construction, and training costs. The story weakens if sales growth depends mostly on higher spending per "
                "order, if store profit keeps falling, or if new stores steal too many visits from older stores."
            ),
        ],
        "number_interpretation": [
            (
                "The most important Chipotle number is not total revenue growth by itself. In FY2025, comparable "
                "sales fell 1.7% because customer transactions fell 2.9% while average spending per order rose 1.2%. "
                "That means fewer customer visits were partly offset by customers paying more per visit."
            ),
            (
                "Q2 2026 looked better because comparable sales rose 2.2% and customer transactions rose 1.0%. "
                "That is better than sales growth caused only by higher prices. Still, one quarter is not enough "
                "to prove that customers have returned to a steady habit of visiting more often."
            ),
            (
                "Restaurant-level margin falling to 25.2% from 27.4% is the warning sign. Restaurant-level margin "
                "means store profit as a percentage of store sales, before corporate overhead. Because Chipotle owns "
                "almost all stores, higher food costs, worker costs, rent, online-order work, and service problems "
                "show up directly in Chipotle's own results."
            ),
            (
                "Digital sales at 38.3% of food and beverage revenue show that many customers order without standing "
                "in the normal line. Chipotlanes, which are pickup lanes for digital orders, were included in 80 of "
                "100 new Q2 openings. That can make stores more convenient, but it only creates value if the extra "
                "sales are large enough to cover construction cost, labor, and kitchen complexity."
            ),
        ],
        "approach_rationale": [
            (
                "The first-principles approach starts with one restaurant. The analysis asks how many customers come "
                "in, how much they spend, what food costs, what workers cost, what rent costs, how many orders the "
                "store can handle, how much the store costs to build, and how long it takes to earn that money back."
            ),
            (
                "The Damodaran approach is used because Chipotle is mainly a growth story. A growth story is only "
                "valuable if the company can put money into new stores and earn more from those stores than the money "
                "costs. Revenue growth alone is not enough."
            ),
            (
                "The Lyn Alden-style macro check is used because food inflation, wage inflation, rent, and household "
                "budgets directly affect Chipotle. If customers feel squeezed, they may visit less often. If costs "
                "rise faster than prices, store profit falls."
            ),
            (
                "Owner earnings are used to ask how much cash is left after Chipotle builds and maintains stores. "
                "Expectations analysis asks what future growth the stock price seems to assume. Industry structure "
                "asks whether Chipotle's visible food and simple menu are strong enough to keep customers from "
                "choosing cheaper meals elsewhere."
            ),
        ],
        "approach_findings": [
            {
                "approach": "First-principles store test",
                "question": "Does one Chipotle restaurant make enough money after all store costs?",
                "evidence_used": "Comparable sales, customer transactions, average spending per order, restaurant-level margin, digital sales, and new-store openings.",
                "what_was_found": (
                    "Chipotle is easier to analyze one restaurant at a time: how many customers visit, how much they spend, what food and workers cost, "
                    "what rent costs, how fast orders move, what the store costs to build, and how long it takes to earn that money back."
                ),
                "why_it_matters": (
                    "This shows why total revenue growth is not enough. A new store helps only if it adds profitable customer visits after all store costs."
                ),
                "what_would_change_the_answer": (
                    "The answer would improve if new stores showed strong sales and profit without hurting older stores. It would weaken if new stores "
                    "mostly moved customers from one Chipotle location to another."
                ),
            },
            {
                "approach": "Damodaran valuation discipline",
                "question": "Is Chipotle's growth worth more than the money it must spend to get that growth?",
                "evidence_used": "Store openings, Chipotlane openings, capital spending, operating cash flow, comparable sales, customer transactions, and store profit.",
                "what_was_found": (
                    "Chipotle is a growth story, but growth has a cost. New stores and Chipotlanes require cash before they produce profit."
                ),
                "why_it_matters": (
                    "The stock is attractive only if the stores opened with that cash earn more than the cash cost and do not weaken older nearby stores."
                ),
                "what_would_change_the_answer": (
                    "The answer would improve if store payback stayed fast and restaurant profit recovered. It would weaken if the company had to spend "
                    "more per store while each store earned less profit."
                ),
            },
            {
                "approach": "Lyn Alden-style macro check",
                "question": "How do inflation and household budgets affect a company that runs its own restaurants?",
                "evidence_used": "Food costs, worker costs, rent pressure, customer transaction trends, and the Q2 2026 restaurant-level margin drop.",
                "what_was_found": (
                    "Chipotle is exposed directly to food prices, worker wages, rent, and household budgets because it owns almost all of its stores."
                ),
                "why_it_matters": (
                    "This helps explain the Q2 2026 warning sign: restaurant-level margin fell even though customer transactions improved."
                ),
                "what_would_change_the_answer": (
                    "The answer would improve if transaction growth continued while store profit recovered. It would weaken if costs kept rising faster "
                    "than Chipotle could raise prices without losing visits."
                ),
            },
            {
                "approach": "Owner cash test",
                "question": "After running stores and building new ones, how much cash is left for shareholders?",
                "evidence_used": "FY2025 operating cash flow of $2.114B, capital spending of $666.3M, and share repurchases of $2.426B.",
                "what_was_found": (
                    "FY2025 operating cash flow was $2.114B, capital spending was $666.3M, and share repurchases were $2.426B."
                ),
                "why_it_matters": (
                    "The company produced cash, but investors still need to judge whether buybacks and new-store spending are both sensible uses of that cash."
                ),
                "what_would_change_the_answer": (
                    "The answer would weaken if buybacks consumed cash while store profit fell or if new-store spending stopped producing strong returns."
                ),
            },
            {
                "approach": "Industry power check",
                "question": "Can Chipotle keep customers paying its prices when cheaper meals are available?",
                "evidence_used": "Transaction trends, average spending per order, the visible-food promise, digital ordering, and restaurant profit pressure.",
                "what_was_found": (
                    "Chipotle has a food-quality and convenience advantage, but customers can still choose cheaper meals if the price feels too high."
                ),
                "why_it_matters": (
                    "That is why customer transactions matter so much. If visits fall and only average spending rises, the growth story is weaker."
                ),
                "what_would_change_the_answer": (
                    "The answer would improve if customers kept visiting more often even after price increases. It would weaken if customers came less often "
                    "or only returned when promotions made the meal cheaper."
                ),
            },
        ],
        "plain_english_walkthrough": [
            (
                "Start with what Chipotle really sells. It sells a repeat meal habit built around visible preparation, "
                "simple customization, perceived food quality, and convenience. Unlike McDonald's, Chipotle owns almost "
                "all of its stores, so the parent company keeps more of the store profit when things go well and absorbs "
                "more of the cost pressure when things go badly."
            ),
            (
                "That company-owned model makes the analysis more direct but harsher. Labor cost, food cost, rent, digital "
                "order complexity, staffing problems, and new-store construction costs show up directly in Chipotle's "
                "reported results. There is less need to guess what franchisees are feeling because Chipotle itself is "
                "the operator."
            ),
            (
                "For Chipotle, comparable sales must be split into transactions and average check. Transactions mean "
                "how often customers show up. Average check means how much they spend per visit. A chain is usually "
                "healthier when both rise, but transaction growth is especially important because it shows customer "
                "frequency rather than just higher prices."
            ),
            (
                "New stores and Chipotlanes are not automatically good. A new store helps shareholders only if it brings "
                "in new customers and earns back what it cost to build. If it takes customers from nearby older stores, "
                "or if the pickup lane adds cost without enough extra sales, total revenue can rise while the company "
                "is not actually becoming much stronger."
            ),
        ],
        "reader_glossary": [
            ("Comparable sales", "Sales growth at restaurants open long enough to compare against a prior period."),
            ("Transactions", "Customer visit count. For Chipotle, transaction recovery is better evidence than sales growth caused only by higher prices."),
            ("Average check", "Average spend per visit. Higher check helps revenue, but can also signal that customers are paying more rather than coming more often."),
            ("Restaurant-level margin", "Restaurant profit after store operating costs, before corporate overhead. It shows whether each store is becoming more or less profitable."),
            ("One-store profit math", "The basic money test for one restaurant: what it costs to build, how much it sells, how much profit it makes, and how long it takes to earn back the build cost."),
            ("New store stealing sales", "A new store takes sales from an older nearby store instead of creating truly new demand."),
        ],
        "company_conclusion": (
            "Chipotle is best understood as a company that owns its restaurant growth directly. That makes the story "
            "clear: more stores and more digital pickup help shareholders only if each store earns enough profit "
            "after food, workers, rent, construction, training, and service problems."
        ),
        "investment_posture": (
            "Chipotle has a believable growth story, but the company itself must pay for food, workers, rent, store "
            "construction, training, and operating mistakes. The store profits must be large enough to cover that burden."
        ),
        "key_metrics": [
            ("FY2025 traffic", "Comparable sales -1.7%; transactions -2.9%; average check +1.2%."),
            ("Q2 2026 recovery", "Comparable sales +2.2%; customer transactions +1.0%; average spending per order +1.2%."),
            ("Store profit pressure", "Q2 restaurant-level margin fell to 25.2% from 27.4%."),
            ("Digital ordering", "Digital sales were 38.3% of Q2 food and beverage revenue."),
            ("New stores", "Opened 100 company-owned restaurants in Q2 2026, including 80 with Chipotlanes."),
        ],
        "framework_lenses": [
            ("First principles", "Break one store into visits, dollars per order, food cost, worker cost, rent, speed, build cost, and payback time."),
            ("Damodaran", "Turn the growth story into numbers: new-store spending, store profit, cash growth, risk, and long-term value."),
            ("Lyn Alden", "Ask how food prices, wages, rent, interest rates, and household budgets affect visits and store profit."),
            ("Owner earnings", "Compare cash from operations with the cash needed to build and maintain restaurants before judging cash left for owners."),
            ("Industry structure", "Ask whether visible food quality and convenience are strong enough to beat cheaper meal choices."),
            ("Expectations", "Ask what future store count and profit level the stock price seems to assume, then test whether the evidence supports it."),
        ],
        "mispricing_questions": [
            "New restaurant openings can hide weakness at older restaurants if new stores take customers from nearby older stores.",
            "Chipotlanes may make pickup easier but still fail to earn enough extra profit after their extra cost.",
            "Digital ordering can rise while kitchen work, delivery costs, wait times, or worker hours also rise.",
            "Customers may like the food but still visit less often if the meal feels too expensive.",
        ],
        "disconfirming_tests": [
            "Customer transactions fall again while sales are held up mainly by customers paying more per order.",
            "Chipotlane stores do not show better sales, better store profit, or faster payback after extra build cost.",
            "Older stores near new openings lose traffic and profit.",
            "Digital ordering grows while service quality or restaurant profit gets worse.",
            "Manager retention, staffing, or food execution weakens as the store base expands.",
        ],
        "watchlist": [
            "For at least the next three quarters, check whether customer visits rise or whether customers are just paying more per order.",
            "Break down the change in restaurant profit by food cost, worker cost, rent, and delivery cost.",
            "Compare sales at new stores with sales at older nearby stores to see whether new stores are stealing customers.",
            "Chipotlane sales and profit compared with similar stores that do not have Chipotlanes.",
            "Check whether cash from operations is enough to fund new stores, maintain old stores, and still support share buybacks.",
        ],
        "comparison_bridge": (
            "Compared with McDonald's, Chipotle keeps more of the store profit when stores do well, but it also "
            "keeps more of the store problems when costs rise or execution slips. Chipotle is the better example "
            "for studying whether new stores earn enough money. McDonald's is the better example for studying "
            "whether the parent company and franchisees are both healthy."
        ),
    },
}


LYN_ALDEN_METHODS = [
    {
        "id": "lyn-fiscal-dominance-and-deficit-liquidity",
        "title": "Fiscal dominance and deficit liquidity",
        "source": "https://www.lynalden.com/fiscal-and-monetary-policy/",
        "keywords": ["bank", "asset management", "insurance", "utility", "defense", "government", "infrastructure", "debt", "rate", "financing"],
        "when_to_use": "Use when deficits, interest expense, policy spending, or Treasury/liquidity conditions can change demand, funding costs, or valuation multiples.",
    },
    {
        "id": "lyn-liquidity-before-solvency",
        "title": "Liquidity before solvency",
        "source": "https://www.lynalden.com/newsletter-archives/",
        "keywords": ["bank", "credit", "insurance", "asset management", "brokerage", "real estate", "reit", "debt", "refinancing", "liquidity"],
        "when_to_use": "Use when the company can look solvent on accounting numbers but fail or re-rate because funding access tightens first.",
    },
    {
        "id": "lyn-long-duration-fiat-claim-risk",
        "title": "Long-duration fiat claim risk",
        "source": "https://www.lynalden.com/june-2026-newsletter/",
        "keywords": ["bond", "insurance", "bank", "duration", "fixed income", "receivable", "finance", "mortgage", "utility", "pension"],
        "when_to_use": "Use when the business owns or issues long-duration nominal claims that are sensitive to inflation, repression, or rate volatility.",
    },
    {
        "id": "lyn-energy-and-commodity-underinvestment",
        "title": "Energy and commodity underinvestment",
        "source": "https://www.lynalden.com/august-2022-newsletter/",
        "keywords": ["energy", "oil", "gas", "utility", "materials", "chemicals", "aluminum", "steel", "fertilizer", "power", "data center"],
        "when_to_use": "Use when physical supply, energy availability, commodity cycles, or years of underinvestment shape margins and growth.",
    },
    {
        "id": "lyn-scarce-assets-and-hard-money-portfolio-role",
        "title": "Scarce assets and hard-money portfolio role",
        "source": "https://www.lynalden.com/april-2024-newsletter/",
        "keywords": ["gold", "bitcoin", "commodity", "producer", "resource", "energy", "mining", "inflation", "scarce"],
        "when_to_use": "Use when the company behaves like a scarce-asset, commodity-producer, or inflation-resilience exposure rather than a normal operating compounder.",
    },
    {
        "id": "lyn-reshoring-and-capital-intensity",
        "title": "Reshoring and capital intensity",
        "source": "https://www.lynalden.com/reshoring/",
        "keywords": ["manufacturing", "industrial", "semiconductor", "materials", "capex", "supply chain", "infrastructure", "factory"],
        "when_to_use": "Use when local production, redundant supply chains, higher cost of capital, or physical capacity expansion drive economics.",
    },
]

OTHER_METHODS = [
    {
        "id": "buffett-owner-earnings",
        "title": "Owner earnings and cash conversion",
        "keywords": ["cash flow", "capex", "buyback", "dividend", "maintenance", "retail", "industrial", "consumer"],
        "when_to_use": "Use when reported earnings and cash available to owners may diverge because of maintenance capex, working capital, or reinvestment burden.",
    },
    {
        "id": "mauboussin-expectations-investing",
        "title": "Expectations investing",
        "keywords": ["growth", "multiple", "pricing", "expectations", "market", "narrative", "valuation"],
        "when_to_use": "Use when the central question is what operating future is already embedded in the current market narrative.",
    },
    {
        "id": "porter-industry-structure",
        "title": "Industry structure and bargaining power",
        "keywords": ["supplier", "customer", "competition", "pricing", "distribution", "channel", "retail", "wholesale"],
        "when_to_use": "Use when margins depend on supplier power, customer concentration, substitute products, or competitive intensity.",
    },
    {
        "id": "capital-cycle-analysis",
        "title": "Capital-cycle analysis",
        "keywords": ["capacity", "capex", "commodity", "cycle", "supply", "housing", "energy", "materials", "shipping"],
        "when_to_use": "Use when industry returns depend on whether capital is entering or leaving the sector.",
    },
    {
        "id": "quality-moat-reinvestment-runway",
        "title": "Quality, moat, and reinvestment runway",
        "keywords": ["brand", "network", "platform", "recurring", "loyalty", "subscription", "installed base", "scale"],
        "when_to_use": "Use when durability depends on customer habit, brand trust, switching costs, scale, or an installed base.",
    },
    {
        "id": "credit-underwriting-and-refinancing-risk",
        "title": "Credit underwriting and refinancing risk",
        "keywords": ["debt", "leverage", "maturity", "credit", "loan", "interest", "refinancing", "bank"],
        "when_to_use": "Use when downside is controlled by debt maturities, funding access, covenant pressure, or asset quality.",
    },
]


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "company"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def read_companies() -> list[dict[str, str]]:
    with COMPANIES_CSV.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        headers = next(reader)
        rows = []
        for raw in reader:
            if len(raw) > len(headers):
                overflow = len(raw) - len(headers)
                raw = [raw[0], ",".join(raw[1 : 2 + overflow]), *raw[2 + overflow :]]
            rows.append(dict(zip(headers, raw)))
    by_slug: dict[str, dict[str, str]] = {}
    for row in rows:
        slug = row["company_slug"]
        if slug not in by_slug:
            by_slug[slug] = row
            continue
        if by_slug[slug].get("coverage_status") == "seeded" and row.get("coverage_status") != "seeded":
            by_slug[slug] = row
    return list(by_slug.values())


def load_damodaran_library() -> dict[str, Any]:
    if not DAMODARAN_LIBRARY.exists():
        raise FileNotFoundError(f"missing Damodaran method library: {DAMODARAN_LIBRARY}")
    return load_json(DAMODARAN_LIBRARY)


def source_roster_row_count() -> int:
    with COMPANIES_CSV.open(newline="", encoding="utf-8") as handle:
        reader = csv.reader(handle)
        next(reader)
        return sum(1 for _ in reader)


def company_text(company: dict[str, str], detailed: dict[str, Any] | None) -> str:
    parts = [
        company.get("company_name", ""),
        company.get("ticker", ""),
        company.get("sector", ""),
        company.get("industry", ""),
        company.get("analyst_notes", ""),
    ]
    if detailed:
        parts.extend(
            [
                str(detailed.get("primary_question", "")),
                str(detailed.get("core_answer", "")),
                json.dumps(detailed.get("mechanisms", [])),
                json.dumps(detailed.get("investment_read", {})),
                json.dumps(detailed.get("operating_evidence", [])),
                json.dumps(detailed.get("axial_codes", [])),
            ]
        )
    return " ".join(parts).lower()


def sentence_from_note(note: str) -> str:
    cleaned = re.sub(r"\s+", " ", note.strip())
    if not cleaned:
        return "The current roster supplies identity and coverage metadata, but a richer company packet is still needed before making firm company-specific claims."
    pieces = re.split(r"(?<=[.!?])\s+", cleaned)
    return pieces[0]


def extract_section(markdown: str, heading: str) -> str:
    pattern = re.compile(
        r"^## " + re.escape(heading) + r"\s*$\n(?P<body>.*?)(?=^## |\Z)",
        re.MULTILINE | re.DOTALL,
    )
    match = pattern.search(markdown)
    return match.group("body").strip() if match else ""


def bullets_from_section(section: str, limit: int = 5) -> list[str]:
    bullets = []
    for raw_line in section.splitlines():
        line = raw_line.strip()
        if not line.startswith("- "):
            continue
        text = re.sub(r"\s+", " ", line[2:].strip())
        if text:
            bullets.append(text)
        if len(bullets) >= limit:
            break
    return bullets


def bullets_from_matching_headings(markdown: str, heading_patterns: list[str], limit: int = 6) -> list[str]:
    bullets: list[str] = []
    headings = re.findall(r"^## (.+?)\s*$", markdown, flags=re.MULTILINE)
    for heading in headings:
        lowered = heading.lower()
        if not any(re.search(pattern, lowered) for pattern in heading_patterns):
            continue
        bullets.extend(bullets_from_section(extract_section(markdown, heading), limit=limit))
        if len(bullets) >= limit:
            break
    return bullets[:limit]


def quarter_like_bullets(bullets: list[str], limit: int = 6) -> list[str]:
    matches = [
        bullet
        for bullet in bullets
        if re.search(r"(?<![a-z0-9])q[1-4](?![a-z0-9])|quarter|fy20\d{2}", bullet.lower())
    ]
    return matches[:limit]


def fill_to_minimum(primary: list[str], fallbacks: list[list[str]], minimum: int = 3, limit: int = 6) -> list[str]:
    result = list(primary)
    seen = set(result)
    for fallback in fallbacks:
        for item in fallback:
            if item in seen:
                continue
            result.append(item)
            seen.add(item)
            if len(result) >= limit:
                return result
        if len(result) >= minimum:
            return result
    return result[:limit]


def packet_context(local_artifacts: list[str]) -> dict[str, Any]:
    packet_path = next((path for path in local_artifacts if path.endswith("company-packet.md")), "")
    if not packet_path:
        return {
            "packet_path": "",
            "annual_takeaways": [],
            "quarterly_takeaways": [],
            "signal_takeaways": [],
        }
    markdown = (ROOT / packet_path).read_text(encoding="utf-8", errors="replace")
    annual = []
    for heading in (
        "Annual report takeaways",
        "Annual takeaways from `2025`",
        "Annual report read: FY2025",
        "Fiscal 2025 annual picture",
        "Source-complete operating baseline",
        "Core facts captured",
    ):
        annual.extend(bullets_from_section(extract_section(markdown, heading), limit=6))
        if annual:
            break
    if not annual:
        annual = bullets_from_matching_headings(
            markdown,
            [r"annual", r"what the business is", r"source posture"],
            limit=6,
        )
    quarterly = []
    for heading in (
        "Quarter-by-quarter takeaways",
        "Latest three reported quarters as of `2026-08-10`",
        "Reported-period takeaways",
        "Quarter-by-quarter read",
        "Quarter chain",
    ):
        quarterly.extend(bullets_from_section(extract_section(markdown, heading), limit=6))
        if quarterly:
            break
    if not quarterly:
        quarterly = bullets_from_matching_headings(
            markdown,
            [r"^q[1-4]\s+20\d{2}$", r"quarter", r"reported-period"],
            limit=6,
        )
    if not quarterly:
        quarterly = quarter_like_bullets(annual, limit=6)
    signals = bullets_from_section(extract_section(markdown, "Signals to feed into higher-level analysis"), limit=6)
    if not signals:
        for heading in (
            "Consumer, cultural, and societal interpretation",
            "Industrial and operating pressures",
            "Repeated higher-order patterns",
            "Working interpretation",
            "Thematic interpretation",
            "Consumer, cultural, and societal read-through",
            "Repeating cross-company patterns",
            "Frontier interpretation",
            "Lane role and thematic interpretation",
            "Structural themes",
            "What .* adds to the cross-company synthesis",
            "Bigger-picture interpretation",
            "What Adobe adds to the broader technology read",
        ):
            signals.extend(bullets_from_section(extract_section(markdown, heading), limit=3))
            if len(signals) >= 6:
                break
    if not signals:
        signals = bullets_from_matching_headings(
            markdown,
            [r"cross-company", r"bigger-picture", r"interpretation", r"signals?", r"themes?", r"what .* adds"],
            limit=6,
        )
    return {
        "packet_path": packet_path,
        "annual_takeaways": annual,
        "quarterly_takeaways": quarterly,
        "signal_takeaways": signals[:6],
    }


def build_analysis_stack(
    company: dict[str, str],
    detailed: dict[str, Any] | None,
    damodaran_routes: list[dict[str, Any]],
    lyn_routes: list[dict[str, Any]],
    other_routes: list[dict[str, Any]],
    local_artifacts: list[str],
) -> dict[str, Any]:
    packet = packet_context(local_artifacts)
    note = company.get("analyst_notes") or ""
    roster_takeaway = sentence_from_note(note)
    quarter_labels = [
        company.get("latest_quarter_label_1", ""),
        company.get("latest_quarter_label_2", ""),
        company.get("latest_quarter_label_3", ""),
    ]
    fallback_quarters = [
        f"Quarter to verify: {label}"
        for label in quarter_labels
        if label
    ]
    if not fallback_quarters:
        fallback_quarters = ["Quarter window is not labeled in the roster row; verify the latest three reported periods from filings."]
    fallback_signals = [
        f"Sector/industry context to test: {company.get('sector', 'Unknown')} / {company.get('industry', 'Unknown')}.",
        "Use the local filing packet or source ledger to turn this roster-level signal into cited operating evidence.",
        "Do not promote this page from routed analysis to finished memo until the packet-derived evidence is populated.",
    ]
    if detailed:
        operating_model = str(detailed.get("core_answer") or sentence_from_note(note))
        operating_claims = [
            str(item.get("claim"))
            for item in detailed.get("operating_evidence", [])
            if isinstance(item, dict) and item.get("claim")
        ]
        mechanism_reads = [
            f"{item.get('name')}: {item.get('first_principles_read')}"
            for item in detailed.get("mechanisms", [])
            if isinstance(item, dict) and item.get("name") and item.get("first_principles_read")
        ]
        deeper_insights = [str(item) for item in detailed.get("deeper_insights", [])]
        investment_read = detailed.get("investment_read", {})
        if isinstance(investment_read, dict):
            valuation_focus = str(
                investment_read.get("valuation_question")
                or investment_read.get("what_matters")
                or investment_read.get("core_question")
                or "Translate the company story into explicit growth, margin, reinvestment, risk, and terminal assumptions."
            )
        else:
            valuation_focus = str(investment_read or "")
    else:
        operating_claims = []
        mechanism_reads = []
        deeper_insights = []
        packet_signal = packet["signal_takeaways"][0] if packet["signal_takeaways"] else ""
        if not packet_signal and packet["annual_takeaways"]:
            packet_signal = packet["annual_takeaways"][0]
        operating_model = packet_signal or sentence_from_note(note)
        valuation_focus = "Translate the annual-report story into explicit growth, margin, reinvestment, risk, and capital-allocation assumptions before treating the company as attractive or unattractive."

    damodaran_questions = [
        route["description"]
        for route in damodaran_routes[:4]
    ]
    lyn_checks = [
        route["when_to_use"]
        for route in lyn_routes[:3]
    ]
    strategy_checks = [
        route["when_to_use"]
        for route in other_routes[:3]
    ]
    evidence_work = [
        "Read the latest annual report and last three quarterly materials before making a valuation claim.",
        "Extract the exact metric, period, and source path for each business-model or margin claim.",
        "Write the disconfirming test that would weaken the current thesis in the next filing window.",
    ]
    if local_artifacts:
        evidence_work.insert(0, f"Start from {local_artifacts[0]} and reconcile it to the company roster row.")

    annual_specific = [claim for claim in operating_claims if "fy" in claim.lower() or "2025" in claim.lower()]
    quarterly_specific = [
        claim for claim in operating_claims if re.search(r"q[1-4]|quarter|2026", claim.lower())
    ]
    annual_takeaways = fill_to_minimum(
        packet["annual_takeaways"],
        [annual_specific, operating_claims, [roster_takeaway]],
    )
    quarterly_takeaways = fill_to_minimum(
        packet["quarterly_takeaways"],
        [quarterly_specific, fallback_quarters],
    )
    signal_takeaways = fill_to_minimum(
        packet["signal_takeaways"],
        [mechanism_reads, deeper_insights, fallback_signals],
    )

    return {
        "operating_model_read": operating_model,
        "packet_path": packet["packet_path"],
        "annual_report_takeaways": annual_takeaways,
        "quarterly_takeaways": quarterly_takeaways,
        "signal_takeaways": signal_takeaways,
        "valuation_focus": valuation_focus,
        "damodaran_questions": damodaran_questions,
        "lyn_macro_liquidity_checks": lyn_checks,
        "strategy_framework_checks": strategy_checks,
        "next_evidence_work": evidence_work,
    }


def score_keywords(text: str, keywords: list[str]) -> int:
    score = 0
    for keyword in keywords:
        pattern = r"(?<![a-z0-9])" + re.escape(keyword.lower()) + r"(?![a-z0-9])"
        if re.search(pattern, text):
            score += 1
    return score


def route_static_methods(text: str, methods: list[dict[str, Any]], minimum: int = 3) -> list[dict[str, Any]]:
    scored = []
    for method in methods:
        score = score_keywords(text, method["keywords"])
        if score:
            scored.append((score, method))
    scored.sort(key=lambda item: (-item[0], item[1]["id"]))
    routed = [method for _, method in scored]
    if len(routed) < minimum:
        existing = {method["id"] for method in routed}
        for method in methods:
            if method["id"] not in existing:
                routed.append(method)
            if len(routed) >= minimum:
                break
    return routed[:6]


def route_damodaran(company: dict[str, str], detailed: dict[str, Any] | None, library: dict[str, Any]) -> list[dict[str, Any]]:
    text = company_text(company, detailed)
    definitions = library["use_case_definitions"]
    use_case_index = library["use_case_index"]
    methods_by_id = {method["id"]: method for method in library["methods"]}
    routed = []
    for use_case, rule in definitions.items():
        score = score_keywords(text, list(rule["keywords"]))
        if score:
            sample_ids = list(use_case_index.get(use_case, []))[:5]
            routed.append(
                {
                    "use_case": use_case,
                    "score": score,
                    "description": rule["description"],
                    "sample_methods": [
                        {
                            "id": method_id,
                            "title": methods_by_id[method_id]["title"],
                            "course": methods_by_id[method_id]["course"],
                        }
                        for method_id in sample_ids
                        if method_id in methods_by_id
                    ],
                }
            )
    routed.sort(key=lambda item: (-item["score"], item["use_case"]))
    if len(routed) < 5:
        fallback = [
            "separate-value-price-and-story",
            "build-or-audit-dcf",
            "test-growth-reinvestment-and-margins",
            "estimate-risk-and-hurdle-rate",
            "set-corporate-finance-decision-rule",
        ]
        existing = {item["use_case"] for item in routed}
        for use_case in fallback:
            if use_case in existing:
                continue
            sample_ids = list(use_case_index.get(use_case, []))[:5]
            routed.append(
                {
                    "use_case": use_case,
                    "score": 0,
                    "description": definitions[use_case]["description"],
                    "sample_methods": [
                        {
                            "id": method_id,
                            "title": methods_by_id[method_id]["title"],
                            "course": methods_by_id[method_id]["course"],
                        }
                        for method_id in sample_ids
                        if method_id in methods_by_id
                    ],
                }
            )
            if len(routed) >= 5:
                break
    return routed[:8]


def load_detailed_company_analyses() -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    by_slug: dict[str, dict[str, Any]] = {}
    by_ticker: dict[str, dict[str, Any]] = {}
    for path in sorted((ROOT / "analysis" / "company-first-principles").glob("*/*/*/company-analysis.json")):
        data = load_json(path)
        slug = path.parent.name
        data["_source_path"] = str(path.relative_to(ROOT))
        by_slug[slug] = data
        ticker = str(data.get("ticker") or "").upper()
        if ticker:
            by_ticker[ticker] = data
    return by_slug, by_ticker


def build_artifact_index(company_slugs: set[str]) -> dict[str, list[str]]:
    artifacts: dict[str, list[str]] = {slug: [] for slug in company_slugs}
    # A small number of source packets use the issuer's shorter legal or IR
    # directory name rather than the normalized roster slug. Keep the mapping
    # explicit so packet discovery is reproducible and does not depend on
    # manually editing generated registry files.
    aliases = {
        "astrana-health-inc": "astrana-health",
        "the-tjx-companies-inc": "tjx-companies-inc",
    }
    roots = [ROOT / "analysis" / "company-first-principles", ROOT / "extracted"]
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if not path.is_file() or path.suffix not in {".md", ".json", ".csv"}:
                continue
            path_text = str(path.relative_to(ROOT))
            for company_slug in company_slugs:
                lookup_slugs = (company_slug, aliases.get(company_slug, ""))
                if any(candidate and candidate in path_text for candidate in lookup_slugs):
                    artifacts[company_slug].append(path_text)
    return {slug: sorted(paths)[:12] for slug, paths in artifacts.items()}


def page_path(company_slug: str) -> Path:
    return OUTPUT_COMPANIES / f"{company_slug}.html"


def data_path(company_slug: str) -> Path:
    return OUTPUT_DATA / f"{company_slug}.json"


def analysis_status(entry: dict[str, Any]) -> str:
    if entry["has_detailed_first_principles_packet"]:
        return "detailed-first-principles"
    if any(path.endswith("company-packet.md") for path in entry["local_artifacts"]):
        return "packet-backed"
    return "roster-workbench"


def company_dataset_entry(entry: dict[str, Any]) -> dict[str, Any]:
    company = entry["company"]
    deep = DEEP_EXEMPLARS.get(company["company_slug"])
    return {
        "company_slug": company["company_slug"],
        "company_name": company["company_name"],
        "ticker": company.get("ticker"),
        "exchange": company.get("exchange"),
        "sector": company.get("sector"),
        "industry": company.get("industry"),
        "coverage_status": company.get("coverage_status"),
        "analysis_status": entry["analysis_status"],
        "deep_exemplar": bool(deep),
        "template_role": deep["template_role"] if deep else "",
        "page": str(page_path(company["company_slug"]).relative_to(ROOT)),
        "data": str(data_path(company["company_slug"]).relative_to(ROOT)),
        "has_detailed_first_principles_packet": entry["has_detailed_first_principles_packet"],
        "local_artifacts": entry["local_artifacts"],
        "analysis_stack": entry["analysis_stack"],
        "damodaran_routes": [
            {
                "use_case": route["use_case"],
                "description": route["description"],
                "sample_methods": route["sample_methods"],
            }
            for route in entry["damodaran_routes"]
        ],
        "lyn_alden_routes": [
            {
                "id": route["id"],
                "title": route["title"],
                "source": route["source"],
                "when_to_use": route["when_to_use"],
            }
            for route in entry["lyn_alden_routes"]
        ],
        "other_framework_routes": [
            {
                "id": route["id"],
                "title": route["title"],
                "when_to_use": route["when_to_use"],
            }
            for route in entry["other_framework_routes"]
        ],
    }


def rel(path: str) -> str:
    return html.escape(path)


def plain_page_text(text: str) -> str:
    replacements = {
        "cash return by store cohort": "profit from each group of stores opened around the same time",
        "mature sales": "sales after a store has been open long enough to settle into normal operations",
        "durable habit": "lasting customer habit",
        "Transactions turn negative again": "Customer visits fall again",
        "transactions turn negative again": "customer visits fall again",
        "comparable sales": "sales at restaurants open long enough to compare with last year",
        "Comparable sales": "Sales at restaurants open long enough to compare with last year",
        "average check": "average spending per order",
        "Average check": "Average spending per order",
        "payback": "time needed to earn back the build cost",
        "Payback": "Time needed to earn back the build cost",
    }
    cleaned = str(text)
    for old, new in replacements.items():
        cleaned = cleaned.replace(old, new)
    return cleaned


def render_simple_markdown(markdown: str) -> str:
    html_parts: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            html_parts.append(f"<p>{html.escape(' '.join(paragraph))}</p>")
            paragraph.clear()

    def flush_list() -> None:
        if list_items:
            html_parts.append("<ul>" + "".join(f"<li>{html.escape(item)}</li>" for item in list_items) + "</ul>")
            list_items.clear()

    for raw_line in markdown.splitlines():
        line = raw_line.strip()
        if not line:
            flush_paragraph()
            flush_list()
            continue
        if line.startswith("# "):
            flush_paragraph()
            flush_list()
            html_parts.append(f"<h2>{html.escape(line[2:].strip())}</h2>")
        elif line.startswith("## "):
            flush_paragraph()
            flush_list()
            html_parts.append(f"<h3>{html.escape(line[3:].strip())}</h3>")
        elif line.startswith("- "):
            flush_paragraph()
            list_items.append(line[2:].strip())
        else:
            paragraph.append(line)
    flush_paragraph()
    flush_list()
    return "\n".join(html_parts)


def deep_memo_html(company_slug: str) -> str:
    path = DEEP_MEMO_ROOT / f"{company_slug}.md"
    if not path.exists():
        return ""
    return render_simple_markdown(path.read_text(encoding="utf-8"))


PLAIN_DAMODARAN_ROUTE_DESCRIPTIONS = {
    "build-or-audit-dcf": "Use this when the story must become a cash estimate: future cash in, future cash out, risk, and long-term value.",
    "choose-investing-philosophy": "Use this to ask whether this kind of company fits the investor's patience, skill, and risk tolerance.",
    "separate-value-price-and-story": "Use this to keep three things separate: what the business may be worth, what the stock costs today, and the story people tell about it.",
    "test-growth-reinvestment-and-margins": "Use this to test whether growth is good growth: more sales, enough profit, and not too much money required to get that growth.",
    "account-for-institutions-trust-and-fit": "Use this when trust, incentives, culture, franchise relationships, or customer habits change the business result.",
    "estimate-risk-and-hurdle-rate": "Use this to ask how uncertain the future cash is and how much return an investor should demand for taking that risk.",
    "evaluate-control-synergy-and-acquisitions": "Use this when ownership changes, deals, or management control could change the cash the business produces.",
    "set-corporate-finance-decision-rule": "Use this to ask whether management is putting money where it can earn more than it costs.",
}

PLAIN_DAMODARAN_ROUTE_TITLES = {
    "build-or-audit-dcf": "Cash-flow valuation",
    "choose-investing-philosophy": "Investor fit",
    "separate-value-price-and-story": "Value, price, and story",
    "test-growth-reinvestment-and-margins": "Growth quality",
    "account-for-institutions-trust-and-fit": "Trust and incentives",
    "estimate-risk-and-hurdle-rate": "Risk and required return",
    "evaluate-control-synergy-and-acquisitions": "Deals and control",
    "set-corporate-finance-decision-rule": "Management money choices",
}

PLAIN_LYN_ROUTE_DESCRIPTIONS = {
    "lyn-fiscal-dominance-and-deficit-liquidity": "Use this to ask whether government spending, interest rates, and household cash conditions affect demand or valuation.",
    "lyn-liquidity-before-solvency": "Use this to ask whether a company can run into cash or funding pressure before long-term accounting value looks broken.",
    "lyn-long-duration-fiat-claim-risk": "Use this when long-term dollar claims can lose value because inflation or rates change.",
    "lyn-energy-and-commodity-underinvestment": "Use this when energy, raw materials, or years of low supply investment change company costs or profits.",
    "lyn-scarce-assets-and-hard-money-portfolio-role": "Use this when the company behaves more like an inflation-protection or scarce-resource holding than a normal operating business.",
    "lyn-reshoring-and-capital-intensity": "Use this when local production, new factories, duplicated supply chains, or heavy physical investment drive results.",
}

PLAIN_LYN_ROUTE_TITLES = {
    "lyn-fiscal-dominance-and-deficit-liquidity": "Government spending, rates, and household cash",
    "lyn-liquidity-before-solvency": "Cash pressure before accounting trouble",
    "lyn-long-duration-fiat-claim-risk": "Inflation and long-term dollar promises",
    "lyn-energy-and-commodity-underinvestment": "Energy and raw-material supply",
    "lyn-scarce-assets-and-hard-money-portfolio-role": "Scarce assets and inflation protection",
    "lyn-reshoring-and-capital-intensity": "Local production and heavy investment",
}


def render_deep_company_page(entry: dict[str, Any], deep: dict[str, Any]) -> str:
    company = entry["company"]
    detailed = entry["detailed_analysis"]
    stack = entry["analysis_stack"]
    evidence = entry["local_artifacts"]
    title = html.escape(company["company_name"])
    subtitle = html.escape(f"{company.get('ticker', '')} / {company.get('sector', '')} / {company.get('industry', '')}")
    paired_slug = deep["paired_slug"]
    paired_name = deep["paired_name"]
    paired_href = f"{paired_slug}.html"
    data_href = html.escape(f"../data/{company['company_slug']}.json")
    source_register = list(detailed.get("source_register", [])) if detailed else []
    operating_evidence = list(detailed.get("operating_evidence", [])) if detailed else []
    mechanisms = list(detailed.get("mechanisms", [])) if detailed else []
    deep_questions = list(detailed.get("deep_questions", [])) if detailed else []
    full_memo_html = deep_memo_html(company["company_slug"])

    def metric_cards(items: list[tuple[str, str]]) -> str:
        return "\n".join(
            '<article class="metric"><span>{}</span><strong>{}</strong></article>'.format(
                html.escape(label),
                html.escape(value),
            )
            for label, value in items
        )

    def lens_cards(items: list[tuple[str, str]]) -> str:
        return "\n".join(
            '<article class="lens"><h3>{}</h3><p>{}</p></article>'.format(
                html.escape(label),
                html.escape(value),
            )
            for label, value in items
        )

    def bullet_list(items: list[str]) -> str:
        return "\n".join(f"<li>{html.escape(item)}</li>" for item in items)

    def approach_finding_cards(items: list[dict[str, str]]) -> str:
        return "\n".join(
            '<article><h3>{}</h3><p><strong>Question this approach asks:</strong> {}</p><p><strong>Evidence used here:</strong> {}</p><p><strong>What it found:</strong> {}</p><p><strong>Why it matters:</strong> {}</p><p><strong>What would change the answer:</strong> {}</p></article>'.format(
                html.escape(item["approach"]),
                html.escape(item["question"]),
                html.escape(item["evidence_used"]),
                html.escape(item["what_was_found"]),
                html.escape(item["why_it_matters"]),
                html.escape(item["what_would_change_the_answer"]),
            )
            for item in items
        )

    mechanism_rows = "\n".join(
        "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            html.escape(plain_page_text(item.get("name", ""))),
            html.escape(plain_page_text(item.get("first_principles_read", ""))),
            html.escape(plain_page_text(item.get("what_to_verify_next", ""))),
        )
        for item in mechanisms[:8]
    )
    evidence_rows = "\n".join(
        "<tr><td>{}</td><td>{}</td><td>{}</td></tr>".format(
            html.escape(plain_page_text(item.get("period", "current packet"))),
            html.escape(plain_page_text(item.get("claim", ""))),
            html.escape("; ".join(item.get("sources", []))),
        )
        for item in operating_evidence[:8]
    )
    question_cards = "\n".join(
        '<article class="question"><h3>{}</h3><p>{}</p><p><strong>Weakens if:</strong> {}</p></article>'.format(
            html.escape(plain_page_text(item.get("question", ""))),
            html.escape(plain_page_text(item.get("working_answer", item.get("why_it_matters", "")))),
            html.escape(plain_page_text(item.get("what_would_weaken_it", ""))),
        )
        for item in deep_questions[:6]
    )
    source_items = "\n".join(
        f"<li><code>{html.escape(path)}</code></li>"
        for path in (source_register or evidence)[:14]
    )
    damodaran_items = "\n".join(
        "<li><strong>{}</strong><span>{}</span></li>".format(
            html.escape(PLAIN_DAMODARAN_ROUTE_TITLES.get(route["use_case"], route["use_case"])),
            html.escape(PLAIN_DAMODARAN_ROUTE_DESCRIPTIONS.get(route["use_case"], route["description"])),
        )
        for route in entry["damodaran_routes"][:6]
    )
    lyn_items = "\n".join(
        '<li><strong>{}</strong><span>{}</span><small><a href="{}">source</a></small></li>'.format(
            html.escape(PLAIN_LYN_ROUTE_TITLES.get(route["id"], route["title"])),
            html.escape(PLAIN_LYN_ROUTE_DESCRIPTIONS.get(route["id"], route["when_to_use"])),
            html.escape(route["source"]),
        )
        for route in entry["lyn_alden_routes"][:4]
    )
    thesis = str(detailed.get("core_answer", ""))
    operating_model = stack["operating_model_read"]
    operating_model_paragraph = (
        f"\n      <p>{html.escape(operating_model)}</p>"
        if operating_model and operating_model != thesis
        else ""
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} Deep Cross-Framework Analysis</title>
  <link rel="stylesheet" href="../cross-framework.css">
</head>
<body class="deep-page">
<main>
  <nav><a href="../index.html">Cross-Framework Companies</a></nav>
  <header class="deep-hero">
    <div>
      <p class="eyebrow">Deep exemplar · {html.escape(deep["template_role"])}</p>
      <h1>{title}</h1>
      <p class="subtitle">{subtitle}</p>
      <p class="result-line">{html.escape(deep["analysis_result"])}</p>
      <p>{html.escape(deep["one_line_thesis"])}</p>
    </div>
    <aside class="verdict">
      <span>Investor Conclusion</span>
      <p>{html.escape(deep["investment_posture"])}</p>
      <a href="{data_href}">Machine-readable JSON</a>
      <a href="{html.escape(paired_href)}">Compare with {html.escape(paired_name)}</a>
    </aside>
  </header>

  <section class="metric-strip" aria-label="Key company metrics">
    {metric_cards(deep["key_metrics"])}
  </section>

  <section class="results-panel">
    <h2>Analysis Results</h2>
    <p class="verdict-line">{html.escape(deep["result_verdict"])}</p>
    <p>{html.escape(deep["result_read"])}</p>
    <div class="result-grid">
      <article>
        <h3>What Must Be True</h3>
        <ul>{bullet_list(deep["what_must_be_true"])}</ul>
      </article>
      <article>
        <h3>Evidence Basis</h3>
        <ul>{bullet_list(deep["evidence_basis"])}</ul>
      </article>
    </div>
  </section>

  <section class="full-memo">
    <h2>Full Analysis Memo</h2>
    {full_memo_html or '<p>No full memo source has been written yet.</p>'}
  </section>

  <section class="memo-section">
    <h2>Plain-English Investment Memo</h2>
    <div class="memo-body">
      {"".join(f"<p>{html.escape(item)}</p>" for item in deep["plain_memo"])}
    </div>
  </section>

  <section>
    <h2>First-Principles Explanation</h2>
    <div class="walkthrough">
      {"".join(f"<article><p>{html.escape(item)}</p></article>" for item in deep["plain_english_walkthrough"])}
    </div>
  </section>

  <section>
    <h2>What The Numbers Mean</h2>
    <div class="explanation-list">
      {"".join(f"<article><p>{html.escape(item)}</p></article>" for item in deep["number_interpretation"])}
    </div>
  </section>

  <section>
    <h2>Plain-Language Definitions</h2>
    <div class="glossary-grid">
      {"".join(f"<article><h3>{html.escape(term)}</h3><p>{html.escape(definition)}</p></article>" for term, definition in deep["reader_glossary"])}
    </div>
  </section>

  <section>
    <h2>Approach Used, What It Found, And Why It Matters</h2>
    <div class="approach-grid">
      {approach_finding_cards(deep["approach_findings"])}
    </div>
  </section>

  <section class="split">
    <article>
      <h2>Company Conclusion</h2>
      <p>{html.escape(deep["company_conclusion"])}</p>
    </article>
    <article>
      <h2>What The Market Could Be Missing</h2>
      <ul>{bullet_list(deep["mispricing_questions"])}</ul>
    </article>
  </section>

  <section>
    <h2>Framework Lenses</h2>
    <div class="lens-grid">{lens_cards(deep["framework_lenses"])}</div>
  </section>

  <section>
    <h2>Method Routing</h2>
    <div class="route-grid">
      <div>
        <h3>Damodaran Questions</h3>
        <ul class="method-list compact">{damodaran_items}</ul>
      </div>
      <div>
        <h3>Lyn Alden Checks</h3>
        <ul class="method-list compact">{lyn_items}</ul>
      </div>
    </div>
  </section>

  <section>
    <h2>Annual And Quarter Evidence</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Period</th><th>Claim</th><th>Local source</th></tr></thead>
        <tbody>{evidence_rows}</tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>Business Model Mechanisms</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>Mechanism</th><th>First-principles read</th><th>Next verification</th></tr></thead>
        <tbody>{mechanism_rows}</tbody>
      </table>
    </div>
  </section>

  <section>
    <h2>What Would Prove This Wrong</h2>
    <ul class="check-list">{bullet_list(deep["disconfirming_tests"])}</ul>
  </section>

  <section>
    <h2>Deep Questions</h2>
    <div class="question-grid">{question_cards}</div>
  </section>

  <section class="split">
    <article>
      <h2>Next Filing Watchlist</h2>
      <ul>{bullet_list(deep["watchlist"])}</ul>
    </article>
    <article>
      <h2>Comparison Bridge</h2>
      <p>{html.escape(deep["comparison_bridge"])}</p>
    </article>
  </section>

  <section>
    <h2>Source Register</h2>
    <ul class="source-list">{source_items}</ul>
  </section>
</main>
</body>
</html>
"""


def render_company_page(entry: dict[str, Any]) -> str:
    company = entry["company"]
    deep = DEEP_EXEMPLARS.get(company["company_slug"])
    if deep and entry.get("detailed_analysis"):
        return render_deep_company_page(entry, deep)
    detailed = entry.get("detailed_analysis")
    evidence = entry["local_artifacts"]
    damodaran = entry["damodaran_routes"]
    lyn = entry["lyn_alden_routes"]
    other = entry["other_framework_routes"]
    stack = entry["analysis_stack"]
    title = html.escape(company["company_name"])
    subtitle = html.escape(f"{company.get('ticker', '')} / {company.get('sector', '')} / {company.get('industry', '')}")
    status = html.escape(entry["analysis_status"])
    data_href = html.escape(f"../data/{company['company_slug']}.json")
    notes = html.escape(company.get("analyst_notes") or "No analyst note in roster.")
    core_answer = html.escape(str(detailed.get("core_answer", ""))) if detailed else ""
    primary_question = html.escape(str(detailed.get("primary_question", ""))) if detailed else ""

    def link_list(paths: list[str]) -> str:
        if not paths:
            return "<li>No richer local company artifact found yet; start from the roster row and filing packet.</li>"
        return "\n".join(f'<li><code>{rel(path)}</code></li>' for path in paths)

    damodaran_html = "\n".join(
        "<li><strong>{}</strong><span>{}</span><small>{}</small></li>".format(
            html.escape(route["use_case"]),
            html.escape(route["description"]),
            html.escape(", ".join(method["title"] for method in route["sample_methods"][:3])),
        )
        for route in damodaran
    )
    lyn_html = "\n".join(
        '<li><strong>{}</strong><span>{}</span><small><a href="{}">source</a></small></li>'.format(
            html.escape(method["title"]),
            html.escape(method["when_to_use"]),
            html.escape(method["source"]),
        )
        for method in lyn
    )
    other_html = "\n".join(
        "<li><strong>{}</strong><span>{}</span></li>".format(
            html.escape(method["title"]),
            html.escape(method["when_to_use"]),
        )
        for method in other
    )
    stack_html = """
  <section>
    <h2>Analysis Stack</h2>
    <h3>Business Model Read</h3>
    <p>{operating_model}</p>
    <h3>Annual Report Takeaways</h3>
    <ul>{annual_takeaways}</ul>
    <h3>Latest Quarter Chain</h3>
    <ul>{quarterly_takeaways}</ul>
    <h3>Signal Map</h3>
    <ul>{signal_takeaways}</ul>
    <h3>Valuation Focus</h3>
    <p>{valuation_focus}</p>
    <h3>Damodaran Questions To Answer</h3>
    <ul>{damodaran_questions}</ul>
    <h3>Lyn Alden Macro/Liquidity Checks</h3>
    <ul>{lyn_checks}</ul>
    <h3>Other Strategy Checks</h3>
    <ul>{strategy_checks}</ul>
    <h3>Next Evidence Work</h3>
    <ul>{evidence_work}</ul>
  </section>
""".format(
        operating_model=html.escape(stack["operating_model_read"]),
        annual_takeaways="\n".join(f"<li>{html.escape(item)}</li>" for item in stack["annual_report_takeaways"]) or "<li>No parsed company-packet annual takeaways yet.</li>",
        quarterly_takeaways="\n".join(f"<li>{html.escape(item)}</li>" for item in stack["quarterly_takeaways"]) or "<li>No parsed company-packet quarter-chain takeaways yet.</li>",
        signal_takeaways="\n".join(f"<li>{html.escape(item)}</li>" for item in stack["signal_takeaways"]) or "<li>No parsed company-packet signal map yet.</li>",
        valuation_focus=html.escape(stack["valuation_focus"]),
        damodaran_questions="\n".join(f"<li>{html.escape(item)}</li>" for item in stack["damodaran_questions"]),
        lyn_checks="\n".join(f"<li>{html.escape(item)}</li>" for item in stack["lyn_macro_liquidity_checks"]),
        strategy_checks="\n".join(f"<li>{html.escape(item)}</li>" for item in stack["strategy_framework_checks"]),
        evidence_work="\n".join(f"<li>{html.escape(item)}</li>" for item in stack["next_evidence_work"]),
    )

    detailed_block = ""
    if detailed:
        mechanisms = detailed.get("mechanisms", [])[:5]
        mechanism_items = "\n".join(
            f"<li><strong>{html.escape(str(item.get('name', 'Mechanism')))}</strong><span>{html.escape(str(item.get('first_principles_read', '')))}</span></li>"
            for item in mechanisms
        )
        detailed_block = f"""
        <section>
          <h2>Existing First-Principles Packet</h2>
          <p><strong>Question:</strong> {primary_question}</p>
          <p><strong>Core answer:</strong> {core_answer}</p>
          <ul class="method-list">{mechanism_items}</ul>
        </section>
        """

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} Cross-Framework Analysis</title>
  <link rel="stylesheet" href="../cross-framework.css">
</head>
<body>
<main>
  <nav><a href="../index.html">Cross-Framework Companies</a></nav>
  <header>
    <h1>{title}</h1>
    <p>{subtitle}</p>
    <p><strong>Status:</strong> {status} · <a href="{data_href}">machine-readable analysis JSON</a></p>
  </header>
  <section>
    <h2>Annual-Report Starting Point</h2>
    <p>{notes}</p>
  </section>
  {detailed_block}
  {stack_html}
  <section>
    <h2>Damodaran Routes</h2>
    <ul class="method-list">{damodaran_html}</ul>
  </section>
  <section>
    <h2>Lyn Alden Routes</h2>
    <ul class="method-list">{lyn_html}</ul>
  </section>
  <section>
    <h2>Other Investor/Strategy Routes</h2>
    <ul class="method-list">{other_html}</ul>
  </section>
  <section>
    <h2>Local Evidence</h2>
    <ul>{link_list(evidence)}</ul>
  </section>
  <section>
    <h2>Thesis Workbench</h2>
    <p>Use the routed methods above to convert filing evidence into explicit claims about business model, economic engine, capital burden, valuation drivers, macro sensitivity, and what would prove the thesis wrong.</p>
  </section>
</main>
</body>
</html>
"""


def render_index(entries: list[dict[str, Any]], registry: dict[str, Any]) -> str:
    by_sector: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        by_sector[entry["company"].get("sector", "Unknown")].append(entry)
    exemplar_links = "\n".join(
        '<a class="exemplar-card" href="companies/{slug}.html"><strong>{name}</strong><span>{role}</span><small>{thesis}</small></a>'.format(
            slug=html.escape(entry["company"]["company_slug"]),
            name=html.escape(entry["company"]["company_name"]),
            role=html.escape(DEEP_EXEMPLARS[entry["company"]["company_slug"]]["template_role"]),
            thesis=html.escape(DEEP_EXEMPLARS[entry["company"]["company_slug"]]["one_line_thesis"]),
        )
        for entry in entries
        if entry["company"]["company_slug"] in DEEP_EXEMPLARS
    )
    cards = []
    for sector, sector_entries in sorted(by_sector.items()):
        links = "\n".join(
            '<a href="companies/{slug}.html"><strong>{name}</strong><span>{ticker} / {industry}</span></a>'.format(
                slug=html.escape(entry["company"]["company_slug"]),
                name=html.escape(entry["company"]["company_name"]),
                ticker=html.escape(entry["company"].get("ticker", "")),
                industry=html.escape(entry["company"].get("industry", "")),
            )
            for entry in sector_entries
        )
        cards.append(f"<section><h2>{html.escape(sector)}</h2><div class=\"grid\">{links}</div></section>")
    counts = registry["counts"]
    reader_company_count = len(list((ROOT / "analysis" / "deep-company-pages").glob("*.md")))
    reader_explanation_count = len(list((ROOT / "analysis" / "first-principles").glob("*.md")))
    reader_comparison_count = len(list((ROOT / "analysis" / "cross-sector").glob("*.md")))
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Cross-Framework Company Analysis</title>
  <link rel="stylesheet" href="cross-framework.css">
</head>
<body>
<main>
  <header>
    <h1>Cross-Framework Company Analysis</h1>
    <p>{counts['companies']} company pages routed through annual-report evidence, Damodaran methods, Lyn Alden macro/liquidity methods, and other investor/strategy frameworks.</p>
    <p>{counts['detailed_first_principles_packets']} detailed first-principles pages, {counts['packet_backed_pages']} packet-backed pages, and {counts['roster_workbench_pages']} roster-workbench pages.</p>
    <p><strong>Use the <a href="/">main research reader</a> for the editorial deep layer:</strong> it contains {reader_company_count} company studies, {reader_explanation_count} first-principles explanations, {reader_comparison_count} cross-company comparisons, source trails, and unresolved questions. This index is the broader framework map; a packet-backed page is a useful starting point, not a claim that every page has the same depth.</p>
  </header>
  <section class="exemplar-band">
    <h2>Finished Exemplar Pages</h2>
    <p>These pages define the end-to-end template before scaling the same UX and proof burden across the rest of the company roster.</p>
    <div class="exemplar-grid">{exemplar_links}</div>
  </section>
  {''.join(cards)}
</main>
</body>
</html>
"""


def write_report(registry: dict[str, Any]) -> None:
    counts = registry["counts"]
    companies = registry["companies"]
    status_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    sector_groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for company in companies:
        status_groups[company["analysis_status"]].append(company)
        sector_groups[str(company.get("sector") or "Unknown")].append(company)

    lines = [
        "# Cross-Framework Company Method Report",
        "",
        f"Updated on: {registry['updated_on']}",
        "",
        "## Summary",
        "",
        f"- Source roster rows: {counts['source_roster_rows']}",
        f"- Unique company pages: {counts['companies']}",
        f"- Company data files: {counts['company_data_files']}",
        f"- Deep exemplar pages: {counts['deep_exemplar_pages']}",
        f"- Detailed first-principles pages: {counts['detailed_first_principles_pages']}",
        f"- Packet-backed pages: {counts['packet_backed_pages']}",
        f"- Roster-workbench pages: {counts['roster_workbench_pages']}",
        f"- Damodaran use cases: {counts['damodaran_use_cases']}",
        f"- Lyn Alden methods: {counts['lyn_alden_methods']}",
        f"- Other framework methods: {counts['other_framework_methods']}",
        "",
        "## Method Sources",
        "",
        f"- Damodaran method library: `{registry['damodaran_method_library']}`",
    ]
    for url in registry["lyn_alden_source_urls"]:
        lines.append(f"- Lyn Alden source: {url}")

    lines.extend(["", "## Status Tiers", ""])
    for status in ("detailed-first-principles", "packet-backed", "roster-workbench"):
        lines.append(f"### `{status}`")
        lines.append("")
        for company in status_groups.get(status, [])[:20]:
            lines.append(
                f"- `{company['company_slug']}`: {company['company_name']} "
                f"({company.get('ticker') or 'no ticker'})"
            )
        remaining = len(status_groups.get(status, [])) - 20
        if remaining > 0:
            lines.append(f"- ...and {remaining} more")
        if not status_groups.get(status):
            lines.append("- none")
        lines.append("")

    lines.extend(["## Sector Coverage", ""])
    for sector, sector_companies in sorted(sector_groups.items()):
        lines.append(f"- {sector}: {len(sector_companies)} companies")

    lines.extend(
        [
        "",
        "## Deep Exemplar Standard",
        "",
        "The first finished pair is McDonald's and Chipotle. These pages set the repeatable UX and analysis template for the rest of the roster:",
        "",
        "- clear company conclusion and investor conclusion",
        "- framework-specific method routing",
        "- annual and quarterly evidence table",
        "- business-model mechanism table",
        "- explicit thesis breakers",
        "- next filing watchlist",
        "- peer comparison bridge",
        "",
        "## Release Gate",
            "",
            "Run:",
            "",
            "```bash",
            "python3 scripts/build-cross-framework-company-pages.py",
            "python3 scripts/verify-cross-framework-company-pages.py",
            "```",
            "",
            "The verifier checks registry/page/data parity, framework route coverage,",
            "status-tier validity, and packet-derived annual/quarter/signal content",
            "where local company packets exist.",
            "",
        ]
    )
    REPORT_MD.write_text("\n".join(lines), encoding="utf-8")


def write_css() -> None:
    css = """
:root { color-scheme: light; --ink: #202426; --muted: #5c6569; --line: #d7ddd9; --paper: #f6f4ee; --panel: #ffffff; --accent: #24616a; --accent-2: #8a4f2a; --good: #2f6d4f; --warn: #9b6b20; }
* { box-sizing: border-box; }
body { margin: 0; background: var(--paper); color: var(--ink); font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
main { max-width: 1120px; margin: 0 auto; padding: 32px 20px 54px; }
nav { margin-bottom: 22px; }
nav a { color: var(--accent); font-weight: 700; text-decoration: none; }
header { border-bottom: 1px solid var(--line); padding-bottom: 22px; margin-bottom: 22px; }
h1 { font-size: clamp(30px, 4vw, 48px); line-height: 1.04; margin: 0 0 10px; letter-spacing: 0; }
h2 { font-size: 22px; margin: 28px 0 12px; letter-spacing: 0; }
h3 { font-size: 16px; margin: 18px 0 8px; letter-spacing: 0; }
p { color: var(--muted); line-height: 1.6; }
a { color: var(--accent); }
code { white-space: normal; overflow-wrap: anywhere; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 10px; }
.grid a { display: block; padding: 13px 14px; border: 1px solid var(--line); border-radius: 8px; background: var(--panel); color: var(--ink); text-decoration: none; min-height: 82px; }
.grid span, .method-list span, small { display: block; color: var(--muted); font-weight: 400; margin-top: 5px; line-height: 1.45; }
.method-list { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 12px; padding: 0; list-style: none; }
.method-list li { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 14px; }
.method-list.compact { grid-template-columns: 1fr; }
li { line-height: 1.5; margin-bottom: 7px; }
section { margin-bottom: 18px; }
.exemplar-band { border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); padding: 18px 0 24px; }
.exemplar-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 12px; }
.exemplar-card { display: block; min-height: 150px; padding: 16px; border: 1px solid var(--line); border-left: 5px solid var(--accent-2); border-radius: 8px; background: var(--panel); color: var(--ink); text-decoration: none; }
.exemplar-card span, .exemplar-card small { display: block; margin-top: 8px; color: var(--muted); line-height: 1.45; }
.deep-page main { max-width: 1180px; }
.deep-hero { display: grid; grid-template-columns: minmax(0, 1fr) 340px; gap: 24px; align-items: stretch; }
.eyebrow { margin: 0 0 8px; color: var(--accent-2); font-size: 13px; font-weight: 800; text-transform: uppercase; }
.subtitle { color: var(--ink); font-weight: 700; }
.result-line { color: var(--ink); font-size: 20px; font-weight: 800; line-height: 1.45; }
.verdict { border: 1px solid var(--line); border-radius: 8px; background: var(--panel); padding: 18px; }
.verdict span { display: block; color: var(--accent-2); font-size: 13px; font-weight: 800; text-transform: uppercase; }
.verdict a { display: block; margin-top: 10px; font-weight: 800; text-decoration: none; }
.metric-strip { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 10px; }
.metric, .lens, .question, .split > article { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 15px; }
.metric span { display: block; color: var(--accent); font-size: 12px; font-weight: 800; text-transform: uppercase; }
.metric strong { display: block; margin-top: 8px; line-height: 1.35; }
.results-panel { border: 2px solid var(--accent); border-radius: 8px; background: #ffffff; padding: 18px; }
.results-panel h2 { margin-top: 0; }
.verdict-line { color: var(--ink); font-size: 18px; font-weight: 800; }
.result-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; margin-top: 10px; }
.result-grid article { border-top: 1px solid var(--line); padding-top: 10px; }
.full-memo { background: #ffffff; border: 1px solid var(--line); border-radius: 8px; padding: 22px; }
.full-memo > h2 { margin-top: 0; }
.full-memo h2:not(:first-child), .full-memo h3 { margin-top: 24px; }
.full-memo p, .full-memo li { color: var(--ink); font-size: 17px; line-height: 1.72; }
.full-memo ul { padding-left: 24px; }
.memo-section { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 20px; }
.memo-section h2 { margin-top: 0; }
.memo-body { max-width: 880px; }
.memo-body p { color: var(--ink); font-size: 18px; line-height: 1.72; margin: 0 0 16px; }
.memo-body p:last-child { margin-bottom: 0; }
.walkthrough { display: grid; gap: 12px; }
.walkthrough article { background: #fbfbf8; border: 1px solid var(--line); border-radius: 8px; padding: 16px; }
.walkthrough p { margin: 0; color: var(--ink); font-size: 17px; line-height: 1.7; }
.explanation-list { display: grid; gap: 10px; }
.explanation-list article { background: var(--panel); border-left: 4px solid var(--accent); border-radius: 8px; padding: 12px 14px; }
.explanation-list p { margin: 0; color: var(--ink); }
.approach-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.approach-grid article { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 15px; }
.approach-grid h3 { margin-top: 0; color: var(--accent); }
.approach-grid p { color: var(--ink); }
.glossary-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 10px; }
.glossary-grid article { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 13px; }
.glossary-grid h3 { margin-top: 0; color: var(--accent); }
.glossary-grid p { margin-bottom: 0; }
.split { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }
.lens-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.lens h3, .question h3 { margin-top: 0; }
.route-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px; }
.table-wrap { overflow-x: auto; border: 1px solid var(--line); border-radius: 8px; background: var(--panel); }
table { width: 100%; border-collapse: collapse; min-width: 760px; }
th, td { padding: 12px; border-bottom: 1px solid var(--line); text-align: left; vertical-align: top; line-height: 1.45; }
th { background: #eef2ef; color: var(--ink); font-size: 13px; }
td { color: var(--muted); }
.check-list, .source-list { background: var(--panel); border: 1px solid var(--line); border-radius: 8px; padding: 16px 16px 16px 34px; }
.check-list li::marker { color: var(--warn); }
.question-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
@media (max-width: 860px) {
  .deep-hero, .split, .route-grid, .result-grid, .approach-grid { grid-template-columns: 1fr; }
  .metric-strip, .lens-grid, .question-grid, .glossary-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}
@media (max-width: 560px) {
  main { padding: 24px 14px 42px; }
  .metric-strip, .lens-grid, .question-grid, .glossary-grid { grid-template-columns: 1fr; }
}
"""
    (OUTPUT_ROOT / "cross-framework.css").write_text(css.strip() + "\n", encoding="utf-8")


def build() -> dict[str, Any]:
    source_row_count = source_roster_row_count()
    companies = read_companies()
    damodaran_library = load_damodaran_library()
    detailed_by_slug, detailed_by_ticker = load_detailed_company_analyses()
    roster_slugs = {company["company_slug"] for company in companies}
    for slug, detailed in sorted(detailed_by_slug.items()):
        if slug in roster_slugs:
            continue
        companies.append(
            {
                "company_slug": slug,
                "company_name": str(detailed.get("company") or slug.replace("-", " ").title()),
                "ticker": str(detailed.get("ticker") or ""),
                "exchange": "",
                "sector": "Services",
                "industry": "Restaurants",
                "fiscal_year_end": "",
                "annualreports_url": "",
                "ir_url": "",
                "sec_cik": "",
                "target_annual_year": "",
                "latest_quarter_label_1": "",
                "latest_quarter_label_2": "",
                "latest_quarter_label_3": "",
                "coverage_status": "detailed-first-principles-only",
                "analyst_notes": str(detailed.get("core_answer") or ""),
            }
        )
    artifact_index = build_artifact_index({company["company_slug"] for company in companies})
    OUTPUT_COMPANIES.mkdir(parents=True, exist_ok=True)
    OUTPUT_DATA.mkdir(parents=True, exist_ok=True)

    entries = []
    for company in companies:
        company_slug = company["company_slug"]
        detailed = detailed_by_slug.get(company_slug) or detailed_by_ticker.get(
            str(company.get("ticker") or "").upper()
        )
        text = company_text(company, detailed)
        entry = {
            "company": company,
            "has_detailed_first_principles_packet": detailed is not None,
            "detailed_analysis": detailed,
            "local_artifacts": artifact_index.get(company_slug, []),
            "damodaran_routes": route_damodaran(company, detailed, damodaran_library),
            "lyn_alden_routes": route_static_methods(text, LYN_ALDEN_METHODS),
            "other_framework_routes": route_static_methods(text, OTHER_METHODS),
        }
        entry["analysis_stack"] = build_analysis_stack(
            company,
            detailed,
            entry["damodaran_routes"],
            entry["lyn_alden_routes"],
            entry["other_framework_routes"],
            entry["local_artifacts"],
        )
        entry["analysis_status"] = analysis_status(entry)
        (page_path(company_slug)).write_text(render_company_page(entry), encoding="utf-8")
        write_json(data_path(company_slug), company_dataset_entry(entry))
        entries.append(entry)

    status_counts: dict[str, int] = defaultdict(int)
    for entry in entries:
        status_counts[entry["analysis_status"]] += 1

    registry = {
        "workspace": "annual-report-research",
        "updated_on": date.today().isoformat(),
        "description": "Cross-framework company routing layer over the annual-report company roster.",
        "damodaran_method_library": str(DAMODARAN_LIBRARY),
        "lyn_alden_source_urls": sorted({method["source"] for method in LYN_ALDEN_METHODS}),
        "counts": {
            "source_roster_rows": source_row_count,
            "companies": len(entries),
            "detailed_first_principles_packets": sum(
                1 for entry in entries if entry["has_detailed_first_principles_packet"]
            ),
            "damodaran_use_cases": len(damodaran_library["use_case_definitions"]),
            "lyn_alden_methods": len(LYN_ALDEN_METHODS),
            "other_framework_methods": len(OTHER_METHODS),
            "company_pages": len(list(OUTPUT_COMPANIES.glob("*.html"))),
            "company_data_files": len(list(OUTPUT_DATA.glob("*.json"))),
            "detailed_first_principles_pages": status_counts["detailed-first-principles"],
            "packet_backed_pages": status_counts["packet-backed"],
            "roster_workbench_pages": status_counts["roster-workbench"],
            "deep_exemplar_pages": sum(1 for entry in entries if entry["company"]["company_slug"] in DEEP_EXEMPLARS),
        },
        "companies": [company_dataset_entry(entry) for entry in entries],
    }
    write_css()
    (OUTPUT_ROOT / "index.html").write_text(render_index(entries, registry), encoding="utf-8")
    write_json(REGISTRY_JSON, registry)
    write_report(registry)
    return registry


def main() -> None:
    registry = build()
    counts = registry["counts"]
    print(
        "Cross-framework company pages built:",
        f"{counts['companies']} companies,",
        f"{counts['detailed_first_principles_packets']} detailed packets,",
        f"{counts['company_pages']} pages",
    )


if __name__ == "__main__":
    main()
