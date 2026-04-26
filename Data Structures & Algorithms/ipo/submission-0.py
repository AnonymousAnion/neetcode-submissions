class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        
        min_cap_req_heap = []

        for i, cap_req in enumerate(capital):

            heapq.heappush(min_cap_req_heap, (cap_req, i))

        total_profit = w
        max_profit_heap = []

        for i in range(k):

            while min_cap_req_heap and min_cap_req_heap[0][0] <= total_profit:

                cap_req, index = heapq.heappop(min_cap_req_heap)
                heapq.heappush_max(max_profit_heap, profits[index])

            if max_profit_heap: # There are projects we can pursue

                total_profit += heapq.heappop_max(max_profit_heap)

            else:

                break # No affordable projects with current capital to pursue

        return total_profit