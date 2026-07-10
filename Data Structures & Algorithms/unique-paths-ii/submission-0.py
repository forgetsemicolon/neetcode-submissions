class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        R, C = len(obstacleGrid), len(obstacleGrid[0])
        dp = {(R-1, C-1): 1}

        def dfs(i, j):
            if i == R or j == C or obstacleGrid[i][j] == 1:
                return 0

            elif (i,j) in dp:
                return dp[(i,j)]

            else:
                dp[(i,j)] = dfs(i+1, j) + dfs(i, j+1)

            
            return dp[(i,j)]


        return dfs(0,0)