class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # fal = {}
        # for s, d, p in flights:
        #     fal.setdefault(s, []).append((d, p))
        
        # best = [float('inf')] * n
        # queue = deque([(src, 0, 0)])

        # while queue:
        #     cur, stops, cost = queue.popleft()
        #     for d, c in fal.get(cur, []):
        #         new_cost = cost + c
        #         if new_cost < best[d] and stops <= k:
        #             best[d] = new_cost
        #             queue.append((d, stops + 1, new_cost))
        
        # return best[dst] if best[dst] < float('inf') else -1

        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmpPrices = prices.copy()

            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < tmpPrices[d]:
                    tmpPrices[d] = prices[s] + p
            prices = tmpPrices
        
        return -1 if prices[dst] == float("inf") else prices[dst]


