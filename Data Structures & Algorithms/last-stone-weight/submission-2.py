class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = [-stone for stone in stones]
        heapq.heapify(stonesHeap)

        while len(stonesHeap) > 1:
            stone1 = -heapq.heappop(stonesHeap)
            stone2 = -heapq.heappop(stonesHeap)

            if stone1 == stone2:
                continue
            elif stone1 > stone2:
                heapq.heappush(stonesHeap, stone2 - stone1)

        return -stonesHeap[0] if stonesHeap else 0
            

        