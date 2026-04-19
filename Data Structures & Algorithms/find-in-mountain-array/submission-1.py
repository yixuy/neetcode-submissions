class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        left = 0
        right = mountainArr.length() - 1
        peak = 0
        while left + 1 < right:
            mid = (left + right) // 2

            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                left = mid
            else:
                right = mid

        if mountainArr.get(left) < mountainArr.get(right):
            peak = right
        else:
            peak = left 
        self.res = []
        left = 0
        right = mountainArr.length() - 1
        def binarySearch(left, right, increasing):
            while left + 1 < right:
                mid = (left + right) // 2
                if increasing:
                    if mountainArr.get(mid) < target:
                        left = mid 
                    else:
                        right = mid
                else:
                    if mountainArr.get(mid) < target:
                        right = mid
                    else:
                        left = mid 

            if mountainArr.get(left) == target:
                self.res.append(left)
            if mountainArr.get(right) == target:
                self.res.append(right)
        binarySearch(left, peak, True)
        binarySearch(peak, right, False)
   
        return min(self.res) if self.res else -1

