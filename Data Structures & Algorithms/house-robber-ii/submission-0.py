class Solution:

    def non_continuous_rob(self, nums: List[int]) -> int:

        if len(nums) == 0:

            return 0
        
        elif len(nums) == 1:

            return nums[0]

        elif len(nums) == 2:

            return max(nums[0], nums[1])

        nums[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):

            nums[i] = max(nums[i-1], nums[i] + nums[i-2])

        return nums[-1]

    def rob(self, nums: List[int]) -> int:

        if 1 == len(nums):

            return nums[0]

        return max(self.non_continuous_rob(nums[1:]), self.non_continuous_rob(nums[:len(nums) - 1]))