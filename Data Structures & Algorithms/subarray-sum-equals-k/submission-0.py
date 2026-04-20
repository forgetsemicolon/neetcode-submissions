class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = res = 0
        prefixSum = {0:1}

        for num in nums:
            currSum += num
            diff = currSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum,0)

        return res


        # l = 0
        # r = 0
        # res = 0

        # if len(nums) == 1 and nums[0] != k:
        #     return 0
        
        # if not nums:
        #     return 0

        # curr_sum = 0
        # while l <= r and r < len(nums):
        #     curr_sum = sum(nums[l:r+1])
        #     if curr_sum == k:
        #         res += 1
        #         l += 1
        #         r += 1
        #     else:
        #         r += 1

