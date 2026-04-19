class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # slide window
        curSum = 0
        res = nums[0]
    
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n  
            if res < curSum:
                res = curSum
            
        return res
            


    
