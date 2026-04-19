class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda pair:pair[0])
        res = [intervals[0]]
        for start, end in intervals[1:]:
            if res[-1][1] >= start:
                res[-1][1] = max(end, res[-1][1])
            else:
                res.append([start, end])

        return res
        
                