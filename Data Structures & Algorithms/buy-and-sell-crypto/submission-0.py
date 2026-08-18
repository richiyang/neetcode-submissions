class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minl, l = prices[0], 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] - minl > res:
                res = prices[i] - minl
            if prices[i] < minl:
                minl = prices[i]
            
        return res