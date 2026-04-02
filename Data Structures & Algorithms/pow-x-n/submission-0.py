class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0.0

        if n == 0:
            return 1.0

        if n < 0:
            return 1.0 / self.myPow(x,-n)

        res = self.myPow(x, n//2)
        if n%2 == 0:
            return res * res

        else:
            return res * res * x