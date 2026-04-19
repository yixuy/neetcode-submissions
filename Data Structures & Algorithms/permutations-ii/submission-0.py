class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        def dfs(temp, visit):
            if len(temp) == len(nums) and  temp not in self.res:
                self.res.append(temp + [])
       
            if len(temp) > len(nums):
                return 

            for i in range(len(nums)):
                if i not in visit:
                    temp.append(nums[i])
                    visit.append(i)
                    dfs(temp, visit)
                    temp.pop()
                    visit.remove(i)


        # nums.sort()
        self.res = []
  
        dfs([], [])
        return self.res






        