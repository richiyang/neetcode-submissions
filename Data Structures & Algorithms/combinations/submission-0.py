class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def helper(i, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return
            
            if i > n:
                return
            
            for j in range(i, n + 1):
                curr.append(j)
                helper(j + 1, curr)
                curr.pop()
            
        helper(1, [])
        return res