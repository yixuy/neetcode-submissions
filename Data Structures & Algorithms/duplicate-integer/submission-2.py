class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        pre = len(nums)
        curr_len = len(set(nums))

        return pre != curr_len
            
