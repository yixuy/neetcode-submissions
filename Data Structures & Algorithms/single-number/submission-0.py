class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            # use xor 
            res = res ^ num
        return res
