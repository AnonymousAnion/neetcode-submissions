class StockSpanner:

    def __init__(self):

        self.stack = []
        self.span = []

    def next(self, price: int) -> int:

        current_span = 1

        while self.stack and price >= self.stack[-1][0]:

            prev_price, index = self.stack.pop()
            current_span += self.span[index]
        
        self.span.append(current_span)
        self.stack.append((price, len(self.span) - 1))

        return self.span[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)