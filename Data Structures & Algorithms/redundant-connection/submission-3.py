class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.size = {}

        for i in range(1, n + 1):
            self.parent[i] = i
            self.size[i] = 1

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px != py:
            if self.size[px] > self.size[py]:
                self.parent[py] = px
                self.size[px] += self.size[py]
            else:
                self.parent[px] = py
                self.size[py] += self.size[px]
            return True
        return False

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge
        
        return None

        
