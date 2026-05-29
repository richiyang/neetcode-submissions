class Graph:
    
    def __init__(self):
        self.graph = {}


    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.graph:
            self.graph[src] = set()
        if dst not in self.graph:
            self.graph[dst] = set()
        self.graph[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.graph or dst not in self.graph:
            return False
        if dst not in self.graph[src]:
            return False
        self.graph[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        return self._dfs(src, dst, visit)

    def _dfs(self, src: int, dst: int, visit: set) -> bool:
        if src == dst:
            return True
        visit.add(src)
        for neighbor in self.graph.get(src, []):
            if neighbor not in visit:
                if self._dfs(neighbor, dst, visit):
                    return True
        return False

    def hasPathBFS(self, src: int, dst: int) -> bool:
        visit = set()
        queue = deque([src])
        while queue:
            curr = queue.popleft()
            if curr == dst:
                return True
            visit.add(curr)
            for neighbor in self.graph.get(curr, []):
                if neighbor not in visit:
                    queue.append(neighbor)
                    visit.add(neighbor)
        return False

