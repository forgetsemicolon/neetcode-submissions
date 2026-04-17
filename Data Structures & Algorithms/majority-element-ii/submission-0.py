class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        majority = len(nums) // 3

        res = []

        for num in freq.keys():
            if freq[num] > majority:
                res.append(num)


        return res