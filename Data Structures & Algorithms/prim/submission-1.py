class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for s, d, w in edges:
            adj[s].append([d, w])
            adj[d].append([s, w])
        
        res = 0
        visit = set()
        minH = [[0, 0]]
        
        while minH and len(visit) < n:
            w, d = heapq.heappop(minH)
            if d in visit:
                continue
            visit.add(d)
            res += w
            for d2, w2 in adj[d]:
                if d2 not in visit:
                    heapq.heappush(minH, [w2, d2])
        
        return res if len(visit) == n else -1