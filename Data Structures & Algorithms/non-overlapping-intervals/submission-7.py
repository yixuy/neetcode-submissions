class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        intervals = sorted(intervals)
        left = intervals[0][1]
        count = 0

        for right in range(1, len(intervals)):
            if left > intervals[right][0]:
                count += 1
                left = min(intervals[right][1], left)
            else:
                left = intervals[right][1]

        return count
            