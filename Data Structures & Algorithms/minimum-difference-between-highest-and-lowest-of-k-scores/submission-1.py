class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        min_diff = float("inf")

        for i in range(0, len(nums) - k + 1):

            lowest = nums[i]
            highest = nums[i + k - 1]

            diff = highest - lowest

            if diff < min_diff:

                min_diff = diff

        return min_diff