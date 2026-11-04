# Nine method errors I found in my own research

For months I designed a system to invest in Bitcoin and altcoins by cycles. It had documents, frozen parameters and
results that looked solid. Then I audited it from scratch and found nine method errors. None was a calculation mistake:
they were design errors, the kind you cannot see by looking at the numbers.

I am writing them down because **the pattern matters more than the figures.** If you research your own strategies, you are
likely to make some of them.

## 1. Testing only with survivors

My portfolio tests used 24 hand-picked coins. All 24 still trade today. In the 2022-2024 cycle there were actually 364
eligible coins, and 54% of them no longer exist.

**Lesson:** ask what you could buy on that date, not what exists today.

## 2. Mistaking the edge of the search for the optimum

I optimised Bitcoin's weight over a grid of values. The best one landed at the end of the grid. When I extended the grid,
the optimum moved to the new end.

**Lesson:** a maximum at the edge of the grid is not a maximum; it is where the search stopped.

## 3. Reading "there was no data" as "the filter protected me"

In one test, the system invested nothing in 2018-2020 and it looked as if its entry filter had protected it. In fact, the
indicator I had modelled **did not exist yet** on those dates.

**Lesson:** before celebrating that a rule "stayed out", check that it had something to decide with.

## 4. Selling at the top… knowing where the top was

The system's historical exit started selling exactly at the highs of each cycle: dates you only know afterwards. The
curious part is that **knowing the top made the result worse** (it returned between 0.775 and 0.944 times what it did
without that advantage), because the rule sold very little at first and almost everything once the price had already
collapsed.

**Lesson:** look for future dates hidden in the parameters, not only in the code.

## 5. Modelling the wrong rule

In my first reconstruction of the entry filter I used a 200-week average. The real rule used a different combination of
indicators. With the wrong one, I concluded that only one cycle could be evaluated; with the right one, all three could.

**Lesson:** when you rebuild a system, go to the frozen code, not to your memory of how it worked.

## 6. A "buy and hold" that bought at the bottom

The passive benchmark started on dates chosen after the fact: **five of the six start dates were bottoms identified
later**. The worst, the bottom of the March 2020 crash, returns almost +1,000% over the following year.

When I repeated the comparison with 63 monthly start dates chosen by nobody, the conclusion reversed.

**Lesson:** the benchmark can cheat too.

## 7. A null result on a contaminated design

A risk-management component seemed to add nothing when the cycles started at bottoms. With arbitrary start dates, it
added value in all nine combinations tested. The data was the same; what changed was where I started looking.

**Lesson:** a "does not work" obtained with a flawed design is not a "does not work". Redo it before throwing the idea away.

## 8. Explaining before measuring

I blamed a strategy's drop on its correlation filters. When I removed them one at a time, those filters turned out to be
**exactly inert**: the result did not change at all. Another piece was to blame.

**Lesson:** a plausible explanation is not an attribution. Only removing the pieces one at a time (ablation) attributes.

## 9. A rule that "won" because it avoided another rule of mine

The same risk rule from point 7 seemed to add +20% to returns. With the system's own emergency exit switched off, its
effect became **−2.3%**. It did not create value: it prevented another rule of mine from firing, one that, once triggered,
left the portfolio in cash forever (and fired in a third of the three-year windows in Bitcoin's history).

**Lesson:** when one rule improves the result a lot, check that it is not covering up a defect in another.

## What changed afterwards

These errors were not exotic. They share one thing: **in every case, a property of the way I tested was read as a property
of the market.** Since then:

- I test on universes as they existed on each date;
- I write the rules and the success criterion before looking at the result;
- I always compare with a starting point nobody chose;
- and I separate what is documented from what is validated. That something is written in my documents does not mean it is
  proven.

*Héctor Sandoval · BICAPITAL Research*

---

*Educational and research content. Not investment advice or a personalised recommendation. Audit of my own research on
historical Bitcoin and altcoin data. The author invests personal capital in cryptocurrencies.*
