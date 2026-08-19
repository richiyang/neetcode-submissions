class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        a = set()
        p = set()
        visit = set()
        
        def dfs(x, y):
            res = ''
            if (x, y) in visit:
                if (x, y) in a:
                    res += 'a'
                if (x, y) in p:
                    res += 'p'
                return res 
            
            visit.add((x, y))
            for i, j in directions:
                x2, y2 = x + i, y + j
                if x2 >= len(heights) or y2 >= len(heights[0]):
                    res += 'a'
                elif x2 < 0 or y2 < 0:
                    res += 'p'
                elif heights[x2][y2] <= heights[x][y]:
                    res += dfs(x2, y2)
            
            if 'a' in res:
                a.add((x, y))
            if 'p' in res:
                p.add((x, y))
            return res
        
        changed = True
        while changed:
            old = len(a) + len(p)
            visit.clear()
            for i in range(len(heights)):
                for j in range(len(heights[0])):
                    dfs(i, j)
            changed = (len(a) + len(p)) != old
        
        res = list(a & p)
        for i in range(len(res)):
            res[i] = list(res[i])
        return res

            

            
        


                