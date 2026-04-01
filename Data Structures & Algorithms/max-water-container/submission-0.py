class Solution:

    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_area = 0

        while left != right:

            combined_height = min(heights[left], heights[right])
            width = right - left

            area = combined_height * width

            if area > max_area:

                max_area = area

            if heights[left] > heights[right]:

                right -= 1

            else:

                left += 1

        return max_area


        