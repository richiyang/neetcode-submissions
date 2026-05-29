class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = math.inf
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minimum:
            self.minimum = val
        

    def pop(self) -> None:
        val = self.top()
        self.stack.pop()
        if val == self.minimum:
            self.minimum = min(self.stack) if self.stack else math.inf
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minimum
        
