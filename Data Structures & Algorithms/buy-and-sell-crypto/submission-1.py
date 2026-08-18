class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minl = prices[0]
        res = 0
        for i in range(len(prices)):
            res = max(res, prices[i] - minl)
            minl = min(minl, prices[i])
            
        return res