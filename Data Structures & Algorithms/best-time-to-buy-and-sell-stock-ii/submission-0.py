class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = {}

        def dp(i, bought):
            if i == len(prices):
                return 0

            if (i, bought) in profits:
                return profits[(i, bought)]

            res = dp(i+1, bought)

            if bought:
                res = max(res, prices[i] + dp(i+1, False))
            else:
                res = max(res, -prices[i] + dp(i+1, True))

            profits[(i, bought)] = res

            return res


        return dp(0, False)