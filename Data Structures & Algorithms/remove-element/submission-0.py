class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        l: int = 0

        for i, num in enumerate(nums):

            if val != num:

                nums[l] = nums[i]
                l += 1

        return l
