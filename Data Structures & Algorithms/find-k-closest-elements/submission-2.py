class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1

        while r-l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1

        return arr[l:r+1]
        
        
        # # Use a list of tuples to handle duplicate values in the input array
        # diffs = [(abs(n - x), n) for n in arr]

        # res = []

        # # Sort by distance first, then by value for tie-breaking
        # sorted_diffs = sorted(diffs, key=lambda item: (item[0], item[1]))

        # for i in range(k):
        #     res.append(sorted_diffs[i][1])

        # return sorted(res)