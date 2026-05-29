from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        points = list(map(lambda x: (sqrt(x[0] ** 2 + x[1] ** 2), x), points))
        heapq.heapify(points)
        for _ in range(k):
            res.append(heapq.heappop(points)[1])

        return res

        