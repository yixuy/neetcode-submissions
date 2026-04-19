class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]


        memo = [-1] * len(nums)
        memo[0] = nums[0]
        memo[1] = max(nums[0], nums[1])
    
        def dp(n):
            if memo[n] != -1:
                return memo[n]
            if n - 2 >= 0:
                memo[n] = max(dp(n-2) + nums[n] , dp(n-1)) 

            return memo[n]

       
        # print(memo)
        return  dp(len(nums) - 1)
        