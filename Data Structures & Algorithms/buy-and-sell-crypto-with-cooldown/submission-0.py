class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        dp[(0, 'free')] = 0
        dp[(0, 'hold')] = -prices[0]
        dp[(0, 'sold')] = -float('inf')

        def helper(i, s):
            if (i,s) in dp:
                return dp[(i,s)]

            if i < 0:
                return -float('inf')

            if (s=='free'):
                dp[(i,'free')] = max(helper(i-1,'free'), helper(i-1,'sold'))
            elif (s=='hold'):
                dp[(i,'hold')] = max(helper(i-1,'hold'), helper(i-1,'free') - prices[i])
            else:
                dp[(i,'sold')] = helper(i-1,'hold') + prices[i]

            return dp[(i, s)]

        return max(helper(len(prices)-1, 'free'), helper(len(prices)-1, 'sold'))

