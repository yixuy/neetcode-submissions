class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.res = []
        def dfs(index, temp, temp_sum):
            if temp_sum == target:
                self.res.append(temp + [])
                return 
            if temp_sum > target:
                return 

            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(i, temp, temp_sum + nums[i])
                temp.pop()


        dfs(0, [], 0)
        return self.res