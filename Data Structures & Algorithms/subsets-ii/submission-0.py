class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        curSet = []
        subsets = []

        def helper(i: int) -> None:

            nonlocal nums
            nonlocal curSet
            nonlocal subsets

            if i >= len(nums):

                subsets.append(curSet.copy())
                return

            # Branch with index added
            curSet.append(nums[i])
            helper(i + 1)

            # Branch without index added
            curSet.pop()

            # Ignore future duplicates - Otherwise, repeating work
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:

                i += 1 

            helper(i + 1)

        helper(0)

        return subsets