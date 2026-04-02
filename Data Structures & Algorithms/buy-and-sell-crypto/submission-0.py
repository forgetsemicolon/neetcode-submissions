class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(1,len(prices)):
            selling_price = prices[i]
            buying_price = min(prices[:i])

            profit = selling_price - buying_price

            maxProfit = max(profit, maxProfit)

        return maxProfit 