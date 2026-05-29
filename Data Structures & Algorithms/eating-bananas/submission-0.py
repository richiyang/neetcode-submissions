class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def timeToEat(rate: int) -> int:
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p) / k)
            return totalTime

        while l <= r:
            k = (l + r) // 2

            if timeToEat(k) <= h:
                res = k
                r = k - 1
            else:
                l = k + 1
        
        return res