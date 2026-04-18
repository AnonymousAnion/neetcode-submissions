class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        
        if not nums:

            return [[lower, upper]]

        missing_ranges = []
        
        if lower != nums[0]:

            missing_ranges.append([lower, nums[0] - 1])

        for i in range(len(nums) - 1):

            num = nums[i]
            next_num = nums[i + 1]

            if next_num - num > 1:

                missing_ranges.append([num + 1, next_num - 1])

        if upper != nums[-1]:

            missing_ranges.append([nums[-1] + 1, upper])

        return missing_ranges