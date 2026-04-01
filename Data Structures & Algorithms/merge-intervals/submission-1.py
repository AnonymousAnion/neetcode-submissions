class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key = lambda interval: interval[0])
        non_overlapping_intervals = []
        prev_interval_end = -1

        #print(intervals)

        for interval in intervals:

            #print("Non-overlapping intervals: ", non_overlapping_intervals)

            if interval[0] <= prev_interval_end:

                # Combine:
                # Assign the max of the last non-overlapping
                # interval's end time and the current
                # interval's end time.
                non_overlapping_intervals[-1][1] = max(interval[1], non_overlapping_intervals[-1][1])

            else:

                non_overlapping_intervals.append(interval)

            prev_interval_end = max(interval[1], non_overlapping_intervals[-1][1])

        return non_overlapping_intervals