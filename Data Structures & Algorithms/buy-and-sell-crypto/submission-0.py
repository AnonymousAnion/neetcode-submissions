class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        minimum = prices[0]

        for i in range(1, len(prices)):

            price = prices[i]
            max_profit = max(max_profit, price - minimum)
            minimum = min(minimum, price)

        return max_profit