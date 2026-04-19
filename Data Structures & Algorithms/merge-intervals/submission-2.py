class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        left = 0 
        intervals = sorted(intervals)
        for right in range(1, len(intervals)):
            if intervals[right][0] <= intervals[left][1]:
                intervals[left][1] = max(intervals[right][1], intervals[left][1])
            else:
                left += 1
                intervals[left] = intervals[right]

        return intervals[:left+1]







