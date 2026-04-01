class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        prev_num: int = nums[0]

        unique_elements = 1

        for i in range(1, len(nums)):

            num = nums[i]

            if num != prev_num:

                nums[unique_elements] = num
                unique_elements += 1

            prev_num = num

        return unique_elements