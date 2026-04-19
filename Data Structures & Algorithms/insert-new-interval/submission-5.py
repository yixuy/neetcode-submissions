class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        #  [[1,3],[4,6]], [2,5]
        #  edge case:
        #  [[]]

        if intervals == []:
            intervals.append(newInterval)
            return intervals
        old = len(intervals)
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
        if old + 1 != len(intervals):
            intervals.append(newInterval) 
        print(intervals)
        left = 0
        for right in range(1, len(intervals)):
            if intervals[left][1] >= intervals[right][0]:
                intervals[left][1] = max(intervals[left][1], intervals[right][1])
                # print(intervals[left][1] )
            else:
                left += 1
                intervals[left] = intervals[right] 
            
        return intervals[:left+1]
          