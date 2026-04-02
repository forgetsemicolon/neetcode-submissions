class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        prev_sum = nums[0]
        max_sum = nums[0]

        for i in range(1,len(nums)):
            if prev_sum >= 0:
                prev_sum = prev_sum + nums[i]
            else:
                prev_sum = nums[i]

            max_sum = max(prev_sum, max_sum)

        return max_sum