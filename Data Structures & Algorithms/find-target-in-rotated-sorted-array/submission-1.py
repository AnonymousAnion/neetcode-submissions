class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l + (r - l) // 2

            print("M: ", m)

            if target == nums[m]:

                return m

            elif nums[r] > nums[l]: # Sorted subarray

                if target > nums[m]:

                    l = m + 1

                else:

                    r = m - 1

            elif nums[m] >= nums[l]: # Ascending from l to m

                if target <= nums[m] and target > nums[r]:

                    r = m - 1

                else:

                    l = m + 1
            else:

                if target > nums[r] or target < nums[m]:

                    r = m - 1

                else:

                    l = m + 1

            print("[l, r]: [{0}, {1}]".format(l, r))

        return -1