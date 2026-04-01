class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.minimum = 0

    def push(self, val: int) -> None:

        self.stack.append(val)

        if 1 == len(self.stack):

            self.minimum = val

        else:

            if val < self.minimum:

                self.minimum = val

        self.min_stack.append(self.minimum)
        

    def pop(self) -> None:

        self.stack.pop()
        self.min_stack.pop()

        if len(self.min_stack) > 0:
            
            self.minimum = self.min_stack[-1]
        

    def top(self) -> int:

        return self.stack[-1]
        

    def getMin(self) -> int:

        return self.min_stack[-1]
