class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        nums_set = set()

        for num in nums:
            if num <= 0:
                continue
            else:
                nums_set.add(num)

        n = len(nums_set)

        for i in range(1,n+1):
            if i not in nums_set:
                return i
            else:
                continue

        return n+1

        