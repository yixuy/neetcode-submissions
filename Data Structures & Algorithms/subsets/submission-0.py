class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        

        def dfs(temp, start_index):
            if len(temp) > len(nums):
                return 
            self.res.append(temp + [])
            for i in range(start_index, len(nums)):
                temp.append(nums[i])
                dfs(temp, i+1)
                temp.pop(-1)


        dfs([], 0)
        return self.res