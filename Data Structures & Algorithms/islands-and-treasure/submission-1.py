from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2147483647
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append(((r, c)))
        
        while q:
            cur = q.popleft()
            y, x = cur
            
            for a, b in directions:
                new_x = x + a
                new_y = y + b
                if new_x < 0 or new_x>= len(grid[0]) or new_y < 0 or new_y >= len(grid) or grid[new_y][new_x] != INF:
                    continue
                q.append(((new_y, new_x)))
            
                grid[new_y][new_x] = grid[y][x] + 1




