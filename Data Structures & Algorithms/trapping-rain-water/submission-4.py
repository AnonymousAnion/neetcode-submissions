from collections import deque
class Solution:
    def trap(self, heights: List[int]) -> int:

        if not heights:

            return 0

        total_rain = 0

        l = 0
        r = len(heights) - 1
        max_l = heights[l]
        max_r = heights[r]

        while l < r:

            if max_l > max_r:

                r -= 1
                max_r = max(max_r, heights[r])
                total_rain += max_r - heights[r]

            else:

                l += 1
                max_l = max(max_l, heights[l])
                total_rain += max_l - heights[l]

        return total_rain

