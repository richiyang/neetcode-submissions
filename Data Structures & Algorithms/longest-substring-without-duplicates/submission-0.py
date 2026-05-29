class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, l = 0, 0
        chars = set()
        for r, c in enumerate(s):
            while c in chars:
                chars.remove(s[l])
                l += 1
            chars.add(c)
            res = max(res, r - l + 1)
        
        return res
