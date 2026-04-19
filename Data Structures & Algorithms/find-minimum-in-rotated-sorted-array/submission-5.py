class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1 
        
        while left + 1 < right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                if nums[left] <= nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[left] <= nums[mid]:
                    left = mid
                else:
                    right = mid
        if nums[left] < nums[right]:
            return nums[left]
        else:
            return nums[right]
        