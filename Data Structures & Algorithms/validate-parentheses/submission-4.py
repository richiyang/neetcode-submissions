class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openBracket = ('(', '[', '{')
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in openBracket:
                stack.append(c)
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False