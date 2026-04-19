class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
    
        for i, a in enumerate(self.arr):
            if a > num:
                self.arr.insert(i, num)
                return
        self.arr.append(num)

    def findMedian(self) -> float:
        # if len(self.arr) <= 1:
        #     return self.arr[0]
        print(self.arr)
        if len(self.arr) % 2 == 0:
            return (self.arr[len(self.arr) // 2 - 1] + self.arr[len(self.arr) // 2 ])/2
        else:
          
            return self.arr[len(self.arr) // 2 ]

        


        