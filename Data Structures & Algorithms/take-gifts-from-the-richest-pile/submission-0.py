class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        # Max heap where we pop and then push back
        # the square root
        # At the end we take the sum of the heap.
        heapq.heapify_max(gifts)

        for i in range(k):

            pile = heapq.heappop_max(gifts)
            heapq.heappush_max(gifts, floor(sqrt(pile)))

        return sum(gifts)