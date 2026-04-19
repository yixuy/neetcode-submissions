class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # 1 1 1 2 
        def dfs(temp, visit):
            if len(temp) == len(nums):
                self.res.append(temp + [])
       
            if len(temp) > len(nums):
                return 

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and i-1 not in visit:
                    continue
                if i not in visit:
                    temp.append(nums[i])
                    visit.append(i)
                    dfs(temp, visit)
                    temp.pop()
                    visit.remove(i)


        nums.sort()
        self.res = []
  
        dfs([], [])
        return self.res






        