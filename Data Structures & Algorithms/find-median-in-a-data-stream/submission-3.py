class MedianFinder:

    # def __init__(self):
    #     self.arr = []

    # def addNum(self, num: int) -> None:
        
    #     for i, a in enumerate(self.arr):
    #         if a > num:
    #             self.arr.insert(i, num)
    #             return
    #     self.arr.append(num)

    # def findMedian(self) -> float:
    #     # if len(self.arr) <= 1:
    #     #     return self.arr[0]
    #     print(self.arr)
    #     if len(self.arr) % 2 == 0:
    #         return (self.arr[len(self.arr) // 2 - 1] + self.arr[len(self.arr) // 2 ])/2
    #     else:
          
    #         return self.arr[len(self.arr) // 2 ]
    
    def __init__(self):
        self.large = []
        self.small = []

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)
        
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -1 * heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -1 * heapq.heappop(self.large))


    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (self.large[0] + -1 * self.small[0])/2
      
        


        