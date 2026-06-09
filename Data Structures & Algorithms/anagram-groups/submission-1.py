class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs: 
            ca = [0] * 26
            for c in s:
                ca[ord(c) - ord('a')] += 1
            d.setdefault(tuple(ca), []).append(s)
        return list(d.values())