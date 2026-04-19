class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = []
    
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        timeList = self.timeMap[key]
        print(timeList)
        left = 0
        right = len(timeList) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if  timeList[mid][1] < timestamp:
                left = mid
            else:
                right = mid
  
        if  timeList[right][1] <= timestamp:
            return timeList[right][0]
        if  timeList[left][1] <= timestamp:
            return timeList[left][0]
        return ""