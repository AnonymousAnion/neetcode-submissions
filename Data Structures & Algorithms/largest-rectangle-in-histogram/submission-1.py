class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        max_area = 0

        stack = []
        
        for i, height in enumerate(heights):

            max_area = max(max_area, height)

            if not stack or height > stack[-1][1]:

                stack.append((i, height))

            else:

                while stack and height <= stack[-1][1]:

                    prev_index, prev_value = stack.pop()
                    area = prev_value * (i - prev_index)
                    max_area = max(max_area, area)

                stack.append((prev_index, height))

        while stack:

            index, value = stack.pop()
            area = value * (len(heights) - index)
            max_area = max(max_area, area)

        return max_area