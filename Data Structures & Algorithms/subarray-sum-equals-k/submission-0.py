

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        k_equivalents = 0

        for i, num in enumerate(nums):

            current_sum += num

            if current_sum - k in prefix_sums:

                k_equivalents += prefix_sums[current_sum - k]

            prefix_sums[current_sum] += 1

        return k_equivalents


