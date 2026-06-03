class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        arr = [[0, 0] for _ in range(len(strs))]
        for i, s in enumerate(strs):
            for c in s:
                arr[i][ord(c) - ord('0')] += 1
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for zeros, ones in arr:
            for j in range(m, zeros - 1, -1):
                for k in range(n, ones - 1, -1):
                    dp[j][k] = max(dp[j][k], 1 + dp[j - zeros][k - ones])
        
        return dp[m][n]