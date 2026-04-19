class TimeMap:
    def binarySearch(self, arr, timestamp):
        left = 0
        right = len(arr) - 1
        arr.sort()
        print(arr)
        while left + 1 < right:
            mid = (left + right) // 2
            if timestamp == arr[mid][0]:
                return arr[mid][1]
            elif timestamp <  arr[mid][0]:
                right = mid
            else:
                left  = mid
    
        if arr[right][0] <= timestamp:
            return arr[right][1]
        if arr[left][0] <= timestamp:
            return arr[left][1]
        return ""
    def __init__(self):
        self.time_mapping = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:      
        self.time_mapping[key].append((timestamp, value))
    
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_mapping:
            return ""
        return self.binarySearch(self.time_mapping[key], timestamp)
       



      

