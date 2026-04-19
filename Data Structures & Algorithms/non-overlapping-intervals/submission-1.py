class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda pair: pair[1])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            if res[-1][1] > start:
                res[-1][1] = min(end, res[-1][1])
            else:
                res.append([start, end])

        return len(intervals) - len(res)

[1,11],[2,12], [11,22], [1,100]
