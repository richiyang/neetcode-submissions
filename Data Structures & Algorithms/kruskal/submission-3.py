class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, v):
        if self.par[v] != v:
            self.par[v] = self.find(self.par[v])
        return self.par[v]
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
        self.size[p1] += self.size[p2]
        self.par[p2] = p1
        return True

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key = lambda e: e[2])
        res, components = 0, n
        uf = UnionFind(n)

        for v1, v2, w in edges:
            if uf.union(v1, v2):
                res += w
                components -= 1
        
        return res if components == 1 else -1
        # minH = []
        # for v1, v2, w in edges:
        #     heapq.heappush(minH, [w, v1, v2])

        # uf = UnionFind(n)
        # res, components = 0, n

        # while components > 1 and minH:
        #     w, v1, v2 = heapq.heappop(minH)
        #     if uf.union(v1, v2):
        #         res += w
        #         components -= 1
        
        # return res if components == 1 else -1
