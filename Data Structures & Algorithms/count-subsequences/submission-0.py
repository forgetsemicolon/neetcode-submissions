class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}

        def helper(i,j):

            if (i,j) in dp:
                return dp[(i,j)]

            elif i == 0 and j != 0:
                dp[(i,j)] = 0

            elif i != 0 and j == 0:
                dp[(i,j)] = 1

            elif i == 0 and j == 0:
                dp[(i,j)] = 1

            elif s[i-1] == t[j-1]:
                dp[(i,j)] = helper(i-1,j-1) + helper(i-1,j)

            else:
                dp[(i,j)] = helper(i-1, j)

            return dp[(i,j)]

        return helper(len(s), len(t))