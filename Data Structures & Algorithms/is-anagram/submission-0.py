class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        for i in s:
            if i in letters:
                letters[i] += 1
            else:
                letters[i] = 1
        for i in t:
            if i not in letters:
                return False
            letters[i] -= 1
        for letter in letters:
            if letters[letter] != 0:
                return False
        return True
        