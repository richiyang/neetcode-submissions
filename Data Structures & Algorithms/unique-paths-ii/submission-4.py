class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0] * cols
        for i in range(cols):
            if obstacleGrid[0][i] == 1:
                break
            cur[i] = 1

        for i in range(1, rows):
            if obstacleGrid[i][0] == 1:
                cur[0] = 0
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    cur[j] = 0
                    continue
                cur[j] += cur[j - 1]
            
        return cur[-1]