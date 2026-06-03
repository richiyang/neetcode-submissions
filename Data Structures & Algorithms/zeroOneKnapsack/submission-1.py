class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N, M = len(profit), capacity
        dp = [0] * (M + 1)

        for c in range(M + 1):
            if c >= weight[0]:
                dp[c] = profit[0]
        
        for r in range(1, N):
            curRow = [0] * (M + 1)
            for c in range(M + 1):
                skip = dp[c]
                incl = 0
                if c >= weight[r]:
                    incl = profit[r] + dp[c - weight[r]]
                curRow[c] = max(skip, incl)
            dp = curRow
        
        return dp[-1]