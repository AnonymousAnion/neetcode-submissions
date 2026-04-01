import math

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        def reverse(l: int = 0, r = len(nums) - 1) -> None:

            while l < r:

                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp

                l += 1
                r -= 1

        if k > 0:

            reverse()
            reverse(0, k - 1)
            reverse(k)
        