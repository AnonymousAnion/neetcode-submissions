class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        
        freqs = Counter(nums)

        largest_integer = -1

        for i in range(len(nums) - 1, -1, -1):

            if freqs[nums[i]] == 1 and nums[i] > largest_integer:

                largest_integer = nums[i]

        return largest_integer