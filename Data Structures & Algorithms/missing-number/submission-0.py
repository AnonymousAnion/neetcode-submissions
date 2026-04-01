import math

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        expected_sum = len(nums) * math.ceil(len(nums) / 2) if len(nums) % 2 == 1 else len(nums) * (len(nums) // 2) + len(nums) // 2
        
        # print([i for i in range(0, 100)])
        # print("n: ", len(nums))
        # print("Expected Sum: ", expected_sum)
        # print("Sum: ", sum(nums))
        # print("Missing Num: ", str(expected_sum - sum(nums)))
        return expected_sum - sum(nums)