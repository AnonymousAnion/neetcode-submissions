class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        # Zero out negative numbers
        for i, num in enumerate(nums):

            if num < 0:

                nums[i] = 0

        # Mark numbers at indices negative
        # if that number - 1 is present in the array
        for i, num in enumerate(nums):

            present_index = abs(num) - 1

            if 0 <= present_index < len(nums):

                val = nums[present_index]

                if val < 0: # Already Marked

                    continue

                elif 0 == val:

                    nums[present_index] = -(len(nums) + 1)

                else:

                    nums[present_index] = -val

        # Find the first missing positive number
        for i, num in enumerate(nums):

            if num >= 0:

                return i + 1

        return len(nums) + 1

