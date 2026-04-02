class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        dp = {}
        balloons = [1] + nums + [1]

        def helper(l,r):
            if l > r:
                return 0

            if (l,r) in dp:
                return dp[(l,r)]

            max = 0
            for k in range(l,r+1):
                coins = (balloons[l-1] * balloons[k] * balloons[r+1]) + helper(l, k-1) + helper(k+1, r)
                if coins > max:
                    max = coins

            dp[(l,r)] = max

            return dp[(l,r)]

        return helper(1, len(balloons)-2)
