class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left = 0
        nums = list(set(nums))
        right = len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid
    
        if nums[left] == target or nums[right] == target:
            return True
        return False    