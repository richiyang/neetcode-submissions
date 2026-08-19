from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        INF = 2147483647
        visit = set()
        q = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append(((r, c), 0))
        
        while q:
            cur, dist = q.popleft()
            x, y = cur
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            if (x, y) in visit:
                continue
            if grid[x][y] == -1:
                visit.add((x, y))
                continue
            
            for a, b in directions:
                q.append(((x + a, y + b), dist + 1))
            
            grid[x][y] = dist
            visit.add((x, y))