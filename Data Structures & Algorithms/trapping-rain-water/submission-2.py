from collections import deque
class Solution:
    def trap(self, heights: List[int]) -> int:

        deltas = [0]

        # 1.) Find the derivative of elevation
        # e.g. (the change in height between adjacent neighbors)
        for i in range(1, len(heights)):

            deltas.append(heights[i] - heights[i-1])

        # print("Deltas: ")
        # print(deltas)

        # 2.) Go R -> L recording the tallest peak
        # to the right of each peak. Also, go L -> R
        # to record the tallest peak to the left of each peak.

        # a) Gather tallest peak to the left of each peak
        tallest_left_peak = [0]
        left_max = heights[0]

        for i in range(1, len(heights)):
            
            tallest_left_peak.append(left_max)
            left_max = max(left_max, heights[i])

        # print("Tallest Peak to the Left: ")
        # print(tallest_left_peak)

        # b) Gather Tallest peak to the right of each peak
        tallest_right_peak = deque()
        tallest_right_peak.append(0)
        right_max = heights[-1]

        for i in range(len(heights) - 2, -1, -1):

            tallest_right_peak.appendleft(right_max)
            right_max = max(right_max, heights[i])

        # print("Tallest Peak to the Right: ")
        # print(tallest_right_peak)

        # 3.) Only keep peaks if there aren't taller peaks to
        # BOTH their right and left
        optimal_peaks: List[(int, int)] = []

        # Store a saved peak's index and height
        for i, delta in enumerate(deltas):

            save_peak: bool = False

            # Special Case; Last Index (no peaks to right)
            if len(deltas) - 1 == i:

                if delta > 0:

                    save_peak = True

            # Special Case: First Index (No peaks to left)
            elif i == 0:
                
                if heights[i] > 0 and i + 1 < len(deltas) and deltas[i + 1] <= 0:

                    save_peak = True

            elif delta > 0 and deltas[i+1] <=0:

                if heights[i] >= tallest_left_peak[i] or heights[i] >= tallest_right_peak[i]:

                    save_peak = True

            if save_peak:

                optimal_peaks.append((i, heights[i]))

        # print("Optimal Peaks: ")
        # print(optimal_peaks)

        # 4.) Use L and R pointers between peaks to calculate
        # aggregate trapped rain water
        trapped_rain = 0

        for i in range(0, len(optimal_peaks) - 1):

            blocked_rain = 0
            left_peak = optimal_peaks[i]
            right_peak = optimal_peaks[i + 1]
            min_shared_height = min(left_peak[1], right_peak[1])
            width = right_peak[0] - left_peak[0] - 1
            total_area = min_shared_height * width

            # Calculate Blocked Rain
            for j in range(left_peak[0] + 1, right_peak[0]):

                blocked_rain += min(min_shared_height, heights[j])

            trapped_rain += total_area - blocked_rain

        return trapped_rain

