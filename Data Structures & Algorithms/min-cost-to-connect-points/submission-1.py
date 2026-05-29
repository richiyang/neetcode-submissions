class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for i in range(len(points)):
            pt1 = tuple(points[i])
            x1, y1 = pt1[0], pt1[1]
            for j in range(i + 1, len(points)):
                pt2 = tuple(points[j])
                x2, y2 = pt2[0], pt2[1]
                adj[pt1].append([abs(x1 - x2) + abs(y1 - y2), pt2])
                adj[pt2].append([abs(x1 - x2) + abs(y1 - y2), pt1])
            
        minH = [[0, tuple(points[0])]]
        res = 0
        visit = set()
        while minH:
            w1, pt1 = heapq.heappop(minH)
            if pt1 in visit:
                continue
            res += w1
            visit.add(pt1)
            for w2, pt2 in adj[pt1]:
                if pt2 not in visit:
                    heapq.heappush(minH, [w2, pt2]) 
        
        return res