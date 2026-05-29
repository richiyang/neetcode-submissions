class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtoc = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 
                6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        
        res = []
        
        def helper(i, cur):
            if len(cur) == len(digits) and len(digits) > 0:
                res.append(''.join(cur))
            
            if i >= len(digits):
                return
            
            c = dtoc[int(digits[i])]
            for j in range(len(c)):
                helper(i + 1, cur + c[j])
        
        helper(0, '')
        return res
