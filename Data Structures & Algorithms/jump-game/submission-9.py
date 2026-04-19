class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums: 
            return False
        memo = {}
        memo[0] = True

        def dp(n):
            if n in memo:
                return memo[n]
            memo[n] = False 
            for i in range(n):
                if nums[i] + i >= n:
                    memo[n] = True and dp(i)
            return memo[n] 

        return dp(len(nums) - 1)
        
