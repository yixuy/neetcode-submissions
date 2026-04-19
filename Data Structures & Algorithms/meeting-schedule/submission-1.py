"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        times = []

        for interval in intervals:
            times.append([interval.start,1])
            times.append([interval.end,-1])
        
        times = sorted(times)
        count = 0
        
        for time in times:
            count += time[1]
            if count > 1:
                return False

        return True
        