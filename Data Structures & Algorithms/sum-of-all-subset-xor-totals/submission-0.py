class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        self.res = 0
        def dfs(index, temp_sum):
            temp = 0 
            for num in temp_sum:
                temp ^= num 
            self.res += temp

            for i in range(index, len(nums)):
                temp_sum.append(nums[i])
                dfs(i + 1, temp_sum)
                temp_sum.pop()

        dfs(0, [])
        return self.res 