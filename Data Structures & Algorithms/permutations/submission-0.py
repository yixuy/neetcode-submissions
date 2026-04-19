class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(visit, temp):
            if len(visit) == len(nums):
                self.res.append([] + temp)

            for i in range(len(nums)):
                if i not in visit:
                    visit.add(i)
                    temp.append(nums[i])
                    dfs(visit, temp)
                    visit.remove(i)
                    temp.pop()

        visit = set()
        temp = []
        dfs(visit, temp)
        return self.res 

            
        
        
