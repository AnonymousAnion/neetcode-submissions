class Solution:
    def search(self, nums: List[int], target: int) -> int:

        upper_bound = len(nums) - 1
        lower_bound = 0
        search_index = (upper_bound - lower_bound) // 2 + lower_bound

        while upper_bound >= lower_bound:

            num = nums[search_index]

            #print("Num: ", num)

            if num == target:

                return search_index

            elif num > target:

                upper_bound = search_index - 1

            else:

                lower_bound = search_index + 1

            search_index = (upper_bound - lower_bound) // 2 + lower_bound

        return -1
        