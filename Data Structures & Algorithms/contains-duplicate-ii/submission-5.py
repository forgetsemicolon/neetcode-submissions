class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0

        while i < len(nums):
            for j in range(i+1, i+k+1):
                if j < len(nums) and nums[i] == nums[j]:
                    return True

            i += 1

        return False