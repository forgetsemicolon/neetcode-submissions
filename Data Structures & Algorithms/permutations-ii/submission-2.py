class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        nums.sort()
        used = [False] * len(nums)

        def dfs():
            if len(subset) == len(nums):
                print(subset)
                res.append(subset.copy())
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                    continue

                used[i] = True
                subset.append(nums[i])
                dfs()
                subset.pop()
                used[i] = False

        dfs()

        return res