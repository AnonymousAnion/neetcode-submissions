"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals or len(intervals) <= 1:

            return True

        intervals.sort(key = lambda interval: interval.start)

        prev_interval_end = 0
        for interval in intervals:

            #print("({0}, {1})".format(interval.start, interval.end))

            if interval.start < prev_interval_end:

                return False

            prev_interval_end = interval.end

        return True