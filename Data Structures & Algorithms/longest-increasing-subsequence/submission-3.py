class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)   
        memo = [-1] * n 
        memo[n-1] = 1
        def dp(i):
            if memo[i] != -1:
                return memo[i]

            temp = 1
            for j in range(i + 1, n):
                if nums[i] < nums[j]:
                    temp = max(temp, 1 + dp(j))

            memo[i] = temp
            return temp
        for i in range(n):
            dp(i)
        return max(memo)
            