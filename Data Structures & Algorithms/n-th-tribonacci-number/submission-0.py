class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        def helper(n):
            if n in dp:
                return dp[n]

            dp[n] = helper(n-3) + helper(n-2) + helper(n-1)

            return dp[n]


        return helper(n)