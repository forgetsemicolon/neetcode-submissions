class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False

        subsets = [0] * k

        subset_sum = total / k

        nums.sort(reverse=True)

        def dfs(i):
            if i == len(nums):
                return True

            for num in range(k):
                if subsets[num] + nums[i] <= subset_sum:
                    subsets[num] += nums[i]

                    if dfs(i+1):
                        return True

                    subsets[num] -= nums[i]

                if subsets[num] == 0:
                    break

            return False

        return dfs(0)