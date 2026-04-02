class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}

        def helper(i,j):
            if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            move = [[1,0], [0,1], [-1,0], [0,-1]]
            max_p = 0

            for (k,l) in move:
                if (i+k) >= 0 and (i+k) < len(matrix) and (j+l) >= 0 and (j+l) < len(matrix[0]) and matrix[i+k][j+l] > matrix[i][j]:
                    if helper(i+k, j+l) > max_p:
                        max_p = helper(i+k, j+l)

            if max_p == 0:
                dp[(i,j)] = 1
                return dp[(i,j)]

            dp[(i,j)] = 1 + max_p

            return dp[(i,j)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                helper(i,j)

        return max(dp.values())