class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        parent = [i for i in range(n)]
        rank = [0] * n

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            pari = find(i)
            parj = find(j)
            if pari == parj:
                return False

            if rank[pari] < rank[parj]:
                parent[pari] = parj
            elif rank[parj] < rank[pari]:
                parent[parj] = pari
            else:
                parent[parj] = pari
                rank[pari] += 1
            return True
        
        for v1, v2 in edges:
            if not union(v1, v2):
                return False
        
        return True
        
