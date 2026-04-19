class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        self.res = []
        candidates.sort()
        def dfs(temp, index, temp_sum):
            if temp_sum == target:
                self.res.append(temp + [])
                return 
            if temp_sum > target:
                return 
            for i in range(index, len(candidates)):
                if i > index and candidates[i-1] == candidates[i]:
                    continue
                temp.append(candidates[i])
                dfs(temp, i + 1, temp_sum + candidates[i])
                temp.pop()   
        dfs([], 0, 0)
        return self.res 