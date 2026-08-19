class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1h = {}
        s2h = {}
        s1l = len(s1)
        if s1l > len(s2):
            return False

        for c in s1:
            s1h[c] = s1h.get(c, 0) + 1
    
        
        for i in range(s1l):
            s2h[s2[i]] = s2h.get(s2[i], 0) + 1
        
        if s2h == s1h:
            return True

        for r in range(s1l, len(s2)):
            s2h[s2[r]] = s2h.get(s2[r], 0) + 1
            s2h[s2[r - s1l]] -= 1
            if s2h[s2[r - s1l]] == 0:
                del s2h[s2[r - s1l]]
            
            if s2h == s1h:
                return True
            
        return False