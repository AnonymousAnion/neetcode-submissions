class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l + (r - l) // 2

            #print("M: ", m)

            if target == nums[m]:

                return m

            elif nums[l] <= nums[m]: # Ascending from l to m

                if target > nums[m] or target < nums[l]:

                    l = m + 1

                else:

                    r = m - 1

            else: # Ascending from m to r

                if target <= nums[m] or target > nums[r]:

                    r = m - 1

                else:

                    l = l + 1

            #print("[l, r]: [{0}, {1}]".format(l, r))

        return -1