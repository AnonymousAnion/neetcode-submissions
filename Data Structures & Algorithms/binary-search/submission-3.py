class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def binary_search(lower_bound = 0, upper_bound = len(nums) - 1, t = target) -> int:

            middle = (upper_bound - lower_bound) // 2 + lower_bound

            if lower_bound <= upper_bound:

                if t > nums[middle]:

                    return binary_search(middle + 1, upper_bound, t)

                elif t < nums[middle]:

                    return binary_search(lower_bound, middle - 1, t)

                else:

                    return middle

            return -1

        return binary_search()

                