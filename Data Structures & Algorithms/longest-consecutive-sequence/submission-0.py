class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) < 1:

            return 0

        unique_nums = set(nums)

        lcs = 1

        for num in unique_nums:

            current_lcs = 1

            if num - 1 not in unique_nums: # Sequence start

                current_lcs = 1

                while num + 1 in unique_nums:

                    current_lcs += 1
                    num = num + 1

            lcs = max(lcs, current_lcs)

        return lcs