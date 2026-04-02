class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def helper(rem, i):
            if i == len(nums):
                if rem == 0:
                    return 1
                if rem != 0:
                    return 0

            if (rem, i) in dp:
                return dp[(rem, i)]

            ways = 0
            ways += helper(rem-nums[i], i+1)
            ways += helper(rem+nums[i], i+1)

            dp[(rem, i)] = ways

            return dp[(rem,i)]

        return helper(target, 0)