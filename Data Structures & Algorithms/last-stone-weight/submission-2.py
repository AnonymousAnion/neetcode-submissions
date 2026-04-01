import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = []

        for stone in stones:

            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:

            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)

            if heaviest == second_heaviest:

                continue # None added back, both destroyed

            else:

                diff = heaviest - second_heaviest
                heapq.heappush(max_heap, -diff)

        if len(max_heap) > 0:

            return -max_heap[0]

        return 0