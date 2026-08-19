class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = set(['+', '-', '*', '/'])

        for c in tokens:
            if c not in ops:
                stack.append(int(c))
            elif c in ops:
                b, a = stack.pop(), stack.pop()
                if c == '+':
                    stack.append(a + b)
                elif c == '-':
                    stack.append(a - b)
                elif c == '*':
                    stack.append(a * b)
                elif c == '/':
                    stack.append(int(a / b))
            
        return stack.pop()