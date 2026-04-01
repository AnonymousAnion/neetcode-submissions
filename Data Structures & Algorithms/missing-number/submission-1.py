import math

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        expected_sum = len(nums) * math.ceil(len(nums) / 2) if len(nums) % 2 == 1 else len(nums) * (len(nums) // 2) + len(nums) // 2
        
        return expected_sum - sum(nums)