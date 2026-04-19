class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        def dfs(index, temp):
            if len(temp) == k:
                self.res.append(temp + [])
                
            for i in range(index, n):
                temp.append(i + 1)
                dfs(i + 1, temp)
                temp.remove(i + 1)
             
        
        dfs(0, [])
        return self.res