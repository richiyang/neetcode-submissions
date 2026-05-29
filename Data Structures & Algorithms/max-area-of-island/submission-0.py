class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                grid[r][c] == 0):
                return 0
            area = 1
            grid[r][c] = 0
            for dr, dc in directions:
                area += dfs(r + dr, c + dc)
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea
            
