import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def countTime(speed):
            count = 0
            for p in piles:
                count += math.ceil(p / speed)
            return count 
        
        left = 1
        right = max(piles) 

        while left + 1 < right:
            mid = (left + right) // 2

            if countTime(mid) <= h:
                right = mid
            else:
                left = mid
            
        if countTime(left) <= h:
            return left
        if countTime(right) <= h:
            return right


        