class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        if target > nums[r]:

            return r + 1
        
        elif target < nums[l]:

            return l

        while l <= r:

            m = l + (r - l) // 2

            if target > nums[m]:

                l = m + 1

            elif target < nums[m]:

                r = m - 1

            else:

                return m

        return r + 1

