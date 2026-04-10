class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_index = 0
        num_index = 0

        # Search for 0s
        for i, num in enumerate(nums):

            if num == 0:

                break

            zero_index += 1

        for i in range(zero_index, len(nums)):

            num = nums[i]

            if num != 0:

                nums[zero_index] = num
                nums[i] = 0
                zero_index += 1