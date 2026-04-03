class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        
        # Binary search for the lower bound
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l + (r - l) // 2 # overflow resistant calculation

            if target >= nums[m]:

                l = m + 1

            else:

                r = m - 1

        # print("l: ", l)
        # print("r: ", r)

        max_index = l - 1

        # print("max index: ", max_index)
        # print("Max index Value: ", nums[max_index])

        if nums[max_index] != target:

            return False

        # Binary search for the upper bound
        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l + (r - l) // 2 # overflow resistant calculation

            if target <= nums[m]:

                r = m - 1

            else:

                l = m + 1

        # print("l: ", l)
        # print("r: ", r)

        min_index = r + 1

        # print("min index: ", min_index)
        # print("Min index Value: ", nums[min_index])

        if max_index - min_index + 1 > len(nums) / 2:

            return True

        return False
