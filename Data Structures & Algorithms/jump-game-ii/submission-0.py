class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = {}

        def helper(i):
            if i in dp:
                return dp[i]

            if i == len(nums) - 1:
                return 0

            if nums[i] == 0:
                dp[i] = float('inf')
                return dp[i]

            dp[i] = 1 + min(helper(i+j) for j in range(1,nums[i]+1) if (i+j) < len(nums))

            return dp[i]

        return helper(0)