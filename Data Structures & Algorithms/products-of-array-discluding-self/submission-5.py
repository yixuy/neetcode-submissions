class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        total_zero = 0
        for i in range(len(nums)):
            if total_zero == 0 and nums[i] == 0:
                total_zero += 1
                continue
            elif nums[i] == 0:
                total_prod = 0
                break 

            total_prod *= nums[i]
        
        for i in range(len(nums)):
            if total_zero == 0:
                nums[i] = total_prod // nums[i]
            else:
                if nums[i] != 0:
                    nums[i] = 0 // nums[i]
                else:
                    nums[i] = total_prod 
      

        return nums