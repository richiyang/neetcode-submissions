class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dtoc = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 
                6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}
        
        res = []

        for d in digits:
            tmp = []
            d = int(d)
            for c in dtoc[d]:
                if not res:
                    tmp.append(c)
                else:
                    for x in res:
                        tmp.append(x + c)
            res = tmp
        return res