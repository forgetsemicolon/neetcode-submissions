class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = {}

        def helper(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                dp[(i,j)] = helper(i+1, j+1) + 1

            else:
                dp[(i,j)] = max(helper(i+1,j), helper(i,j+1))

            return dp[(i,j)]


        return helper(0,0)