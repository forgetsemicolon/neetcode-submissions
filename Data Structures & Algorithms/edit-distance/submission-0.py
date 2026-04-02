class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = {}

        def helper(i,j):
            if i >= len(word1) and j < len(word2):
                dp[(i,j)] = len(word2) - j
                return dp[(i,j)]

            if i < len(word1) and j >= len(word2):
                dp[(i,j)] = len(word1) - i
                return dp[(i,j)]
            
            if i >= len(word1) and j >= len(word2):
                return 0

            if (i, j) in dp:
                return dp[(i,j)]

            if word1[i] == word2[j]:
                dp[(i,j)] = helper(i+1, j+1)

            else:
                dp[(i,j)] = 1 + min(
                    helper(i+1, j+1), # replace
                    helper(i+1, j), # delete
                    helper(i, j+1) # insert
                )

            return dp[(i,j)]


        return helper(0,0)

            