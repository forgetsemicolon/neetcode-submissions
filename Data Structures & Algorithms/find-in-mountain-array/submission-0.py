# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l, r = 0, mountainArr.length()-1

        while l < r:
            m = (l + r) // 2
            peakEle = mountainArr.get(m)
            rightEle = mountainArr.get(m+1)

            if peakEle < rightEle:
                l = m + 1  # ascending, peak is to the right
            else:
                r = m      # descending, peak is here or to the left
            
        peak = l

        l, r = 0, peak

        while l <= r:
            m = (l + r) // 2
            ele = mountainArr.get(m)

            if ele == target:
                return m
            elif ele < target:
                l = m+1
            else:
                r = m-1

        l, r = peak+1, mountainArr.length()-1

        while l <= r:
            m = (l+r) // 2
            ele = mountainArr.get(m)

            if ele == target:
                return m
            elif ele > target:
                l = m+1
            else:
                r = m-1

        return -1