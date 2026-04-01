class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        curComb = []
        curSum = 0
        combinations = []

        def helper(i: int) -> None:

            nonlocal curComb
            nonlocal curSum
            nonlocal combinations

            if curSum == target:

                combinations.append(curComb.copy())

            if curSum >= target:

                return

            if i >= len(nums):

                return

            for j in range(i, len(nums)):

                curComb.append(nums[j])
                curSum += nums[j]
                helper(j)
                curComb.pop()
                curSum -= nums[j]

        helper(0)

        return combinations