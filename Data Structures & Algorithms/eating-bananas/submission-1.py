import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles) 
        def getHours(mid):
            count = 0
            for pile in piles:
                count += math.ceil( pile/mid)
            return count
        while left + 1 < right:
            mid = (left + right) // 2
          
            
            if getHours(mid) == h:
                right = mid
            elif getHours(mid) > h:
                left = mid
            else:
                right = mid
        
        if getHours(left) <= h:
            return left
        if getHours(right) <= h:
            return right


        