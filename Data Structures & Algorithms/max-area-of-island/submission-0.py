class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        maxArea = 0
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            visited.add((r, c))
            q.append((r, c))
            area = 1

            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]

                for dr, dc in directions:
                    r, c = row+dr, col+dc

                    if r in range(ROWS) and c in range(COLS) and (r, c) not in visited and grid[r][c] == 1:
                        area += 1
                        visited.add((r, c))
                        q.append((r, c))
            
            return area
                

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)

        return maxArea