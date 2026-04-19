class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort()
        def dfs(index, temp):
            if len(temp) <= len(nums):
                self.res.append(temp + []) 
            else:
                return 
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue 
                temp.append(nums[i])
                dfs(i + 1, temp)
                temp.remove(nums[i])
            
        dfs(0, [])
        return self.res 





