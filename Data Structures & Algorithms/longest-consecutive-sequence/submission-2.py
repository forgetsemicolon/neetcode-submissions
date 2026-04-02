class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0
        cons_set = set()

        for num in nums_set:
            # check if it is the start of a sequence
            if num-1 not in nums_set:
                length = 0
                while (num+length) in nums_set:
                    length += 1
                longest = max(length, longest)


        return longest

