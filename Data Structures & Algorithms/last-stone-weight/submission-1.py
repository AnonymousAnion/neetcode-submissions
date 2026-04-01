import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = []

        for stone in stones:

            heapq.heappush(max_heap, -stone)

        #print("max_heap", max_heap)

        while len(max_heap) > 1:

            #print("max_heap", max_heap)

            heaviest = -heapq.heappop(max_heap)
            second_heaviest = -heapq.heappop(max_heap)

            #print("Comparing {0} and {1}".format(str(heaviest), str(second_heaviest)))

            if heaviest == second_heaviest:

                continue # None added back, both destroyed

            else:

                diff = heaviest - second_heaviest
                #print("Adding back: ", diff)
                heapq.heappush(max_heap, -diff)

        if len(max_heap) > 0:

            return -max_heap[0]

        return 0