class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        pres = { c:set() for c in range(numCourses) }
        for pre, nxt in prerequisites:
            pres[nxt].add(pre)
        
        def dfs(crs):
            if crs not in prereqMap:
                prereqMap[crs] = set()
                for pre in pres[crs]:
                    prereqMap[crs] |= dfs(pre)
                prereqMap[crs].add(crs)
            return prereqMap[crs]
        
        prereqMap = {}
        for i in range(numCourses):
            dfs(i)
        
        return [pre in prereqMap[crs] for pre, crs in queries]