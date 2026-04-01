class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        sums = dict()
        
        for i, num in enumerate(nums):

            if num in sums:

                return [sums[num], i]

            else:

                sums.update({target - num: i})

        return [0, 0]