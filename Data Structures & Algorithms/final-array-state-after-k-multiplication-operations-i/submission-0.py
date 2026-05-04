class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        mappings = []

        for i, num in enumerate(nums):

            heapq.heappush(mappings, (num, i))

        for i in range(k):

            val, index = heapq.heappop(mappings)
            nums[index] *= multiplier
            heapq.heappush(mappings, (nums[index], index))

        return nums