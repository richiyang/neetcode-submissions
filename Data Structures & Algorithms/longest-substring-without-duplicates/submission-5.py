class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        res = 0
        l = 0
        chars = set(s[l])
        print(chars)
        for r in range(1, len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            
            res = max(res, r - l + 1)
    
        return res