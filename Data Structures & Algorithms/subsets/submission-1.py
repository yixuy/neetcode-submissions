class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []

        def dfs(index, temp):
            if temp not in self.res:
                self.res.append(temp + [])
                 
            if len(temp) >= len(nums):
                return 

            for i in range(index, len(nums)):
                temp.append(nums[i])
                dfs(i + 1, temp)
                temp.pop()

        dfs(0, [])            

        return self.res