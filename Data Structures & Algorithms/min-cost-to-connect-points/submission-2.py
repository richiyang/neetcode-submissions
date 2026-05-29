class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
            
        minH = [[0, 0]]
        res = 0
        visit = set()
        while len(visit) < len(points):
            w1, pt1 = heapq.heappop(minH)
            if pt1 in visit:
                continue
            res += w1
            visit.add(pt1)
            for w2, pt2 in adj[pt1]:
                if pt2 not in visit:
                    heapq.heappush(minH, [w2, pt2]) 
        
        return res