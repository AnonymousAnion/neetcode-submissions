class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        curSet = []
        subsets = []
        
        def helper(i: int) -> None:

            nonlocal curSet
            nonlocal subsets
            nonlocal nums

            if i >= len(nums):

                subsets.append(curSet.copy())
                return

            # Branch with index added
            curSet.append(nums[i])
            helper(i + 1)

            # Branch with index Removed
            curSet.pop()
            helper(i + 1)

        helper(0)

        return subsets