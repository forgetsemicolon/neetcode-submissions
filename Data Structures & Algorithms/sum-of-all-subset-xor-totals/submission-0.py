from functools import reduce
from operator import xor

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_array = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                if not subset:
                    xor_total = 0
                else:
                    xor_total = reduce(xor, subset.copy())
                xor_array.append(xor_total)
                return

            subset.append(nums[i])
            print(subset)
            dfs(i+1)

            subset.pop()
            print(subset)
            dfs(i+1)

        dfs(0)
        return sum(xor_array)