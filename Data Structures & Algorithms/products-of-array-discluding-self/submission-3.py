class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        total_prod = 1
        # calculate the total product 
        contain_zero = 0 
        for num in nums:
            if num != 0:
                total_prod = total_prod * num
            else:
                contain_zero += 1
        if contain_zero > 1 :
            return [0] * len(nums)
        res = [0] * len(nums)
        # div each element to get one of them 
        for i, num in enumerate(nums):
            if contain_zero > 0:
                if num != 0:
                    res[i] = 0
                else:
                    res[i] = total_prod
            else:
                res[i] = (total_prod//num)

        return res