"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        times = []
        for interval in intervals:
            times.append((interval.start, 1))
            times.append((interval.end, -1))
        times = sorted(times)
        res = 0
        count = 0
        for time, val in times:
            count += val
            res = max(res, count)
        return res
