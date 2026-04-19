class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if target < nums[mid]:
                right = mid
            else:
                left = mid 

        if target <= nums[left]:
            return left 
        if target <= nums[right]:
            return right 
        
        return len(nums) 