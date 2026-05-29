class UnionFind:
    def __init__(self, n: int):
        self.parent = {}
        self.size = {}
        self.num_components = n

        for i in range(1, n + 1):
            self.parent[i] = i
            self.size[i] = 1

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)

        if px != py:
            if self.size[px] > self.size[py]:
                self.parent[py] = px
                self.size[px] += self.size[py]
            else:
                self.parent[px] = py
                self.size[py] += self.size[px]
            self.num_components -= 1
            return True
        return False

    def getNumComponents(self) -> int:
        return self.num_components


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                return edge
        
        return None

        
