class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {}

        def helper(i):
            if i in dp:
                return dp[i]

            dp[i] = 1

            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], helper(j) + 1)

            return dp[i]


        for i in range(len(nums)):
            helper(i)

        return max(dp.values()) if dp else 0