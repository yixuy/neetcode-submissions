class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums: List[int]) -> int:
        first = 0
        second = 0
        
        for num in nums:
            temp = max(first + num, second)
            first = second 
            second = temp 

        return second 