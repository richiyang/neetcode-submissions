class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            if i == ')':
                if len(stack) > 0 and stack.pop() == '(':
                    continue
                return False
            if i == '}':
                if len(stack) > 0 and stack.pop() == '{':
                    continue
                return False
            if i == ']':
                if len(stack) > 0 and stack.pop() == '[':
                    continue
                return False
        return len(stack) == 0