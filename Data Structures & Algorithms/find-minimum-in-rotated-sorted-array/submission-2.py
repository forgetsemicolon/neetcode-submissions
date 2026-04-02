class Solution:
    def findMin(self, nums: List[int]) -> int:
        # since the array has been rotated,
        # the rotated array now has a deflection
        # point along which on the right of it
        # elements are sorted and left of it
        # elements are sorted. We need to find that 
        # point and that is the min. When we use
        # bin search, l, r, mid - atleast 2 are 
        # on the same side. if nums[mid] > nums[l],
        # l and mid are on same side. Otherwise mid
        # and r are on the same side

        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
                break

            m = (l + r) // 2 
            res = min(nums[m], res)
            if nums[m] >= nums[l]: # at some point, the array is going to be so small that m and l will start coinciding
                l = m + 1
            else:
                r = m - 1

        return res
