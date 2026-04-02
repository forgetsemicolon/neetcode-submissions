import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k can range between 1 and max(piles)
        # so we need to do a binary search to
        # find k such that hours taken is less
        # than h. 

        l = 1
        r = max(piles)
        min_k = max(piles)

        while l <= r:
            m = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)

            if hours > h:
                l = m + 1
            elif hours <= h:
                min_k = min(m, min_k)
                r = m-1

        return min_k