class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pres = { c:set() for c in range(numCourses) }
        for pre, nxt in prerequisites:
            pres[nxt].add(pre)

        visit = set()
        
        def dfs(crs):
            if crs in visit:
                return
            visit.add(crs)
            for pre in pres[crs]:
                dfs(pre)
                pres[crs] = set.union(pres[crs], pres[pre])
        
        for i in range(numCourses):
            dfs(i)
            
        res = []
        for pre, crs in queries:
            res.append(pre in pres[crs])
        
        return res