class Solution:
    def climbStairs(self, n: int) -> int:
        first = 0
        second = 1
        # 1 2 3 4  
        # 1 2 3 

        for i in range( n):
            temp = second
            second = first + second 
            first = temp 
        return second
        