class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for x, y in edges:
            adj[x].append(y)
        
        topSort = []
        visit = set()
        path = set()

        def dfs(i):
            if i in path:
                return False
            if i in visit:
                return True
            path.add(i)
            visit.add(i)
            for j in adj[i]:
                if dfs(j) == False:
                    return False
            path.remove(i)
            topSort.append(i)
        
        for i in range(n):
            if dfs(i) == False:
                return []
        
        topSort.reverse()
        return topSort