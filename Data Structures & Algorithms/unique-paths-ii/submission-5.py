class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0] * cols
        cur[0] = 1

        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                cur[0] = 0
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                    continue
                cur[j] += cur[j - 1]
            
        return cur[-1]