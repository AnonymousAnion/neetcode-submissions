class MinStack:

    def __init__(self):
        
        self.stack = []
        self.min_stack = []
        self.minimum = 0

    def push(self, val: int) -> None:

        self.minimum = val if not self.stack else min(self.minimum, val)

        self.stack.append(val)
        self.min_stack.append(self.minimum)

    def pop(self) -> None:
        
        self.min_stack.pop()
        self.minimum = self.getMin()
        return self.stack.pop()

    def top(self) -> int:

        return self.stack[-1]

    def getMin(self) -> int:
        
        return self.min_stack[-1] if self.min_stack else 0