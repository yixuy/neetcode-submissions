class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, target: int, temp_res:  List[int]):
            if sum(temp_res) == target:
                # need .copy()
                res.append(temp_res.copy())
                return 
            if index >= len(nums) or  sum(temp_res) > target:
                return 
            temp_res.append(nums[index])
            dfs(index, target, temp_res)
            temp_res.pop()
            dfs(index+1, target, temp_res)  
            
        dfs(0, target, [])
        return res
