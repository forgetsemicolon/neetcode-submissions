class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
            
        l, r = 1, x//2

        while True:
            if l > r:
                return r

            m = (l+r) // 2

            if x > m*m:
                l = m+1
            
            elif x < m*m:
                r = m-1

            else:
                return m