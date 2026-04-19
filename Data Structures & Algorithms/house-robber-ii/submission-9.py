class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_line(curr_nums):
            if len(curr_nums) == 0:
                return 0
            if len(curr_nums) == 1:
                return curr_nums[0]
            memo = [-1] * len(curr_nums)
            memo[0] = curr_nums[0]
            memo[1] = max(curr_nums[0], curr_nums[1])
            
            def dp(n):
                if memo[n] != -1:
                    return memo[n]
                if n - 2 >= 0:
                    memo[n] = max(dp(n - 2) + curr_nums[n], dp(n - 1))
            
                return memo[n]

            return dp(len(curr_nums)-1)

        return max(rob_line(nums[1:]), rob_line(nums[:-1]))
        