class MyQueue:

    def __init__(self):

        self.forward = []
        self.reverse = []

    def push(self, x: int) -> None:

        self.forward.append(x)

    def reque(self) -> None:

        n = len(self.forward)

        for i in range(n):

            self.reverse.append(self.forward.pop())

    def restack(self) -> None:

        n = len(self.reverse)

        for i in range(n):

            self.forward.append(self.reverse.pop())

    def pop(self) -> int:

        if not self.reverse:
            self.reque()

        return self.reverse.pop()

    def peek(self) -> int:

        if not self.reverse:

            self.reque()

        return self.reverse[-1]

    def empty(self) -> bool:
        
        return len(self.forward) <= 0 and len(self.reverse) <= 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()