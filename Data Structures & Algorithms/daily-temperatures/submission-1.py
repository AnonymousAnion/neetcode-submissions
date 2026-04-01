class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        
        for i, temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:

                lesser_temp, temp_index = stack.pop()
                temperatures[temp_index] = i - temp_index

            stack.append((temp,i))

        while stack:

            peak_prefix_temp, temp_index = stack.pop()
            temperatures[temp_index] = 0

        return temperatures
            