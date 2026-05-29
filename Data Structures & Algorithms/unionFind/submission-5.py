class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
        self.num_components = n

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
