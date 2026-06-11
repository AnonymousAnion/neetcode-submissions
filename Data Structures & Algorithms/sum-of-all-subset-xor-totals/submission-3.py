class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        sums = []
        curSet = []

        def dfs(i: int) -> None:

            nonlocal sums
            nonlocal curSet
            nonlocal nums

            if i == len(nums):

                sums.append(curSet.copy())
                return

            # Add element
            curSet.append(nums[i])
            dfs(i + 1)

            # Don't add element
            curSet.pop()
            dfs(i + 1)

        dfs(0)
        
        def xor_sum(arr: List[List[int]]) -> int:

            total = 0

            for subset in arr:

                if not subset:

                    continue

                xor = subset[0]

                for i in range(1, len(subset)):

                    xor ^= subset[i]

                total += xor

            return total

        return xor_sum(sums)