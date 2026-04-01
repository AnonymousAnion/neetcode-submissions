class Solution:


    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = l = 0
        r = len(nums) - 1

        def swap(i1: int, i2: int) -> None:

            temp = nums[i1]
            nums[i1] = nums[i2]
            nums[i2] = temp
        
        while i <= r:

            if 0 == nums[i]:

                swap(l, i)
                l += 1

            elif 2 == nums[i]:

                swap(i, r)
                r -= 1
                i -= 1

            i += 1

        return nums
