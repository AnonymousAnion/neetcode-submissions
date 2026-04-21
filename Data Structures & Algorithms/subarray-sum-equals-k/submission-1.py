class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count = 0
        freqs = Counter()
        freqs[0] = 1
        total = 0

        for num in nums:

            total += num
            count += freqs[total - k]
            freqs[total] += 1

        return count