class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            # i is not the first index i.e. 0 and the num is same as num before it
            if i > 0 and a == nums[i-1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                sum_nums = nums[j] + nums[k]
                if sum_nums == -a:
                    res.append([a, nums[j], nums[k]])
                    j += 1

                    # while it's the same value as last one, we keep shifting ensuring j<k
                    while nums[j] == nums[j-1] and j < k:
                        j += 1
                
                elif sum_nums < -a:
                    j += 1

                elif sum_nums > -a:
                    k -= 1

        return res