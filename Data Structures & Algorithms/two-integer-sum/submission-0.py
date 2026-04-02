class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0,1]

        for i in range(len(nums)-1):
            diff = target - nums[i]

            for j in range(i + 1, len(nums)):
                if nums[j] == diff:
                    return [i, j]