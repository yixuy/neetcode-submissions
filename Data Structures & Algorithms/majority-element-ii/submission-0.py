class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mapping = {}

        for num in nums:
            mapping[num] = mapping.get(num, 0) + 1
        res = []
        for key, value in mapping.items():
            if value > math.floor(len(nums) / 3):
                res.append(key)

        return res