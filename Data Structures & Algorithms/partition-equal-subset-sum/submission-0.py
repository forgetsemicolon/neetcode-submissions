class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}

        def helper(i, remaining):
            if remaining == 0:
                return True

            if i >= len(nums):
                return False

            if (i, remaining) in dp:
                return dp[(i, remaining)]

            if remaining-nums[i] >= 0:
                dp[(i,remaining)] = helper(i+1, remaining) or helper(i+1, remaining - nums[i])

            else:
                dp[(i,remaining)] = helper(i+1, remaining)

            return dp[(i, remaining)]

        s = sum(nums)
        if s%2 != 0: return False

        return helper(0, s//2)
            