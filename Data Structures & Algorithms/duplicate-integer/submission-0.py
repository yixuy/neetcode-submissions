class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort();
        prev_num = 0
        next_num = prev_num
        nums_len = len(nums)
        for i in range(0, nums_len-1):
            if nums[i] == nums[i+1]:
                return True;
        return False
            