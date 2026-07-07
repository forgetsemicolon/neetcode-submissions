class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {0 : 1}

        def dfs(total):
            if total in dp:
                return dp[total]

            res = 0
            for i in range(len(nums)):
                if nums[i] > total:
                    break

                res += dfs(total - nums[i])

            dp[total] = res
            return res

        return dfs(target)