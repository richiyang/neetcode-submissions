class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            if not lower[l].isalnum():
                l += 1
                continue
            if not lower[r].isalnum():
                r -= 1
                continue
            if lower[l] != lower[r]:
                return False
            else:
                l += 1
                r -= 1

        return True