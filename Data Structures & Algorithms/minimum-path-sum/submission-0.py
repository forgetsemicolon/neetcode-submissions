class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = {}

        def dfs(i,j):

            if i < 0 or j < 0 or i >= ROWS or j >= COLS:
                return float('inf')

            if i == ROWS - 1 and j == COLS - 1:
                return grid[i][j]

            if (i,j) in dp:
                return dp[(i,j)]

            dp[(i,j)] = grid[i][j] + min(dfs(i+1, j), dfs(i, j+1))

            return dp[(i,j)]

        return dfs(0,0)

            