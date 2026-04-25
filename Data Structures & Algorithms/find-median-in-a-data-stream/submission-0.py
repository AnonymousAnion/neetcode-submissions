class MedianFinder:

    def __init__(self):

        self.bigs = [] # Min heap of elements bigger than median
        self.smalls = [] # Max heap of elements smaller than median

    def addNum(self, num: int) -> None:

        if not self.smalls:

            self.smalls.append(num)
            return

        if num <= self.findMedian():

            heapq.heappush_max(self.smalls, num)

        else:

            heapq.heappush(self.bigs, num)

        # Rebalance as necessary
        if len(self.smalls) > len(self.bigs) + 1:

            heapq.heappush(self.bigs, heapq.heappop_max(self.smalls))

        elif len(self.bigs) > len(self.smalls):

            heapq.heappush_max(self.smalls, heapq.heappop(self.bigs))

    def findMedian(self) -> float:

        n = len(self.smalls) + len(self.bigs)

        if n % 2: # Odd length

            return self.smalls[0]

        return (self.smalls[0] + self.bigs[0]) / 2