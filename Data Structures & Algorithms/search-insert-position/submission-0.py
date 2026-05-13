class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        def binSearch(l, r):
            if l > r:
                return l

            m = (l + r) // 2

            if nums[m] == target:
                return m

            elif target < nums[m]:
                return binSearch(l, m-1)

            else:
                return binSearch(m+1, r)

            
        return binSearch(0, len(nums)-1)