class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dest_i = len(nums) - 1

        for i in range(dest_i-1, -1, -1):
            if nums[i] >= dest_i - i:
                dest_i = i


        return dest_i == 0