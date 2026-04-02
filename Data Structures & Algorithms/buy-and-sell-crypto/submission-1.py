class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while l<r and r < len(prices):
            profit = prices[r] - prices[l]
            if profit < 0:
                l = r
                r += 1
            else:
                maxProfit = max(profit, maxProfit)
                r += 1

        return maxProfit 



        # maxProfit = 0

        # for i in range(1,len(prices)):
        #     selling_price = prices[i]
        #     buying_price = min(prices[:i])

        #     profit = selling_price - buying_price

        #     maxProfit = max(profit, maxProfit)

        # return maxProfit 