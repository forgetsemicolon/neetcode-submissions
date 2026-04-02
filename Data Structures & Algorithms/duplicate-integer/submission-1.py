class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for num in nums:
            if num not in freq.keys():
                freq[num] = 1
            else:
                freq[num] += 1
                return True

        return False