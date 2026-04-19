class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # not continguous
        # for i in range(len(nums)-1, -1, -1):
        #     for j in range(i+1, len(nums)):
        #         if arr[i] * nums[j] > 0:
        #             arr[i] = max(arr[i], arr[i] * nums[j])
        
         
        res = max(nums)
        currMax, currMin = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1,1
                continue
            temp = currMax * n
            currMax = max(currMax*n , currMin*n, n)
            currMin = min(temp, currMin*n, n)
            res = max(res, currMax)
        return res