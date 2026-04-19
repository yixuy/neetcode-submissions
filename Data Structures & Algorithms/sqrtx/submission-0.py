class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x 

        while left + 1 < right:
            mid = (left + right) // 2

            if mid * mid == x:
                return mid 
            elif mid * mid < x:
                left = mid
            else:
                right = mid
        if left * left <= x:
            return left 
        if right * right <= x:
            return right

        return 