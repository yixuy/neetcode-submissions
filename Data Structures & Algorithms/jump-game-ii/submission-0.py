class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def dp(memo, index):
            if index in memo:
                return memo[index]
            memo[index] = float('INF')
            for i in range(index):
                if i + nums[i] >= index:
                    memo[index] = min(memo[index], dp(memo, i) + 1)
            return memo[index]

        memo = {}
        memo[0] = 0
        
        return dp(memo, len(nums) - 1)

        

        