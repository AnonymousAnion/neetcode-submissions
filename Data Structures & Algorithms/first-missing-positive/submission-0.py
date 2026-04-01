class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        present_nums = set(nums)
        n = len(nums)

        # Search the 
        for i in range(1, n + 1):

            if i not in present_nums:

                return i

        return n + 1