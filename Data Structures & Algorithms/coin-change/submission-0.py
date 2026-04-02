class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(i):
            if i == 0:
                return 0

            if i < 0:
                return float('inf')
            
            if i in dp:
                return dp[i]

            res = 1 + min(dfs(i - coin) for coin in coins)

            dp[i] = res

            return res

        res = dfs(amount)

        return res if res != float('inf') else -1
