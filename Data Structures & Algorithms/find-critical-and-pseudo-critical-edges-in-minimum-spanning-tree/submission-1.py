class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = list(range(n))
        self.size = [1] * n
    
    def find(self, v):
        if self.par[v] != v:
            self.par[v] = self.find(self.par[v])
        return self.par[v]
    
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        self.n -= 1
        if self.size[p1] < self.size[p2]:
            p1, p2 = p2, p1
        self.size[p1] += self.size[p2]
        self.par[p2] = p1
        return True
    
    def isConnected(self):
        return self.n == 1

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, e in enumerate(edges):
            e.append(i)
        edges.sort(key = lambda e: e[2])

        def findMST(index, include):
            uf = UnionFind(n)
            wt = 0
            if include:
                wt += edges[index][2]
                uf.union(edges[index][0], edges[index][1])
            
            for i, e in enumerate(edges):
                if i == index:
                    continue
                if uf.union(e[0], e[1]):
                    wt += e[2]
            return wt if uf.isConnected() else float("inf")
        
        mst_wt = findMST(-1, False)
        critical, pseudo = [], []
        for i, e in enumerate(edges):
            if mst_wt < findMST(i, False):
                critical.append(e[3])
            elif mst_wt == findMST(i, True):
                pseudo.append(e[3])
        
        return [critical, pseudo]