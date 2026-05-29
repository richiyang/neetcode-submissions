class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n

        for i in range(m - 1, -1, -1):
            cur = [0] * n
            cur[-1] = 1
            
            for j in range(n - 2, -1, -1):
                cur[j] = prev[j] + cur[j + 1]
            
            prev = cur
        
        return prev[0]
