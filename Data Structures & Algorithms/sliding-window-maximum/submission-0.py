class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        maximums = []
        heap = []

        for i, num in enumerate(nums):

            heapq.heappush_max(heap, (num, i))

            if i >= k - 1:

                val, index = heap[0]

                while index <= i - k:

                    heapq.heappop_max(heap)
                    val, index = heap[0]

                maximums.append(val)

        return maximums