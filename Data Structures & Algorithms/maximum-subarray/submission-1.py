class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_sum = nums[0]
        running_total = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]
            running_total = max(num, num + running_total)
            max_sum = max(max_sum, running_total)

        return max_sum