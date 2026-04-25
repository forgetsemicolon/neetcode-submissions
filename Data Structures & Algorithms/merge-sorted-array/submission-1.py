class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m
        j = 0

        while i < (m+n) and j < n:
            nums1[i] = nums2[j]

            i += 1
            j += 1

        return nums1.sort()