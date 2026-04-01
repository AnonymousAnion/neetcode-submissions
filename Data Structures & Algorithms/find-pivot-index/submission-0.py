from collections import deque

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        # Get the prefix sums
        prefix_sums = []
        current_sum = 0

        for num in nums:

            current_sum += num
            prefix_sums.append(current_sum)

        # print("Prefix Sums: ")
        # print(prefix_sums)

        # Get the suffix sums
        suffix_sums = deque()
        current_sum = 0

        for num in reversed(nums):

            current_sum += num
            suffix_sums.appendleft(current_sum)

        # print("Suffix Sums: ")
        # print(suffix_sums)

        # Traverse the array ignoring the ends of the
        # array to check if the suffix sum for the index
        # to the right of the current index is equal to
        # the prefix sum for the index to the left of the
        # current index
        for i in range(0, len(nums)):
            
            left_sum = prefix_sums[i-1] if i > 0 else 0
            right_sum = suffix_sums[i+1] if i < len(nums) - 1 else 0

            if left_sum == right_sum:

                return i

        return -1
        