class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.size[rx] > self.size[ry]:
                self.parent[ry] = rx
                self.size[rx] += self.size[ry]
            else:
                self.parent[rx] = ry
                self.size[ry] += self.size[rx]
            self.num_components -= 1
        
    def getNumComponents(self):
        return self.num_components

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        for edge in edges:
            uf.union(edge[0], edge[1])
        
        return uf.getNumComponents()