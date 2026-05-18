class MovingAverage:

    def __init__(self, size: int):

        self.size = size
        self.window = deque()
        self.sma = 0

    def next(self, val: int) -> float:

        self.window.append(val)
        self.sma += val

        if len(self.window) > self.size:

            removed_val = self.window.popleft()
            self.sma -= removed_val

        return self.sma / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
