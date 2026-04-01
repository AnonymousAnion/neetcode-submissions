import math

class Solution:

    def findDuplicate(self, nums: List[int]) -> int:
        
        slow = fast = 0

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:

                break

        trace = 0

        while True:

            slow = nums[slow]
            trace = nums[trace]

            if slow == trace:

                return slow

        return -1