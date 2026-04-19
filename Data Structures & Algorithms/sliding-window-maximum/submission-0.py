class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        temp = []
        if k > len(nums):
            return max(nums)
        
        for i in range(k):
            temp.append(nums[i])
        res.append(max(temp))
        
        for i in range(k, len(nums)):
            temp.remove(nums[i-k])
            temp.append(nums[i])
            res.append(max(temp))

        return res
            