class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = {}

        if len(s1) + len(s2) != len(s3):
            return False

        def helper(i, j):
            if (i, j) in dp:
                return dp[(i,j)]

            if i == 0 and j == 0:
                return True

            if i == 0 and j > 0:
                dp[(i,j)] = helper(i, j-1) and s2[j-1] == s3[j-1]
            elif i > 0 and j == 0:
                dp[(i,j)] = helper(i-1, j) and s1[i-1] == s3[i-1]
            else:
                dp[(i,j)] = (helper(i-1,j) and s1[i-1] == s3[i+j-1]) or (helper(i, j-1) and s2[j-1] == s3[i+j-1])

            return dp[(i,j)]

        return helper(len(s1), len(s2))