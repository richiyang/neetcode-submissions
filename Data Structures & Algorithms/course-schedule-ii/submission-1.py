class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[crs] += 1
            adj[pre].append(crs)
        
        topSort = []
        
        def dfs(node):
            topSort.append(node)
            indegree[node] -= 1
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    dfs(nei)
        
        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)

        return topSort if len(topSort) == numCourses else []