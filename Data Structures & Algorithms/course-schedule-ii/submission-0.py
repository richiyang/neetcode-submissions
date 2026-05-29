class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for crs, pre in prerequisites:
            indegree[pre] += 1
            adj[crs].append(pre)
        
        topSort = []
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            pre = q.popleft()
            topSort.append(pre)
            for crs in adj[pre]:
                indegree[crs] -= 1
                if indegree[crs] == 0:
                    q.append(crs)
        
        topSort.reverse()
        return topSort if len(topSort) == numCourses else []