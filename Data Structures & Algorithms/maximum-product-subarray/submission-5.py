class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = 1
        min_p = 1
        res = nums[0]
        
        for n in nums:
            tmp_max_p = max_p * n
            max_p = max(tmp_max_p, min_p * n, n )
            min_p = min(tmp_max_p, min_p * n, n )
            res = max(res, max_p)

        return res 