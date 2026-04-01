class Solution:
    def canJump(self, nums: List[int]) -> bool:

        minimum_necessary_jump = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):

            num = nums[i]

            if nums[i] + i >= minimum_necessary_jump:

                minimum_necessary_jump = i

        return 0 == minimum_necessary_jump
        