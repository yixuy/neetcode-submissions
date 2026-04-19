"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in  intervals])
        end = sorted([i.end for i in  intervals])

        max_count = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                e += 1
                count -= 1
            max_count = max(count, max_count)
        return max_count