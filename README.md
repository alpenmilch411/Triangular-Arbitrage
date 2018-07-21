# Triangular arbitrage
Explore whether there are profit opportunities through triangular/cross-rate arbitrage on cryptoexchanges.

## Triangular Arbitrage Definition
This type of arbitrage is a riskless profit that occurs when a quoted exchange rate does not equal the market's cross-exchange rate. It exploits an inefficiency in the market where one market is overvalued and another is undervalued. 

## Preliminary results
The following graph plots the expected profit over time of buy_cross_sell_quote & buy_quote_sell_cross processes on the coinbase pro platform. Taker fee thresholds: Tier 1 = 0.1 %, Tier 2 = 0.2 %, Tier 3 = 0.3%

![alt text](https://github.com/alpenmilch411/Triangular-Arbitrage/blob/master/triangular_profits.png)

Insight:
- Ignoring fees, there are profit opportunities
- Including fee strucures, the profit opportunities are significantly reduced.
- In the observed timeframe tier 3 (0.3% fee per trade) traders were not able to profit trough triangular arbitrage

-> For the average trader triangular arbitrage is not possible, unless average 30-day trading volume is increased in order to benefit from better fee terms.

TODO:
- Add further exchanges, NEXT: Bitfinex, HitBTC
- If profits are possible, implement automatic trading code
- API Call Rate Limits: Find way to increase API calls
- Improve cross rate computation process in order to handle exchanges with higher number of currency pairs/base currencies dynamically (thether, btc, etc)
