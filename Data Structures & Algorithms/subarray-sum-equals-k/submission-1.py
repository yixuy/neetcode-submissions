class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # presum
        presum = (len(nums) + 1) * [0]

        for i in range(1, len(nums) + 1):
            presum[i] = presum[i-1] + nums[i-1]
        print(presum)
        # presum[k+1] - presum[i] = k
        mapping = {}
        res = 0
        for i in range(len(presum)):
            if presum[i] in mapping:
                res += mapping[presum[i]] 
                 
            mapping[presum[i] + k] = mapping.get(presum[i] + k, 0) + 1
        return res
    