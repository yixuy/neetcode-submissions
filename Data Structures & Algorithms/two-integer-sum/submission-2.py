class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j and nums[j] + nums[i] == target:
        #             return [i, j]
        mapping = {}
        for i, n in enumerate(nums):
            if (target - n) in mapping:
                return [mapping[target - n], i]
            else: 
                mapping[n] = i
        return []
