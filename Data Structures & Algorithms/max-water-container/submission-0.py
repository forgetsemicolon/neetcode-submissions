class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # we want to use 2 pointer such that one pointer is at
        # the start and the other is at the end and then we 
        # calculate the volume of water by (j - i) * min(height[i], height[j])
        # move the pointer with smaller height value 

        i = 0
        j = len(heights) - 1
        max_vol = 0

        while i < j:
            vol = (j - i) * min(heights[i], heights[j])
            if vol > max_vol:
                max_vol = vol

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1

        return max_vol
            
