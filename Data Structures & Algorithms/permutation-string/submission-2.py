class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26: 
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1 
            l += 1

        return matches == 26
        # s1h = {}
        # s2h = {}
        # s1l = len(s1)
        # if s1l > len(s2):
        #     return False

        # for c in s1:
        #     s1h[c] = s1h.get(c, 0) + 1
    
        
        # for i in range(s1l):
        #     s2h[s2[i]] = s2h.get(s2[i], 0) + 1
        
        # if s2h == s1h:
        #     return True

        # for r in range(s1l, len(s2)):
        #     s2h[s2[r]] = s2h.get(s2[r], 0) + 1
        #     s2h[s2[r - s1l]] -= 1
        #     if s2h[s2[r - s1l]] == 0:
        #         del s2h[s2[r - s1l]]
            
        #     if s2h == s1h:
        #         return True
            
        # return False