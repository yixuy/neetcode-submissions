class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        max_num = len(nums)
        res = 0
        max_res = 0

        for i in range(max_num+1):
            max_res += i

        for num in nums:
            res += num

        return max_res - res 