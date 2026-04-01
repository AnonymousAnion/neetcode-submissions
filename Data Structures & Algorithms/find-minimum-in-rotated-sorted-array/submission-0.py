class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1
        minimum = nums[0]

        while l <= r:

            if nums[l] < nums[r]:

                minimum = min(minimum, nums[l])
                break

            m = l + (r - l) // 2

            minimum = min(minimum, nums[m])

            if nums[m] >= nums[l]:
                # We are ascending from l to m
                # but we know that l is not the minimum
                # (see condition at top of while).
                # Therefore, we know the minimum is to the
                # right.
                l = m + 1

            else:
                # We know there was a global minimum between
                # [l, m] inclusive.
                r = m - 1

        return minimum