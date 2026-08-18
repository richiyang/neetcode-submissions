class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        chars = set()
        print(chars)
        for r in range(0, len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            
            res = max(res, r - l + 1)
    
        return res