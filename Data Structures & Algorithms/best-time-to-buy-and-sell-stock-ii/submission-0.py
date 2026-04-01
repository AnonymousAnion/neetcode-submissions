class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        prev_price = prices[0]

        for i, price in enumerate(prices, start = 1):

            profit = price - prev_price

            if profit > 0:

                max_profit += profit

            prev_price = price

        return max_profit